# -*- encoding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import config


app = Flask(__name__)
app.config.from_object(config.config_dict['config'])
db = SQLAlchemy(app)

# 创建时间和修改时间的字段封装在类里，下面可以直接调用
class Base(object):
  create_time = db.Column(db.DateTime,default=datetime.now())
  update_time = db.Column(db.DateTime,default=datetime.now())


#管理员表继承自Base（继承父类里的时间字段），db.Model创建表必须添加的
class Admin(Base,db.Model):
    # 创建表名
    __tablename__ = 'admin'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20),nullable=Flask)
    pass_hash = db.Column(db.String(200),nullable=Flask)


table_user_new = db.Table('user_collection',
                          db.Column('id',db.Integer,primary_key=True),
                          db.Column('user_id',db.Integer,db.ForeignKey('user.id')),
                          db.Column('news_id',db.Integer,db.ForeignKey('news.id'))
                          )


class User(Base,db.Model):
    __tablename__ = 'user'
    # primary_key = True 自带自增
    id = db.Column(db.Integer, primary_key=True)
    # index = True，创建索引,nick_name昵称
    nick_name = db.Column(db.String(20),index=True)
    password_hash = db.Column(db.String(200), nullable=Flask)
    # mobile手机号码
    mobile = db.Column(db.String(11), nullable=Flask)
    # avatar_url分类路由
    avatar_url = db.Column(db.String(256))
    # last_login最后登录时间
    last_login = db.Column(db.DateTime)
    # signature签名
    signature = db.Column(db.String(512))
    # gender性别
    gender = db.Column(db.String(10),default='Man',nullable=Flask)
    news = db.relationship('News',backref='author',lazy='dynamic')
    # backref='users'反向查找，lazy='dynamic'动态查找
    # 通过db.relationship，连接第三张表secondary=table_user_new（不加引号填类名，加引号填表名）
    # 通过以上操作完成表多对多
    news_collection = db.relationship('News',secondary=table_user_new,
                                      backref='users',lazy='dynamic')

class Category(Base,db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    relate_news = db.relationship('News',backref='relate_category',lazy='dynamic')


class News(Base,db.Model):
    __tablename__ = 'news'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    #source来源
    source = db.Column(db.String(30))
    # index_image_u图片路由
    index_image_u = db.Column(db.String(100))
    # digest摘要
    digest = db.Column(db.String(255))
    # clicks点击数量
    clicks = db.Column(db.Integer)
    #content内容
    content = db.Column(db.Text)
    # db.ForeignKey('user.id')外键
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'),index = True)
    # user_id用户id
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),index = True)
    #status新闻状态，1，审核中，2，通过，3，未通过
    status = db.Column(db.Integer)
    # reason审核失败的原因
    reason = db.Column(db.String(100))


class Comment(Base,db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    news_id = db.Column(db.Integer,db.ForeignKey('news.id'),index = True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),index = True)
    # content内容
    content = db.Column(db.String(255))





if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    app.run()














