# 🍲 FoodShare — Don't Waste Food

> **Connecting surplus food with people who need it.**

FoodShare is a web-based food donation and redistribution platform designed to reduce food wastage by connecting **Donors** with **Volunteers/NGOs**.

The platform allows donors to share surplus food instead of wasting it, while volunteers can find and claim available food for collection and distribution.

---

## 🌱 Problem Statement

A significant amount of food is wasted every day, while many people and communities still face food insecurity.

Some common problems are:

* Surplus food is often thrown away.
* Donors may not know where to donate excess food.
* NGOs and volunteers may not know where surplus food is available.
* Food donation activities can be difficult to organize manually.
* There is a need for a simple platform to connect donors and volunteers.

### 💡 Our Solution

FoodShare provides a centralized platform where donors can post surplus food and volunteers can view and claim available donations.

```text
        SURPLUS FOOD
             │
             ▼
          DONOR
             │
             │  Post Food
             ▼
        FOODSHARE
             │
             │  View / Claim
             ▼
      VOLUNTEER / NGO
             │
             │  Collect
             ▼
       PEOPLE IN NEED
```

---

# 🎯 Objectives

* Reduce food wastage.
* Encourage food donation.
* Connect food donors with volunteers and NGOs.
* Make food donation easier and more organized.
* Allow volunteers to find available food.
* Track food donations and claimed food.
* Build a simple and accessible food-sharing platform.

---

# 👥 User Roles

FoodShare is designed around different user roles.

## 👤 Donor

A donor is a person or organization that has surplus food available for donation.

### Donor can:

* Register and log in.
* Access the donor dashboard.
* Add food donations.
* View their posted donations.
* Track the status of their donations.

---

## 🤝 Volunteer

A volunteer helps collect and distribute donated food.

### Volunteer can:

* Register and log in.
* Access the volunteer dashboard.
* View available food donations.
* Claim available donations.
* View their claimed donations.
* Track claimed food.

---

## 🛡️ Admin

The administrator is responsible for managing and monitoring the FoodShare platform.

The admin role can be extended to include:

* User management
* Donation monitoring
* Platform management
* Activity monitoring
* Reports and statistics

---

# 🔄 How FoodShare Works

### 1. Registration

A user creates an account and selects the appropriate role.

### 2. Login

The user logs into FoodShare.

### 3. Donor Posts Food

The donor enters the details of the surplus food and submits the donation.

### 4. Donation Becomes Available

The donation is stored in the database and can be displayed to volunteers.

### 5. Volunteer Views Available Food

The volunteer visits the available donations page and views food that can be claimed.

### 6. Volunteer Claims Food

The volunteer claims an available donation.

### 7. Collection & Distribution

The volunteer collects the food and helps distribute it to people who need it.

```text
Register
   ↓
Login
   ↓
Select Role
   │
   ├───────────────┐
   ↓               ↓
 Donor          Volunteer
   ↓               ↓
Add Food       View Available
   ↓               ↓
Posted Food    Claim Food
   └───────┬───────┘
           ↓
       Food Collection
           ↓
       Distribution
```

---

# ✨ Key Features

## 🔐 Authentication

* User registration
* User login
* User logout
* Role-based dashboard access

## 🍱 Food Donation

* Add food donation
* Store donation details
* View posted donations
* Track donation status

## 🤝 Food Claiming

* View available donations
* Claim available food
* View claimed donations

## 📊 Dashboard

Separate dashboard experience for users based on their role.

## 🗄️ Database

FoodShare uses SQLite during development for storing application data.

---

# 🛠️ Technology Stack

### Frontend

* HTML5
* CSS3
* JavaScript
* Django Templates

### Backend

* Python
* Django

### Database

* SQLite

### Development Tools

* Visual Studio Code
* Git
* GitHub

---

# 📁 Project Structure

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

# 🏗️ Application Structure

FoodShare is divided into two main Django applications.

## `accounts`

Responsible for user-related functionality.

```text
accounts/
├── models.py
├── views.py
├── urls.py
└── ...
```

It handles functionality such as:

* Registration
* Login
* Logout
* User roles
* Account-related operations

---

## `donations`

Responsible for food donation functionality.

```text
donations/
├── models.py
├── views.py
├── urls.py
└── ...
```

It handles:

* Creating donations
* Viewing donations
* Available donations
* Claiming donations
* Claimed donations
* Donation-related operations

---

# 🔗 Application Flow

```text
                  FOODSHARE
                      │
          ┌───────────┴───────────┐
          │                       │
      ACCOUNTS                 DONATIONS
          │                       │
          ↓                       ↓
   Registration/Login       Add Food Donation
          │                       │
          ↓                       ↓
      User Role              Food Database
          │                       │
     ┌────┴────┐                  ↓
     ↓         ↓           Available Food
   Donor    Volunteer             │
     │         │                  ↓
     ↓         └────────────► Claim
     │                            │
     └────────────────────────────┘
```

---

# 🗃️ Database

FoodShare uses **SQLite** as the development database.

Django ORM is used to interact with the database.

```text
Django Models
      ↓
 Django ORM
      ↓
    SQLite
```

Database migrations are managed using Django.

```bash
python manage.py makemigrations
python manage.py migrate
```

---

# ⚙️ Installation & Setup

## 1. Clone the Repository

```bash
git clone <your-github-repository-url>
```

Move into the project directory:

```bash
cd foodshare
```

---

## 2. Create Virtual Environment

```bash
python -m venv DjangoEnv
```

### Windows

```bash
DjangoEnv\Scripts\activate
```

---

## 3. Install Django

```bash
pip install django
```

If the project contains a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

---

## 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 5. Start the Development Server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

---

# 🔒 Security

The Django backend provides security mechanisms such as:

* Password hashing
* Authentication
* CSRF protection
* Session management
* Server-side validation
* Role-based access control

Additional security configuration should be applied before production deployment.

---

# 📚 Documentation

Detailed documentation is available in separate files:

### 🎨 Frontend Documentation

See:

**[FRONTEND.md](FRONTEND.md)**

Includes:

* HTML templates
* CSS
* JavaScript
* Page structure
* Donor interface
* Volunteer interface
* Frontend workflow

### ⚙️ Backend Documentation

See:

**[BACKEND.md](BACKEND.md)**

Includes:

* Django architecture
* `accounts` application
* `donations` application
* Models
* Views
* URLs
* Database
* Authentication
* Donation workflow

---

# 🚧 Project Status

**FoodShare is currently under development.**

### Current development areas

* [x] Project structure
* [x] User authentication structure
* [x] Donor interface
* [x] Volunteer interface
* [x] Donation application
* [x] Django backend
* [x] SQLite database
* [ ] Complete donation workflow
* [ ] Complete claim workflow
* [ ] Complete admin functionality
* [ ] Testing
* [ ] Deployment

---

# 🚀 Future Enhancements

Future versions of FoodShare can include:

* 📍 Location-based food matching
* 🗺️ Map integration
* 🔔 Notifications
* 📧 Email notifications
* 📸 Food image uploads
* 🔎 Advanced search and filtering
* 📊 Donation statistics
* ⏰ Food expiry alerts
* ⭐ Volunteer/NGO ratings
* 📱 Mobile application
* 🤖 Smart donor-volunteer matching

---

# 🌍 Social Impact

FoodShare aims to turn surplus food into an opportunity to help others.

Instead of:

```text
Surplus Food → Waste
```

FoodShare aims for:

```text
Surplus Food
      ↓
    Donor
      ↓
  FoodShare
      ↓
  Volunteer
      ↓
Collection & Distribution
      ↓
 People in Need
```

The goal is simple:

> **Don't Waste Food. Share It.**

---

# 👨‍💻 Team

## FoodShare — Don't Waste Food

**Team Members:**

* Member 1 — Name
* Member 2 — Name
* Member 3 — Name
* Member 4 — Name

---

# 📄 License

This project is currently developed for educational and hackathon purposes.

---

## ❤️ FoodShare

### **Don't Waste Food. Share It.**
