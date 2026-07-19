# 🚗 Project Overview

The **Car Dealership Inventory Management System** is a full-stack web application developed using the **Django Framework** as part of a **Test-Driven Development (TDD)** assessment. The system enables dealerships to efficiently manage vehicle inventory through a secure, role-based interface while providing essential inventory operations, search capabilities, and administrative controls.

The application follows a modular architecture, where each feature is implemented as an independent component with a strong focus on **clean code**, **maintainability**, and **scalability**. Throughout the development process, **unit tests were written alongside feature implementation** to ensure correctness, improve reliability, and align with TDD best practices.

The platform supports the complete inventory lifecycle—from vehicle registration and inventory management to stock updates, purchase tracking, and real-time dashboard insights. Administrative users have full control over inventory operations, while authentication and authorization mechanisms ensure secure access to protected resources.

---

## 🎯 Project Objectives

- Develop a robust inventory management system using Django.
- Follow **Test-Driven Development (TDD)** principles throughout the project lifecycle.
- Implement secure user authentication and role-based authorization.
- Provide complete CRUD functionality for vehicle inventory management.
- Enable efficient vehicle search and filtering capabilities.
- Manage vehicle purchases and inventory restocking operations.
- Present meaningful inventory insights through interactive dashboards.
- Ensure data integrity using comprehensive validation and error handling.
- Maintain a clean, modular, and scalable project structure suitable for future enhancements.

---

## ✨ Key Capabilities

- 🔐 Secure User Authentication & Authorization
- 🚗 Complete Vehicle Inventory Management
- 📦 Purchase & Restocking Operations
- 🔍 Advanced Vehicle Search & Filtering
- 📊 Inventory & Administrative Dashboards
- ✅ Server-side Form Validation
- ❌ Custom Error Handling Pages
- 🧪 Comprehensive Unit Testing (TDD)
- 🏗️ Modular Django Application Architecture
- 📱 Responsive User Interface with Bootstrap

---

## 🏆 Project Highlights

- Built with a **Test-Driven Development (TDD)** approach.
- Designed using Django's **MTV (Model-Template-View)** architecture.
- Implements secure authentication using Django's built-in authentication system.
- Role-based access control for administrative operations.
- Modular project structure following Django best practices.
- Responsive frontend integrated with Bootstrap templates.
- SQLite database for lightweight and efficient data management.
- Clean codebase emphasizing readability, maintainability, and extensibility.

---

## 🖼️ Project Preview

> **The screenshots below provide an overview of the application's interface. Detailed screenshots for each module are available in their respective sections.**

<!-- Replace these placeholders with actual screenshots -->

<p align="center">
  <img src="images/project/home_page.png" alt="Home Page" width="45%">
  &nbsp;
  <img src="images/project/dashboard_overview.png" alt="Dashboard Overview" width="45%">
</p>

# ⚡ Key Features

The Car Dealership Inventory Management System is designed to streamline dealership operations through secure inventory management, intuitive user workflows, and a modular architecture. The application provides the following core features:

---

## 🔐 Authentication & Authorization

- Secure user registration and login system
- Session-based authentication using Django
- Role-based access control for administrators
- Protected routes for authorized users only
- Secure logout and session termination
- User-friendly authentication error handling

---

## 🚗 Vehicle Inventory Management

- Add new vehicles to the inventory
- View all available vehicles
- Display detailed information for each vehicle
- Update existing vehicle records
- Delete vehicles with confirmation
- Track inventory using quantity management
- Automatically record creation and modification timestamps

---

## 📦 Inventory Operations

- Purchase vehicles directly from inventory
- Automatically reduce stock after each purchase
- Prevent purchases when inventory is out of stock
- Restock existing vehicles through the admin panel
- Maintain accurate inventory quantities

---

## 🔍 Search & Filtering

- Search vehicles by make
- Search by model
- Filter vehicles by category
- Filter inventory using price ranges
- Quickly locate vehicles from large inventories

---

## 📊 Dashboard & Analytics

- Display total vehicle inventory
- Show total stock availability
- Highlight low-stock vehicles
- View recent purchase activity
- Provide quick inventory insights for administrators

---

## 👨‍💼 Administrative Features

- Dedicated administrative dashboard
- Vehicle management interface
- Inventory restocking controls
- Purchase history management
- Secure access to privileged operations

---

## ✅ Validation & Error Handling

- Server-side form validation
- Required field validation
- Price validation
- Quantity validation
- Duplicate user validation
- Password confirmation checks
- Custom 403, 404, and 500 error pages
- Friendly feedback using Django Messages Framework

---

## 🧪 Test-Driven Development (TDD)

- Unit tests for authentication
- CRUD operation testing
- Inventory operation testing
- Search functionality testing
- Permission and authorization testing
- Validation testing
- Reliable and maintainable test suite

---

## 🏗️ Technical Highlights

- Built with Django Framework
- Modular application architecture
- Template inheritance for reusable UI components
- SQLite database integration
- Bootstrap-based responsive interface
- Django ORM for database operations
- Secure CSRF protection
- Static file management
- Organized URL routing
- Clean and maintainable codebase

---

## 🖼️ Feature Overview

> **The following screenshots provide a high-level overview of the application's major functionalities. Detailed screenshots for each feature are included in their respective modules.**

<p align="center">
  <img src="images/features/authentication.png" alt="Authentication Module" width="30%">
  <img src="images/features/inventory.png" alt="Vehicle Inventory" width="30%">
  <img src="images/features/dashboard.png" alt="Dashboard" width="30%">
</p>

# 🛠️ Technology Stack

The **Car Dealership Inventory Management System** is built using a modern and lightweight technology stack that emphasizes simplicity, maintainability, and rapid development. The application follows Django's **MTV (Model-Template-View)** architecture and integrates Bootstrap for a responsive user interface.

---

## 💻 Backend

| Technology | Purpose |
|------------|---------|
| **Python 3.x** | Core programming language used for backend development |
| **Django** | High-level Python web framework for rapid application development |
| **Django ORM** | Database abstraction layer for performing CRUD operations without writing raw SQL |
| **SQLite3** | Lightweight relational database used for local development and testing |

---

## 🎨 Frontend

| Technology | Purpose |
|------------|---------|
| **HTML5** | Structure and layout of web pages |
| **CSS3** | Styling and responsive design |
| **Bootstrap 5** | Responsive UI framework and pre-built components |
| **JavaScript (ES6)** | Client-side interactivity and dynamic behavior |
| **Django Templates** | Server-side rendering using Django's template engine |

---

## 🧪 Testing

| Technology | Purpose |
|------------|---------|
| **Django Test Framework** | Unit and integration testing |
| **Python unittest** | Test case implementation and assertions |
| **Test-Driven Development (TDD)** | Feature development driven by automated tests |

---

## 🛠️ Development Tools

| Tool | Purpose |
|------|---------|
| **Git** | Version control |
| **GitHub** | Source code hosting and collaboration |
| **Python Virtual Environment (venv)** | Dependency isolation |
| **pip** | Python package management |
| **VS Code** | Primary code editor and development environment |

---

## 📁 Project Architecture

The project follows Django's recommended modular architecture to ensure scalability, maintainability, and separation of concerns.

- **Models** – Database schema and business entities
- **Views** – Application logic and request handling
- **Templates** – Dynamic HTML rendering
- **URLs** – Centralized route management
- **Static Files** – CSS, JavaScript, images, and assets
- **Forms** – User input handling and validation
- **Tests** – Automated unit and integration testing

---

## ⚙️ Core Django Features Utilized

- Django Authentication System
- Django ORM
- Django Forms
- Template Inheritance
- URL Routing
- Static & Media File Management
- Django Messages Framework
- Session Management
- CSRF Protection
- Built-in Admin Panel
- Custom Error Pages
- Middleware Support

---

## 📦 Major Python Packages

| Package | Usage |
|---------|-------|
| **Django** | Web framework |
| **Pillow** *(Optional)* | Image handling (if vehicle images are supported) |

> Additional dependencies and exact package versions are listed in the **`requirements.txt`** file.

---

## 🖼️ Technology Overview

> **The following diagram illustrates the overall technology stack used in the application.**

<p align="center">
    <img src="images/tech/technology_stack.png" alt="Technology Stack" width="80%">
</p>

---

## 🏗️ Architecture Flow

```text
                    User
                      │
                      ▼
              Django Templates
                      │
                      ▼
               Django Views
                      │
                      ▼
               Django Models
                      │
                      ▼
                Django ORM
                      │
                      ▼
                  SQLite3
```

---

## 🚀 Why This Stack?

- ✔️ Rapid development using Django's batteries-included framework
- ✔️ Clean and maintainable MVC-inspired (MTV) architecture
- ✔️ Lightweight SQLite database suitable for assessment projects
- ✔️ Responsive user interface built with Bootstrap
- ✔️ Secure authentication and authorization out of the box
- ✔️ Strong support for Test-Driven Development (TDD)
- ✔️ Easy deployment and future scalability to databases like PostgreSQL or MySQL

# 🏗️ Project Architecture

The **Car Dealership Inventory Management System** is designed using Django's **MTV (Model-Template-View)** architectural pattern. The application is organized into modular components that separate business logic, presentation, and data management, resulting in a clean, scalable, and maintainable codebase.

The project emphasizes **reusability**, **separation of concerns**, and **modular development**, allowing each feature to be developed, tested, and maintained independently.

---

## 🏛️ Architectural Pattern

The application follows Django's **MTV (Model-Template-View)** architecture.

```text
                 ┌────────────────────┐
                 │        User        │
                 └─────────┬──────────┘
                           │
                     HTTP Request
                           │
                           ▼
                 ┌────────────────────┐
                 │        URLs        │
                 │   (Route Mapping)  │
                 └─────────┬──────────┘
                           │
                           ▼
                 ┌────────────────────┐
                 │       Views        │
                 │ Business Logic     │
                 └─────────┬──────────┘
                           │
        ┌──────────────────┴──────────────────┐
        ▼                                     ▼
┌──────────────────┐                 ┌──────────────────┐
│      Models      │                 │    Templates     │
│ Database Layer   │                 │ Presentation UI  │
└─────────┬────────┘                 └─────────▲────────┘
          │                                    │
          ▼                                    │
    ┌───────────────┐                          │
    │   SQLite DB   │──────────────────────────┘
    └───────────────┘

                  HTTP Response
                         │
                         ▼
                       User
```

---

# 🧩 Application Layers

## 📌 Presentation Layer

Responsible for rendering the user interface and displaying dynamic content.

### Components

- Django Templates
- Bootstrap UI
- HTML5
- CSS3
- JavaScript
- Template Inheritance
- Reusable Components
  - Navbar
  - Sidebar
  - Footer
  - Messages

---

## ⚙️ Application Layer

Contains the core business logic that processes user requests and coordinates application behavior.

### Responsibilities

- User Authentication
- Authorization
- Vehicle Management
- Inventory Operations
- Search & Filtering
- Dashboard Statistics
- Validation
- Error Handling

---

## 🗄️ Data Layer

Responsible for persistent data storage using Django ORM.

### Components

- Vehicle Model
- User Model
- Purchase History
- Inventory Records
- SQLite Database

---

# 📂 High-Level Project Structure

```text
car-dealership-inventory-system/
│
├── dealership/                 # Django project configuration
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── inventory/                  # Inventory application
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── admin.py
│   ├── tests.py
│   └── migrations/
│
├── templates/                  # HTML templates
│   ├── base.html
│   ├── partials/
│   ├── authentication/
│   ├── inventory/
│   ├── dashboard/
│   └── errors/
│
├── static/                     # Static assets
│   ├── css/
│   ├── js/
│   ├── images/
│   └── vendor/
│
├── media/                      # Uploaded files (optional)
│
├── requirements.txt
├── manage.py
├── README.md
└── PROMPTS.md
```

---

# 🔄 Request Lifecycle

The following sequence illustrates how a typical request is processed within the application.

```text
User Action
      │
      ▼
Browser Request
      │
      ▼
URL Dispatcher
      │
      ▼
View Function / Class-Based View
      │
      ▼
Business Logic Execution
      │
      ▼
Database Query (ORM)
      │
      ▼
Model Instance
      │
      ▼
Template Rendering
      │
      ▼
HTTP Response
      │
      ▼
User Interface
```

---

# 🔐 Security Architecture

The application leverages Django's built-in security mechanisms to protect user data and application resources.

### Implemented Security Features

- Session-Based Authentication
- Role-Based Authorization
- Password Hashing
- CSRF Protection
- Form Validation
- SQL Injection Prevention (Django ORM)
- XSS Protection through Template Escaping
- Login Required Decorators
- Admin-Only Access Control
- Secure Logout & Session Management

---

# 🧪 Test-Driven Architecture

Each major feature is developed following a **Test-Driven Development (TDD)** workflow.

```text
Write Test
     │
     ▼
Run Test (Fail)
     │
     ▼
Implement Feature
     │
     ▼
Run Test (Pass)
     │
     ▼
Refactor Code
     │
     ▼
Repeat
```

This iterative process ensures that every functionality is validated through automated tests before being considered complete.

---

# 📈 Design Principles

The project is built around modern software engineering principles to improve code quality and long-term maintainability.

- ✔️ Modular Architecture
- ✔️ Separation of Concerns
- ✔️ Reusable Components
- ✔️ DRY (Don't Repeat Yourself)
- ✔️ Clean Code Practices
- ✔️ Scalable Folder Structure
- ✔️ Maintainable Business Logic
- ✔️ Consistent Naming Conventions
- ✔️ Test-Driven Development
- ✔️ Secure Development Practices

---

# 🖼️ Architecture Overview

> **The following diagram illustrates the overall architecture and component interactions within the application.**

<p align="center">
    <img src="images/architecture/project_architecture.png"
         alt="Project Architecture"
         width="85%">
</p>

# 📁 Project Structure

The project is organized using Django's recommended directory structure to promote **modularity**, **maintainability**, and **scalability**. Each component has a clearly defined responsibility, making the codebase easier to understand, extend, and test.

---

## 📂 Directory Overview

```text
car-dealership-inventory-system/
│
├── dealership/                     # Django project configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── inventory/                      # Main application
│   ├── migrations/
│   ├── templates/
│   ├── tests/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
│
├── templates/                      # Global templates
│   ├── partials/
│   │   ├── navbar.html
│   │   ├── sidebar.html
│   │   ├── footer.html
│   │   └── messages.html
│   │
│   ├── authentication/
│   ├── inventory/
│   ├── dashboard/
│   ├── admin/
│   ├── errors/
│   └── base.html
│
├── static/                         # Static assets
│   ├── css/
│   ├── js/
│   ├── images/
│   ├── fonts/
│   └── vendor/
│
├── media/                          # Uploaded media files (optional)
│
├── screenshots/                    # README application screenshots
│   ├── foundation/
│   ├── authentication/
│   ├── vehicle/
│   ├── inventory/
│   ├── search/
│   ├── dashboard/
│   ├── admin/
│   └── validation/
│
├── requirements.txt
├── manage.py
├── README.md
├── PROMPTS.md
├── .gitignore
└── db.sqlite3
```

---

# 📦 Directory Responsibilities

| Directory / File | Description |
|------------------|-------------|
| **dealership/** | Contains the Django project's core configuration, including settings, URL routing, and WSGI/ASGI entry points. |
| **inventory/** | Main application containing models, views, forms, URLs, tests, and business logic related to vehicle inventory. |
| **templates/** | Stores reusable HTML templates, page layouts, and shared UI components. |
| **static/** | Holds CSS, JavaScript, images, fonts, and third-party frontend assets. |
| **media/** | Stores uploaded files, such as vehicle images (if enabled). |
| **screenshots/** | Contains application screenshots referenced throughout the README documentation. |
| **requirements.txt** | Lists all Python dependencies required to run the project. |
| **manage.py** | Django's command-line utility for development and project management. |
| **README.md** | Project documentation, setup guide, and feature overview. |
| **PROMPTS.md** | Documentation of AI prompts used during project development. |
| **.gitignore** | Specifies files and directories excluded from version control. |
| **db.sqlite3** | SQLite database used during local development. |

---

# 🧩 Application Components

The project is divided into logical components, each with a single responsibility.

## ⚙️ Backend

- Django Framework
- Python
- SQLite Database
- Django ORM
- Authentication System
- Business Logic
- URL Routing
- Forms & Validation

---

## 🎨 Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- Django Template Engine

---

## 🧪 Testing

- Unit Tests
- Authentication Tests
- CRUD Tests
- Search Tests
- Inventory Tests
- Validation Tests
- Permission Tests

---

# 📄 Key Files

### `settings.py`

Application-wide configuration including:

- Installed Applications
- Middleware
- Templates
- Database Configuration
- Static Files
- Authentication Settings

---

### `urls.py`

Defines the URL routing structure for the project and individual applications.

---

### `models.py`

Contains database models representing:

- Vehicles
- Purchase Records
- Other application entities

---

### `views.py`

Implements the application's business logic, including:

- Authentication
- Vehicle CRUD Operations
- Inventory Management
- Dashboard
- Search
- Error Handling

---

### `forms.py`

Defines Django forms responsible for:

- Input Validation
- User Registration
- Login
- Vehicle Management

---

### `tests.py`

Contains automated test cases following the **Test-Driven Development (TDD)** methodology.

---

# 🏗️ Project Organization Principles

The directory structure is designed around the following software engineering principles:

- ✔️ Modular Design
- ✔️ Separation of Concerns
- ✔️ Reusable Templates
- ✔️ Organized Static Assets
- ✔️ Clean URL Structure
- ✔️ Maintainable Codebase
- ✔️ Easy Feature Expansion
- ✔️ Testability
- ✔️ Scalable Architecture

---

# 🔄 Module Organization

```text
Foundation
      │
      ├── Authentication
      │
      ├── Vehicle Management
      │
      ├── Inventory Operations
      │
      ├── Search & Filtering
      │
      ├── Dashboard
      │
      ├── Admin Management
      │
      ├── Validation & Error Handling
      │
      └── Testing (TDD)
```

Each module is implemented independently while sharing common templates, static assets, and utilities to encourage code reuse and simplify maintenance.

---

# 🖼️ Project Structure Preview

> **The following screenshot illustrates the project structure as viewed in the development environment.**

<p align="center">
    <img src="screenshots/project/project_structure.png"
         alt="Project Structure"
         width="85%">
</p>

# ⚙️ Local Setup & Installation

Follow the steps below to set up and run the **Car Dealership Inventory Management System** on your local machine for development and testing.

---

# 📋 Prerequisites

Before starting, ensure the following software is installed on your system:

| Software | Recommended Version |
|----------|---------------------|
| Python | 3.11+ |
| Git | Latest |
| pip | Latest |
| Virtual Environment (venv) | Built-in with Python |
| Code Editor | VS Code (Recommended) |

Verify your installation:

```bash
python --version
pip --version
git --version
```

---

# 📥 Clone the Repository

Clone the project from GitHub and navigate to the project directory.

```bash
git clone https://github.com/<your-username>/car-dealership-inventory-system.git
```

```bash
cd car-dealership-inventory-system
```

> Replace `<your-username>` with your actual GitHub username.

---

# 🐍 Create a Virtual Environment

Creating a virtual environment isolates project dependencies from your global Python installation.

### Windows

```bash
python -m venv venv
```

### macOS / Linux

```bash
python3 -m venv venv
```

---

# ▶️ Activate the Virtual Environment

### Windows (Command Prompt)

```cmd
venv\Scripts\activate
```

### Windows (PowerShell)

```powershell
venv\Scripts\Activate.ps1
```

### macOS / Linux

```bash
source venv/bin/activate
```

After activation, your terminal should display:

```text
(venv)
```

---

# 📦 Install Project Dependencies

Install all required Python packages using the provided `requirements.txt` file.

```bash
pip install -r requirements.txt
```

To verify the installed packages:

```bash
pip list
```

---

# ⚙️ Configure the Database

This project uses **SQLite3** as the default database, which requires no additional configuration.

Apply all database migrations:

```bash
python manage.py migrate
```

---

# 👤 Create an Administrator Account

Create a superuser to access the Django administration panel.

```bash
python manage.py createsuperuser
```

Provide the required information:

```text
Username:
Email:
Password:
Password (again):
```

---

# ▶️ Run the Development Server

Start the Django development server.

```bash
python manage.py runserver
```

If successful, you should see output similar to:

```text
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL+C.
```

---

# 🌐 Access the Application

Once the server is running, open your browser and visit:

| Page | URL |
|------|-----|
| Home Page | http://127.0.0.1:8000/ |
| Login | http://127.0.0.1:8000/login/ |
| Register | http://127.0.0.1:8000/register/ |
| Admin Panel | http://127.0.0.1:8000/admin/ |

> **Note:** The URLs above may vary depending on your URL configuration.

---

# 🧪 Running the Test Suite

Execute the complete test suite to verify that all application features are functioning correctly.

Run all tests:

```bash
python manage.py test
```

Run tests with increased verbosity:

```bash
python manage.py test --verbosity=2
```

---

# 📁 Collect Static Files (Production)

Before deploying the project, collect all static assets into a single directory.

```bash
python manage.py collectstatic
```

---

# 🛠️ Common Development Commands

| Command | Purpose |
|----------|---------|
| `python manage.py runserver` | Start the development server |
| `python manage.py migrate` | Apply database migrations |
| `python manage.py makemigrations` | Create new migration files |
| `python manage.py createsuperuser` | Create an administrator account |
| `python manage.py test` | Run automated tests |
| `python manage.py collectstatic` | Collect static files for deployment |
| `deactivate` | Exit the virtual environment |

---

# 🖼️ Local Setup Preview

> **The following screenshots illustrate the local setup and successful project execution.**

<p align="center">
    <img src="screenshots/setup/project_running.png"
         alt="Running Development Server"
         width="48%">
    &nbsp;
    <img src="screenshots/setup/homepage.png"
         alt="Application Home Page"
         width="48%">
</p>

---

# 🚀 Setup Complete

If all the above steps have been completed successfully, the **Car Dealership Inventory Management System** is now ready for development, testing, and exploration on your local machine.

# 🔄 Application Workflow

The **Car Dealership Inventory Management System** follows a structured workflow that enables secure user authentication, efficient inventory management, and seamless administrative operations. Each module interacts cohesively to provide a reliable and intuitive user experience while maintaining data integrity throughout the application.

---

# 🏁 Application Flow Overview

The following diagram illustrates the overall workflow of the system from user authentication to inventory management.

```text
                     Start
                       │
                       ▼
                Open Application
                       │
                       ▼
              User Authentication
             (Login / Registration)
                       │
          ┌────────────┴────────────┐
          │                         │
          ▼                         ▼
    Authentication             Authentication
       Successful                  Failed
          │                         │
          ▼                         ▼
      Dashboard              Display Error Message
          │
          ▼
   Browse Vehicle Inventory
          │
          ▼
   Search / Filter Vehicles
          │
          ▼
   View Vehicle Details
          │
     ┌────┴─────┐
     │          │
     ▼          ▼
Purchase     Admin Operations
Vehicle      (Add / Update /
                 Delete /
                Restock)
     │              │
     └──────┬───────┘
            ▼
     Update Inventory
            │
            ▼
     Dashboard Updated
            │
            ▼
          Logout
            │
            ▼
            End
```

---

# 👤 User Workflow

A regular user can securely access the system and interact with the available inventory.

### User Journey

1. Open the application.
2. Register a new account (if required).
3. Log in using valid credentials.
4. Browse the available vehicle inventory.
5. Search and filter vehicles.
6. View detailed vehicle information.
7. Purchase available vehicles.
8. Logout securely.

---

# 👨‍💼 Administrator Workflow

Administrators have additional privileges to manage the dealership inventory.

### Administrator Journey

1. Log in with administrator credentials.
2. Access the administrative dashboard.
3. Add new vehicles.
4. Update existing vehicle information.
5. Delete obsolete vehicles.
6. Restock inventory.
7. Monitor stock availability.
8. Review purchase history.
9. Logout securely.

---

# 🚗 Vehicle Management Workflow

```text
Add Vehicle
      │
      ▼
Validate Form
      │
      ▼
Save Vehicle
      │
      ▼
Inventory Updated
      │
      ▼
Display Success Message
```

---

# 🛒 Purchase Workflow

```text
Select Vehicle
       │
       ▼
Check Stock Availability
       │
 ┌─────┴─────┐
 │           │
 ▼           ▼
Available   Out of Stock
 │              │
 ▼              ▼
Purchase    Display Error
Vehicle
 │
 ▼
Reduce Quantity
 │
 ▼
Save Changes
 │
 ▼
Show Success Message
```

---

# 📦 Restock Workflow

```text
Administrator
      │
      ▼
Select Vehicle
      │
      ▼
Enter Restock Quantity
      │
      ▼
Validate Quantity
      │
      ▼
Update Inventory
      │
      ▼
Display Success Message
```

---

# 🔍 Search Workflow

```text
Enter Search Criteria
        │
        ▼
Search by:

• Make
• Model
• Category
• Price Range
        │
        ▼
Query Database
        │
        ▼
Display Matching Vehicles
```

---

# 🔐 Authentication Workflow

```text
User Login
      │
      ▼
Validate Credentials
      │
 ┌────┴─────┐
 │          │
 ▼          ▼
Valid     Invalid
 │          │
 ▼          ▼
Create     Display Error
Session
 │
 ▼
Redirect to Dashboard
```

---

# 📊 Dashboard Workflow

The dashboard provides a consolidated overview of the dealership inventory.

It automatically displays:

- Total Vehicles
- Total Inventory Stock
- Low Stock Vehicles
- Recent Purchases
- Quick Administrative Actions

The dashboard updates dynamically as inventory operations are performed.

---

# 🧪 Testing Workflow (TDD)

Every feature is implemented following the Test-Driven Development methodology.

```text
Write Test
     │
     ▼
Run Test
(Fails)
     │
     ▼
Implement Feature
     │
     ▼
Run Test
(Passes)
     │
     ▼
Refactor Code
     │
     ▼
Commit Changes
```

---

# 🔄 End-to-End System Flow

```text
User
 │
 ▼
Authentication
 │
 ▼
Authorization
 │
 ▼
Dashboard
 │
 ▼
Vehicle Inventory
 │
 ├───────────────┐
 │               │
 ▼               ▼
Search       Vehicle Details
 │               │
 ▼               ▼
Results      Purchase Vehicle
 │               │
 └──────┬────────┘
        ▼
Update Inventory
        │
        ▼
Dashboard Statistics
        │
        ▼
Logout
```

---

# 🎯 Workflow Highlights

- ✔️ Secure authentication and session management
- ✔️ Role-based access for administrators
- ✔️ Complete vehicle inventory lifecycle management
- ✔️ Automatic inventory updates after purchases and restocking
- ✔️ Efficient vehicle search and filtering
- ✔️ Real-time dashboard statistics
- ✔️ Comprehensive server-side validation
- ✔️ Test-driven development for reliable feature implementation

---

# 🖼️ Application Workflow Preview

> **The following screenshots demonstrate the primary workflow and user journey throughout the application.**

<p align="center">
    <img src="screenshots/workflow/user_workflow.png"
         alt="User Workflow"
         width="48%">
    &nbsp;
    <img src="screenshots/workflow/admin_workflow.png"
         alt="Admin Workflow"
         width="48%">
</p>

# 🧩 Core Project Foundation

The **Core Project Foundation** establishes the reusable infrastructure upon which the entire application is built. Rather than implementing business-specific functionality, this phase focuses on creating a consistent project layout, shared user interface components, centralized routing, and common utilities that are leveraged across all modules.

By defining these foundational elements early in the development process, the project ensures improved code reusability, easier maintenance, and a consistent user experience throughout the application.

---

# 🎯 Objective

The primary objective of this module is to prepare a solid and scalable foundation for the application by:

- Establishing a reusable application layout
- Organizing templates and URL routing
- Configuring static assets
- Building shared UI components
- Promoting modular development
- Reducing code duplication through template inheritance

---

# ✨ Features Implemented

## 🏠 Base Layout

A centralized `base.html` template serves as the master layout for all pages within the application.

### Responsibilities

- Common HTML structure
- Bootstrap integration
- Global CSS & JavaScript
- Navigation components
- Flash messages
- Content placeholders
- Footer

This allows every page to inherit a consistent layout while only defining page-specific content.

---

## 🧭 Responsive Navigation Bar

A reusable navigation bar provides quick access to major sections of the application.

### Features

- Brand logo/title
- Navigation links
- Authentication-aware menu
- Responsive mobile navigation
- Active page highlighting

---

## 📂 Sidebar Navigation

The sidebar offers structured navigation for authenticated users and administrators.

### Includes

- Dashboard
- Vehicle Inventory
- Add Vehicle
- Purchase History
- User Management *(Admin)*
- Logout

The sidebar adapts based on the authenticated user's permissions.

---

## 🦶 Footer

A reusable footer is included across all pages to provide consistent branding and application information.

### Contains

- Copyright information
- Project name
- Current year
- Additional footer links *(if applicable)*

---

## 💬 Global Messages

The project uses Django's **Messages Framework** to provide real-time feedback to users.

### Supported Message Types

- ✅ Success
- ℹ️ Information
- ⚠️ Warning
- ❌ Error

Messages are displayed consistently across the application using a reusable template partial.

---

## 🛣️ URL Organization

Application routes are organized using Django's URL dispatcher for improved maintainability.

### Benefits

- Modular routing
- Readable URL structure
- Easier feature expansion
- Centralized route management

Example structure:

```text
/
├── login/
├── register/
├── dashboard/
├── vehicles/
├── vehicles/add/
├── vehicles/<id>/
├── vehicles/<id>/edit/
├── search/
└── admin/
```

---

## 🧱 Template Inheritance

To eliminate repetitive HTML, Django's template inheritance mechanism is used throughout the application.

```text
base.html
      │
      ├──────────────┐
      ▼              ▼
 login.html     dashboard.html
      │              │
      ▼              ▼
 inventory.html   vehicle_detail.html
```

### Advantages

- Reusable layouts
- Reduced duplication
- Easier maintenance
- Consistent design across pages

---

## 🎨 Static File Management

Static assets are organized to improve project maintainability and frontend consistency.

### Directory Structure

```text
static/
│
├── css/
├── js/
├── images/
├── fonts/
└── vendor/
```

### Managed Assets

- Stylesheets
- JavaScript files
- Icons
- Images
- Third-party libraries
- Custom frontend resources

---

## 🧰 Common Utilities

Reusable utilities are implemented to simplify development across multiple modules.

Examples include:

- Shared template partials
- Utility functions
- Common form styling
- Navigation helpers
- Authentication checks
- Reusable Bootstrap components

---

# 🏗️ Foundation Architecture

```text
                Base Template
                      │
      ┌───────────────┼───────────────┐
      │               │               │
      ▼               ▼               ▼
   Navbar          Sidebar         Footer
      │               │               │
      └───────────────┼───────────────┘
                      ▼
              Content Placeholder
                      │
       ┌──────────────┼──────────────┐
       ▼              ▼              ▼
 Authentication   Inventory     Dashboard
       │              │              │
       └──────────────┼──────────────┘
                      ▼
              Shared Components
```

---

# ⚙️ Technical Highlights

- Django Template Inheritance
- Reusable HTML Components
- Modular URL Configuration
- Bootstrap 5 Integration
- Django Static Files Framework
- Django Messages Framework
- Responsive Layout Design
- DRY (Don't Repeat Yourself) Principles
- Clean Project Organization

---

# 📈 Benefits

The Core Project Foundation provides several long-term advantages:

- ✔️ Consistent user interface across all pages
- ✔️ Faster development of new features
- ✔️ Improved code maintainability
- ✔️ Reduced code duplication
- ✔️ Centralized application structure
- ✔️ Better scalability for future enhancements
- ✔️ Simplified navigation and routing
- ✔️ Easier collaboration and debugging

---

# 🖼️ Module Preview

> **The following screenshots showcase the shared components and foundational layout used throughout the application.**

### 🏠 Base Layout

<p align="center">
    <img src="screenshots/foundation/base_layout.png"
         alt="Base Layout"
         width="85%">
</p>

---

### 🧭 Navigation & Sidebar

<p align="center">
    <img src="screenshots/foundation/navbar.png"
         alt="Navigation Bar"
         width="48%">
    &nbsp;
    <img src="screenshots/foundation/sidebar.png"
         alt="Sidebar"
         width="48%">
</p>

---

### 💬 Global Messages

<p align="center">
    <img src="screenshots/foundation/messages.png"
         alt="Django Messages Framework"
         width="65%">
</p>

# 🔐 Authentication Module

The **Authentication Module** provides a secure and reliable user access system for the **Car Dealership Inventory Management System**. It leverages Django's built-in authentication framework to handle user registration, login, logout, session management, and authorization.

The module ensures that only authenticated users can access protected resources, while administrative functionalities remain restricted to authorized users through role-based access control.

---

# 🎯 Objective

The primary objective of this module is to provide a secure authentication mechanism that:

- Registers new users
- Authenticates existing users
- Manages user sessions
- Protects restricted pages
- Restricts administrative functionality
- Prevents unauthorized access

---

# ✨ Features Implemented

## 👤 User Registration

New users can create an account through a registration form.

### Registration Features

- User registration form
- Username validation
- Email validation
- Duplicate username prevention
- Duplicate email prevention
- Password confirmation
- Password hashing
- Automatic account creation
- Success and error notifications

---

## 🔑 User Login

Registered users can securely authenticate using their credentials.

### Login Features

- Username-based authentication
- Secure password verification
- Session creation
- Remember authenticated users during active sessions
- Invalid credential handling
- User-friendly error messages

---

## 🚪 Secure Logout

Authenticated users can safely end their session.

### Logout Features

- Session termination
- Authentication cleanup
- Redirect to login or home page
- Prevent access to protected pages after logout

---

## 🛡️ Authorization & Access Control

Sensitive pages are protected using Django's authorization mechanisms.

### Access Restrictions

- Authentication required for protected routes
- Administrator-only pages
- Permission-based navigation
- Unauthorized access prevention
- Automatic redirection for unauthenticated users

---

# 🔒 Security Features

The authentication system utilizes Django's built-in security mechanisms to safeguard user accounts and application resources.

### Implemented Security Measures

- Password Hashing
- Session-Based Authentication
- CSRF Protection
- Secure Login Sessions
- Role-Based Authorization
- Form Validation
- Login Required Decorators
- Built-in Authentication Middleware
- SQL Injection Protection (Django ORM)
- XSS Protection through Template Escaping

---

# ⚙️ Technical Implementation

### Django Components Used

- Django Authentication Framework
- User Model
- Authentication Middleware
- Django Forms
- Django Sessions
- Django Messages Framework
- URL Routing
- Login Required Decorators
- Permission Checks

---

## 📝 Registration Workflow

```text
User Opens Registration Page
            │
            ▼
     Fill Registration Form
            │
            ▼
     Validate User Input
            │
      ┌─────┴─────┐
      │           │
      ▼           ▼
   Validation   Validation
    Failed       Passed
      │           │
      ▼           ▼
Display Errors  Create User
                    │
                    ▼
             Hash Password
                    │
                    ▼
            Save User Account
                    │
                    ▼
          Display Success Message
                    │
                    ▼
             Redirect to Login
```

---

## 🔑 Login Workflow

```text
User Opens Login Page
          │
          ▼
Enter Username & Password
          │
          ▼
Authenticate User
          │
     ┌────┴─────┐
     │          │
     ▼          ▼
 Invalid      Valid
Credentials Credentials
     │          │
     ▼          ▼
Display Error Create Session
                 │
                 ▼
       Redirect to Dashboard
```

---

## 🚪 Logout Workflow

```text
Authenticated User
        │
        ▼
Click Logout
        │
        ▼
Destroy Session
        │
        ▼
Redirect to Login / Home
        │
        ▼
Protected Pages No Longer Accessible
```

---

## 🛡️ Authorization Workflow

```text
User Requests Protected Page
              │
              ▼
Check Authentication
              │
      ┌───────┴────────┐
      │                │
      ▼                ▼
Authenticated    Not Authenticated
      │                │
      ▼                ▼
Check Permissions  Redirect to Login
      │
 ┌────┴────┐
 │         │
 ▼         ▼
Allowed  Denied
 │         │
 ▼         ▼
Access   Display 403 /
Granted  Unauthorized Page
```

---

# 📂 Authentication Components

```text
Authentication Module
│
├── Registration
├── Login
├── Logout
├── Session Management
├── Authorization
├── Form Validation
├── Messages Framework
└── Permission Handling
```

---

# 🧪 Test Coverage

Following the **Test-Driven Development (TDD)** approach, the authentication module is validated through automated unit tests.

### Test Scenarios

- User registration
- Successful login
- Invalid login credentials
- Duplicate username validation
- Duplicate email validation
- Password confirmation validation
- Logout functionality
- Protected route access
- Unauthorized access handling
- Admin-only page restrictions

---

# 📈 Benefits

The Authentication Module provides:

- ✔️ Secure user authentication
- ✔️ Reliable session management
- ✔️ Protected application resources
- ✔️ Role-based authorization
- ✔️ Improved application security
- ✔️ Better user experience through informative feedback
- ✔️ Reusable authentication infrastructure
- ✔️ Scalable foundation for future permission enhancements

---

# 🖼️ Module Preview

> **The following screenshots demonstrate the authentication workflow and user access management features.**

### 👤 User Registration

<p align="center">
    <img src="screenshots/authentication/register.png"
         alt="User Registration"
         width="80%">
</p>

---

### 🔑 User Login

<p align="center">
    <img src="screenshots/authentication/login.png"
         alt="User Login"
         width="80%">
</p>

---

### 🛡️ Authorization & Protected Routes

<p align="center">
    <img src="screenshots/authentication/protected_route.png"
         alt="Protected Route"
         width="48%">
    &nbsp;
    <img src="screenshots/authentication/unauthorized_access.png"
         alt="Unauthorized Access"
         width="48%">
</p>

---

### 🚪 Logout

<p align="center">
    <img src="screenshots/authentication/logout.png"
         alt="User Logout"
         width="70%">
</p>

# 🚗 Vehicle Management Module

The **Vehicle Management Module** serves as the core component of the **Car Dealership Inventory Management System**, enabling administrators to efficiently manage the complete vehicle inventory lifecycle. It provides comprehensive **CRUD (Create, Read, Update, Delete)** operations, allowing authorized users to maintain accurate and up-to-date vehicle records.

Built with Django's Model-View-Template (MTV) architecture, this module ensures secure data management, robust server-side validation, and seamless integration with inventory operations and dashboard analytics.

---

# 🎯 Objective

The primary objective of this module is to provide a centralized system for managing dealership inventory by allowing administrators to:

- Add new vehicles to the inventory
- View all available vehicles
- Display detailed vehicle information
- Update existing vehicle records
- Delete obsolete vehicles
- Maintain accurate stock information
- Ensure data consistency through validation

---

# ✨ Features Implemented

## 🚘 Vehicle Model

The application maintains vehicle information using a dedicated Django model.

### Vehicle Attributes

| Field | Description |
|--------|-------------|
| **Make** | Vehicle manufacturer (e.g., Toyota, Honda) |
| **Model** | Vehicle model name |
| **Category** | Vehicle type/category |
| **Price** | Selling price of the vehicle |
| **Quantity** | Current inventory stock |
| **Created At** | Record creation timestamp |
| **Updated At** | Last modification timestamp |

---

## ➕ Add Vehicle

Administrators can register new vehicles into the inventory through a secure form.

### Features

- Administrator-only access
- Server-side validation
- Required field validation
- Price validation
- Quantity validation
- Success & error notifications
- Automatic database insertion

---

## 📋 View Inventory

Displays all vehicles currently available in the dealership inventory.

### Features

- Organized vehicle listing
- Responsive table/card layout
- Vehicle summary information
- Quick navigation to vehicle details
- Empty inventory handling
- Clean and responsive interface

---

## 🔍 Vehicle Details

Each vehicle has a dedicated detail page containing complete information.

### Displays

- Make
- Model
- Category
- Price
- Quantity Available
- Creation Date
- Last Updated Date

---

## ✏️ Update Vehicle

Administrators can modify existing vehicle information whenever inventory details change.

### Supported Updates

- Make
- Model
- Category
- Price
- Quantity

### Features

- Pre-populated edit form
- Validation before saving
- Automatic timestamp update
- Success confirmation message

---

## 🗑️ Delete Vehicle

Allows administrators to safely remove vehicles from the inventory.

### Features

- Confirmation page before deletion
- Prevent accidental record removal
- Permanent database deletion
- Success notification
- Redirect to updated inventory list

---

# 🔄 CRUD Workflow

```text
                Administrator
                       │
                       ▼
             Vehicle Management
                       │
      ┌────────────────┼────────────────┐
      ▼                ▼                ▼
 Add Vehicle      View Inventory    Vehicle Details
      │                                 │
      ▼                                 ▼
Validate Form                     Edit / Delete
      │                                 │
      ▼                                 ▼
 Save Record                  Update Database
      │                                 │
      └──────────────┬──────────────────┘
                     ▼
             Updated Inventory
```

---

# 📂 Vehicle Lifecycle

```text
Create Vehicle
       │
       ▼
Stored in Database
       │
       ▼
Displayed in Inventory
       │
       ▼
Viewed by Users
       │
       ▼
Updated by Admin
       │
       ▼
Deleted (If Required)
```

---

# ⚙️ Technical Implementation

### Django Components Used

- Django Models
- Django ORM
- Django Forms
- Function-Based / Class-Based Views
- URL Routing
- Template Inheritance
- Django Messages Framework
- Form Validation
- Authentication & Authorization

---

## 🧾 Database Operations

The module performs the following database operations through Django ORM:

- Create Vehicle Record
- Retrieve Vehicle List
- Retrieve Vehicle Details
- Update Existing Vehicle
- Delete Vehicle Record

No raw SQL queries are required, ensuring secure and maintainable database interactions.

---

# 🔒 Access Control

Vehicle management operations are protected using Django's authentication and authorization mechanisms.

| Feature | Access Level |
|----------|--------------|
| View Inventory | Authenticated Users |
| View Vehicle Details | Authenticated Users |
| Add Vehicle | Administrator |
| Update Vehicle | Administrator |
| Delete Vehicle | Administrator |

Unauthorized users attempting to access restricted pages are redirected appropriately or shown an authorization error.

---

# ✅ Validation Rules

The module implements comprehensive server-side validation to maintain data integrity.

### Validation Includes

- Required fields
- Valid price values
- Non-negative quantity
- Correct data types
- Empty form prevention
- Invalid input handling

Users receive clear feedback through Django's Messages Framework whenever validation fails.

---

# 🧪 Test Coverage

Following the **Test-Driven Development (TDD)** methodology, the Vehicle Management Module is validated through automated tests.

### Test Scenarios

- Vehicle creation
- Vehicle retrieval
- Vehicle detail page
- Vehicle update
- Vehicle deletion
- Form validation
- Invalid data handling
- Permission checks
- Admin-only operations
- Inventory display

---

# 📈 Benefits

This module provides several operational advantages:

- ✔️ Centralized inventory management
- ✔️ Complete CRUD functionality
- ✔️ Secure administrator controls
- ✔️ Accurate inventory records
- ✔️ Consistent data validation
- ✔️ Improved maintainability
- ✔️ Scalable data model
- ✔️ Seamless integration with dashboard and inventory operations

---

# 🖼️ Module Preview

> **The following screenshots demonstrate the complete vehicle management workflow.**

### 📋 Vehicle Inventory

<p align="center">
    <img src="screenshots/vehicle/inventory_list.png"
         alt="Vehicle Inventory"
         width="85%">
</p>

---

### ➕ Add Vehicle

<p align="center">
    <img src="screenshots/vehicle/add_vehicle.png"
         alt="Add Vehicle"
         width="80%">
</p>

---

### 🔍 Vehicle Details

<p align="center">
    <img src="screenshots/vehicle/vehicle_details.png"
         alt="Vehicle Details"
         width="80%">
</p>

---

### ✏️ Update Vehicle

<p align="center">
    <img src="screenshots/vehicle/update_vehicle.png"
         alt="Update Vehicle"
         width="48%">
    &nbsp;
    <img src="screenshots/vehicle/update_success.png"
         alt="Update Success"
         width="48%">
</p>

---

### 🗑️ Delete Vehicle

<p align="center">
    <img src="screenshots/vehicle/delete_confirmation.png"
         alt="Delete Confirmation"
         width="48%">
    &nbsp;
    <img src="screenshots/vehicle/delete_success.png"
         alt="Delete Success"
         width="48%">
</p>

# 📦 Inventory Operations Module

The **Inventory Operations Module** manages the movement of vehicle stock within the dealership by handling **vehicle purchases** and **inventory restocking**. It ensures that stock quantities remain accurate, prevents invalid inventory transactions, and maintains the integrity of inventory data throughout the application.

This module works closely with the **Vehicle Management**, **Dashboard**, and **Purchase History** modules to provide real-time inventory updates and operational insights.

---

# 🎯 Objective

The primary objective of this module is to provide reliable inventory control by allowing users to purchase available vehicles while enabling administrators to replenish inventory whenever required.

The module ensures:

- Accurate stock management
- Prevention of negative inventory
- Controlled inventory updates
- Seamless synchronization with dashboard statistics
- Secure administrator-only restocking operations

---

# ✨ Features Implemented

## 🛒 Purchase Vehicle

Authenticated users can purchase vehicles that are currently available in stock.

### Features

- Purchase available vehicles
- Automatic stock reduction
- Real-time inventory updates
- Out-of-stock detection
- Purchase confirmation
- Success and error notifications
- Inventory synchronization

---

## 📦 Restock Vehicle

Administrators can increase the available quantity of existing vehicles whenever inventory needs replenishment.

### Features

- Administrator-only access
- Increase inventory quantity
- Server-side quantity validation
- Immediate inventory update
- Dashboard synchronization
- Success notifications

---

## 🚫 Stock Availability Protection

The system automatically validates inventory before processing a purchase.

### Validation Includes

- Prevent purchasing unavailable vehicles
- Prevent negative stock values
- Disable purchase actions for out-of-stock vehicles
- Display appropriate feedback messages

---

# 🔄 Purchase Workflow

```text
User Selects Vehicle
          │
          ▼
View Vehicle Details
          │
          ▼
Click Purchase
          │
          ▼
Check Available Stock
          │
    ┌─────┴──────┐
    │            │
    ▼            ▼
Stock        Out of Stock
Available
    │            │
    ▼            ▼
Reduce      Display Error
Quantity
    │
    ▼
Save Updated Stock
    │
    ▼
Display Success Message
```

---

# 📦 Restock Workflow

```text
Administrator
      │
      ▼
Select Vehicle
      │
      ▼
Open Restock Form
      │
      ▼
Enter Quantity
      │
      ▼
Validate Input
      │
      ▼
Increase Stock
      │
      ▼
Update Database
      │
      ▼
Display Success Message
```

---

# 📊 Inventory State Flow

```text
Vehicle Added
      │
      ▼
Inventory Available
      │
      ▼
Customer Purchase
      │
      ▼
Reduce Stock
      │
      ▼
Stock Reaches Zero?
      │
 ┌────┴─────┐
 │          │
 ▼          ▼
No         Yes
 │          │
 ▼          ▼
Continue   Disable Purchase
Selling        │
               ▼
      Administrator Restocks
               │
               ▼
       Inventory Available Again
```

---

# ⚙️ Technical Implementation

### Django Components Used

- Django Models
- Django ORM
- Django Forms
- Django Views
- URL Routing
- Template Inheritance
- Django Messages Framework
- Authentication & Authorization
- Server-Side Validation

---

## 🗄️ Database Operations

The Inventory Operations Module performs the following actions using Django ORM:

### Purchase Operation

- Retrieve selected vehicle
- Validate available quantity
- Decrease stock quantity
- Save updated record

### Restock Operation

- Retrieve selected vehicle
- Validate restock quantity
- Increase available stock
- Save updated record

---

# 🔒 Access Control

Inventory operations are protected according to user roles.

| Operation | Access Level |
|-----------|--------------|
| Purchase Vehicle | Authenticated Users |
| Restock Vehicle | Administrator |

Unauthorized users cannot access administrative inventory operations.

---

# ✅ Validation Rules

The module implements comprehensive validation to maintain inventory accuracy.

### Purchase Validation

- Vehicle must exist
- Stock must be greater than zero
- Quantity cannot become negative
- Purchase request must be valid

### Restock Validation

- Positive quantity required
- Vehicle must exist
- Authorized administrator required
- Valid numeric input

---

# 📈 Inventory Synchronization

Inventory changes are automatically reflected across the application.

### Updated Components

- Vehicle Inventory
- Vehicle Details
- Dashboard Statistics
- Purchase History
- Search Results
- Stock Indicators

This ensures users always view the most current inventory information.

---

# 🧪 Test Coverage

The Inventory Operations Module follows the **Test-Driven Development (TDD)** methodology with automated tests covering critical inventory scenarios.

### Test Scenarios

- Successful vehicle purchase
- Stock reduction after purchase
- Prevent purchase when stock is zero
- Restock vehicle successfully
- Inventory quantity updates correctly
- Invalid restock quantity
- Unauthorized restock attempt
- Permission validation
- Inventory synchronization

---

# 📈 Benefits

This module provides several operational benefits:

- ✔️ Accurate inventory tracking
- ✔️ Prevention of negative stock values
- ✔️ Real-time inventory updates
- ✔️ Secure administrative controls
- ✔️ Improved inventory reliability
- ✔️ Seamless integration with dashboard analytics
- ✔️ Enhanced user experience through clear feedback
- ✔️ Scalable inventory management workflow

---

# 🖼️ Module Preview

> **The following screenshots demonstrate the inventory operations workflow, including vehicle purchasing and inventory restocking.**

### 🛒 Purchase Vehicle

<p align="center">
    <img src="screenshots/inventory/purchase_vehicle.png"
         alt="Purchase Vehicle"
         width="80%">
</p>

---

### 📦 Restock Vehicle

<p align="center">
    <img src="screenshots/inventory/restock_vehicle.png"
         alt="Restock Vehicle"
         width="80%">
</p>

---

### 🚫 Out of Stock Handling

<p align="center">
    <img src="screenshots/inventory/out_of_stock.png"
         alt="Out of Stock"
         width="48%">
    &nbsp;
    <img src="screenshots/inventory/restock_success.png"
         alt="Restock Success"
         width="48%">
</p>

# 🔍 Search Module

The **Search Module** enables users to quickly locate vehicles within the dealership inventory using multiple filtering criteria. As the inventory grows, efficient search functionality becomes essential for improving usability and reducing the time required to find specific vehicles.

This module integrates seamlessly with the **Vehicle Management Module** by querying the inventory database and presenting relevant results in real time. It supports both individual and combined search filters, allowing users to narrow down results based on their requirements.

---

# 🎯 Objective

The primary objective of this module is to provide a fast and user-friendly search experience by allowing users to:

- Search vehicles by make
- Search vehicles by model
- Filter vehicles by category
- Filter vehicles within a price range
- Display matching vehicles dynamically
- Improve inventory navigation and accessibility

---

# ✨ Features Implemented

## 🚘 Search by Make

Users can search vehicles based on the manufacturer.

### Example

```text
Toyota
Honda
Hyundai
BMW
Mercedes-Benz
```

---

## 🚗 Search by Model

Allows users to locate vehicles using the model name.

### Example

```text
Civic
Corolla
Creta
Fortuner
Model 3
```

---

## 🗂️ Filter by Category

Vehicles can be filtered according to their category.

### Supported Categories

- Sedan
- SUV
- Hatchback
- Coupe
- Convertible
- Pickup
- Electric Vehicle (EV)
- Luxury

---

## 💰 Filter by Price Range

Users can narrow search results by specifying a price range.

### Example

```text
₹0 – ₹500,000

₹500,001 – ₹1,000,000

₹1,000,001+
```

---

## 🔄 Combined Filtering

Multiple filters can be applied simultaneously for more precise search results.

### Example

```text
Make      : Toyota
Category  : SUV
Price     : ₹10L – ₹20L
```

Result:

```text
Toyota Fortuner
Toyota Urban Cruiser Hyryder
```

---

# 🔄 Search Workflow

```text
User Opens Search Page
            │
            ▼
     Enter Search Criteria
            │
            ▼
Choose One or More Filters
            │
            ▼
Submit Search Request
            │
            ▼
Validate Input
            │
            ▼
Query Database (Django ORM)
            │
            ▼
Retrieve Matching Vehicles
            │
            ▼
Display Search Results
```

---

# 📊 Search Flow Diagram

```text
Vehicle Inventory
        │
        ▼
Search Filters
        │
 ┌──────┼──────────────┬──────────────┐
 ▼      ▼              ▼              ▼
Make   Model       Category      Price Range
        │
        ▼
Generate Query
        │
        ▼
Database Search
        │
        ▼
Matching Vehicles
        │
        ▼
Display Results
```

---

# ⚙️ Technical Implementation

### Django Components Used

- Django ORM
- QuerySet Filtering
- Django Views
- Django Templates
- URL Routing
- GET Parameters
- Bootstrap Forms
- Template Inheritance

---

## 🗄️ Database Querying

The module uses Django ORM to efficiently filter vehicle records based on user-selected criteria.

Typical filtering operations include:

- Exact matching
- Partial text matching
- Case-insensitive search
- Numeric range filtering
- Combined QuerySet filtering

No raw SQL queries are used, ensuring secure and maintainable database interactions.

---

# 📋 Supported Search Parameters

| Search Filter | Description |
|---------------|-------------|
| **Make** | Search by vehicle manufacturer |
| **Model** | Search by vehicle model |
| **Category** | Filter by vehicle category |
| **Price Range** | Filter vehicles within a specified price range |

Multiple filters may be combined to refine search results.

---

# 🔒 Validation & Error Handling

The Search Module gracefully handles various user scenarios.

### Validation Includes

- Empty search submissions
- Invalid price ranges
- No matching vehicles found
- Invalid query parameters
- Safe input processing

Appropriate feedback is displayed using Django's Messages Framework where applicable.

---

# 📈 Performance Considerations

To provide efficient searching even as the inventory grows, the module follows these practices:

- Efficient Django ORM queries
- Lazy QuerySet evaluation
- Server-side filtering
- Minimal database operations
- Optimized page rendering

These practices help reduce unnecessary database load and improve response time.

---

# 🧪 Test Coverage

Following the **Test-Driven Development (TDD)** methodology, the Search Module is validated using automated tests.

### Test Scenarios

- Search by make
- Search by model
- Filter by category
- Filter by price range
- Combined search filters
- No matching results
- Empty search request
- Invalid filter values
- Query accuracy

---

# 📈 Benefits

The Search Module offers several usability improvements:

- ✔️ Faster vehicle discovery
- ✔️ Improved inventory navigation
- ✔️ Multi-criteria filtering
- ✔️ Accurate search results
- ✔️ Scalable search functionality
- ✔️ Better user experience
- ✔️ Reduced time spent locating vehicles
- ✔️ Seamless integration with inventory management

---

# 🖼️ Module Preview

> **The following screenshots demonstrate the vehicle search interface and filtering functionality.**

### 🔍 Vehicle Search

<p align="center">
    <img src="screenshots/search/search_page.png"
         alt="Vehicle Search"
         width="85%">
</p>

---

### 🎯 Filtered Search Results

<p align="center">
    <img src="screenshots/search/search_results.png"
         alt="Search Results"
         width="48%">
    &nbsp;
    <img src="screenshots/search/filter_results.png"
         alt="Filtered Results"
         width="48%">
</p>

---

### 🚫 No Matching Results

<p align="center">
    <img src="screenshots/search/no_results.png"
         alt="No Search Results"
         width="70%">
</p>

# 📊 Dashboard Module

The **Dashboard Module** serves as the central overview of the **Car Dealership Inventory Management System**, providing users and administrators with real-time insights into the current inventory status and dealership operations. Instead of navigating through multiple pages, users can quickly access key metrics, recent activities, and frequently used actions from a single interface.

The dashboard is designed to improve decision-making by presenting important inventory information in a clear, organized, and visually intuitive manner.

---

# 🎯 Objective

The primary objective of the Dashboard Module is to provide a centralized overview of dealership operations by displaying:

- Current inventory statistics
- Vehicle stock availability
- Low-stock alerts
- Recent purchase activity
- Quick access to frequently used features
- Real-time operational insights

---

# ✨ Features Implemented

## 📈 Inventory Statistics

The dashboard displays important inventory metrics to help users monitor the overall status of the dealership.

### Available Statistics

- Total Vehicles
- Total Available Stock
- Available Categories
- Total Inventory Value *(Optional)*
- Active Inventory Records

---

## ⚠️ Low Stock Monitoring

Vehicles with limited stock are highlighted to help administrators identify inventory that requires replenishment.

### Benefits

- Easy identification of low-stock vehicles
- Better inventory planning
- Supports timely restocking decisions

---

## 🛒 Recent Purchase Activity

Displays the most recent vehicle purchase transactions.

### Information Displayed

- Vehicle Name
- Purchase Date
- Remaining Stock
- Purchase Status

This provides administrators with a quick overview of recent inventory movement.

---

## 🚀 Quick Actions

Frequently used operations are accessible directly from the dashboard.

### Quick Access

- Add Vehicle
- View Inventory
- Search Vehicles
- Restock Inventory
- Purchase History

These shortcuts improve navigation and reduce the number of steps required to perform common tasks.

---

## 📋 Inventory Summary

Provides a concise overview of the dealership inventory.

### Summary Includes

- Available Vehicles
- Out-of-Stock Vehicles
- Recently Added Vehicles
- Recently Updated Vehicles

---

# 🔄 Dashboard Workflow

```text
User Login
      │
      ▼
Open Dashboard
      │
      ▼
Fetch Dashboard Data
      │
      ▼
Retrieve Statistics
      │
      ▼
Retrieve Inventory Summary
      │
      ▼
Retrieve Recent Purchases
      │
      ▼
Render Dashboard
      │
      ▼
Display Real-Time Insights
```

---

# 📊 Dashboard Data Flow

```text
                 Database
                     │
     ┌───────────────┼────────────────┐
     ▼               ▼                ▼
Vehicle Data   Purchase History   Inventory Status
     │               │                │
     └───────────────┼────────────────┘
                     ▼
             Dashboard Processing
                     │
                     ▼
          Statistics & Summary Cards
                     │
                     ▼
              Dashboard Interface
```

---

# ⚙️ Technical Implementation

### Django Components Used

- Django ORM
- Django Views
- Django Templates
- Template Inheritance
- Django Context Data
- Bootstrap Cards
- Authentication & Authorization
- Django Messages Framework

---

## 📋 Dashboard Components

| Component | Purpose |
|-----------|---------|
| **Statistics Cards** | Display key inventory metrics |
| **Low Stock Section** | Highlight vehicles requiring restocking |
| **Recent Purchases** | Display latest inventory transactions |
| **Quick Actions** | Provide shortcuts to common operations |
| **Inventory Summary** | Present a concise overview of current inventory |

---

# 🔒 Access Control

Dashboard access is protected based on authentication status.

| Dashboard Feature | Access Level |
|-------------------|--------------|
| View Dashboard | Authenticated Users |
| Inventory Statistics | Authenticated Users |
| Quick Actions | Authenticated Users |
| Administrative Actions | Administrator |

Sensitive administrative actions remain restricted to authorized users.

---

# 📈 Real-Time Updates

The dashboard reflects the latest application data after inventory operations.

Automatically updated after:

- Vehicle Added
- Vehicle Updated
- Vehicle Deleted
- Vehicle Purchased
- Vehicle Restocked

This ensures users always view current dealership information.

---

# 🧪 Test Coverage

The Dashboard Module follows the **Test-Driven Development (TDD)** methodology with automated tests covering all major dashboard functionalities.

### Test Scenarios

- Dashboard loads successfully
- Statistics displayed correctly
- Low-stock vehicles listed
- Recent purchases retrieved
- Quick actions available
- Dashboard access permissions
- Empty inventory handling
- Data synchronization after inventory updates

---

# 📈 Benefits

The Dashboard Module provides several operational advantages:

- ✔️ Centralized application overview
- ✔️ Real-time inventory insights
- ✔️ Improved inventory monitoring
- ✔️ Faster access to common operations
- ✔️ Better administrative decision-making
- ✔️ Enhanced user experience
- ✔️ Seamless integration with inventory operations
- ✔️ Scalable dashboard architecture

---

# 🖼️ Module Preview

> **The following screenshots demonstrate the dashboard interface and real-time inventory insights.**

### 📊 Dashboard Overview

<p align="center">
    <img src="screenshots/dashboard/dashboard_overview.png"
         alt="Dashboard Overview"
         width="85%">
</p>

---

### 📈 Statistics Cards

<p align="center">
    <img src="screenshots/dashboard/statistics_cards.png"
         alt="Dashboard Statistics"
         width="48%">
    &nbsp;
    <img src="screenshots/dashboard/inventory_summary.png"
         alt="Inventory Summary"
         width="48%">
</p>

---

### ⚠️ Low Stock & Recent Purchases

<p align="center">
    <img src="screenshots/dashboard/low_stock.png"
         alt="Low Stock Vehicles"
         width="48%">
    &nbsp;
    <img src="screenshots/dashboard/recent_purchases.png"
         alt="Recent Purchases"
         width="48%">
</p>

# 👨‍💼 Admin Management Module

The **Admin Management Module** provides administrators with centralized control over dealership operations. It extends the application's core functionality by offering administrative dashboards, inventory management tools, purchase monitoring, and user administration capabilities.

This module is protected through **role-based authorization**, ensuring that only users with administrative privileges can access sensitive operations. By centralizing management features, administrators can efficiently monitor dealership performance, maintain inventory, and oversee system activities from a single interface.

---

# 🎯 Objective

The primary objective of this module is to provide administrators with a secure management environment for:

- Monitoring dealership activities
- Managing vehicle inventory
- Tracking purchase history
- Managing application users
- Accessing administrative tools
- Performing privileged operations securely

---

# ✨ Features Implemented

## 📊 Admin Dashboard

The Admin Dashboard provides a centralized overview of dealership operations and important business metrics.

### Dashboard Components

- Total Registered Vehicles
- Total Inventory Stock
- Low Stock Vehicles
- Recent Purchases
- Total Registered Users *(Optional)*
- Quick Administrative Actions

The dashboard enables administrators to monitor dealership performance at a glance.

---

## 🚗 Inventory Administration

Administrators have complete control over vehicle inventory.

### Administrative Operations

- Add Vehicle
- Update Vehicle Information
- Delete Vehicle
- Restock Inventory
- View Complete Inventory

These operations ensure inventory remains accurate and up to date.

---

## 🧾 Purchase History

The system maintains a history of vehicle purchase transactions.

### Purchase Information

- Vehicle Purchased
- Purchase Date & Time
- Customer/User *(if applicable)*
- Remaining Stock
- Purchase Status

This feature provides transparency into inventory movement and supports operational tracking.

---

## 👥 User Management *(Optional)*

Administrators can oversee registered users within the application.

### User Management Features

- View Registered Users
- Monitor User Activity *(Optional)*
- Manage User Roles *(Optional)*
- Enable or Disable User Accounts *(Optional)*

> **Note:** Depending on the assessment scope, user management may be implemented as an optional enhancement.

---

## ⚡ Administrative Quick Actions

To improve productivity, frequently used operations are available directly from the admin interface.

### Quick Actions

- Add New Vehicle
- Restock Inventory
- View Inventory
- Purchase History
- Dashboard
- Logout

---

# 🔄 Administrative Workflow

```text
Administrator Login
         │
         ▼
Verify Administrator Role
         │
         ▼
Access Admin Dashboard
         │
         ▼
Choose Administrative Task
         │
 ┌───────┼──────────────┬───────────────┐
 ▼       ▼              ▼               ▼
Inventory  Purchase   User           Dashboard
Management History   Management      Statistics
 │
 ▼
Perform Operation
 │
 ▼
Update Database
 │
 ▼
Display Success Message
```

---

# 📊 Admin Control Flow

```text
Administrator
      │
      ▼
Authentication
      │
      ▼
Authorization Check
      │
 ┌────┴────┐
 │         │
 ▼         ▼
Allowed   Denied
 │         │
 ▼         ▼
Admin     403 Error /
Dashboard Unauthorized Access
 │
 ▼
Administrative Operations
 │
 ▼
Database Updates
 │
 ▼
Updated Dashboard
```

---

# ⚙️ Technical Implementation

### Django Components Used

- Django Authentication System
- Django Permissions
- Django ORM
- Django Views
- Django Templates
- URL Routing
- Template Inheritance
- Django Messages Framework
- Login Required Decorators

---

## 🔒 Access Control

The Admin Management Module uses role-based authorization to protect administrative features.

| Feature | Access Level |
|----------|--------------|
| Admin Dashboard | Administrator |
| Add Vehicle | Administrator |
| Update Vehicle | Administrator |
| Delete Vehicle | Administrator |
| Restock Inventory | Administrator |
| Purchase History | Administrator |
| User Management *(Optional)* | Administrator |

Any unauthorized access attempts are intercepted and redirected or handled through custom error pages.

---

# 📋 Administrative Responsibilities

Administrators are responsible for maintaining the overall health of the dealership inventory.

### Core Responsibilities

- Inventory Management
- Stock Monitoring
- Purchase Tracking
- Inventory Restocking
- Vehicle Record Maintenance
- User Oversight *(Optional)*
- Operational Monitoring

---

# 📈 Dashboard Insights

The administrative dashboard provides valuable operational information, including:

- Inventory Statistics
- Low Stock Alerts
- Recent Purchases
- Total Vehicles
- Total Stock
- System Activity Summary

These insights help administrators make informed inventory management decisions.

---

# 🧪 Test Coverage

Following the **Test-Driven Development (TDD)** methodology, administrative functionality is validated through automated tests.

### Test Scenarios

- Administrator authentication
- Administrator authorization
- Admin dashboard access
- Add vehicle permissions
- Update vehicle permissions
- Delete vehicle permissions
- Restock permissions
- Purchase history access
- Unauthorized user restrictions
- Role-based access control

---

# 📈 Benefits

The Admin Management Module provides several operational advantages:

- ✔️ Centralized administrative control
- ✔️ Secure role-based access management
- ✔️ Efficient inventory administration
- ✔️ Improved operational monitoring
- ✔️ Better inventory planning
- ✔️ Simplified dealership management
- ✔️ Real-time administrative insights
- ✔️ Scalable management interface

---

# 🖼️ Module Preview

> **The following screenshots demonstrate the administrative interface and management capabilities available to authorized users.**

### 📊 Admin Dashboard

<p align="center">
    <img src="screenshots/admin/admin_dashboard.png"
         alt="Admin Dashboard"
         width="85%">
</p>

---

### 🚗 Inventory Management

<p align="center">
    <img src="screenshots/admin/inventory_management.png"
         alt="Inventory Management"
         width="48%">
    &nbsp;
    <img src="screenshots/admin/vehicle_management.png"
         alt="Vehicle Administration"
         width="48%">
</p>

---

### 🧾 Purchase History

<p align="center">
    <img src="screenshots/admin/purchase_history.png"
         alt="Purchase History"
         width="80%">
</p>

---

### 👥 User Management *(Optional)*

<p align="center">
    <img src="screenshots/admin/user_management.png"
         alt="User Management"
         width="80%">
</p>

# ✅ Validation & Error Handling

The **Validation & Error Handling Module** ensures that all user inputs and application requests are processed safely and correctly. By combining comprehensive **server-side validation** with **custom error handling**, the system maintains data integrity, enhances application security, and provides users with meaningful feedback whenever an invalid operation occurs.

This module is integrated throughout the application, supporting authentication, vehicle management, inventory operations, and administrative functionalities.

---

# 🎯 Objective

The primary objective of this module is to:

- Validate user input before processing
- Prevent invalid or inconsistent data
- Protect the application from unauthorized actions
- Handle unexpected errors gracefully
- Provide informative feedback to users
- Improve overall application reliability

---

# ✨ Features Implemented

## 📝 Form Validation

All forms are validated on the server before any database operation is performed.

### Validation Includes

- Required field validation
- Empty input prevention
- Correct data type validation
- Input length validation
- Numeric field validation
- Invalid input detection
- Duplicate record prevention (where applicable)

---

## 💰 Price Validation

Vehicle prices are validated before saving to the database.

### Rules

- Price must be provided
- Price must be numeric
- Price cannot be negative
- Invalid values are rejected

---

## 📦 Quantity Validation

Inventory quantity is validated to maintain accurate stock information.

### Rules

- Quantity must be numeric
- Quantity cannot be negative
- Invalid quantities are rejected
- Prevent inventory inconsistencies

---

## 🔐 Authentication Validation

Authentication forms include additional security validations.

### Includes

- Username validation
- Duplicate username prevention
- Duplicate email validation
- Password confirmation
- Invalid login credential handling

---

## 🚫 Permission Validation

Protected resources are accessible only to authorized users.

### Access Control

- Login required for protected pages
- Administrator-only functionality
- Unauthorized request detection
- Permission validation before execution

---

# ❌ Custom Error Pages

To provide a consistent and user-friendly experience, the application includes custom error pages for common HTTP errors.

---

## 🚫 403 — Forbidden

Displayed when a user attempts to access a resource without sufficient permissions.

### Example Scenarios

- Non-admin accessing administrative pages
- Restricted management operations
- Unauthorized inventory modifications

---

## 🔍 404 — Page Not Found

Displayed when the requested URL or resource does not exist.

### Example Scenarios

- Invalid URL
- Deleted vehicle
- Missing resource
- Incorrect route

---

## ⚠️ 500 — Internal Server Error

Displayed when an unexpected server-side error occurs.

### Purpose

- Prevent exposing internal application details
- Display a user-friendly error page
- Encourage users to retry later

---

# 🔄 Validation Workflow

```text
User Submits Form
        │
        ▼
Receive Request
        │
        ▼
Server-Side Validation
        │
   ┌────┴─────┐
   │          │
   ▼          ▼
Valid      Invalid
Input       Input
   │          │
   ▼          ▼
Save Data  Display Errors
   │
   ▼
Success Message
```

---

# 🚫 Error Handling Workflow

```text
User Request
      │
      ▼
Process Request
      │
 ┌────┴────────────┐
 │                 │
 ▼                 ▼
Valid Request   Error Detected
 │                 │
 ▼                 ▼
Continue      Determine Error Type
 │                 │
 ▼                 ▼
Success     403 / 404 / 500
                 │
                 ▼
      Display Custom Error Page
```

---

# ⚙️ Technical Implementation

### Django Components Used

- Django Forms
- Form Validation
- Model Validation
- Django Messages Framework
- Authentication Middleware
- Permission Checks
- Custom Error Handlers
- Template Inheritance
- URL Routing

---

# 🔒 Security Measures

Validation and error handling contribute significantly to application security.

### Implemented Protections

- Server-side validation
- Password hashing
- CSRF protection
- Session authentication
- SQL injection prevention (Django ORM)
- XSS protection through template escaping
- Permission-based authorization
- Safe form processing

---

# 💬 User Feedback

The application uses Django's **Messages Framework** to provide immediate feedback after user actions.

### Message Types

| Type | Purpose |
|------|---------|
| ✅ Success | Operation completed successfully |
| ℹ️ Information | General notifications |
| ⚠️ Warning | Potential issues requiring attention |
| ❌ Error | Validation or processing failures |

This ensures users receive clear and consistent feedback across the application.

---

# 🧪 Test Coverage

Following the **Test-Driven Development (TDD)** methodology, validation and error handling are verified using automated tests.

### Test Scenarios

- Required field validation
- Invalid price values
- Invalid quantity values
- Duplicate username
- Duplicate email
- Password confirmation mismatch
- Invalid login credentials
- Unauthorized page access
- 403 error handling
- 404 error handling
- Form validation failures

---

# 📈 Benefits

The Validation & Error Handling Module provides several key benefits:

- ✔️ Improved data integrity
- ✔️ Better application security
- ✔️ Prevention of invalid database records
- ✔️ Consistent user feedback
- ✔️ User-friendly error pages
- ✔️ Reduced application failures
- ✔️ Enhanced reliability
- ✔️ Better overall user experience

---

# 🖼️ Module Preview

> **The following screenshots demonstrate validation messages and custom error pages throughout the application.**

### 📝 Form Validation

<p align="center">
    <img src="screenshots/validation/form_validation.png"
         alt="Form Validation"
         width="80%">
</p>

---

### 💬 Success & Error Messages

<p align="center">
    <img src="screenshots/validation/success_message.png"
         alt="Success Message"
         width="48%">
    &nbsp;
    <img src="screenshots/validation/error_message.png"
         alt="Error Message"
         width="48%">
</p>

---

### ❌ Custom Error Pages

<p align="center">
    <img src="screenshots/validation/403.png"
         alt="403 Forbidden"
         width="31%">
    <img src="screenshots/validation/404.png"
         alt="404 Not Found"
         width="31%">
    <img src="screenshots/validation/500.png"
         alt="500 Internal Server Error"
         width="31%">
</p>

# 🧪 Testing (Test-Driven Development)

The **Car Dealership Inventory Management System** was developed following the principles of **Test-Driven Development (TDD)**, where automated tests were written alongside feature implementation to verify correctness, maintain reliability, and reduce regressions.

Rather than treating testing as a final step, each major feature was validated through dedicated test cases before being considered complete. This approach ensures that the application behaves as expected while making future enhancements safer and easier to implement.

---

# 🎯 Objective

The primary objective of adopting **Test-Driven Development (TDD)** was to:

- Develop reliable and maintainable software
- Detect defects early in the development cycle
- Verify business logic through automated tests
- Prevent regressions during future development
- Improve overall code quality and confidence

---

# 🔄 TDD Development Cycle

The project follows the standard **Red → Green → Refactor** workflow.

```text
          Write Test
               │
               ▼
        Run Test (Fail)
           🔴 RED
               │
               ▼
     Implement Minimum Code
               │
               ▼
        Run Test (Pass)
          🟢 GREEN
               │
               ▼
       Refactor the Code
               │
               ▼
     Ensure All Tests Pass
               │
               ▼
      Proceed to Next Feature
```

---

# 🧩 Testing Strategy

Testing was performed throughout the project lifecycle rather than after implementation.

Each module includes dedicated test cases covering:

- Functional correctness
- Input validation
- Authentication & authorization
- Permission handling
- Database operations
- Business rules
- Error scenarios

---

# 📋 Test Coverage by Module

## 🔐 Authentication Module

### Test Scenarios

- User registration
- Successful login
- Invalid login credentials
- Duplicate username validation
- Duplicate email validation
- Password confirmation validation
- Logout functionality
- Session creation and termination
- Protected route access
- Unauthorized access handling

---

## 🚗 Vehicle Management Module

### Test Scenarios

- Add vehicle
- View inventory
- View vehicle details
- Update vehicle
- Delete vehicle
- Form validation
- Invalid data handling
- Vehicle model validation
- Permission restrictions

---

## 📦 Inventory Operations Module

### Test Scenarios

- Purchase vehicle
- Reduce stock quantity
- Prevent purchase when stock is zero
- Restock vehicle
- Inventory quantity update
- Invalid restock quantity
- Purchase validation
- Inventory synchronization

---

## 🔍 Search Module

### Test Scenarios

- Search by make
- Search by model
- Filter by category
- Filter by price range
- Combined search filters
- Empty search
- No matching results
- Query accuracy

---

## 📊 Dashboard Module

### Test Scenarios

- Dashboard loads successfully
- Statistics calculation
- Low stock detection
- Recent purchases display
- Dashboard synchronization
- Empty inventory handling

---

## 👨‍💼 Admin Module

### Test Scenarios

- Administrator authentication
- Role-based authorization
- Admin dashboard access
- Inventory management permissions
- Purchase history access
- Unauthorized user restrictions

---

## ✅ Validation & Error Handling

### Test Scenarios

- Required field validation
- Invalid price values
- Invalid quantity values
- Duplicate user validation
- Invalid login credentials
- Permission validation
- 403 error page
- 404 error page
- Form validation errors

---

# ⚙️ Testing Tools

| Tool | Purpose |
|------|---------|
| **Django Test Framework** | Unit and integration testing |
| **Python unittest** | Test case implementation |
| **Django Test Client** | Simulating HTTP requests and responses |
| **SQLite Test Database** | Isolated test execution without affecting production data |

---

# 🧪 Running the Test Suite

Execute all automated tests using Django's built-in testing framework.

### Run All Tests

```bash
python manage.py test
```

---

### Run Tests with Detailed Output

```bash
python manage.py test --verbosity=2
```

---

### Run Tests for a Specific App

```bash
python manage.py test inventory
```

---

### Run a Specific Test Class

```bash
python manage.py test inventory.tests.VehicleModelTest
```

---

### Run a Specific Test Method

```bash
python manage.py test inventory.tests.VehicleModelTest.test_create_vehicle
```

---

# 📂 Example Test Structure

```text
inventory/
│
├── tests/
│   ├── test_authentication.py
│   ├── test_vehicle_crud.py
│   ├── test_inventory.py
│   ├── test_search.py
│   ├── test_dashboard.py
│   ├── test_permissions.py
│   └── test_validation.py
```

> *The exact test organization may vary depending on the project's implementation.*

---

# 🔄 Testing Workflow

```text
Implement Feature
        │
        ▼
Write Test Cases
        │
        ▼
Run Tests
        │
 ┌──────┴──────┐
 │             │
 ▼             ▼
Pass         Fail
 │             │
 ▼             ▼
Next Feature  Fix Implementation
      │             │
      └──────┬──────┘
             ▼
      Re-run Test Suite
```

---

# 📈 Benefits of TDD

Following Test-Driven Development throughout the project provides several advantages:

- ✔️ Higher code reliability
- ✔️ Early defect detection
- ✔️ Safer code refactoring
- ✔️ Reduced regression bugs
- ✔️ Better software quality
- ✔️ Easier maintenance
- ✔️ Improved confidence during development
- ✔️ Clear verification of business requirements

---

# 📊 Testing Summary

| Category | Status |
|----------|--------|
| Authentication Tests | ✅ Covered |
| Vehicle CRUD Tests | ✅ Covered |
| Inventory Operation Tests | ✅ Covered |
| Search Tests | ✅ Covered |
| Dashboard Tests | ✅ Covered |
| Permission Tests | ✅ Covered |
| Validation Tests | ✅ Covered |
| Error Handling Tests | ✅ Covered |

---

# 🖼️ Module Preview

> **The following screenshots demonstrate successful test execution and the project's automated testing workflow.**

### 🧪 Test Execution

<p align="center">
    <img src="screenshots/testing/test_execution.png"
         alt="Test Execution"
         width="85%">
</p>

---

### ✅ Successful Test Results

<p align="center">
    <img src="screenshots/testing/test_results.png"
         alt="Successful Test Results"
         width="48%">
    &nbsp;
    <img src="screenshots/testing/test_coverage.png"
         alt="Test Coverage"
         width="48%">
</p>

# 🖼️ Application Screenshots

This section showcases the major interfaces of the **Car Dealership Inventory Management System**. The screenshots demonstrate the application's user interface, core workflows, and key functionalities implemented throughout the project.

> **Note:** The screenshots below represent the final application after completing all development phases. Images are organized module-wise to provide a clear overview of the system.

---

# 🏠 Home Page

The landing page provides users with an introduction to the dealership system and quick navigation to major features.

<p align="center">
    <img src="screenshots/application/home_page.png"
         alt="Home Page"
         width="90%">
</p>

---

# 🔐 Authentication Module

## 👤 User Registration

<p align="center">
    <img src="screenshots/authentication/register.png"
         alt="User Registration"
         width="80%">
</p>

---

## 🔑 User Login

<p align="center">
    <img src="screenshots/authentication/login.png"
         alt="User Login"
         width="80%">
</p>

---

# 📊 Dashboard

The dashboard provides a centralized overview of inventory statistics, recent activities, and quick actions.

<p align="center">
    <img src="screenshots/dashboard/dashboard_overview.png"
         alt="Dashboard"
         width="90%">
</p>

---

# 🚗 Vehicle Management

## 📋 Vehicle Inventory

<p align="center">
    <img src="screenshots/vehicle/inventory_list.png"
         alt="Vehicle Inventory"
         width="90%">
</p>

---

## ➕ Add Vehicle

<p align="center">
    <img src="screenshots/vehicle/add_vehicle.png"
         alt="Add Vehicle"
         width="80%">
</p>

---

## 🔍 Vehicle Details

<p align="center">
    <img src="screenshots/vehicle/vehicle_details.png"
         alt="Vehicle Details"
         width="80%">
</p>

---

## ✏️ Update Vehicle

<p align="center">
    <img src="screenshots/vehicle/update_vehicle.png"
         alt="Update Vehicle"
         width="80%">
</p>

---

## 🗑️ Delete Vehicle

<p align="center">
    <img src="screenshots/vehicle/delete_confirmation.png"
         alt="Delete Vehicle"
         width="80%">
</p>

---

# 📦 Inventory Operations

## 🛒 Purchase Vehicle

<p align="center">
    <img src="screenshots/inventory/purchase_vehicle.png"
         alt="Purchase Vehicle"
         width="80%">
</p>

---

## 📦 Restock Vehicle

<p align="center">
    <img src="screenshots/inventory/restock_vehicle.png"
         alt="Restock Vehicle"
         width="80%">
</p>

---

# 🔍 Search & Filtering

Users can quickly locate vehicles using multiple search filters.

<p align="center">
    <img src="screenshots/search/search_page.png"
         alt="Vehicle Search"
         width="90%">
</p>

---

# 👨‍💼 Admin Dashboard

The administrative interface provides privileged access to inventory management, purchase history, and operational statistics.

<p align="center">
    <img src="screenshots/admin/admin_dashboard.png"
         alt="Admin Dashboard"
         width="90%">
</p>

---

# 🧾 Purchase History

<p align="center">
    <img src="screenshots/admin/purchase_history.png"
         alt="Purchase History"
         width="90%">
</p>

---

# ✅ Validation & Error Handling

## 📝 Form Validation

<p align="center">
    <img src="screenshots/validation/form_validation.png"
         alt="Form Validation"
         width="80%">
</p>

---

## ❌ Custom Error Pages

<p align="center">
    <img src="screenshots/validation/403.png"
         alt="403 Forbidden"
         width="31%">
    <img src="screenshots/validation/404.png"
         alt="404 Not Found"
         width="31%">
    <img src="screenshots/validation/500.png"
         alt="500 Internal Server Error"
         width="31%">
</p>

---

# 🧪 Automated Testing

Successful execution of the project's automated test suite following the **Test-Driven Development (TDD)** approach.

<p align="center">
    <img src="screenshots/testing/test_results.png"
         alt="Automated Testing"
         width="90%">
</p>

---

# 📱 Responsive User Interface

The application is built using **Bootstrap 5**, ensuring a responsive layout across different screen sizes and devices.

<p align="center">
    <img src="screenshots/application/responsive_layout.png"
         alt="Responsive Interface"
         width="90%">
</p>

---

# 📸 Screenshot Directory Structure

For better organization, all screenshots are grouped by application module.

```text
screenshots/
│
├── application/
│   ├── home_page.png
│   └── responsive_layout.png
│
├── authentication/
│   ├── register.png
│   ├── login.png
│   └── logout.png
│
├── dashboard/
│   └── dashboard_overview.png
│
├── vehicle/
│   ├── inventory_list.png
│   ├── add_vehicle.png
│   ├── vehicle_details.png
│   ├── update_vehicle.png
│   └── delete_confirmation.png
│
├── inventory/
│   ├── purchase_vehicle.png
│   ├── restock_vehicle.png
│   └── out_of_stock.png
│
├── search/
│   ├── search_page.png
│   └── search_results.png
│
├── admin/
│   ├── admin_dashboard.png
│   └── purchase_history.png
│
├── validation/
│   ├── form_validation.png
│   ├── 403.png
│   ├── 404.png
│   └── 500.png
│
└── testing/
    ├── test_execution.png
    └── test_results.png
```

---

# 💡 Notes

- All screenshots were captured from the final working version of the application.
- Images are grouped according to their respective modules for easier navigation.
- Placeholder image paths can be replaced with actual screenshots after project completion.
- The screenshots illustrate the complete workflow, from user authentication to inventory management, administrative operations, and automated testing.

# 🚀 Future Improvements

Although the **Car Dealership Inventory Management System** successfully fulfills the assessment requirements, its modular architecture has been designed with scalability in mind. The current implementation establishes a strong foundation that can be extended with additional features to support real-world dealership operations.

The following enhancements are planned for future versions of the application.

---

# 🌟 Planned Enhancements

## 🖼️ Vehicle Image Management

Enhance the inventory by allowing administrators to upload and manage images for each vehicle.

### Proposed Features

- Upload multiple vehicle images
- Image preview before upload
- Thumbnail gallery
- Default placeholder image
- Image management interface

**Benefits**

- Improved user experience
- Better product visualization
- More professional inventory presentation

---

## ❤️ Wishlist & Favorites

Allow users to save vehicles for future reference.

### Proposed Features

- Add vehicles to favorites
- Remove from wishlist
- Personalized wishlist page
- Quick access to saved vehicles

---

## 📄 Invoice Generation

Automatically generate purchase invoices after successful vehicle purchases.

### Proposed Features

- Downloadable PDF invoice
- Purchase summary
- Customer details
- Vehicle details
- Purchase timestamp

---

## 📊 Advanced Analytics Dashboard

Expand the dashboard with richer insights and visual analytics.

### Proposed Features

- Sales trends
- Monthly purchases
- Category-wise inventory
- Revenue statistics
- Interactive charts
- Inventory growth analysis

---

## 🔔 Low Stock Notifications

Notify administrators whenever inventory falls below a predefined threshold.

### Proposed Features

- Dashboard alerts
- Email notifications
- Restock reminders
- Critical stock warnings

---

## 📱 REST API Support

Expose application functionality through RESTful APIs.

### Proposed Features

- Vehicle APIs
- Inventory APIs
- Authentication APIs
- Purchase APIs
- Search APIs

This would enable integration with mobile applications and third-party systems.

---

## 🔍 Advanced Search

Extend the current search module with more powerful filtering capabilities.

### Proposed Features

- Multiple category selection
- Sorting by price
- Sorting by newest vehicles
- Availability filters
- Dynamic search suggestions

---

## 📈 Reports & Export

Allow administrators to export dealership data.

### Proposed Features

- PDF reports
- Excel export
- CSV export
- Inventory reports
- Purchase reports

---

## 📧 Email Notifications

Improve communication by integrating automated email services.

### Proposed Features

- Registration confirmation
- Purchase confirmation
- Password reset
- Inventory notifications
- Administrative alerts

---

## 👥 Enhanced User Management

Extend administrative capabilities for managing application users.

### Proposed Features

- User roles
- Staff accounts
- Account activation
- User activity logs
- Permission management

---

## 💳 Online Payment Integration

Integrate secure payment gateways for online vehicle purchases.

### Potential Integrations

- Razorpay
- Stripe
- PayPal

---

## ☁️ Cloud Deployment

Deploy the application to a production-ready cloud environment.

### Potential Platforms

- Render
- Railway
- PythonAnywhere
- AWS
- Microsoft Azure
- Google Cloud Platform

---

## 🗄️ Database Scalability

Upgrade from SQLite to enterprise-grade database systems.

### Supported Databases

- PostgreSQL
- MySQL
- MariaDB

This enables improved scalability, concurrency, and production readiness.

---

## 📱 Progressive Web App (PWA)

Transform the application into a Progressive Web App.

### Proposed Features

- Installable application
- Offline support
- Push notifications
- Mobile-first experience

---

## 🤖 AI-Powered Recommendations

Integrate Artificial Intelligence to provide intelligent dealership insights.

### Possible Enhancements

- Vehicle recommendations
- Demand forecasting
- Inventory optimization
- Sales trend prediction
- Customer preference analysis

---

# 🛣️ Long-Term Roadmap

```text
Current System
      │
      ▼
Vehicle Images
      │
      ▼
Advanced Search
      │
      ▼
Reports & Analytics
      │
      ▼
REST API
      │
      ▼
Payment Gateway
      │
      ▼
Cloud Deployment
      │
      ▼
AI Recommendations
```

---

# 🎯 Development Goals

Future development will continue to focus on:

- ✔️ Improved user experience
- ✔️ Better performance
- ✔️ Enhanced security
- ✔️ Greater scalability
- ✔️ Modern web technologies
- ✔️ Enterprise-ready architecture
- ✔️ Mobile accessibility
- ✔️ Intelligent inventory management

---

# 📈 Scalability Vision

The modular design of this project allows new features to be integrated with minimal changes to the existing codebase.

Future versions aim to transform the application from a **basic dealership inventory management system** into a **complete dealership management platform**, capable of supporting inventory management, sales operations, customer interactions, reporting, analytics, and cloud-based deployments.

---

# 🖼️ Future Roadmap Preview

> **The diagram below represents the planned evolution of the project beyond the current implementation.**

<p align="center">
    <img src="screenshots/future/project_roadmap.png"
         alt="Project Roadmap"
         width="85%">
</p>

# 🤖 My AI Usage

Artificial Intelligence (AI) was used throughout the development of this project as a **software engineering assistant** to improve productivity, accelerate learning, and assist with problem-solving. Rather than replacing the development process, AI acted as a collaborative tool for understanding concepts, exploring implementation approaches, debugging issues, and improving documentation.

All significant development decisions, feature implementation, integration, testing, and final verification were performed by me to ensure the application met the assessment requirements and functioned as intended.

---

# 🎯 Objective

The purpose of using AI during this project was to:

- Accelerate the learning process
- Improve development efficiency
- Understand Django concepts more effectively
- Assist in debugging complex issues
- Generate better documentation
- Follow professional software engineering practices
- Improve overall project quality

---

# 🛠️ How AI Was Used

AI was used as an assistant during multiple stages of the project development lifecycle.

---

## 📋 Project Planning

AI assisted in organizing the project before implementation.

### Assistance Included

- Breaking the project into development phases
- Creating a logical implementation roadmap
- Suggesting project folder organization
- Planning module dependencies
- Recommending development milestones

---

## 🏗️ Development Assistance

During implementation, AI was primarily used as a technical reference and coding assistant.

### Assistance Included

- Explaining Django concepts
- Understanding framework features
- Suggesting implementation approaches
- Reviewing code structure
- Identifying potential improvements
- Explaining Python and Django best practices

---

## 🐞 Debugging & Problem Solving

AI was frequently used to investigate development issues and identify possible solutions.

### Assistance Included

- Django configuration errors
- Migration issues
- URL routing problems
- Template rendering issues
- Authentication logic
- Form validation
- Database-related errors
- Runtime exceptions
- Testing failures

Every suggested solution was reviewed and verified before being incorporated into the project.

---

## 🧪 Testing Support

AI assisted in improving the project's testing strategy.

### Assistance Included

- Explaining Test-Driven Development (TDD)
- Suggesting unit test scenarios
- Identifying edge cases
- Reviewing validation logic
- Improving test organization

All automated tests were executed and verified locally before considering a feature complete.

---

## 📝 Documentation

AI was also used to improve project documentation and presentation.

### Assistance Included

- README.md preparation
- Feature descriptions
- Technical explanations
- Workflow documentation
- Architecture diagrams
- Module organization
- Markdown formatting

---

# 🔄 AI-Assisted Development Workflow

```text
Project Requirement
         │
         ▼
Understand Problem
         │
         ▼
Consult AI for Guidance
         │
         ▼
Review Suggestions
         │
         ▼
Implement Solution
         │
         ▼
Run & Test Application
         │
         ▼
Verify Results
         │
         ▼
Refine if Necessary
         │
         ▼
Finalize Feature
```

---

# ⚙️ Development Responsibility

Although AI provided technical assistance, the following responsibilities remained entirely my own throughout the project.

| Responsibility | Ownership |
|---------------|-----------|
| Understanding Assessment Requirements | 👤 Me |
| Project Planning | 👤 Me |
| Feature Implementation | 👤 Me |
| Code Integration | 👤 Me |
| Debugging & Fixing Issues | 👤 Me |
| Running Test Cases | 👤 Me |
| Verifying Functionality | 👤 Me |
| Final Documentation Review | 👤 Me |
| Project Submission | 👤 Me |

---

# 🔒 Responsible AI Usage

AI was used responsibly as a development support tool rather than as a replacement for software engineering knowledge or decision-making.

Throughout the project, I ensured that:

- Every AI-generated suggestion was reviewed before implementation.
- Generated code was modified whenever necessary to fit project requirements.
- All application features were manually tested after implementation.
- The final project behavior was verified independently.
- Documentation accurately reflects the completed implementation.

---

# 📚 Learning Outcomes

Using AI throughout this project helped me strengthen both my technical knowledge and development workflow.

### Skills Improved

- Django application development
- Test-Driven Development (TDD)
- Python programming
- Debugging techniques
- Software architecture
- Project organization
- Technical documentation
- Problem-solving skills

Rather than replacing the learning process, AI accelerated it by providing explanations, implementation guidance, and technical references that I validated and applied throughout the project.

---

# 📊 AI Usage Summary

| Development Activity | AI Assistance |
|----------------------|:-------------:|
| Project Planning | ✅ |
| Django Learning | ✅ |
| Code Explanation | ✅ |
| Debugging Support | ✅ |
| Refactoring Suggestions | ✅ |
| Test Scenario Suggestions | ✅ |
| Documentation | ✅ |
| Feature Verification | 👤 Performed by Me |
| Test Execution | 👤 Performed by Me |
| Final Review | 👤 Performed by Me |
| Project Submission | 👤 Performed by Me |

---

# 📈 Benefits

Using AI responsibly during development provided several advantages:

- ✔️ Faster problem solving
- ✔️ Improved understanding of Django concepts
- ✔️ Better code organization
- ✔️ Higher development productivity
- ✔️ Improved documentation quality
- ✔️ Enhanced debugging efficiency
- ✔️ Better adherence to software engineering best practices
- ✔️ Increased confidence during implementation

---

# 🖼️ AI Development Workflow

> **The following illustration summarizes how AI was integrated into the development process as a collaborative engineering assistant.**

<p align="center">
    <img src="screenshots/ai/ai_development_workflow.png"
         alt="AI Development Workflow"
         width="85%">
</p>

---

# 📌 Declaration

This project was developed with the assistance of Artificial Intelligence as a **learning and software development support tool**. AI was used to assist with planning, concept clarification, debugging, testing guidance, and documentation. All generated suggestions were reviewed, validated, and adapted where necessary. The final implementation, testing, verification, and project submission represent my own work and understanding of the completed system.

# 💭 Project Reflection

Developing the **Car Dealership Inventory Management System** was a valuable learning experience that strengthened my understanding of modern web application development using **Python**, **Django**, and **Test-Driven Development (TDD)**. Beyond implementing functional requirements, this project provided practical exposure to designing scalable applications, organizing code effectively, and following professional software engineering practices.

Throughout the development process, I encountered various technical challenges that required careful analysis, debugging, and iterative improvements. Solving these challenges helped me gain confidence in building reliable, maintainable, and well-structured software.

---

# 🎯 Project Objectives Achieved

This project successfully accomplished its primary objectives by:

- Building a modular Django application
- Applying Test-Driven Development (TDD) principles
- Implementing secure user authentication
- Managing vehicle inventory efficiently
- Supporting inventory purchase and restocking operations
- Providing search and filtering capabilities
- Developing an administrative dashboard
- Implementing comprehensive validation and error handling
- Producing clear technical documentation

---

# 📚 Key Learning Outcomes

Working on this project significantly improved my technical and problem-solving skills.

### Technical Skills

- Django project architecture
- Django Models, Views, and Templates (MVT)
- Django ORM
- Authentication and authorization
- Form validation
- Database design
- Bootstrap integration
- Automated testing using Django Test Framework
- Git and version control

---

### Software Engineering Skills

- Test-Driven Development (TDD)
- Modular application design
- Code organization
- Debugging techniques
- Refactoring
- Documentation writing
- Requirement analysis
- Incremental feature development

---

# 🧩 Challenges Faced

Several challenges were encountered during development, providing valuable learning opportunities.

### Major Challenges

- Designing a clean and scalable project structure
- Understanding Django's request-response lifecycle
- Managing user authentication and permissions
- Implementing robust server-side validation
- Handling inventory consistency during purchases
- Writing meaningful automated tests
- Debugging application configuration issues
- Organizing project documentation professionally

Each challenge contributed to a deeper understanding of both Django and software engineering principles.

---

# 🔄 Development Experience

The project was developed in small, manageable phases rather than attempting to build all features at once.

The general workflow followed was:

```text
Requirement Analysis
        │
        ▼
Project Planning
        │
        ▼
Design Module
        │
        ▼
Implement Feature
        │
        ▼
Write & Execute Tests
        │
        ▼
Debug & Refactor
        │
        ▼
Document Feature
        │
        ▼
Proceed to Next Module
```

This incremental approach made the project easier to manage and ensured that each feature was thoroughly tested before moving forward.

---

# 🏆 Professional Practices Followed

During development, several professional software engineering practices were applied.

### Practices Adopted

- Modular project organization
- Meaningful naming conventions
- Separation of concerns
- Code reusability
- Server-side validation
- Automated testing
- Version control with Git
- Clear documentation
- Incremental development
- Continuous verification

---

# 🌱 Personal Growth

Beyond technical implementation, this project helped me develop a more disciplined and structured approach to software development.

Through this experience, I became more confident in:

- Understanding project requirements before coding
- Breaking complex problems into smaller tasks
- Reading framework documentation
- Debugging independently
- Writing cleaner and more maintainable code
- Verifying features through testing
- Creating professional project documentation

These skills will be valuable for future academic projects, internships, and professional software development.

---

# 🚀 Future Perspective

This project serves as a strong foundation for building more advanced Django applications.

In future projects, I plan to explore:

- Django REST Framework
- PostgreSQL
- Docker
- Cloud deployment
- CI/CD pipelines
- Advanced testing strategies
- API development
- Performance optimization
- Scalable application architecture

These technologies will help me build production-ready applications and further enhance my backend development skills.

---

# 📈 Overall Outcome

The successful completion of this project demonstrates my ability to:

- Analyze software requirements
- Design structured applications
- Develop full-stack Django solutions
- Apply Test-Driven Development principles
- Implement secure authentication
- Manage relational databases
- Debug and validate application behavior
- Produce professional technical documentation

Overall, this project has strengthened both my technical foundation and my confidence in developing structured, maintainable, and reliable software systems.

---

# 🖼️ Development Journey

> **The following illustration summarizes the overall journey from project initialization to successful completion.**

<p align="center">
    <img src="screenshots/reflection/development_journey.png"
         alt="Development Journey"
         width="85%">
</p>

---

# 💬 Final Reflection

Completing the **Car Dealership Inventory Management System** has been a rewarding experience that combined learning with practical implementation. It allowed me to apply theoretical concepts in a real-world project while gaining hands-on experience with Django, Test-Driven Development, and professional software engineering practices.

This project not only fulfills the assessment requirements but also represents an important milestone in my journey as a software developer. The knowledge and experience gained throughout its development will serve as a strong foundation for building more complex, scalable, and production-ready applications in the future.

# 👨‍💻 Author

This project was developed as part of a **Test-Driven Development (TDD) assessment** to demonstrate practical skills in Python, Django, software engineering principles, and professional project organization.

---

# 👤 Developer Information

| Field | Details |
|--------|---------|
| **Name** | *Nishit Shingala* |
| **Role** | MCA Student & Python/Django Developer |
| **Project** | Car Dealership Inventory Management System |
| **Technology Stack** | Python, Django, SQLite3, Bootstrap 5 |
| **Development Approach** | Test-Driven Development (TDD) |
| **Project Type** | Academic Assessment Project |

> Replace **Your Name** with your actual name before submitting the project.

---

# 💼 About Me

I am passionate about building clean, scalable, and user-friendly software applications while continuously improving my skills in backend development and software engineering.

This project provided an opportunity to apply theoretical concepts in a practical environment by implementing a modular Django application, following Test-Driven Development practices, and producing professional documentation.

My areas of interest include:

- 🐍 Python Development
- 🌐 Django Web Development
- 📊 Data Science & Machine Learning
- 🗄️ Database Design
- 🧪 Test-Driven Development (TDD)
- ☁️ Cloud Technologies
- 🚀 Software Engineering Best Practices

---

# 🛠️ Technical Skills

### Programming Languages

- Python
- SQL
- HTML
- CSS
- JavaScript (Basics)

---

### Frameworks & Libraries

- Django
- Bootstrap 5

---

### Database

- SQLite3

---

### Development Tools

- Git
- GitHub
- Visual Studio Code
- Django Test Framework

---

# 📚 Learning Goals

Through projects like this, I aim to strengthen my knowledge in:

- Backend Development
- Software Architecture
- REST API Development
- Database Optimization
- Cloud Deployment
- Automated Testing
- Clean Code Practices
- Scalable Application Design

---

# 🙏 Acknowledgements

I would like to thank:

- The project assessors for providing this practical learning opportunity.
- The Django community for its excellent documentation and ecosystem.
- The open-source community for the tools and resources that supported this project's development.
- Everyone who contributes educational content that helps developers learn and grow.

---

# ⭐ Thank You

Thank you for taking the time to review this project.

I hope this repository demonstrates not only the successful implementation of the required functionality but also my commitment to writing clean, maintainable, and well-documented software while following professional software engineering practices.

---

# 🖼️ Author

<p align="center">
    <img src="screenshots/author/profile.png"
         alt="Author"
         width="220">
</p>

<p align="center">
<b>Developed with ❤️ using Python, Django, and Test-Driven Development.</b>
</p>