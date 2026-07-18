/* Reusable presentation components. Kept framework-free for future Django templates. */
window.DealerComponents = (() => {
  const data = window.DealerData;
  const root = () => document.body.dataset.root || '';
  const routeMap = () => {
    if (window.DealerRouteMap) return window.DealerRouteMap;
    const source = document.getElementById('dealer-url-map');
    if (!source) return {};
    try {
      window.DealerRouteMap = JSON.parse(source.textContent);
    } catch (error) {
      window.DealerRouteMap = {};
    }
    return window.DealerRouteMap;
  };
  const url = (path) => {
    const [, target, suffix = ''] = path.match(/^([^?#]+)(.*)$/) || [];
    const mapped = routeMap()[target || path];
    return mapped ? `${mapped}${suffix}` : `${root()}${path}`;
  };
  const authState = () => {
    if (window.DealerAuthState) return window.DealerAuthState;
    const source = document.getElementById('dealer-auth-state');
    if (!source) return {};
    try {
      window.DealerAuthState = JSON.parse(source.textContent);
    } catch (error) {
      window.DealerAuthState = {};
    }
    return window.DealerAuthState;
  };
  const csrfInput = () => {
    const token = authState().csrfToken || '';
    return token ? `<input type="hidden" name="csrfmiddlewaretoken" value="${token}">` : '';
  };
  const isAdminPage = (page) => ['dashboard', 'manage-vehicles', 'add-vehicle', 'update-vehicle', 'delete-confirmation', 'inventory-management', 'purchase-history', 'user-management', 'profile', 'settings'].includes(page);
  const active = (page, expected) => page === expected ? 'active' : '';

  function publicHeader(page) {
    return `
      <header class="site-header" id="siteHeader">
        <nav class="container navbar navbar-expand-lg p-0">
          <a class="navbar-brand d-flex align-items-center gap-2 m-0" href="${url('index.html')}" aria-label="Nexus Motors home">
            <span class="logo-mark"><i class="fa-solid fa-car-side"></i></span><span class="brand-name">Nexus<span class="text-gradient">Motors</span></span>
          </a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#publicNav" aria-controls="publicNav" aria-expanded="false" aria-label="Toggle navigation"><i class="fa-solid fa-bars"></i></button>
          <div class="collapse navbar-collapse" id="publicNav">
            <div class="navbar-nav mx-lg-auto align-items-lg-center gap-lg-1">
              <a class="site-nav-link ${active(page, 'home')}" href="${url('index.html')}">Home</a>
              <a class="site-nav-link ${active(page, 'inventory') || active(page, 'vehicle-details') || active(page, 'search-results')}" href="${url('pages/inventory.html')}">Inventory</a>
              <a class="site-nav-link ${active(page, 'about')}" href="${url('pages/about.html')}">About</a>
              <a class="site-nav-link ${active(page, 'contact')}" href="${url('pages/contact.html')}">Contact</a>
            </div>
            <div class="header-actions d-flex align-items-center gap-2">
              <button class="header-icon-btn" data-action="toggle-theme" aria-label="Toggle colour theme"><i class="fa-solid fa-moon"></i></button>
              ${authState().isSuperuser ? `<a class="btn-outline-dealer text-center" href="${url('pages/profile.html')}">Profile</a><a class="btn-primary-gradient text-center" href="${url('pages/dashboard.html')}">Dashboard <i class="fa-solid fa-arrow-right ms-1"></i></a><a class="btn-outline-dealer text-center" href="${url('pages/logout.html')}">Logout</a>` : `<a class="btn-primary-gradient text-center" href="${url('pages/login.html')}">Log in <i class="fa-solid fa-arrow-right ms-1"></i></a>`}
            </div>
          </div>
        </nav>
      </header>`;
  }

  function adminSidebar(page) {
    const nav = (target, label, icon, badge = '') => `<a class="admin-nav-link ${active(page, target)}" href="${url(`pages/${target === 'dashboard' ? 'dashboard' : target}.html`)}"><i class="fa-solid ${icon}"></i><span>${label}</span>${badge ? `<span class="sidebar-badge">${badge}</span>` : ''}</a>`;
    return `
      <aside class="admin-sidebar" id="adminSidebar" aria-label="Admin navigation">
        <div class="sidebar-head"><a class="d-flex align-items-center gap-2" href="${url('index.html')}"><span class="logo-mark"><i class="fa-solid fa-car-side"></i></span><span class="brand-name">Nexus<span class="text-gradient">Motors</span></span></a></div>
        <div class="side-caption">Operations</div>
        ${nav('dashboard', 'Dashboard', 'fa-grid-2')}
        ${nav('manage-vehicles', 'Vehicles', 'fa-car', '8')}
        ${nav('inventory-management', 'Inventory', 'fa-boxes-stacked', '2')}
        ${nav('purchase-history', 'Purchases', 'fa-receipt')}
        <div class="side-caption">Account</div>
        ${nav('user-management', 'Users', 'fa-users')}
        ${nav('settings', 'Settings', 'fa-gear')}
        ${nav('profile', 'Profile', 'fa-user-gear')}
        <div class="side-caption">Workspace</div>
        <a class="admin-nav-link" href="${url('pages/logout.html')}"><i class="fa-solid fa-arrow-right-from-bracket"></i><span>Log out</span></a>
      </aside>`;
  }

  function adminHeader() {
    return `
      <header class="admin-topbar">
        <div class="container-fluid d-flex align-items-center justify-content-between gap-3 px-3 px-md-4">
          <div class="d-flex align-items-center gap-3"><button class="header-icon-btn d-lg-none" data-action="toggle-sidebar" aria-label="Open admin navigation"><i class="fa-solid fa-bars"></i></button><div class="admin-topbar-search position-relative"><i class="fa-solid fa-magnifying-glass position-absolute top-50 translate-middle-y ms-3 muted small"></i><input class="form-control dealer-control ps-5" aria-label="Search dealership" placeholder="Search vehicles, purchases..."></div></div>
          <div class="d-flex align-items-center gap-2"><button class="header-icon-btn" data-action="toggle-theme" aria-label="Toggle colour theme"><i class="fa-solid fa-moon"></i></button><button class="header-icon-btn position-relative" data-action="toast-notifications" aria-label="View notifications"><i class="fa-regular fa-bell"></i><span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger">3</span></button><a class="topbar-avatar" href="${url('pages/profile.html')}" aria-label="Open profile">AM</a></div>
        </div>
      </header>`;
  }

  function footer() {
    return `
      <footer class="site-footer">
        <div class="container footer-main"><div class="row g-4">
          <div class="col-md-5 col-lg-4"><a class="d-flex align-items-center gap-2 mb-3" href="${url('index.html')}"><span class="logo-mark"><i class="fa-solid fa-car-side"></i></span><span class="brand-name">Nexus<span class="text-gradient">Motors</span></span></a><p class="footer-brand-text">A smarter way to discover trusted vehicles and manage dealership inventory with confidence.</p><div class="d-flex gap-2 mt-4"><a class="social-link" href="#" aria-label="Instagram"><i class="fa-brands fa-instagram"></i></a><a class="social-link" href="#" aria-label="Facebook"><i class="fa-brands fa-facebook-f"></i></a><a class="social-link" href="#" aria-label="LinkedIn"><i class="fa-brands fa-linkedin-in"></i></a></div></div>
          <div class="col-6 col-md-2"><div class="footer-title">Company</div><a class="footer-link" href="${url('pages/about.html')}">About us</a><a class="footer-link" href="${url('pages/contact.html')}">Contact</a><a class="footer-link" href="${url('pages/404.html')}">Careers</a></div>
          <div class="col-6 col-md-2"><div class="footer-title">Inventory</div><a class="footer-link" href="${url('pages/inventory.html')}">Browse vehicles</a><a class="footer-link" href="${url('pages/search-results.html')}">Search vehicles</a><a class="footer-link" href="${url('pages/dashboard.html')}">Dealer portal</a></div>
          <div class="col-6 col-md-2"><div class="footer-title">Support</div><a class="footer-link" href="${url('pages/contact.html')}">Get help</a><a class="footer-link" href="${url('pages/404.html')}">Privacy</a><a class="footer-link" href="${url('pages/404.html')}">Terms</a></div>
          <div class="col-6 col-md-2"><div class="footer-title">Contact</div><span class="footer-link">+1 800 654 0321</span><span class="footer-link">hello@nexusmotors.test</span><span class="footer-link">08:00 19:00, Mon Sat</span></div>
        </div></div><div class="container footer-bottom d-flex flex-column flex-sm-row gap-2 justify-content-between"><span>  2026 Nexus Motors. Frontend demonstration.</span><span>Trusted inventory. Confident decisions.</span></div>
      </footer>`;
  }

  function testDriveModal() {
    return `
      <div class="modal fade dealer-modal" id="testDriveModal" tabindex="-1" aria-labelledby="testDriveModalTitle" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
          <div class="modal-content">
            <div class="modal-header border-0 pb-0"><div><div class="page-kicker mb-1">Test drive request</div><h2 class="modal-title fs-4 fw-bold" id="testDriveModalTitle">Book a test drive</h2></div><button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button></div>
            <form id="testDriveForm" data-mock-form>
              <div class="modal-body pt-3"><p class="muted small mb-4">Tell us when you would like to experience <strong class="text-white" id="testDriveVehicleName">this vehicle</strong>. This is a frontend-only request.</p><input type="hidden" id="testDriveVehicle" name="vehicle"><div class="row g-3"><div class="col-md-6"><label class="form-label form-label-dealer" for="testDriveName">Your name</label><input class="form-control dealer-control" id="testDriveName" name="name" autocomplete="name" placeholder="Alex Morgan" required></div><div class="col-md-6"><label class="form-label form-label-dealer" for="testDrivePhone">Phone number</label><input class="form-control dealer-control" id="testDrivePhone" name="phone" autocomplete="tel" placeholder="+1 555 012 3456" required></div><div class="col-12"><label class="form-label form-label-dealer" for="testDriveEmail">Email address</label><input class="form-control dealer-control" type="email" id="testDriveEmail" name="email" autocomplete="email" placeholder="alex@example.com" required></div><div class="col-12"><label class="form-label form-label-dealer" for="testDriveDate">Preferred date</label><input class="form-control dealer-control" type="date" id="testDriveDate" name="preferred_date" required></div></div></div>
              <div class="modal-footer border-0 pt-0"><button type="button" class="btn-outline-dealer" data-bs-dismiss="modal">Cancel</button><button class="btn-primary-gradient" type="submit"><i class="fa-regular fa-calendar-check me-1"></i>Request test drive</button></div>
            </form>
          </div>
        </div>
      </div>`;
  }

  function installShell(page) {
    const header = document.querySelector('[data-site-header]');
    const footerTarget = document.querySelector('[data-site-footer]');
    if (isAdminPage(page)) {
      document.body.classList.add('admin-body');
      header.innerHTML = `${adminSidebar(page)}${adminHeader()}`;
      footerTarget.remove();
    } else {
      header.innerHTML = publicHeader(page);
      footerTarget.innerHTML = footer();
    }
    if (!document.getElementById('testDriveModal')) document.body.insertAdjacentHTML('beforeend', testDriveModal());
  }

  function statusBadge(status) {
    const map = { Available: 'stock-available', 'Low Stock': 'stock-low', 'Out of Stock': 'stock-out', Completed: 'stock-available', Processing: 'stock-low', Active: 'stock-available', Inactive: 'stock-out' };
    return `<span class="stock-badge ${map[status] || 'tag-badge'}">${status === 'Available' ? '<i class="fa-solid fa-circle fa-2xs"></i>' : ''}${status}</span>`;
  }

  function vehicleCard(vehicle) {
    const tags = vehicle.labels.map(label => `<span class="mini-badge tag-badge">${label}</span>`).join('');
    const canPurchase = vehicle.quantity > 0;
    return `
      <article class="vehicle-card" data-vehicle-card="${vehicle.id}">
        <div class="vehicle-media"><img src="${vehicle.image}" alt="${vehicle.year} ${vehicle.make} ${vehicle.model}" loading="lazy"><div class="vehicle-badges">${statusBadge(vehicle.status)}${tags}</div></div>
        <div class="vehicle-card-body"><div class="d-flex justify-content-between gap-2 align-items-start"><div><div class="vehicle-category">${vehicle.category}</div><a class="vehicle-title" href="${url(`pages/vehicle-details.html?id=${vehicle.id}`)}">${vehicle.make} ${vehicle.model}</a></div><div class="text-end"><div class="vehicle-price">${vehicle.price}</div><small class="muted">${vehicle.quantity} in stock</small></div></div>
          <div class="vehicle-meta"><span><i class="fa-regular fa-calendar"></i>${vehicle.year}</span><span><i class="fa-solid fa-gas-pump"></i>${vehicle.fuel}</span><span><i class="fa-solid fa-gear"></i>${vehicle.transmission}</span></div>
          <div class="d-flex gap-2"><a class="btn-outline-dealer flex-grow-1 text-center" href="${url(`pages/vehicle-details.html?id=${vehicle.id}`)}">Details</a><button class="btn-primary-gradient flex-grow-1 purchase-button" data-action="purchase" data-vehicle-id="${vehicle.id}" ${canPurchase ? '' : 'disabled'}>${canPurchase ? 'Purchase' : 'Sold out'}</button></div>
        </div>
      </article>`;
  }

  function statCard(icon, value, label, change, down = false) {
    return `<div class="stat-card"><div class="d-flex align-items-start justify-content-between"><div class="stat-card-icon"><i class="fa-solid ${icon}"></i></div><span class="stat-change ${down ? 'down' : ''}">${change}</span></div><div class="stat-value">${value}</div><div class="stat-label">${label}</div></div>`;
  }

  function breadcrumb(items) { return `<nav aria-label="Breadcrumb"><ol class="breadcrumb breadcrumb-dealer">${items.map((item, index) => `<li class="breadcrumb-item ${index === items.length - 1 ? 'active' : ''}">${index === items.length - 1 ? item.label : `<a href="${url(item.href)}">${item.label}</a>`}</li>`).join('')}</ol></nav>`; }

  function pageHero(kicker, title, text, crumbs) {
    return `<section class="page-hero"><div class="container"><div class="row align-items-end g-3"><div class="col-lg-8"><div class="page-kicker">${kicker}</div><h1 class="page-title">${title}</h1><p class="muted mb-0">${text}</p></div><div class="col-lg-4 d-lg-flex justify-content-lg-end">${breadcrumb(crumbs)}</div></div></div></section>`;
  }

  function filterPanel() {
    return `<aside class="filter-panel" aria-label="Vehicle filters"><div class="d-flex justify-content-between align-items-center mb-4"><h2 class="filter-panel-title mb-0">Filter inventory</h2><button class="btn btn-link form-link p-0" data-action="clear-filters">Reset</button></div>
      <div class="mb-3"><label class="filter-label" for="inventorySearch">Search</label><input class="form-control dealer-control" id="inventorySearch" data-filter="query" placeholder="Make, model, or keyword"></div>
      <div class="mb-3"><label class="filter-label" for="filterMake">Make</label><select class="form-select dealer-select" id="filterMake" data-filter="make"><option value="">All makes</option>${data.brands.map(brand => `<option>${brand}</option>`).join('')}</select></div>
      <div class="mb-3"><label class="filter-label" for="filterCategory">Category</label><select class="form-select dealer-select" id="filterCategory" data-filter="category"><option value="">All categories</option><option>Luxury SUV</option><option>Luxury Sedan</option><option>Electric SUV</option><option>Premium SUV</option><option>Performance Coupe</option><option>Family SUV</option></select></div>
      <div class="row g-2 mb-3"><div class="col-6"><label class="filter-label" for="filterMinPrice">Min price</label><input class="form-control dealer-control" type="number" id="filterMinPrice" data-filter="min-price" placeholder="$20k"></div><div class="col-6"><label class="filter-label" for="filterMaxPrice">Max price</label><input class="form-control dealer-control" type="number" id="filterMaxPrice" data-filter="max-price" placeholder="$80k"></div></div>
      <div class="mb-3"><label class="filter-label" for="filterTransmission">Transmission</label><select class="form-select dealer-select" id="filterTransmission" data-filter="transmission"><option value="">All types</option><option>Automatic</option><option>Manual</option></select></div>
      <div class="mb-3"><label class="filter-label" for="filterFuel">Fuel type</label><select class="form-select dealer-select" id="filterFuel" data-filter="fuel"><option value="">All fuel types</option><option>Petrol</option><option>Diesel</option><option>Electric</option></select></div>
      <div class="mb-4"><label class="filter-label" for="filterAvailability">Availability</label><select class="form-select dealer-select" id="filterAvailability" data-filter="status"><option value="">Any availability</option><option>Available</option><option>Low Stock</option><option>Out of Stock</option></select></div>
      <button class="btn-primary-gradient w-100" data-action="apply-filters"><i class="fa-solid fa-sliders me-1"></i>Apply filters</button></aside>`;
  }

  function emptyState(title, text, icon = 'fa-car') { return `<div class="empty-state"><div class="empty-state-icon"><i class="fa-solid ${icon}"></i></div><h3 class="fs-5 fw-bold">${title}</h3><p class="muted small mb-0">${text}</p></div>`; }

  function adminPageHeader(title, subtitle, crumb) { return `<div class="d-flex flex-column flex-md-row align-items-md-end justify-content-between gap-3 mb-4"><div><div class="tiny-label mb-2">Dealer operations</div><h1 class="admin-page-title mb-1">${title}</h1><p class="muted small mb-0">${subtitle}</p></div>${breadcrumb([{ label: 'Admin', href: 'pages/dashboard.html' }, { label: crumb || title }])}</div>`; }

  return { data, url, root, authState, csrfInput, isAdminPage, installShell, vehicleCard, statCard, statusBadge, breadcrumb, pageHero, filterPanel, emptyState, adminPageHeader };
})();
