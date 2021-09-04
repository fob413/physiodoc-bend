# flask-rest-api-setup
Starter template for building your Flask REST API applications.

# Built With
This App was developed with the following stack:
- Python
- Flask
- Flask-restful
- PostgreSQL

# Requirements
- Python 3+
- Python PIP
- PostgreSQL

# Installation
- Fork this repository.
- Create a `.env` file as shwon in the `.env.sample` file.
- Setup your database.
- In your terminal, `cd` into the project's `dir`.
- Run `pip install -r requirements.txt` to install required modules.
- Run `python manage.py db init` to setup alembic migrations.
- Run `python manage.py db migrate -m='<migration message>'` to create migration files.
- Run `python manage.py db upgrade ` to run the migration files into the database.

# Start the App
- In your terminal, `cd` into the project's `dir`
- Run `python server.py`
