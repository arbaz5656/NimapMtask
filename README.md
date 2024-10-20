
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
- **Database**: MySQL/PostgreSQL (based on your project setup)
- **Tools**: XAMPP (for local MySQL setup)
- **API Testing**: Postman

## Installation Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/arbaz5656/NimapMtask.git
   cd your-repo-name
   ```

2. **Create and activate a virtual environment:**
   ```bash
   source ven/bin/activate  # On Windows, use ven\Scripts\activate
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup the database:**
   - Ensure MySQL is installed and running.
   - Configure your database settings in `settings.py`.
   - Apply migrations:
     ```bash
     python manage.py migrate
     ```

5. **Run the server:**
   ```bash
   python manage.py runserver
   ```

6. **Create a superuser for admin access:**
   ```bash
   python manage.py createsuperuser
   ```

7. **Access the API:**
   - Use Postman to interact with the API. Default URL:
     ```
     http://127.0.0.1:8000/
     ```

## API Endpoints

### 1. **Client Endpoints**
- **Create a new client:**
  ```
  POST /clients/
  ```

- **Retrieve a client by ID:**
  ```
  GET /clients/:id/
  ```

- **Update client information:**
  ```
  PATCH /clients/:id/
  ```

- **Delete a client:**
  ```
  DELETE /clients/:id/
  ```

### 2. **Project Endpoints**
- **Create a new project and assign users:**
  ```
  POST /clients/:id/projects/
  ```

- **List all projects assigned to a logged-in user:**
  ```
  GET /projects/
  ```

### 3. **Authentication Endpoints**
- **Obtain JWT Token:**
  ```
  POST /Napp/token/
  ```

- **Refresh JWT Token:**
  ```
  POST /Napp/token/refresh/
  ```

## Example API Request

### Create a new project and assign users:

- **Endpoint:**
  ```
  POST /clients/2/projects/
  ```

- **Request Body:**
  ```json
  {
      "project_name": "Project A",
      "users": [
          {
              "id": 1,
              "name": "Rohit"
          }
      ]
  }
  ```

- **Response:**
  ```json
  {
      "id": 3,
      "project_name": "Project A",
      "client": "Nimap",
      "users": [
          {
              "id": 1,
              "name": "Rohit"
          }
      ],
      "created_at": "2019-12-24T11:03:55.931739+05:30",
      "created_by": "Ganesh"
  }
  ```
![Screenshot (288)](https://github.com/user-attachments/assets/06643baf-f7e4-47c9-953a-ec931e029615)

