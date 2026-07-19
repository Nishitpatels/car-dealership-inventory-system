# Car Dealership Inventory System

A full-stack Car Dealership Inventory System built with Django, SQLite, and Bootstrap. The application preserves the original Nexus Motors frontend design while backing every inventory, purchase, authentication, and dashboard workflow with a production-quality Django implementation.

## Project Description

Nexus Motors is a dealership inventory platform that lets customers browse vehicles, search inventory, and purchase cars, while administrators manage stock, vehicles, users, and operational dashboards.

## Tech Stack

- Python 3
- Django 6
- SQLite3
- Bootstrap 5
- Chart.js (admin revenue chart)
- Font Awesome

## Project Structure

```
Car Dealership/
├── authentication/     # Registration, login, access control
├── inventory/          # Vehicle model, CRUD, search, restock
├── purchases/          # Purchase workflow and history
├── dashboard/          # Admin dashboard and user management
├── core/               # Public pages (home, about, contact)
├── dealership/         # Project settings and root URLs
├── templates/          # Django templates (Bootstrap UI)
├── static/             # CSS, JS, and vehicle images
└── manage.py
```

## Setup Instructions

### 1. Clone the repository

```bash
git clone <repository-url>
cd "Car Dealership"
```

### 2. Create and activate a virtual environment (recommended)

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### 3. Install Django

```bash
pip install django
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

This creates the SQLite database and seeds initial vehicle inventory.

### 5. Create a superuser (admin account)

```bash
python manage.py createsuperuser
```

Use this account on the **Admin Login** page (`/accounts/admin-login/`).

### 6. Run the development server

```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Features

### Authentication
- Customer registration and login
- Separate admin login for superusers
- Session-based authentication with CSRF protection
- Role-based access control (superuser vs customer)

### Inventory
- Browse all vehicles
- Search by make, model, category, and price range
- Vehicle detail pages with live stock status
- Admin vehicle CRUD (add, update, delete)
- Admin restock workflow
- Vehicle images stored in `static/images/vehicles/`

### Purchases
- Authenticated customers can purchase vehicles
- Stock decreases atomically on purchase
- Purchase history for customers and admins
- Out-of-stock validation

### Dashboards
- **Admin dashboard**: dynamic stats, revenue chart, recent vehicles, recent purchases, low-stock alerts
- **User dashboard**: personal purchases, spending summary, quick actions
- **User management**: list users, deactivate accounts

### Security
- Protected routes for admin and authenticated pages
- Superuser-only admin operations
- Safe redirect handling on purchase actions

## Testing

Run the full test suite:

```bash
python manage.py test
```

Tests cover authentication, inventory CRUD, search, purchase workflow, restock, access control, and dashboard behaviour.

## Default Routes

| Route | Description |
|-------|-------------|
| `/` | Home |
| `/accounts/register/` | Customer registration |
| `/accounts/login/` | Customer login |
| `/accounts/admin-login/` | Admin login |
| `/inventory/` | Vehicle inventory |
| `/inventory/search-results/` | Search results |
| `/purchases/history/` | Purchase history |
| `/dashboard/` | Admin dashboard |

## My AI Usage

### Tools Used
- **Cursor AI (Composer)** — primary development assistant for analysis, implementation, and testing

### How AI Was Used
- Analysed the existing partially implemented codebase before making changes
- Compared project state against assessment requirements
- Implemented missing backend integration, tests, vehicle image mapping, and dynamic dashboard data
- Generated and refined Django tests for authentication, inventory, purchases, and dashboards
- Updated documentation and preserved the existing Bootstrap UI without redesign

### Reflection
AI significantly accelerated the audit and completion phase by mapping assessment requirements to existing architecture quickly. Manual review was still required to avoid overwriting completed modules, preserve UI conventions, and ensure business logic (stock updates, permissions, atomic purchases) remained correct. The most effective workflow was: analyse first, extend existing services/views, then verify with automated tests.

---

© 2026 Nexus Motors — Car Dealership Inventory System
