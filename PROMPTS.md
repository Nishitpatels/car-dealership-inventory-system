# Frontend Customization Prompt

## Role
Act as a Senior Full-Stack Engineer, UI/UX Designer, and Bootstrap Expert.

## Objective
Customize the existing **NexusAI Bootstrap template** into a **Car Dealership Inventory System** while preserving its design language, animations, responsiveness, typography, spacing, colors, and overall visual identity.

## Constraints
- Frontend only (no backend/business logic).
- Keep Bootstrap, HTML5, CSS3, and existing JavaScript.
- Do not use React, Vue, Angular, Tailwind, or other UI libraries.
- Reuse existing sections where possible; add new ones only when necessary.
- Use dummy/static data, placeholder images, and mock interactions.

## Pages
**Public:** Home, About, Vehicle Inventory, Vehicle Details, Search Results, Login, Register, Contact, 404.  
**Admin:** Dashboard, Manage Vehicles, Add/Update Vehicle, Delete Confirmation, Inventory Management, Purchase History, User Management, Profile, Settings.

## Core Features
- Homepage: Hero, Featured Vehicles, Inventory Stats, Brands, Testimonials, FAQ, CTA, Contact, Footer.
- Vehicle Cards: Image, Make, Model, Category, Price, Stock, Fuel, Transmission, Year, Status badges, View Details, Purchase (disabled if out of stock).
- Vehicle Details: Gallery, Specifications, Features, Price, Quantity, Engine, Mileage, Related Vehicles.
- Search & Filters: Make, Model, Category, Price, Fuel, Transmission, Availability, Sorting.
- Admin Dashboard: Statistics, Charts (placeholder), Recent Activities, Low Stock Alerts, Quick Actions.
- CRUD UI: Bootstrap tables and forms for vehicle, inventory, purchase, and user management.

## UI Requirements
- Responsive Bootstrap layout.
- Reusable components (Vehicle Card, Dashboard Card, Search Bar, Filter Panel, Tables, Modals, Breadcrumbs, Pagination).
- Professional icons, rounded cards, modern shadows, responsive forms.
- Toasts, alerts, loading skeletons, empty states, confirmation dialogs (placeholders).

## Dummy Data
Use realistic vehicle data (BMW, Mercedes, Audi, Toyota, Honda, Hyundai, Kia, Tesla, Ford, Mahindra, Tata) with professional placeholder images and specifications.

## Project Structure
Organize assets into:
- `assets/`
- `css/`
- `js/`
- `images/`
- `pages/`
- `components/`
- `partials/`

## Code Standards
- Semantic HTML5.
- Reusable Bootstrap classes.
- Minimal custom CSS.
- No duplicated code.
- No inline CSS/JS.
- Comment major sections.
- Keep structure modular and maintainable.

## Django Compatibility
Design pages for future Django integration:
- Repeatable containers for cards.
- Tables ready for template loops.
- Forms with proper `id` and `name` attributes.
- Meaningful classes/IDs for buttons and components.

## Important
Generate **only frontend code**. Do not implement Django, APIs, authentication, database, or backend logic.

# Django Project Initialization Prompt

## Role
Act as a Senior Django Software Engineer following professional software engineering practices.

## Objective
Initialize a clean, scalable **Car Dealership Inventory System** for a TDD-based assessment.

## Constraints
- Project initialization only.
- No business logic, CRUD, authentication, APIs, or database models.
- Backend: Python, Django, SQLite3.
- Frontend Bootstrap template already exists.

## Tasks

### 1. Environment Setup
- Create and activate a Windows virtual environment.
- Install the latest stable Django.
- Generate `requirements.txt`.

### 2. Django Project
- Create project: `dealership`
- Create apps:
  - `authentication`
  - `inventory`
  - `purchases`
  - `dashboard`
  - `core`
- Explain each app's purpose.
- Register all apps in `INSTALLED_APPS`.

### 3. Configuration
Configure:
- SQLite (default)
- `STATIC_URL`
- `STATICFILES_DIRS`
- `MEDIA_URL`
- `MEDIA_ROOT`
- Project-level `templates/`
Create:
- `templates/`
- `static/`
- `media/`

### 4. Frontend Integration
Move the Bootstrap template into Django.
Use template inheritance and create:
- `base.html`
- `navbar.html`
- `sidebar.html`
- `footer.html`
- `messages.html`
Preserve the existing UI without backend logic.

### 5. Folder Structure
Prepare:
- `dealership/`
- `authentication/`
- `inventory/`
- `purchases/`
- `dashboard/`
- `core/`
- `templates/`
- `partials/`
- `static/` (`css/`, `js/`, `images/`)
- `media/`
- `tests/`
- `README.md`
- `PROMPTS.md`
- `requirements.txt`
- `.gitignore`

### 6. Git Setup
Initialize Git and create `.gitignore` for:
- `venv/`
- `__pycache__/`
- `db.sqlite3`
- `media/`
- `.idea/`
- `.vscode/`
- `.pytest_cache/`

### 7. Documentation
Generate an initial `README.md` containing:
- Project Title
- Description
- Objectives
- Tech Stack
- Project Structure
- Placeholder sections for Setup, Features, Testing, AI Usage
- License

Generate `PROMPTS.md` with:
- Project Initialization
- Prompt
- AI Tool
- Purpose
- Notes

### 8. Version Control
Suggest the first commit:
`chore(project): initialize Django project structure`
Include the required AI co-author trailer from the assessment.

### 9. Final Output
Summarize:
- ✔ Created folders
- ✔ Installed packages
- ✔ Django apps
- ✔ Files created
- ✔ Git initialized
- ✔ Ready for Authentication feature

# Django Template Architecture Migration Prompt

## Role
Act as a Senior Django Software Engineer responsible for converting an existing Bootstrap frontend into a clean, maintainable Django Template architecture.

## Objective
Reorganize the existing frontend into Django templates **without changing the UI**. Use the HTML files in `HtmlFiles/` as the **single source of truth**.

## Constraints
- No redesign or UI enhancements.
- No backend implementation (views, models, URLs, forms, CRUD, authentication, APIs).
- Preserve all colors, fonts, icons, layouts, responsiveness, Bootstrap components, JavaScript, CSS, and animations.

## Tasks

### 1. Analyze Existing HTML
Inspect every file in `HtmlFiles/` and identify:
- Common layouts
- Navigation
- Sidebar
- Footer
- Head section
- Stylesheets
- Scripts
- Reusable components

### 2. Create Template Architecture
Create reusable templates:
- `base.html`
- `partials/head.html`
- `partials/navbar.html`
- `partials/sidebar.html`
- `partials/footer.html`
- `partials/messages.html`
- `partials/breadcrumbs.html` *(if needed)*
- `partials/pagination.html` *(if needed)*

### 3. Use Template Inheritance
All pages should:
- Extend `base.html`
- Use blocks: `title`, `content`, `extra_css`, `extra_js`

### 4. Configure Static Assets
Replace all asset paths with Django `{% static %}` tags for CSS, JS, images, fonts, and icons. Load `{% load static %}` only in `base.html`.

### 5. Convert HTML Pages
Convert every HTML file into Django templates while removing duplicated code. Organize templates by app, e.g.:
- `templates/core/`
- `templates/authentication/`
- `templates/inventory/`
- `templates/dashboard/`

### 6. Code Quality
- Keep templates modular and readable.
- Preserve useful comments.
- Ensure templates are ready for future Django integration.

## Final Output
Provide:
- Folder structure created
- Partial templates created
- Converted Django templates
- Reused HTML files
- Duplicate code extracted/removed
- Confirmation that the UI remains visually unchanged

> Perform **only** the Django template architecture migration. Do **not** implement any backend functionality.

# Django Routing & Template Rendering Prompt

## Role
Act as a Senior Django Software Engineer following professional Django best practices.

## Objective
Configure Django so the existing Bootstrap frontend is fully renderable. After `python manage.py runserver`, the Bootstrap homepage should load instead of the default Django page. Use `HtmlFiles/` as the **source of truth**.

## Constraints
- **Do not implement:** models, forms, CRUD, authentication, database operations, APIs, JWT, TDD tests, or business logic.
- Views should **only render templates**.
- Preserve the existing Bootstrap UI exactly.

## Tasks

### 1. Organize Views
Create function-based views in the appropriate apps (`core`, `authentication`, `inventory`, `dashboard`, `purchases`). Keep views modular.

### 2. Create Render Views
Add render-only views for all frontend pages (Home, About, Contact, Login, Register, Dashboard, Inventory, Vehicle Details, Search Results, Add/Update Vehicle, Delete Confirmation, Manage Vehicles, Inventory Management, Purchase History, User Management, Profile, Settings, 404, and any page found in `HtmlFiles/`).

### 3. Configure URLs
- Create app-level `urls.py`.
- Configure project-level `urls.py` using `include()`.
- Use namespaces and meaningful route names.
- Configure static/media serving in development.
- Add custom error handlers if needed.

### 4. Connect Templates
Link every view to its corresponding Django template and verify template inheritance (`base.html`).

### 5. Update Navigation
Replace all hardcoded links in navbar, sidebar, footer, buttons, cards, dropdowns, and menus with Django `{% url %}` tags.

### 6. Verify Static Assets
Ensure all CSS, JavaScript, Bootstrap assets, images, fonts, and icons load correctly using `{% static %}`.

### 7. Recover Missing Content
If any template is incomplete, restore it from `HtmlFiles/` without changing the design.

### 8. Project Verification
Confirm:
- No missing templates or URLs
- No `TemplateDoesNotExist`
- No `NoReverseMatch`
- No broken navigation
- No missing static files
- No import or circular import errors
- No runtime configuration issues
- `python manage.py runserver` opens the Bootstrap homepage successfully

## Final Output
Provide:
- Views created
- `urls.py` files modified
- Templates connected
- Navigation links updated
- Templates recovered from `HtmlFiles`
- Configuration changes made
- Folder structure changes (if any)
- Confirmation that:
  - Bootstrap homepage replaces the Django welcome page
  - All pages render successfully
  - No backend logic was implemented
  - Project is ready for **Feature 2 – Authentication**

  # Feature 2: Admin Authentication Prompt

## Role
Act as a Senior Django Software Engineer following professional Django best practices.

## Objective
Implement authentication for an **existing Django Superuser** using the Bootstrap login page. On successful login, redirect to the **Bootstrap Admin Dashboard** (not `/admin/`).

## Constraints
- **Do not implement:** user registration, customer login, CRUD, search, purchases, restocking, APIs, JWT, or unrelated business logic.
- Preserve the Bootstrap UI exactly.
- Use the existing Bootstrap Admin Dashboard as the production interface.

## Tasks

### 1. Authentication
Use Django's built-in authentication:
- `authenticate()`
- `login()`
- `logout()`
- `request.user`
- `is_authenticated`
- `is_staff`
- `is_superuser`

### 2. Login
- Reuse the existing Bootstrap login template.
- Authenticate using username and password.
- On success, create a session and redirect to the Bootstrap Admin Dashboard.
- On failure, remain on the login page and display a Bootstrap error message.

### 3. Access Control
Protect all admin pages (Dashboard, Manage Vehicles, Inventory Management, Purchase History, User Management, Settings, and future admin pages).
- Anonymous users → redirect to login.
- Authenticated non-superusers → return HTTP 403 or redirect appropriately.
- Superusers only → full access.

Use reusable authorization with `login_required`, `user_passes_test`, or equivalent.

### 4. Logout
- Destroy the session securely.
- Redirect to the login page.
- Display a logout success message.

### 5. Navigation
Update templates so:
- Logged-in admin sees: Dashboard, Profile, Logout.
- Anonymous users see: Login.

### 6. Messages
Integrate Django Messages Framework using existing Bootstrap alert components for:
- Login successful
- Invalid credentials
- Logged out successfully
- Permission denied

### 7. Verification
Confirm:
- Superuser can log in.
- Invalid credentials are rejected.
- Anonymous users are redirected.
- Non-superusers cannot access admin pages.
- Logout destroys the session.
- Bootstrap Admin Dashboard loads successfully.
- No template, URL, or authentication errors.

## Final Output
Provide:
- Files modified
- Views implemented
- URLs added
- Templates updated
- Authentication workflow summary
- Access control summary
- Session management summary
- Confirmation that:
  - Bootstrap UI remained unchanged
  - Django authentication is integrated
  - Existing Superuser can log in
  - Bootstrap Admin Dashboard is the production admin interface
  - Project is ready for **Feature 3 – User Registration**


# Feature 3: Complete Authentication Module

## Role
Act as a Senior Django Software Engineer following professional Django best practices.

## Objective
Implement a secure, modular authentication system using Django's built-in authentication framework while preserving the existing Bootstrap UI.

## Constraints
- Keep the Bootstrap design unchanged.
- Use `HtmlFiles/` as the template reference.
- No vehicle management, CRUD, APIs, or unrelated business logic.

## Tasks

### 1. User Model & Database
- Use Django's built-in `User` model unless an extension is justified.
- Create and apply migrations if required.

### 2. User Registration
Create a registration page for **normal users only** with:
- First Name, Last Name, Username, Email
- Password & Confirm Password

Validate:
- Required fields
- Unique username/email
- Valid email
- Password confirmation
- Password strength
- Trim whitespace

Hash passwords securely and redirect to **User Login** after successful registration.

### 3. User Login
- Create a dedicated user login page.
- Authenticate normal users.
- Start a session and redirect to the appropriate landing page.
- Show Bootstrap error messages for invalid credentials.

### 4. Admin Login
Maintain a separate admin login:
- Authenticate only Django Superusers.
- Reject normal users.
- Redirect to the Bootstrap Admin Dashboard.

### 5. Logout
Implement secure logout for both users and admins, destroy the session, and redirect appropriately.

### 6. Access Control
- Anonymous users → no protected pages.
- Normal users → no admin pages.
- Superusers → full access.

Use `login_required`, `user_passes_test`, or reusable authorization helpers.

### 7. Navigation & Templates
Update templates dynamically:
- Anonymous: Login, Register
- Authenticated User: Profile, Logout
- Superuser: Dashboard, Profile, Logout

Replace authentication-related placeholders with Django template variables.

### 8. Forms & Messages
Create reusable `forms.py` where appropriate.
Use Django Messages Framework for:
- Registration successful
- Invalid credentials
- Duplicate username/email
- Password mismatch
- Logout successful
- Permission denied

Display messages using existing Bootstrap alert components.

### 9. Security
- CSRF protection
- Django password hashing
- Session authentication
- Prevent unauthorized access
- Follow Django security best practices

### 10. Verification
Confirm:
- Registration works
- Duplicate username/email rejected
- Password confirmation validated
- User/Admin login works
- Invalid credentials rejected
- Logout destroys session
- Sessions persist correctly
- Protected pages secured
- No migration, URL, template, or import errors
- Bootstrap UI remains unchanged

## Final Output
Provide:
- Files created & modified
- Models used
- Forms created
- Views & URLs added
- Templates updated
- Database changes & migrations
- Authentication and authorization flow
- Validation summary
- Session management summary
- Security improvements
- Confirmation that:
  - User Registration completed
  - User Login completed
  - Admin Login completed
  - Logout completed
  - Database updated
  - Bootstrap UI unchanged
  - Project is ready for **Feature 4 – Vehicle Management**

# Feature 4: Vehicle Management Module

## Role
Act as a Senior Django Software Engineer following production-quality Django architecture and best practices.

## Objective
Implement the complete **Vehicle Management** module by integrating the existing Bootstrap UI with SQLite. Replace all static vehicle data with dynamic database content.

## Constraints
- Preserve the Bootstrap UI exactly.
- Use `HtmlFiles/` as the template reference.
- Only Superusers can manage vehicles.
- Normal users can only view inventory and vehicle details.

## Tasks

### 1. Vehicle Model
Create a `Vehicle` model with:
- `id`
- `make`
- `model`
- `category`
- `price`
- `quantity`
- `description`
- `image`
- `created_at`
- `updated_at`

Use appropriate field types, validators, `__str__()`, and create/apply migrations.

### 2. Vehicle Forms
Create Bootstrap-compatible `ModelForm`s with validation for:
- Required fields
- Positive price
- Positive quantity
- Valid category
- Image upload

### 3. Vehicle CRUD
Implement:
- Add Vehicle (Superuser only)
- View Inventory (Public)
- Vehicle Details (Public)
- Update Vehicle (Superuser only)
- Delete Vehicle with confirmation (Superuser only)

Reuse the existing Bootstrap templates without redesign.

### 4. Inventory Integration
Replace all hardcoded vehicle cards with database-driven data displaying:
- Image
- Make & Model
- Category
- Price
- Quantity
- Availability

Add pagination if appropriate.

### 5. Vehicle Images
- Store images in `static/images/vehicles/`.
- Reuse existing images when available.
- If downloading is supported, cache images locally.
- Fall back to a default placeholder when necessary.
- Never break if offline.

### 6. URLs & Views
Create clean routes and modular views for:
- Inventory
- Vehicle Details
- Add Vehicle
- Update Vehicle
- Delete Vehicle

Keep code reusable and DRY.

### 7. Search Preparation
Prepare reusable queryset logic so future filtering by Make, Model, Category, and Price can be added easily without implementing search now.

### 8. Error Handling
Handle gracefully:
- Vehicle not found
- Invalid image
- Missing fields
- Invalid quantity/price
- Permission denied

### 9. Verification
Confirm:
- Vehicle creation, update, deletion
- Validation works
- Inventory renders from SQLite
- Vehicle details display correctly
- Admin authorization enforced
- Images load correctly
- No migration, template, URL, or navigation errors
- Bootstrap UI remains unchanged

## Final Output
Provide:
- Models created
- Forms created
- Views created
- URLs added
- Templates updated
- Migrations created
- Database changes
- Image management strategy
- Files added to `static/images/vehicles/`
- UI pages connected
- Authorization summary
- Validation summary
- Confirmation that:
  - Vehicle Model completed
  - Add Vehicle completed
  - Inventory completed
  - Vehicle Details completed
  - Update Vehicle completed
  - Delete Vehicle completed
  - SQLite integrated
  - Bootstrap UI preserved
  - Project is ready for **Feature 5 – Inventory Operations (Purchase & Restock)**

# Feature 5: Inventory Operations & System Completion

## Role
Act as a Senior Django Software Engineer following production-quality Django architecture and best practices.

## Objective
Complete the remaining modules by integrating Django backend functionality into the existing Bootstrap frontend while preserving the UI.

## Constraints
- Do not redesign or modify Bootstrap, CSS, layout, typography, icons, animations, or responsiveness.
- Replace all remaining static data with SQLite-backed data.

## Tasks

### 1. Purchase Vehicle
- Create a purchase workflow.
- Decrease vehicle quantity atomically.
- Prevent negative stock and race conditions.
- Disable Purchase button when quantity reaches zero and display **Out of Stock**.
- Store purchase records linked to the logged-in user (vehicle, user, date, quantity, price).
- Display Bootstrap success/error messages.

### 2. Restock Vehicle (Admin)
- Superuser only.
- Increase stock with validation.
- Update inventory immediately.
- Reuse the existing Bootstrap Restock page.

### 3. Purchase History
Create a `Purchase` model (if needed).
- Admin: view all purchases.
- User: view only their purchases.
- Show vehicle, image, purchase date, quantity, price, and status.
- Sort newest first.

### 4. Search Module
Implement search using GET parameters with filters for:
- Make
- Model
- Category
- Price range

Support combined filters and retain selected values after submission.

### 5. User Dashboard
Display:
- Welcome message
- Profile information
- Purchased vehicles
- Recent purchases
- Total purchases
- Quick actions
- Profile settings
- Logout

Never expose admin data.

### 6. Admin Dashboard
Replace all placeholders with live SQLite data:
- Total Vehicles
- Total Users
- Available Stock
- Out of Stock
- Low Stock
- Recent Purchases
- Inventory Value
- Recent Registered Users
- Quick links

### 7. User Management
Superuser only.
- View users
- Deactivate or remove users
- Prevent Superuser deletion
- Use confirmation dialogs

### 8. Inventory Management
Highlight:
- Low Stock
- Out of Stock
- Recently Added
- Recently Updated

### 9. Database & Performance
- Maintain proper model relationships.
- Create/apply migrations.
- Use `select_related()` and `prefetch_related()` where appropriate.
- Avoid N+1 queries.

### 10. Authorization & Error Handling
- Anonymous: no purchases or dashboards.
- Users: no admin features.
- Admin: full access.

Handle gracefully:
- Vehicle not found
- Out of stock
- Invalid purchase
- Invalid search
- Invalid quantity
- Permission denied

Display Bootstrap alerts.

### 11. Verification
Confirm:
- Purchases reduce stock correctly.
- Stock never becomes negative.
- Purchase button disables at zero stock.
- Restocking updates inventory.
- Search works for individual and combined filters.
- Purchase history persists.
- User/Admin dashboards display live data.
- User management restrictions work.
- SQLite data is fully integrated.
- No migration, template, URL, or navigation errors.
- Bootstrap UI remains unchanged.

## Final Output
Provide:
- Models created/updated
- Views implemented
- Forms created
- URLs added
- Templates modified
- Database migrations
- Purchase workflow summary
- Restock workflow summary
- Search implementation summary
- User Dashboard summary
- Admin Dashboard summary
- Purchase History summary
- User Management summary
- Authorization summary
- Performance improvements
- Confirmation that:
  - Purchase Vehicle completed
  - Restock Vehicle completed
  - Search Module completed
  - User Dashboard completed
  - Admin Dashboard completed
  - Purchase History completed
  - User Management completed
  - SQLite fully integrated
  - Bootstrap UI preserved
  - Project is feature-complete according to the assessment


# Final Audit, QA & Submission Readiness

## Role
Act as a Senior Django Software Engineer, Technical Architect, and QA Engineer.

## Objective
Perform a **production-level audit** of the completed Car Dealership Inventory System. Preserve all working functionality, fix only necessary issues, and ensure the project fully satisfies **AI_Kata_Car_Dealership_Inventory_System_V2.pdf**.

## Constraints
- Do **not** redesign the UI or overwrite working code.
- Do **not** regenerate completed features.
- Preserve the Bootstrap theme exactly.
- Make only backend integrations, bug fixes, optimizations, and missing feature implementations.

## Phase 1 – Project Audit
Review the entire project:
- Django apps, models, forms, views, URLs, templates
- Static assets (CSS, JS, images)
- Authentication & authorization
- Vehicle Management, Inventory, Purchase workflow
- Search, Dashboards, User Management, Purchase History
- Error pages, validation, database relationships, migrations

Identify:
- Working features
- Partially implemented or missing features
- Broken UI elements, navigation, buttons
- Placeholder/static content
- Security, performance, validation, or database issues

Fix only confirmed issues.

## Phase 2 – Application Polish
- Remove remaining dummy content, broken links, unused buttons, static counters, placeholder cards, and incomplete forms.
- Replace remaining placeholders with SQLite-backed data where appropriate.

## Functional Review
### User Dashboard
- Allow users to update first/last name and profile.
- Show personal information, purchased vehicles, and purchase history.
- Validate updates and display Bootstrap messages.

### Search
Verify admin and user search:
- Make
- Model
- Category
- Price range
- Combined filters
- Preserve filter values
- Handle empty results gracefully.

### Admin Dashboard
Replace all dashboard statistics with live data:
- Total Vehicles
- Total Users
- Inventory Value
- Available/Low/Out of Stock
- Recent Purchases
- Recent Users
- Quick Actions

### Validation
Audit all forms:
- Required fields
- Email, username, password validation
- Price & quantity validation
- Duplicate checks
- Trim whitespace
- Consistent Bootstrap validation messages

### Error Pages
Implement and configure:
- 403
- 404
- 500

Reuse the existing Bootstrap theme.

## Database & Security Review
- Verify relationships, constraints, cascade behavior, validation, and indexes.
- Generate migrations only if required.
- Confirm CSRF protection, password hashing, session handling, permission checks, and prevent privilege escalation.

## Performance
Optimize where beneficial using:
- `select_related()`
- `prefetch_related()`
- Query optimization
- Removal of redundant database calls

## Testing (TDD)
Review existing tests first and add only missing tests for:
- Authentication
- Vehicle CRUD
- Search
- Purchase workflow
- Permissions
- Validation

Ensure the complete test suite passes.

## Final QA Checklist
Verify:
- No template, URL, migration, or import errors
- No broken navigation, forms, CRUD, search, dashboards, or purchase workflow
- No console errors
- No missing static assets or images
- Bootstrap UI remains unchanged

## Final Output
Provide:
- Features fixed & completed
- Bugs resolved
- Validation, dashboard, search, and user profile improvements
- Error pages implemented
- Database, security, and performance improvements
- Tests added/updated
- Assessment checklist (Completed / Remaining)
- Confirmation that the project satisfies **AI_Kata_Car_Dealership_Inventory_System_V2.pdf** and is ready for final submission

