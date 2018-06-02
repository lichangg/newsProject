from flask import Blueprint, jsonify
from flask import render_template
from flask import request
from flask import session

from models import UserInfo, NewsCategory, NewsInfo

news_blueprint=Blueprint('news',__name__)

@news_blueprint.route('/')
def index():
    #查询分类，用于显示
    category_list=NewsCategory.query.all()

    #判断用户是否登录
    if 'user_id' in session:
        user=UserInfo.query.get(session['user_id'])
    else:
        user=None

    # 此处注意，理论上我们只需要找点击排前六的新闻就行了，不必担心这里一下子把所有的新闻都查出来再进行切片
    # 赋值号右边是生成了一个最后用limit限制了的sql语句，所以性能很高
    count_list = NewsInfo.query.filter_by(status=2).order_by(NewsInfo.click_count.desc())[0:6]

    return render_template(
        'news/index.html',
        category_list=category_list,
        user=user,
        count_list=count_list
    )

# 用ajax动态加载数据
@news_blueprint.route('/newslist')
def newslist():
    # 查询新闻数据==>[news,news,...]==>json
    # 接收请求的页码值
    page = int(request.args.get('page', '1'))
    # 查询已通过新闻信息
    pagination = NewsInfo.query.filter_by(status=2)
    # 接收分类的编号
    category_id = int(request.args.get('category_id', '0'))
    if category_id:
        pagination = pagination.filter_by(category_id=category_id)
    # 排序，分页
    pagination = pagination. \
        order_by(NewsInfo.update_time.desc()). \
        paginate(page, 4, False)
    # 获取当前页的数据
    news_list = pagination.items
    # pagination.pages
    # 将python语言中的类型转换为json
    news_list2 = []
    for news in news_list:
        news_dict = {
            'id': news.id,
            'pic': news.pic_url,
            'title': news.title,
            'summary': news.summary,
            'user_avatar': news.user.avatar_url,
            'user_nick_name': news.user.nick_name,
            'update_time': news.update_time.strftime('%Y-%m-%d'),
            'user_id': news.user.id,
            'category_id': news.category_id
        }
        news_list2.append(news_dict)

    return jsonify(news_list=news_list2)
