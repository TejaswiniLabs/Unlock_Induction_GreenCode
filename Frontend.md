# FoodShare — Frontend Documentation

## 1. Overview

The FoodShare frontend is the user interface through which users interact with the food donation platform.

The interface is designed around three main user roles:

* Donor
* Volunteer
* Admin

The frontend uses Django templates together with HTML, CSS, JavaScript, and static files.

---

## 2. Technologies Used

| Technology       | Purpose                       |
| ---------------- | ----------------------------- |
| HTML5            | Page structure                |
| CSS3             | Styling and responsive layout |
| JavaScript       | Client-side interactions      |
| Django Templates | Dynamic page rendering        |
| Static Files     | CSS and JavaScript management |

---

# 3. Frontend Structure

```text
foodshare/
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── dashboard.html
│   │
│   ├── donor/
│   │   ├── add_donation.html
│   │   └── donations.html
│   │
│   └── volunteer/
│       ├── available.html
│       └── claimed.html
│
└── static/
    ├── css/
    └── js/
```

---

# 4. Base Template

### `base.html`

`base.html` acts as the common layout for the application.

It can contain common elements such as:

* Navigation bar
* Logo
* Main content area
* Footer
* CSS and JavaScript imports

Other pages can extend the base template instead of repeating the same HTML structure.

Conceptually:

```text
base.html
    │
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

---

# 5. Authentication Interface

### `login.html`

The login page allows registered users to access their FoodShare account.

The page contains:

* Username/email field
* Password field
* Login button
* Registration/navigation option

After successful login, the user is redirected according to their role.

```text
Login
  ↓
Authentication
  ↓
Check Role
  ↓
Dashboard
```

---

# 6. Dashboard

### `dashboard.html`

The dashboard acts as the main page after login.

The content displayed can depend on the logged-in user's role.

```text
                    Dashboard
                        │
          ┌─────────────┼─────────────┐
          ↓             ↓             ↓
        Donor       Volunteer        Admin
          ↓             ↓             ↓
     Donor UI      Volunteer UI    Admin UI
```

The dashboard provides navigation to the functionality available to the current user.

---

# 7. Donor Pages

## `donor/add_donation.html`

This page allows a donor to create a new food donation.

The donor provides the required food information and submits the donation.

Typical information can include:

* Food name
* Food description
* Quantity
* Food type
* Location
* Expiry/consume-before information
* Other relevant donation details

### Workflow

```text
Donor
  ↓
Add Donation
  ↓
Fill Form
  ↓
Submit
  ↓
Django Backend
  ↓
Donation Saved
```

---

## `donor/donations.html`

This page displays the donations created by the logged-in donor.

The donor can view information such as:

* Food name
* Quantity
* Location
* Donation status
* Date
* Claim information

This page allows the donor to keep track of their posted food.

---

# 8. Volunteer Pages

## `volunteer/available.html`

This page displays food donations that are currently available for volunteers to claim.

A volunteer can view relevant donation information and claim an available donation.

### Workflow

```text
Available Donations
        ↓
Volunteer selects donation
        ↓
View Details
        ↓
Claim Donation
        ↓
Donation assigned
```

---

## `volunteer/claimed.html`

This page displays donations that have already been claimed by the logged-in volunteer.

It allows the volunteer to keep track of their claimed donations and their current status.

---

# 9. Static Files

FoodShare uses Django static files for frontend assets.

```text
static/
├── css/
└── js/
```

## CSS

CSS files are responsible for:

* Page layout
* Colors
* Typography
* Forms
* Buttons
* Cards
* Navigation
* Responsive design

## JavaScript

JavaScript can be used for:

* Form validation
* Interactive components
* Dynamic UI behavior
* Confirmation dialogs
* Search/filter functionality
* Client-side interactions

---

# 10. Frontend–Backend Flow

The frontend communicates with Django through requests.

```text
User
 ↓
HTML Template
 ↓
Form / Action
 ↓
Django URL
 ↓
Django View
 ↓
Database
 ↓
Django View
 ↓
Template
 ↓
Updated UI
```

For example, when a donor adds food:

```text
add_donation.html
       ↓
   Submit Form
       ↓
donations/urls.py
       ↓
donations/views.py
       ↓
donations/models.py
       ↓
     SQLite
       ↓
Response
       ↓
donations.html
```

---

# 11. Role-Based Interface

FoodShare provides different functionality depending on the user's role.

| Role      | Frontend Pages                                    |
| --------- | ------------------------------------------------- |
| Donor     | Dashboard, Add Donation, My Donations             |
| Volunteer | Dashboard, Available Donations, Claimed Donations |
| Admin     | Dashboard / administrative functionality          |

Users should only be able to access pages and actions permitted for their role.

---

# 12. Design Goals

The FoodShare frontend focuses on:

* Simple navigation
* Clean user interface
* Easy donation posting
* Easy donation claiming
* Clear donation status
* Responsive design
* Role-specific dashboards

---

# 13. Future Frontend Improvements

Possible improvements include:

* Responsive mobile-first design
* Donation search and filters
* Location-based donation display
* Food images
* Notification interface
* Interactive maps
* Donation statistics
* Improved accessibility
* Mobile application interface
