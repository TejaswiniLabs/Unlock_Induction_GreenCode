# FoodShare — Backend Documentation

## 1. Overview

The FoodShare backend is developed using **Python and Django**.

It manages:

* User accounts
* Authentication
* User roles
* Food donations
* Donation claiming
* Database operations
* Request handling
* Template rendering

The backend is divided into two main Django applications:

* `accounts`
* `donations`

---

# 2. Backend Structure

```text
foodshare/
│
├── manage.py
│
├── foodshare/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── accounts/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── donations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── templates/
│   └── ...
│
└── static/
    ├── css/
    └── js/
```

---

# 3. Django Project

## `foodshare/`

This is the main Django project configuration directory.

### `settings.py`

Contains project configuration such as:

* Installed applications
* Database configuration
* Templates
* Static files
* Middleware
* Authentication configuration

### `urls.py`

Acts as the main URL configuration for the project.

It connects the project's URLs with the URLs of the Django applications.

Conceptually:

```text
foodshare/urls.py
       │
       ├── accounts/urls.py
       │
       └── donations/urls.py
```

---

# 4. `accounts` Application

The `accounts` application manages user-related functionality.

```text
accounts/
├── models.py
├── views.py
├── urls.py
└── ...
```

## Responsibilities

The application handles:

* User registration
* User login
* User logout
* User roles
* User-related information
* Authentication-related functionality

---

# 5. User Roles

FoodShare is designed around three roles:

```text
Donor
Volunteer
Admin
```

### Donor

A donor can:

* Add food donations
* View their donations
* Track their posted donations

### Volunteer

A volunteer can:

* View available donations
* Claim donations
* View claimed donations

### Admin

The administrator is responsible for managing and monitoring the platform.

---

# 6. `accounts/models.py`

The account model defines how user information is stored in the database.

The model can contain information required for authentication and role management.

A role field can distinguish between:

```text
DONOR
VOLUNTEER
ADMIN
```

The exact fields depend on the implementation in the current `models.py`.

---

# 7. `accounts/views.py`

The views handle account-related requests.

Typical operations include:

```text
Registration
    ↓
Validate user information
    ↓
Create account
    ↓
Login
    ↓
Identify user role
    ↓
Redirect to appropriate dashboard
```

---

# 8. `accounts/urls.py`

The account URL configuration maps account-related URLs to their corresponding views.

Typical routes include:

```text
/register/
/login/
/logout/
```

The exact routes depend on the current implementation.

---

# 9. `donations` Application

The `donations` application manages the food donation functionality.

```text
donations/
├── models.py
├── views.py
├── urls.py
└── ...
```

## Responsibilities

The application handles:

* Creating donations
* Displaying donations
* Managing donation records
* Displaying available donations
* Claiming donations
* Tracking claimed donations

---

# 10. Food Donation Model

## `donations/models.py`

The donation model represents a food donation in the database.

A donation is associated with a donor and contains the information required to describe the available food.

Possible information includes:

* Donor
* Food name
* Description
* Quantity
* Location
* Expiry/consume-before information
* Date/time
* Status

The exact fields should match the implemented model.

---

# 11. Donation Status

The donation system can use statuses to identify the current state of a donation.

For example:

```text
Available
    ↓
Claimed
    ↓
Completed
```

The exact status values should match the choices defined in `donations/models.py`.

---

# 12. Donation Workflow

### Step 1 — Donor Adds Food

```text
Donor
 ↓
add_donation.html
 ↓
POST Request
 ↓
donations/views.py
 ↓
Donation Model
 ↓
Database
```

---

### Step 2 — Donation Becomes Available

The newly created donation can be displayed on the volunteer's available donations page.

```text
Database
   ↓
Query available donations
   ↓
available.html
```

---

### Step 3 — Volunteer Claims Donation

```text
Volunteer
   ↓
available.html
   ↓
Claim
   ↓
donations/views.py
   ↓
Update Donation
   ↓
Database
```

The donation is then associated with the volunteer and is no longer treated as an unclaimed donation.

---

### Step 4 — Volunteer Views Claimed Donation

The volunteer can view their claimed donations through:

```text
volunteer/claimed.html
```

---

# 13. `donations/views.py`

The donation views handle operations such as:

* Displaying the donation form
* Creating donations
* Displaying donor donations
* Displaying available donations
* Claiming donations
* Displaying claimed donations

The view receives the request, performs the required operation, interacts with the model/database, and returns the appropriate response.

---

# 14. `donations/urls.py`

The donation URL configuration connects donation-related URLs to their views.

Conceptually:

```text
donations/
    │
    ├── add/
    ├── my-donations/
    ├── available/
    └── claimed/
```

The actual URL names should follow the routes implemented in the project.

---

# 15. Database

FoodShare uses **SQLite** during development.

```text
SQLite
  ↓
db.sqlite3
```

Django ORM is used to interact with the database.

The basic flow is:

```text
Django Model
     ↓
Django ORM
     ↓
SQLite Database
```

---

# 16. Django ORM

Instead of manually writing SQL for every operation, Django ORM allows the application to work with database records using Python models.

For example:

```text
Donation Model
      ↓
Django ORM
      ↓
SQLite Table
```

This makes database operations easier to manage inside the Django application.

---

# 17. Authentication Flow

```text
User
 ↓
Registration
 ↓
Account Created
 ↓
Login
 ↓
Authentication
 ↓
Role Identified
 ↓
Dashboard
```

The user's role determines which functionality they should be able to access.

---

# 18. Authorization

Authentication and authorization are separate concepts.

### Authentication

Determines:

> Who is the user?

### Authorization

Determines:

> What is the user allowed to do?

For FoodShare:

```text
Donor
 ├── Add donation
 └── View own donations

Volunteer
 ├── View available donations
 └── Claim donations

Admin
 └── Administrative functionality
```

Views should verify the user's role before allowing restricted operations.

---

# 19. Templates

Django templates are stored in:

```text
templates/
```

Current structure:

```text
templates/
├── base.html
├── login.html
├── dashboard.html
│
├── donor/
│   ├── add_donation.html
│   └── donations.html
│
└── volunteer/
    ├── available.html
    └── claimed.html
```

The backend sends data from the views to these templates.

---

# 20. Static Files

Static frontend resources are stored in:

```text
static/
├── css/
└── js/
```

These files provide the styling and client-side functionality for the Django templates.

---

# 21. Backend Request Flow

A typical request follows this pattern:

```text
Browser
   ↓
URL
   ↓
urls.py
   ↓
views.py
   ↓
models.py
   ↓
SQLite
   ↓
models.py
   ↓
views.py
   ↓
Template
   ↓
Browser
```

---

# 22. Example: Adding a Donation

```text
1. Donor opens Add Donation page
                ↓
2. Django renders add_donation.html
                ↓
3. Donor submits the form
                ↓
4. Request reaches donation URL
                ↓
5. Donation view processes request
                ↓
6. Data is validated
                ↓
7. Donation model is created
                ↓
8. Data is saved to SQLite
                ↓
9. Donor is redirected
                ↓
10. Donation appears in My Donations
```

---

# 23. Example: Claiming a Donation

```text
1. Volunteer opens Available Donations
                ↓
2. Django retrieves available donations
                ↓
3. Volunteer selects Claim
                ↓
4. Request reaches donation view
                ↓
5. Donation is updated
                ↓
6. Volunteer is associated with donation
                ↓
7. Donation status changes
                ↓
8. Donation appears in Claimed Donations
```

---

# 24. Migrations

Django migrations are used to create and update database tables.

Create migrations:

```bash
python manage.py makemigrations
```

Apply migrations:

```bash
python manage.py migrate
```

---

# 25. Running the Backend

Activate the virtual environment and run:

```bash
python manage.py runserver
```

The development server will normally be available at:

```text
http://127.0.0.1:8000/
```

---

# 26. Testing

The backend should be tested for:

### Accounts

* Registration
* Login
* Logout
* Invalid credentials
* Role assignment
* Unauthorized access

### Donations

* Add donation
* View donations
* View available donations
* Claim donation
* View claimed donations
* Donation status updates

### Authorization

Verify that:

* Donors cannot perform volunteer-only actions.
* Volunteers cannot perform donor-only actions.
* Restricted pages cannot be accessed by unauthorized users.

---

# 27. Future Backend Improvements

Possible future additions include:

* Django REST Framework API
* Location-based donation matching
* Notifications
* Email notifications
* Food expiry alerts
* Donation analytics
* Image upload
* Advanced search and filtering
* Google Maps/location integration
* PostgreSQL for production deployment
