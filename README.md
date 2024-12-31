# Job Portal Application

## Overview

This Job Portal application allows users to register, register their company, and post job listings. It provides features for creating, editing, and deleting job posts, with permissions ensuring users can only manage job posts associated with their own company. The application is built using Django and includes a simple SQLite database setup.

## Features

- **User Authentication**: Users can sign up, log in, logout and manage their accounts.
- **Company Registration**: After signing up, users can register their company details (e.g., Company Name, Address, Contact Number).
- **Job Post Management**: Users can create, update, and delete job posts for their registered company. Each job post contains:
  - Job Title
  - Job Description
  - Location
  - Salary Range
  - Tags
- **Permissions**: 
  - Only authenticated users can access job posting features.
  - Users can only manage job posts for their own company.

## Setup Instructions

Follow the steps below to set up and run the Job Portal application locally:

### 1. Clone the Repository

````bash
git clone https://github.com/jankithakkar-aub/JobPortal.git
cd JobPortal
````

### 2. Install the Dependencies

Create a virtual environment and install the required dependencies:

````bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
````

### 3. Setup Database

Run migrations to set up the database schema:

````bash
python manage.py migrate
````

### 4. Create Superuser (Optional)

If you want to access the Django admin, you can create a superuser:

````bash
python manage.py createsuperuser
````

### 5. Run the Development Server

Start the Django development server:

````bash
python manage.py runserver
````
Now, you can access the application at http://127.0.0.1:8000/.

## Application Structure

The main components of the application are as follows:

1. Users: Django's built-in authentication system handles user registration, login, and management.
2. Company Registration: A model to store details about the user's company.
3. Job Post Management: A model to manage job postings, along with views for creating, editing, deleting, and listing job posts.
4. Templates: HTML templates are used for rendering forms and job postings.

### File And Directory Structure

````bash
JobPortal/
│
├── JobPortal/
│   ├── urls.py
│   ├── views.py
├── jobs/
|   ├── migrations/
│   ├── templates/
|   ├── urls.py
│   ├── views.py
|   ├── models.py
│   ├── admin.py
|   ├── forms.py
├── templates/ 
├── venv/
├── manage.py                 
├── requirements.txt
└── .gitignore
````





