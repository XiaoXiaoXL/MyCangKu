# -*- encoding: utf-8 -*-
# 将所有操作封装到文件（包）导入到该文件下
from flask import Flask
# modules.上上级文件夹，web上级文件夹.index本文件
# index_blue index.py文件中的对象名
from modules.web.index import index_blue
from modules.web.user import user_blue
from modules.admin.admin import admin_blue
# 导入防攻击包（防止别人盗用信息）
from flask_wtf import CsrfProtect
import config
# 导入操作数据库的包
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# app下的config配置文件，（文件名.类名）
app.config.from_object(config.config_dict['config'])
# 注册蓝图首页，新闻展示
app.register_blueprint(index_blue,url_prefix='/')
# 注册蓝图user页面，用户信息相关
app.register_blueprint(user_blue,url_prefix='/user')
# 注册蓝图admin页面，管理员信息
app.register_blueprint(admin_blue,url_prefix='/admin')
# 调用防攻击模块
CsrfProtect(app)
# 实例化操作数据库的包，以后直接使用db(对象)操作
db = SQLAlchemy(app)
