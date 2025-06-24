<!-- # Late Show API -->

A Flask REST API for managing a late night TV show system with guests, episodes, and appearances.

<!-- ## Features -->

- MVC architecture
- PostgreSQL database
- JWT authentication
- CRUD operations for guests, episodes, and appearances
- Protected routes for authorized users

<!-- ## Setup -->

<!-- ### Prerequisites -->

- Python 3.9+
- PostgreSQL
- pipenv

<!-- ### Installation -->

1. Clone the repository:
   ```bash
   git clone https://github.com/<username>/late-show-api-challenge.git
   cd late-show-api-challenge

2. pipenv install flask flask_sqlalchemy flask_migrate flask-jwt-extended psycopg2-binary
pipenv shell

3. export FLASK_APP=server/app.py
flask db init
flask db migrate -m "initial migration"
flask db upgrade