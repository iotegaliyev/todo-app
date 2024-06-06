## Todo app backend system

The Todo App Backend System is built using Django Rest Framework (DRF) with PostgreSQL as the primary database. It
provides a robust API for managing todo tasks and user authentication.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/iotegaliyev/todo-app.git
   cd todo-app
   ```
2. Create and Activate Virtual Environment:
   ```sh
   # Create a virtual environment
   python -m venv venv

   # Activate the virtual environment (Windows)
   .\venv\Scripts\activate

   # Activate the virtual environment (Mac/Linux)
   source venv/bin/activate
   ```
3. Install requirements
   ```sh
   pip install -r requirements.txt
   ```

4. Create .env File:
   * Duplicate .env.example and rename it to `.env`.
   * Update the variables in .env as per your environment setup:
   ```sh
   SECRET_KEY=your_secret_key_here
   DEBUG=True  # Set to False in production
   DB_NAME=postgres
   DB_USER=postgres
   DB_PASSWORD=postgres
   DB_HOST=db
   DB_PORT=5432
   ```

5. Launch with Docker Compose:
   ```sh
   docker-compose up -d
   ```

### API documentation

* POST `/api/auth/register/`

  Registers a new user with username, first_name, last_name and password.


* POST `/api/auth/login/`

  Obtains JWT token by providing username and password for authentication.


* POST `/api/auth/token/refresh/`

  Refreshes JWT token to extend authentication validity.


* GET `/api/tasks/`

  Retrieves all tasks.


* POST `/api/tasks/`

  Creates a new task with title, description and status (new, in_progress, completed).


* GET `/api/tasks/<id>/`

  Retrieves a specific task by its id.


* PUT `/api/tasks/<id>/`

  Updates a specific task by its id.


* DELETE `/api/tasks/<id>/`

  Removes a specific task by its id.


* GET `/api/users/<userId>/tasks/`

  Retrieves a list of tasks associated with a specific user.


* PATCH `/api/tasks/<id>/complete/`

  Marks a specific task as completed.


* GET `/api/tasks/status/?status=<status>`

  Filters tasks based on status.


