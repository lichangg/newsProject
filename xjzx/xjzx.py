from flask_script import Manager
from apps import create_app
from config import Development
from models import db
from flask_migrate import Migrate,MigrateCommand


app=create_app(Development())
db.init_app(app)


manager=Manager(app)
migrate=Migrate(app,db)
manager.add_command('db',MigrateCommand)


if __name__ == '__main__':
    manager.run()
