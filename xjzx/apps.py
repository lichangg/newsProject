from flask import Flask
from admin_views import admin_blueprint
from news_views import news_blueprint
from user_views import user_blueprint
# 不是flask里面的Session是flask_session里面的
from flask_session import Session
def create_app(config):
    app=Flask(__name__)
    app.config.from_object(config)

    app.register_blueprint(admin_blueprint)
    app.register_blueprint(news_blueprint)
    app.register_blueprint(user_blueprint)

    import logging
    from logging.handlers import RotatingFileHandler
    # 设置日志的记录等级
    logging.basicConfig(level=logging.DEBUG)  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    # 即100Ｍ的文件空间满了以后自动创建log2,然后log3...(logs目录需要手动创建)
    # 在十个文件满了之后会依次删除第一个日志文件，第二个，第三个...
    file_log_handler = RotatingFileHandler(config.BASE_DIR + "/logs/xjzx.log", maxBytes=1024 * 1024 * 100,
                                           backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)
    # 调用的时候就用current_app.logger_xjzx.error('错误信息')
    app.logger_xjzx = logging
    Session(app)
    return app