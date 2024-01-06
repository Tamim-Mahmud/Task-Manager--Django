# Task Management Web Application with Django

Branch: dev0.0.1

This project is a task management web application developed using Django. The application allows multiple users to create, view, update, and delete tasks. It utilizes Django templates for rendering views, PostgreSQL for the database, and Django ORM for managing database relations. The development practices include the use of virtual environments, environment variables, and Git.

## Features

- User authentication and authorization
- Create, view, update, and delete tasks
- Searching and sorting in database
- Django-rest-framework for REST API
- Mark completed task
- Individual user profile and searching
- Utilizes Django templates for rendering views
- PostgreSQL database for data storag
-  Django ORM for managing database relations
- Follows proper development practices using virtual environments, environment variables, and Git

## Setup


2. **Create a Virtual Environment:**

    ```bash
    python -m venv venv
    ```

2. **Activate the Virtual Environment:**

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables:**

    Create a `.env` file in the project root and configure the following variables:

    ```dotenv
    DEBUG=True
    SECRET_KEY=your_secret_key
    DATABASE_URL=postgresql://your_database_user:your_database_password@localhost:5432/your_database_name
    ```

5. **Run the Development Server:**

    ```bash
    python manage.py runserver
    ```

    The application will be accessible at `http://127.0.0.1:8000/`.

## Usage

1. **ACCESS REST API:**

   Visit `http://127.0.0.1:8000/api/`

  Visit `http://localhost:8000/api/all_task/`
    
  Visit `http://localhost:8000/api/all_task/34/`

    Follow the prompts to create a superuser account.

2. **Access Admin Panel:**

    Visit `http://127.0.0.1:8000/admin/` and log in with admin,admin
