/* Django integration layer for database-backed pages and POST workflows. */
(function () {
  const C = window.DealerComponents;
  const originalPages = window.DealerPages;
  const D = window.DealerData || {};

  if (!C || !originalPages) return;

  const vehicles = () => D.vehicles || [];
  const purchases = () => D.purchases || [];
  const userPurchases = () => D.userPurchases || purchases();
  const users = () => D.users || [];
  const stats = () => D.stats || {};
  const money = (value) => value || '$0';
  const number = (value) => Number(value || 0).toLocaleString();

  function postForm(action, fields) {
    const form = document.createElement('form');
    form.method = 'post';
    form.action = action;
    form.style.display = 'none';
    form.insertAdjacentHTML('beforeend', C.csrfInput());
    Object.entries(fields).forEach(([name, value]) => {
      const input = document.createElement('input');
      input.type = 'hidden';
      input.name = name;
      input.value = value;
      form.appendChild(input);
    });
    document.body.appendChild(form);
    form.submit();
  }

  function hydrateFilters() {
    const params = new URLSearchParams(window.location.search);
    const mapping = {
      query: params.get('query') || params.get('q') || '',
      make: params.get('make') || '',
      model: params.get('model') || '',
      category: params.get('category') || '',
      'min-price': params.get('min_price') || '',
      'max-price': params.get('max_price') || params.get('budget') || '',
      status: params.get('availability') || params.get('status') || ''
    };
    Object.entries(mapping).forEach(([key, value]) => {
      const field = document.querySelector(`[data-filter="${key}"]`);
      if (field) field.value = value;
    });
  }

  function searchUrlFromControls() {
    const params = new URLSearchParams();
    const add = (name, selector) => {
      const value = document.querySelector(selector)?.value?.trim();
      if (value) params.set(name, value);
    };
    add('query', '[data-filter="query"]');
    add('make', '[data-filter="make"]');
    add('model', '[data-filter="model"]');
    add('category', '[data-filter="category"]');
    add('min_price', '[data-filter="min-price"]');
    add('max_price', '[data-filter="max-price"]');
    add('availability', '[data-filter="status"]');
    const query = params.toString();
    return `${C.url('pages/search-results.html')}${query ? `?${query}` : ''}`;
  }

  function emptyRow(message, colspan, icon = 'fa-circle-info') {
    return `<tr><td colspan="${colspan}">${C.emptyState(message, 'Records will appear here as soon as matching SQLite data exists.', icon)}</td></tr>`;
  }

  function recentVehicleList() {
    const items = vehicles().slice(0, 5);
    if (!items.length) return C.emptyState('No vehicles yet', 'Add vehicles to populate dashboard inventory widgets.');
    return `<div class="list-group list-group-flush bg-transparent">${items.map(item => `<a class="list-group-item dealer-list-item d-flex align-items-center gap-3" href="${C.url(`pages/vehicle-details.html?id=${item.id}`)}"><span class="table-car-thumb"><img src="${item.image}" alt="${item.make} ${item.model}"></span><span class="flex-grow-1"><strong>${item.make} ${item.model}</strong><small>${item.category} · ${item.quantity} in stock</small></span>${C.statusBadge(item.status)}</a>`).join('')}</div>`;
  }

  function activityList() {
    const purchaseItems = purchases().slice(0, 4).map(item => ({ type: 'purchase', date: item.date, title: item.customer, text: `Purchased ${item.quantity} × ${item.vehicle} for ${item.total}` }));
    const registrationItems = users().slice(0, 4).map(user => ({ type: 'user', date: user.joinedAt, title: user.name, text: `New account registered as ${user.role}` }));
    const items = [...purchaseItems, ...registrationItems].slice(0, 5);
    if (!items.length) return C.emptyState('No recent purchases', 'Completed purchases and new registrations will appear here automatically.', 'fa-receipt');
    return `<div class="activity-list">${items.map(item => `<div class="activity-item"><span class="activity-dot"></span><div><strong>${item.title}</strong><p>${item.text}</p><small>${item.date}</small></div></div>`).join('')}</div>`;
  }

  function dashboard() {
    const s = stats();
    const lowStock = vehicles().filter(item => item.quantity > 0 && item.quantity <= 2);
    const outStock = vehicles().filter(item => item.quantity <= 0);
    const alertText = [...lowStock, ...outStock].slice(0, 3).map(item => `${item.make} ${item.model}`).join(', ') || 'No critical inventory alerts';
    return `<div class="admin-content"><div class="container-fluid p-0">${C.adminPageHeader(`Good morning, ${C.displayName()}`, 'Here is what is happening across your dealership today.', 'Dashboard')}<div class="row g-3 mb-4"><div class="col-6 col-xl-2">${C.statCard('fa-car', number(s.totalVehicles), 'Total vehicles', 'From SQLite')}</div><div class="col-6 col-xl-2">${C.statCard('fa-circle-check', number(s.availableStock), 'Available stock', `${number(s.totalUnits)} total units`)}</div><div class="col-6 col-xl-2">${C.statCard('fa-circle-xmark', number(s.outOfStock), 'Out of stock', `${number(s.lowStock)} low stock`, s.outOfStock > 0)}</div><div class="col-6 col-xl-2">${C.statCard('fa-receipt', number(s.totalPurchases), 'Total purchases', 'Stored records')}</div><div class="col-6 col-xl-2">${C.statCard('fa-users', number(s.totalUsers), 'Total users', 'Registered accounts')}</div><div class="col-6 col-xl-2">${C.statCard('fa-dollar-sign', money(s.revenue), 'Revenue', 'Completed purchases')}</div></div><div class="row g-4"><div class="col-xl-8"><div class="chart-card h-100"><div class="d-flex justify-content-between align-items-center mb-3"><div><h3 class="mb-1">Revenue overview</h3><span class="muted small">Purchase revenue placeholder chart with live total cards</span></div><span class="stock-badge stock-available">${money(s.revenue)}</span></div><div class="chart-holder"><canvas id="revenueChart" aria-label="Revenue placeholder chart"></canvas></div></div></div><div class="col-xl-4"><div class="chart-card h-100"><h3 class="mb-1">Quick actions</h3><p class="muted small mb-3">Keep operations moving.</p><div class="d-grid gap-2"><a class="btn-primary-gradient text-center" href="${C.url('pages/add-vehicle.html')}"><i class="fa-solid fa-plus me-1"></i>Add vehicle</a><a class="btn-outline-dealer text-center" href="${C.url('pages/inventory-management.html')}"><i class="fa-solid fa-boxes-stacked me-1"></i>Update inventory</a><a class="btn-outline-dealer text-center" href="${C.url('pages/invite-user.html')}"><i class="fa-solid fa-user-plus me-1"></i>Invite user</a><a class="btn-outline-dealer text-center" href="${C.url('pages/user-management.html')}"><i class="fa-solid fa-users me-1"></i>Manage users</a></div><div class="alert-card mt-4"><i class="fa-solid fa-triangle-exclamation"></i><div><strong class="small">${number(Number(s.lowStock || 0) + Number(s.outOfStock || 0))} inventory alerts</strong><p>${alertText}</p></div></div></div></div><div class="col-xl-7"><div class="chart-card"><div class="d-flex justify-content-between align-items-center mb-2"><h3 class="mb-0">Recent vehicles</h3><a class="form-link" href="${C.url('pages/manage-vehicles.html')}">Manage all</a></div>${recentVehicleList()}</div></div><div class="col-xl-5"><div class="chart-card"><div class="d-flex justify-content-between align-items-center mb-2"><h3 class="mb-0">Recent activity</h3><span class="tiny-label">SQLite</span></div>${activityList()}</div></div></div></div></div>`;
  }

  function inventoryManagement() {
    const s = stats();
    const alerts = vehicles().filter(item => item.quantity <= 2);
    const alertText = alerts.length ? `${alerts.length} vehicle${alerts.length === 1 ? '' : 's'} need attention: ${alerts.slice(0, 3).map(item => `${item.make} ${item.model}`).join(', ')}.` : 'All vehicles are currently above the low-stock threshold.';
    const rows = vehicles().map(item => `<tr><td><div class="d-flex align-items-center gap-3"><span class="table-car-thumb"><img src="${item.image}" alt="${item.make} ${item.model}"></span><div><div class="table-primary">${item.make} ${item.model}</div><div class="table-subtitle">${item.category}</div></div></div></td><td><span class="quantity-control"><button data-action="mock-toast" aria-label="Decrease disabled">−</button><strong data-stock-count="${item.id}">${item.quantity}</strong><button data-action="stock-change" data-id="${item.id}" data-delta="1" aria-label="Increase ${item.model} stock">+</button></span></td><td>${C.statusBadge(item.status)}</td><td>${item.updatedAt}</td><td class="text-end"><button class="btn-outline-dealer py-1 px-2" data-action="stock-change" data-id="${item.id}" data-delta="5">Restock +5</button></td></tr>`).join('');
    return `<div class="admin-content"><div class="container-fluid p-0">${C.adminPageHeader('Inventory management', 'Adjust stock quantities and act on low-inventory alerts.', 'Inventory')}<div class="row g-4 mb-4"><div class="col-lg-8"><div class="alert-card h-100"><i class="fa-solid fa-triangle-exclamation fa-lg"></i><div><strong>Low inventory alert</strong><p>${alertText}</p></div><a class="form-link ms-auto text-nowrap" href="#stockTable">Review stock</a></div></div><div class="col-lg-4">${C.statCard('fa-boxes-stacked', number(s.totalUnits), 'Total units available', `Across ${number(s.totalVehicles)} vehicle lines`)}</div></div><div class="admin-table-wrap" id="stockTable"><table class="table admin-table"><thead><tr><th>Vehicle</th><th>Current quantity</th><th>Availability</th><th>Last updated</th><th class="text-end">Stock actions</th></tr></thead><tbody>${rows || emptyRow('No inventory records found', 5, 'fa-boxes-stacked')}</tbody></table></div></div></div>`;
  }

  function purchaseHistory() {
    const data = C.authState().isSuperuser ? purchases() : userPurchases();
    const s = stats();
    const title = C.authState().isSuperuser ? 'Purchase history' : 'My purchases';
    const subtitle = C.authState().isSuperuser ? 'Review vehicle purchases and their current fulfilment status.' : 'Review the vehicles purchased through your Nexus Motors account.';
    const header = C.authState().isSuperuser ? C.adminPageHeader(title, subtitle, 'Purchases') : C.pageHero('Purchase history', 'Your <span class="text-gradient">purchases.</span>', subtitle, [{ label: 'Home', href: 'index.html' }, { label: 'Purchases' }]);
    const rows = data.map(item => `<tr><td class="table-primary">${item.code}</td><td>${item.customer}</td><td><div class="d-flex align-items-center gap-3"><span class="table-car-thumb"><img src="${item.vehicleImage}" alt="${item.vehicle}"></span><div><div class="table-primary">${item.vehicle}</div><div class="table-subtitle">Vehicle purchase</div></div></div></td><td class="table-primary">${item.price}</td><td>${item.quantity}</td><td>${item.date}</td><td>${C.statusBadge(item.status)}</td></tr>`).join('');
    return `${C.authState().isSuperuser ? '<div class="admin-content"><div class="container-fluid p-0">' : ''}${header}<section class="${C.authState().isSuperuser ? '' : 'section-pad'}"><div class="${C.authState().isSuperuser ? '' : 'container'}"><div class="row g-3 mb-4"><div class="col-md-4">${C.statCard('fa-receipt', number(data.length), 'Purchase records', 'Newest first')}</div><div class="col-md-4">${C.statCard('fa-clock', '0', 'Pending fulfilment', 'All completed')}</div><div class="col-md-4">${C.statCard('fa-dollar-sign', C.authState().isSuperuser ? money(s.revenue) : money(data.reduce((sum, item) => sum + Number(item.totalValue || 0), 0) ? `$${data.reduce((sum, item) => sum + Number(item.totalValue || 0), 0).toLocaleString()}` : '$0'), 'Revenue', 'Completed purchases')}</div></div><div class="admin-table-wrap"><table class="table admin-table"><thead><tr><th>Purchase ID</th><th>Customer</th><th>Vehicle</th><th>Price</th><th>Quantity</th><th>Date</th><th>Status</th></tr></thead><tbody>${rows || emptyRow('No purchases yet', 7, 'fa-receipt')}</tbody></table></div></div></section>${C.authState().isSuperuser ? '</div></div>' : ''}`;
  }

  function userManagement() {
    const rows = users().map(user => `<tr><td><div class="d-flex align-items-center gap-3"><span class="avatar-circle">${user.initials}</span><div><div class="table-primary">${user.name}</div><div class="table-subtitle">${user.email || user.username}</div></div></div></td><td><span class="mini-badge tag-badge">${user.role}</span></td><td>${C.statusBadge(user.status)}</td><td>${user.lastLogin}</td><td class="text-end">${user.isSuperuser ? '<button class="action-icon delete ms-1" disabled aria-label="Superuser protected"><i class="fa-solid fa-shield-halved"></i></button>' : `<form class="d-inline" method="post" action="${C.url('actions/deactivate-user.html')}" onsubmit="return confirm('Deactivate this user account?');">${C.csrfInput()}<input type="hidden" name="user_id" value="${user.id}"><button class="action-icon delete ms-1" type="submit" aria-label="Deactivate ${user.name}"><i class="fa-solid fa-user-xmark"></i></button></form>`}</td></tr>`).join('');
    return `<div class="admin-content"><div class="container-fluid p-0">${C.adminPageHeader('User management', 'Manage customer and internal dealership accounts.', 'Users')}<div class="d-flex flex-column flex-md-row gap-2 justify-content-between mb-4"><div class="position-relative"><i class="fa-solid fa-magnifying-glass position-absolute top-50 translate-middle-y ms-3 muted small"></i><input class="form-control dealer-control ps-5" placeholder="Search users"></div><a class="btn-primary-gradient text-center" href="${C.url('pages/invite-user.html')}"><i class="fa-solid fa-user-plus me-1"></i>Invite user</a></div><div class="admin-table-wrap"><table class="table admin-table"><thead><tr><th>User</th><th>Role</th><th>Status</th><th>Last login</th><th class="text-end">Actions</th></tr></thead><tbody>${rows || emptyRow('No users found', 5, 'fa-users')}</tbody></table></div></div></div>`;
  }

  function inviteUser() {
    return `<div class="admin-content"><div class="container-fluid p-0">${C.adminPageHeader('Invite user', 'Create a new customer or staff account for the Nexus Motors platform.', 'Invite user')}<form method="post" action="${C.url('pages/invite-user.html')}" novalidate>${C.csrfInput()}<div class="row g-4"><div class="col-xl-8"><div class="admin-form-card"><h2>Account details</h2><div class="row g-3"><div class="col-md-6"><label class="form-label form-label-dealer" for="inviteFirstName">First name</label><input class="form-control dealer-control" id="inviteFirstName" name="first_name" autocomplete="given-name" placeholder="Alex" required></div><div class="col-md-6"><label class="form-label form-label-dealer" for="inviteLastName">Last name</label><input class="form-control dealer-control" id="inviteLastName" name="last_name" autocomplete="family-name" placeholder="Morgan" required></div><div class="col-md-6"><label class="form-label form-label-dealer" for="inviteUsername">Username</label><input class="form-control dealer-control" id="inviteUsername" name="username" autocomplete="username" placeholder="alexmorgan" required></div><div class="col-md-6"><label class="form-label form-label-dealer" for="inviteEmail">Email address</label><input class="form-control dealer-control" type="email" id="inviteEmail" name="email" autocomplete="email" placeholder="alex@example.com" required></div><div class="col-md-6"><label class="form-label form-label-dealer" for="invitePassword">Password</label><input class="form-control dealer-control" type="password" id="invitePassword" name="password1" autocomplete="new-password" placeholder=" " required><div class="form-help">Use a strong password that is not similar to personal information.</div></div><div class="col-md-6"><label class="form-label form-label-dealer" for="inviteConfirmPassword">Confirm password</label><input class="form-control dealer-control" type="password" id="inviteConfirmPassword" name="password2" autocomplete="new-password" placeholder=" " required></div></div><div class="form-section-rule"></div><h2>Account permissions</h2><div class="setting-row"><div class="info-icon"><i class="fa-solid fa-circle-check"></i></div><div class="flex-grow-1"><h4>Active account</h4><p>Allow this user to sign in immediately after creation.</p></div><div class="form-check form-switch"><input class="form-check-input" id="inviteActive" type="checkbox" name="is_active" checked><label class="visually-hidden" for="inviteActive">Active account</label></div></div><div class="setting-row"><div class="info-icon"><i class="fa-solid fa-user-shield"></i></div><div class="flex-grow-1"><h4>Staff access</h4><p>Grant staff permissions for internal dealership tools. Superuser access is never assigned here.</p></div><div class="form-check form-switch"><input class="form-check-input" id="inviteStaff" type="checkbox" name="is_staff"><label class="visually-hidden" for="inviteStaff">Staff access</label></div></div></div></div><div class="col-xl-4"><div class="admin-form-card"><h2>Before you invite</h2><p class="muted small">New accounts are stored securely in SQLite with hashed passwords. Duplicate usernames and emails are rejected automatically.</p><div class="form-section-rule"></div><div class="d-grid gap-2"><button class="btn-primary-gradient py-3" type="submit"><i class="fa-solid fa-user-plus me-1"></i>Create account</button><a class="btn-outline-dealer py-3 text-center" href="${C.url('pages/user-management.html')}">Cancel</a></div></div></div></div></form></div></div>`;
  }

  function userDashboard() {
    const auth = C.authState();
    const data = userPurchases();
    const totalSpent = data.reduce((sum, item) => sum + Number(item.totalValue || 0), 0);
    const recentRows = data.slice(0, 4).map(item => `<tr><td><div class="d-flex align-items-center gap-3"><span class="table-car-thumb"><img src="${item.vehicleImage}" alt="${item.vehicle}"></span><div><div class="table-primary">${item.vehicle}</div><div class="table-subtitle">${item.date}</div></div></div></td><td>${item.quantity}</td><td class="table-primary">${item.total}</td><td>${C.statusBadge(item.status)}</td></tr>`).join('');
    return `${C.pageHero('Customer dashboard', `Welcome back, <span class="text-gradient">${C.displayName()}</span>`, 'Track your purchases, profile details and quick actions from one secure customer workspace.', [{ label: 'Home', href: 'index.html' }, { label: 'Dashboard' }])}<section class="section-pad"><div class="container"><div class="row g-3 mb-4"><div class="col-md-4">${C.statCard('fa-receipt', number(data.length), 'Total purchases', 'Your account')}</div><div class="col-md-4">${C.statCard('fa-dollar-sign', `$${totalSpent.toLocaleString()}`, 'Total spent', 'Completed purchases')}</div><div class="col-md-4">${C.statCard('fa-user-shield', 'Active', 'Session status', auth.username || 'Logged in')}</div></div><div class="row g-4"><div class="col-xl-8"><div class="admin-table-wrap"><table class="table admin-table"><thead><tr><th>Vehicle</th><th>Quantity</th><th>Total</th><th>Status</th></tr></thead><tbody>${recentRows || emptyRow('No purchases yet', 4, 'fa-car')}</tbody></table></div></div><div class="col-xl-4"><div class="chart-card h-100"><h3 class="mb-1">Quick actions</h3><p class="muted small mb-3">Continue your dealership journey.</p><div class="d-grid gap-2"><a class="btn-primary-gradient text-center" href="${C.url('pages/inventory.html')}"><i class="fa-solid fa-car me-1"></i>Browse inventory</a><a class="btn-outline-dealer text-center" href="${C.url('pages/purchase-history.html')}"><i class="fa-solid fa-receipt me-1"></i>Purchase history</a><a class="btn-outline-dealer text-center" href="${C.url('pages/user-profile.html')}"><i class="fa-solid fa-user me-1"></i>Profile settings</a><a class="btn-outline-dealer text-center" href="${C.url('pages/logout.html')}"><i class="fa-solid fa-arrow-right-from-bracket me-1"></i>Logout</a></div></div></div></div></div></section>`;
  }

  function home() {
    const s = stats();
    const featured = vehicles().slice(0, 3);
    const latest = vehicles().slice(3, 6);
    const cardGrid = (items, id) => `<div class="row g-4" id="${id}">${items.map(item => `<div class="col-md-6 col-xl-4">${C.vehicleCard(item)}</div>`).join('')}</div>`;
    const availablePct = s.totalVehicles ? Math.round((s.availableVehicleLines / s.totalVehicles) * 100) : 0;
    return `
      <section class="dealer-hero"><div class="container position-relative"><div class="hero-copy" data-aos="fade-up"><span class="hero-overline"><span class="live-dot"></span> ${number(s.availableStock)} units ready across ${number(s.totalVehicles)} listings</span><h1 class="hero-title">Find the vehicle that <span class="text-gradient">moves you.</span></h1><p class="hero-description">Explore a trusted collection of premium, certified and carefully inspected vehicles   all in one seamless dealership experience.</p>
        <form class="hero-search" data-search-form><div class="row g-0 align-items-center"><div class="col-lg-4 hero-search-field"><label for="homeSearch">What are you looking for?</label><input id="homeSearch" class="form-control" name="query" placeholder="SUV, electric, BMW..."></div><div class="col-lg-3 hero-search-field"><label for="homeMake">Make</label><select id="homeMake" name="make" class="form-select"><option value="">Any make</option>${(D.brands || []).map(brand => `<option>${brand}</option>`).join('')}</select></div><div class="col-lg-3 hero-search-field"><label for="homeBudget">Budget</label><select id="homeBudget" name="budget" class="form-select"><option value="">Any budget</option><option value="40000">Up to $40,000</option><option value="60000">Up to $60,000</option><option value="80000">Up to $80,000</option></select></div><div class="col-lg-2 ps-lg-2 pt-2 pt-lg-0"><button class="btn-primary-gradient w-100 py-3" type="submit"><i class="fa-solid fa-magnifying-glass me-1"></i> Search</button></div></div></form>
        <div class="row g-3 hero-quick-stat"><div class="col-4"><strong>${number(s.totalVehicles)}</strong><span class="d-block">Vehicles listed</span></div><div class="col-4"><strong>${availablePct}%</strong><span class="d-block">In stock</span></div><div class="col-4"><strong>${money(s.inventoryValue)}</strong><span class="d-block">Inventory value</span></div></div>
      </div></div></section>
      <section class="section-pad"><div class="container"><div class="row g-3 text-center"><div class="col-6 col-lg-3" data-aos="fade-up">${C.statCard('fa-car', number(s.totalVehicles), 'Vehicles in inventory', 'From SQLite')}</div><div class="col-6 col-lg-3" data-aos="fade-up" data-aos-delay="60">${C.statCard('fa-circle-check', number(s.availableStock), 'Ready to drive', `${availablePct}% available`)}</div><div class="col-6 col-lg-3" data-aos="fade-up" data-aos-delay="120">${C.statCard('fa-circle-xmark', number(s.outOfStock), 'Out of stock', `${number(s.lowStock)} low stock`, s.outOfStock > 0)}</div><div class="col-6 col-lg-3" data-aos="fade-up" data-aos-delay="180">${C.statCard('fa-receipt', number(s.totalPurchases), 'Completed purchases', money(s.revenue))}</div></div></div></section>
      <section class="pb-5"><div class="container"><div class="d-flex flex-column flex-md-row align-items-md-end justify-content-between gap-3 mb-4"><div data-aos="fade-up"><div class="page-kicker">Featured collection</div><h2 class="stitle mb-2">Vehicles worth a <span class="text-gradient">closer look.</span></h2><p class="muted mb-0">Verified stock, transparent details and a selection made for every drive.</p></div><a class="btn-outline-dealer" href="${C.url('pages/inventory.html')}">Explore all vehicles <i class="fa-solid fa-arrow-right ms-1"></i></a></div>${cardGrid(featured, 'featuredVehicles')}</div></section>
      <section class="section-pad pt-4"><div class="container"><div class="d-flex flex-column flex-md-row align-items-md-end justify-content-between gap-3 mb-4"><div><div class="page-kicker">Latest arrivals</div><h2 class="stitle mb-2">Fresh on the <span class="text-gradient">forecourt.</span></h2></div><a href="${C.url('pages/search-results.html')}" class="form-link">View search results <i class="fa-solid fa-arrow-right ms-1"></i></a></div>${cardGrid(latest, 'latestVehicles')}</div></section>`;
  }

  function vehicleDetails() {
    const params = new URLSearchParams(window.location.search);
    const vehicle = vehicles().find(item => String(item.id) === String(params.get('id'))) || vehicles()[0];
    if (!vehicle) return C.emptyState('Vehicle not found', 'This vehicle is no longer in inventory.', 'fa-car');
    const auth = C.authState();
    const purchaseHelp = auth.isAuthenticated
      ? 'Purchases are recorded in SQLite and inventory is updated immediately.'
      : `<a class="form-link" href="${C.url('pages/login.html')}">Log in</a> to complete a purchase.`;
    return `${C.pageHero('Vehicle details', `${vehicle.make} <span class="text-gradient">${vehicle.model}</span>`, `${vehicle.year}   ${vehicle.category}   ${vehicle.mileage}`, [{ label: 'Home', href: 'index.html' }, { label: 'Inventory', href: 'pages/inventory.html' }, { label: `${vehicle.make} ${vehicle.model}` }])}<section class="section-pad"><div class="container"><div class="row g-4 align-items-start"><div class="col-lg-7"><div class="gallery-main"><img id="mainVehicleImage" src="${vehicle.gallery[0]}" alt="${vehicle.make} ${vehicle.model}"></div><article class="surface-card p-4 p-md-5 mt-4"><div class="page-kicker">Overview</div><h2 class="fs-3 fw-bold mt-2">Designed for the drive ahead.</h2><p class="muted mb-4">${vehicle.description}</p></article></div><div class="col-lg-5"><aside class="surface-card detail-summary"><div class="d-flex justify-content-between gap-2 align-items-start"><div><div class="vehicle-category">${vehicle.category}</div><h2 class="fs-3 fw-bold mb-0 mt-1">${vehicle.make} ${vehicle.model}</h2></div>${C.statusBadge(vehicle.status)}</div><div class="detail-price mt-4">${vehicle.price}</div><div class="spec-grid my-4"><div class="spec-item"><i class="fa-regular fa-calendar"></i><span>Model year</span><strong>${vehicle.year}</strong></div><div class="spec-item"><i class="fa-solid fa-gauge-high"></i><span>Stock</span><strong>${vehicle.quantity} units</strong></div><div class="spec-item"><i class="fa-solid fa-gas-pump"></i><span>Fuel</span><strong>${vehicle.fuel}</strong></div><div class="spec-item"><i class="fa-solid fa-gear"></i><span>Transmission</span><strong>${vehicle.transmission}</strong></div></div><div class="d-grid gap-2"><button class="btn-primary-gradient py-3 purchase-button" data-action="purchase" data-vehicle-id="${vehicle.id}" ${vehicle.quantity && auth.isAuthenticated ? '' : 'disabled'}><i class="fa-solid fa-bag-shopping me-1"></i>${vehicle.quantity ? (auth.isAuthenticated ? 'Purchase vehicle' : 'Log in to purchase') : 'Currently unavailable'}</button></div><p class="form-help text-center mb-0 mt-3"><i class="fa-solid fa-shield-halved me-1"></i>${purchaseHelp}</p></aside></div></div></div></section>`;
  }

  function searchResults() {
    const params = new URLSearchParams(window.location.search);
    const terms = [params.get('query') || params.get('q'), params.get('make'), params.get('model'), params.get('category')].filter(Boolean);
    const queryLabel = terms.length ? terms.join(' · ') : 'all vehicles';
    return `${C.pageHero('Search results', `Search results for <span class="text-gradient">${queryLabel}</span>`, 'Browse matching inventory, then fine-tune the list with the filters.', [{ label: 'Home', href: 'index.html' }, { label: 'Inventory', href: 'pages/inventory.html' }, { label: 'Search results' }])}<section class="section-pad"><div class="container"><div class="row g-4"><div class="col-lg-3">${C.filterPanel()}</div><div class="col-lg-9"><div class="surface-card p-3 mb-4 d-flex gap-3 align-items-center"><div class="info-icon flex-shrink-0"><i class="fa-solid fa-magnifying-glass"></i></div><div><strong>${vehicles().length} close matches found</strong><p class="muted small mb-0">Results are drawn from the live SQLite vehicle inventory.</p></div></div><div class="results-toolbar d-flex justify-content-between align-items-center mb-4"><span class="results-count" id="resultsCount">Showing ${vehicles().length} matching vehicles</span></div><div class="row g-4" id="vehicleResults">${vehicles().map(item => `<div class="col-md-6 col-xl-4">${C.vehicleCard(item)}</div>`).join('') || `<div class="col-12">${C.emptyState('No vehicles found', 'Try changing your filters or clearing the current search.', 'fa-magnifying-glass')}</div>`}</div></div></div></div></section>`;
  }

  function manageVehicles() {
    const rows = vehicles().map(item => `<tr><td><div class="d-flex align-items-center gap-3"><span class="table-car-thumb"><img src="${item.image}" alt="${item.make} ${item.model}"></span><div><div class="table-primary">${item.make} ${item.model}</div><div class="table-subtitle">${item.year}   ${item.fuel}</div></div></div></td><td>${item.category}</td><td class="table-primary">${item.price}</td><td>${item.quantity}</td><td>${C.statusBadge(item.status)}</td><td class="text-end"><a class="action-icon" href="${C.url(`pages/vehicle-details.html?id=${item.id}`)}" aria-label="View ${item.model}"><i class="fa-regular fa-eye"></i></a><a class="action-icon ms-1" href="${C.url(`pages/update-vehicle.html?id=${item.id}`)}" aria-label="Edit ${item.model}"><i class="fa-solid fa-pen"></i></a><a class="action-icon delete ms-1" href="${C.url(`pages/delete-confirmation.html?id=${item.id}`)}" aria-label="Delete ${item.model}"><i class="fa-solid fa-trash"></i></a></td></tr>`).join('');
    return `<div class="admin-content"><div class="container-fluid p-0">${C.adminPageHeader('Manage vehicles', 'View, edit and track every vehicle in the dealership inventory.', 'Vehicles')}<div class="d-flex flex-column flex-md-row gap-2 justify-content-between mb-4"><a class="btn-primary-gradient text-center ms-md-auto" href="${C.url('pages/add-vehicle.html')}"><i class="fa-solid fa-plus me-1"></i>Add vehicle</a></div><div class="admin-table-wrap"><table class="table admin-table"><thead><tr><th>Vehicle</th><th>Category</th><th>Price</th><th>Quantity</th><th>Status</th><th class="text-end">Actions</th></tr></thead><tbody>${rows || emptyRow('No vehicles found', 6, 'fa-car')}</tbody></table></div></div></div>`;
  }

  const overrides = {
    home,
    'vehicle-details': vehicleDetails,
    'search-results': searchResults,
    'manage-vehicles': manageVehicles,
    dashboard,
    'inventory-management': inventoryManagement,
    'purchase-history': purchaseHistory,
    'user-management': userManagement,
    'invite-user': inviteUser,
    'user-dashboard': userDashboard
  };

  window.DealerPages = {
    render(page) {
      const html = overrides[page] ? overrides[page]() : originalPages.render(page);
      requestAnimationFrame(hydrateFilters);
      return html;
    }
  };

  document.addEventListener('click', (event) => {
    const control = event.target.closest('[data-action]');
    if (!control) return;

    if (control.dataset.action === 'purchase') {
      event.preventDefault();
      event.stopPropagation();
      postForm(C.url('actions/purchase-vehicle.html'), {
        vehicle_id: control.dataset.vehicleId,
        quantity: 1
      });
    }

    if (control.dataset.action === 'stock-change') {
      event.preventDefault();
      event.stopPropagation();
      const quantity = Math.max(1, Number(control.dataset.delta || 1));
      postForm(C.url('actions/restock-vehicle.html'), {
        vehicle_id: control.dataset.id,
        quantity
      });
    }

    if (control.dataset.action === 'apply-filters') {
      event.preventDefault();
      event.stopPropagation();
      window.location.href = searchUrlFromControls();
    }

    if (control.dataset.action === 'clear-filters') {
      event.preventDefault();
      event.stopPropagation();
      window.location.href = C.url('pages/inventory.html');
    }
  }, true);

  document.addEventListener('submit', (event) => {
    if (!event.target.matches('[data-search-form]')) return;
    event.preventDefault();
    event.stopPropagation();
    const params = new URLSearchParams();
    const query = event.target.querySelector('[name="query"]')?.value?.trim();
    const make = event.target.querySelector('[name="make"]')?.value?.trim();
    const budget = event.target.querySelector('[name="budget"]')?.value?.trim();
    if (query) params.set('query', query);
    if (make) params.set('make', make);
    if (budget) params.set('max_price', budget);
    const suffix = params.toString();
    window.location.href = `${C.url('pages/search-results.html')}${suffix ? `?${suffix}` : ''}`;
  }, true);
})();
