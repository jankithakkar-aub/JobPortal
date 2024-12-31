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


