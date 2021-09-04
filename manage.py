import os
import logging

from flask_script import Manager, Server, prompt_bool, Shell
from flask_migrate import MigrateCommand
from logging.handlers import RotatingFileHandler
from sqlalchemy.exc import SQLAlchemyError

try:
    from server import create_flask_app
    from api.models import db, SampleModel
except ImportError:
    from .server import create_flask_app
    from .api.models import db, SampleModel

environment = os.getenv("FLASK_CONFIG")
app = create_flask_app(environment)

app.secret_key = os.getenv("APP_SECRET")

port = int(os.environ.get('PORT', 5000))
server = Server(host="0.0.0.0", port=port)


# initialize flask script
manager = Manager(app)

# enable migration commands
manager.add_command("runserver", server)
manager.add_command("db", MigrateCommand)


@manager.command
def clear_database(prompt=True):
    if environment == "production":
        print("\n\n\tNot happening! Aborting...\n\n Aborted\n\n")
        return

    if environment in ["testing", "development"]:
        if (prompt_bool("\n\nAre you sure you want wipe all your previous data?")):
            try:
                # drops all the tables
                db.drop_all()
                db.session.commit()

                # creates all the tables
                db.create_all()
            except SQLAlchemyError as error:
                db.session.rollback()
                print("\n\n\tCommand could not execute due to the error below! Aborting...\n\n Aborted\n\n" + str(
                    error) + "\n\n")
                return
    else:
        print("\n\n\tAborting... Invalid environment '{}'.\n\n"
              .format(environment))


@manager.command
def seed_sample_function(prompt=True):
    if environment == "production":
        print("\n\n\tNot happening! Aborting...\n\n Aborted\n\n")
        return

    if environment in ["testing", "development"]:
        try:
            # seed default roles
            sample_item = SampleModel()
            sample_item.save()

            message = "Error seeding to the database"
        except SQLAlchemyError as error:
            db.session.rollback()
            message = "\n\n\tThe error below occured when trying to seed the database\n\n\n" + str(error) + "\n\n"

        print(message)
    else:
        print("\n\n\tAborting... Invalid environment '{}'.\n\n"
              .format(environment))


# initialize the log handler
handler = RotatingFileHandler('errors.log', maxBytes=10000000, backupCount=5)
formatter = logging.Formatter("%(asctime)s | %(pathname)s:%(lineno)d | %(funcName)s | %(levelname)s | %(message)s ")
# set the log handler level
handler.setLevel(logging.INFO)
# set the app logger level
app.logger.setLevel(logging.INFO)
werkzeug_handler = logging.getLogger('werkzeug')
handler.setFormatter(formatter)
app.logger.addHandler(handler)
app.logger.addHandler(werkzeug_handler)

manager.run()
