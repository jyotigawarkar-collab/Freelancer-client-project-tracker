Freelancer Client & Project Tracker

A Python-based desktop application designed to help freelancers manage their clients, projects, payments, and reports in one place.

Project Overview

The Freelancer Client & Project Tracker is a management system developed using Python, Tkinter, and MySQL. It provides a simple graphical interface for managing client information, tracking projects, monitoring payments, and viewing project summaries.

The system stores data in a MySQL database and allows users to perform CRUD operations such as adding, viewing, updating, and deleting records.

Features

- User Login
- Dashboard with project statistics
- Client Management
  - Add Client
  - View Clients
  - Update Client
  - Delete Client
- Project Management
  - Add Project
  - View Projects
  - Update Project
  - Delete Project
- Payment Tracking
  - Project Budget
  - Amount Paid
  - Remaining Amount
  - Payment Status
- Reports & Summary
  - Total Clients
  - Total Projects
  - Pending Projects
  - In Progress Projects
  - Completed Projects
  - Total Budget
  - Total Amount Paid
  - Remaining Amount
- Logout
- MySQL database integration

Technologies Used

- Python – Main programming language and application logic
- Tkinter – Graphical User Interface
- MySQL – Database management and data storage
- MySQL Connector/Python – Connects Python with MySQL
- Aiven MySQL – Cloud-hosted MySQL database
- Pydroid 3 – Development and testing environment on Android

Database

The project uses MySQL with the following main tables:

Users

Stores login credentials.

Clients

Stores client details such as:

- Client ID
- Client Name
- Email
- Phone
- Company
- Address

Projects

Stores project details such as:

- Project ID
- Client ID
- Project Name
- Category
- Start Date
- Deadline
- Budget
- Amount Paid
- Status
- Description

Project Workflow

Login
   ↓
Dashboard
   ↓
 ┌───────────────┬────────────────┐
 │    Clients    │    Projects    │
 ├───────────────┼────────────────┤
 │   Payments    │    Reports     │
 └───────────────┴────────────────┘
   ↓
Logout
   ↓
Login

CRUD Operations

The system uses standard database operations:

- INSERT – Add new client/project records
- SELECT – View records and generate reports
- UPDATE – Modify existing records
- DELETE – Remove records

Payment Calculation

The remaining payment is calculated automatically:

Remaining Amount = Budget - Amount Paid

Payment status is displayed as:

- Pending – No payment received
- Partially Paid – Some amount has been paid
- Fully Paid – Complete payment received

Advantages

- Simple and user-friendly interface
- Centralized client and project management
- Easy payment tracking
- Automatic project and payment summary
- MySQL database provides organized data storage
- Reduces manual record keeping

Future Scope

The project can be extended with:

- Invoice generation
- Payment history
- Client search and advanced filtering
- Email notifications
- Project deadline reminders
- Export reports to Excel or PDF
- Improved authentication and password security

Author

Developed as a BCA academic project using Python, Tkinter, and MySQL.
