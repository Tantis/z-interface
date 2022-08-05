import os
from flask_migrate import Migrate, MigrateCommand
from interface import app, db
from flask_script import Shell, Manager
from orm.model import User

# app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
