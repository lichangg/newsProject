from flask_script import Manager
from apps import create_app
from config import DevelopConfig
from models import db
from flask_migrate import Migrate,MigrateCommand


app=create_app(DevelopConfig())
#csrf保护
from flask_wtf.csrf import CSRFProtect
CSRFProtect(app)
db.init_app(app)


manager=Manager(app)
migrate=Migrate(app,db)
manager.add_command('db',MigrateCommand)


if __name__ == '__main__':
    manager.run()
