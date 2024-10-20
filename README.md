# Client-Project Management API

This is a **Client-Project Management API** built with Django and Django REST Framework (DRF). The API allows you to manage clients, projects, and users, including creating projects for clients and assigning users to these projects.

## Features

- **Create and Manage Clients**: Add clients and update or delete client information.
- **Create Projects for Clients**: Assign existing users to a project under a client.
- **User and Project Association**: Associate users to projects and retrieve projects based on assigned users.
- **Authentication**: Secured endpoints with JWT Authentication.
- **API Documentation**: Easily accessible via Postman.

## Technologies Used

- **Backend Framework**: Django 4.x, Django REST Framework
- **Database**: MySQL
- **Tools**: XAMPP (for local MySQL setup)
- **API Testing**: Postman

## Installation Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/arbaz5656/NimapMtask.git
   cd NimapMtask
   Create and Activate a Virtual Environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Database Setup:

Set up MySQL/PostgreSQL, and create the required database.
Update DATABASES settings in settings.py with your database configuration.
Migrate Database:

bash
Copy code
python manage.py migrate
Create Superuser:

bash
Copy code
python manage.py createsuperuser
Run the Development Server:

bash
Copy code
python manage.py runserver
