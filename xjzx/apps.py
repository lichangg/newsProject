from flask import Flask
from admin_views import admin_blueprint
from news_views import news_blueprint
from user_views import user_blueprint

def create_app(config):
    app=Flask(__name__)
    app.config.from_object(config)

    app.register_blueprint(admin_blueprint)
    app.register_blueprint(news_blueprint)
    app.register_blueprint(user_blueprint)

    return app