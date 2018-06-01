from flask import Blueprint
from flask import render_template
from flask import session

from models import UserInfo

news_blueprint=Blueprint('news',__name__)

@news_blueprint.route('/')
def index():
    # user_id = session['user_id']
    # user = UserInfo.query.get(user_id)
    return render_template('news/index.html')
