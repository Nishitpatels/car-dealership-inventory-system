/* Page bootstrapping and static UI behaviour. No API calls or backend logic. */
(function () {
  const C = window.DealerComponents;
  const P = window.DealerPages;
  const D = window.DealerData;
  const page = document.body.dataset.page;

  function showToast(title, message, icon = 'fa-circle-check') {
    const region = document.querySelector('[data-toast-region]');
    if (!region) return;
    region.innerHTML = `<div class="dealer-toast-wrap"><div class="dealer-toast"><i class="fa-solid ${icon}"></i><div><strong>${title}</strong><span>${message}</span></div></div></div>`;
    window.setTimeout(() => { region.innerHTML = ''; }, 4200);
  }

  function setStatus(vehicle) {
    if (vehicle.quantity <= 0) vehicle.status = 'Out of Stock';
    else if (vehicle.quantity <= 2) vehicle.status = 'Low Stock';
    else vehicle.status = 'Available';
  }

  function renderPage() {
    document.getElementById('page-content').innerHTML = P.render(page);
    if (window.AOS) window.AOS.init({ duration: 650, once: true, offset: 30 });
    requestAnimationFrame(initRevenueChart);
  }

  function initRevenueChart() {
    const canvas = document.getElementById('revenueChart');
    if (!canvas || !window.Chart) return;
    if (window.dealerRevenueChart) window.dealerRevenueChart.destroy();
    const context = canvas.getContext('2d');
    const gradient = context.createLinearGradient(0, 0, 0, 280);
    gradient.addColorStop(0, 'rgba(139,92,246,.35)');
    gradient.addColorStop(1, 'rgba(59,130,246,.01)');
    window.dealerRevenueChart = new Chart(context, {
      type: 'line',
      data: { labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'], datasets: [{ data: [286, 324, 301, 368, 410, 424, 486], borderColor: '#8b5cf6', backgroundColor: gradient, borderWidth: 2.5, fill: true, tension: .42, pointRadius: 3, pointBackgroundColor: '#a78bfa' }] },
      options: { maintainAspectRatio: false, plugins: { legend: { display: false }, tooltip: { backgroundColor: 'rgba(22,22,42,.96)', titleColor: '#ddd6fe', bodyColor: '#d4d4e8', displayColors: false, callbacks: { label: item => ` $${item.parsed.y}k revenue` } } }, scales: { x: { grid: { display: false }, ticks: { color: '#7878a0', font: { family: 'Space Grotesk', size: 11 } } }, y: { border: { display: false }, grid: { color: 'rgba(255,255,255,.06)' }, ticks: { color: '#7878a0', font: { family: 'Space Grotesk', size: 11 }, callback: value => `$${value}k` } } } }
    });
  }

  function filterVehicles() {
    const query = (document.querySelector('[data-filter="query"]')?.value || '').toLowerCase().trim();
    const make = document.querySelector('[data-filter="make"]')?.value || '';
    const category = document.querySelector('[data-filter="category"]')?.value || '';
    const transmission = document.querySelector('[data-filter="transmission"]')?.value || '';
    const fuel = document.querySelector('[data-filter="fuel"]')?.value || '';
    const status = document.querySelector('[data-filter="status"]')?.value || '';
    const minPrice = Number(document.querySelector('[data-filter="min-price"]')?.value || 0);
    const maxPrice = Number(document.querySelector('[data-filter="max-price"]')?.value || Number.MAX_SAFE_INTEGER);
    const sort = document.querySelector('[data-filter="sort"]')?.value || 'newest';
    let matches = D.vehicles.filter(item => {
      const words = `${item.make} ${item.model} ${item.category}`.toLowerCase();
      return (!query || words.includes(query)) && (!make || item.make === make) && (!category || item.category === category) && (!transmission || item.transmission === transmission) && (!fuel || item.fuel === fuel) && (!status || item.status === status) && item.priceValue >= minPrice && item.priceValue <= maxPrice;
    });
    if (sort === 'price-low') matches.sort((a, b) => a.priceValue - b.priceValue);
    if (sort === 'price-high') matches.sort((a, b) => b.priceValue - a.priceValue);
    if (sort === 'newest') matches.sort((a, b) => b.year - a.year);
    const result = document.getElementById('vehicleResults');
    const count = document.getElementById('resultsCount');
    const activeFilters = document.getElementById('activeFilters');
    if (result) result.innerHTML = matches.length ? matches.map(item => `<div class="col-md-6 col-xl-4">${C.vehicleCard(item)}</div>`).join('') : `<div class="col-12">${C.emptyState('No vehicles found', 'Try changing your filters or clearing the current search.', 'fa-magnifying-glass')}</div>`;
    if (count) count.textContent = `Showing ${matches.length} ${matches.length === 1 ? 'vehicle' : 'vehicles'}`;
    if (activeFilters) {
      const labels = [query && `Search: ${query}`, make, category, fuel, transmission, status].filter(Boolean);
      activeFilters.innerHTML = labels.map(label => `<span class="active-filter">${label}</span>`).join('');
    }
  }

  function clearFilters() {
    document.querySelectorAll('[data-filter]').forEach(input => { if (input.tagName === 'SELECT') input.selectedIndex = 0; else input.value = ''; });
    filterVehicles();
  }

  function purchase(vehicleId) {
    const vehicle = D.vehicles.find(item => item.id === vehicleId);
    if (!vehicle || vehicle.quantity <= 0) { showToast('Vehicle unavailable', 'This vehicle is currently out of stock.', 'fa-circle-xmark'); return; }
    vehicle.quantity -= 1;
    setStatus(vehicle);
    showToast('Purchase request noted', `${vehicle.make} ${vehicle.model} now has ${vehicle.quantity} unit${vehicle.quantity === 1 ? '' : 's'} remaining.`, 'fa-bag-shopping');
    renderPage();
  }

  function changeStock(id, delta) {
    const vehicle = D.vehicles.find(item => item.id === id);
    if (!vehicle) return;
    vehicle.quantity = Math.max(0, vehicle.quantity + Number(delta));
    setStatus(vehicle);
    const quantity = document.querySelector(`[data-stock-count="${id}"]`);
    const status = document.querySelector(`[data-stock-status="${id}"]`);
    if (quantity) quantity.textContent = vehicle.quantity;
    if (status) status.innerHTML = C.statusBadge(vehicle.status);
    showToast('Inventory adjusted', `${vehicle.make} ${vehicle.model} quantity is now ${vehicle.quantity}.`, 'fa-boxes-stacked');
  }

  function switchGallery(image, button) {
    const main = document.getElementById('mainVehicleImage');
    if (!main) return;
    main.src = image;
    document.querySelectorAll('.gallery-thumb').forEach(item => item.classList.remove('active'));
    button.classList.add('active');
  }

  function toggleTheme() {
    document.documentElement.classList.toggle('lm');
    const light = document.documentElement.classList.contains('lm');
    document.querySelectorAll('[data-action="toggle-theme"] i').forEach(icon => { icon.className = `fa-solid ${light ? 'fa-sun' : 'fa-moon'}`; });
    if (window.dealerRevenueChart) {
      const grid = light ? 'rgba(0,0,0,.08)' : 'rgba(255,255,255,.06)';
      window.dealerRevenueChart.options.scales.y.grid.color = grid;
      window.dealerRevenueChart.update();
    }
  }

  document.addEventListener('click', (event) => {
    const control = event.target.closest('[data-action]');
    if (!control) return;
    const action = control.dataset.action;
    if (action === 'purchase') purchase(control.dataset.vehicleId);
    if (action === 'apply-filters') filterVehicles();
    if (action === 'clear-filters') clearFilters();
    if (action === 'gallery-image') switchGallery(control.dataset.image, control);
    if (action === 'toggle-theme') toggleTheme();
    if (action === 'toggle-sidebar') document.getElementById('adminSidebar')?.classList.toggle('open');
    if (action === 'stock-change') changeStock(control.dataset.id, control.dataset.delta);
    if (action === 'delete-mock') showToast('Delete action acknowledged', 'This is a frontend-only confirmation; the inventory record is unchanged.', 'fa-trash');
    if (action === 'toast-notifications') showToast('3 notifications', 'Two low-inventory warnings and one new purchase are waiting.', 'fa-bell');
    if (action === 'mock-toast') showToast('Demo action', 'This interface action is ready to be connected to Django later.', 'fa-sparkles');
  });

  document.addEventListener('change', (event) => { if (event.target.matches('[data-filter="sort"]')) filterVehicles(); });
  document.addEventListener('submit', (event) => {
    if (event.target.matches('[data-search-form]')) {
      event.preventDefault();
      const query = event.target.querySelector('[name="query"]')?.value || '';
      const make = event.target.querySelector('[name="make"]')?.value || '';
      const term = query || make || 'all vehicles';
      window.location.href = C.url(`pages/search-results.html?q=${encodeURIComponent(term)}`);
    }
    if (event.target.matches('[data-mock-form]')) {
      event.preventDefault();
      showToast('Form captured', 'This is a static frontend form. It is ready for Django form handling later.', 'fa-floppy-disk');
    }
  });

  window.addEventListener('scroll', () => document.getElementById('siteHeader')?.classList.toggle('is-scrolled', window.scrollY > 12), { passive: true });
  C.installShell(page);
  renderPage();
})();
