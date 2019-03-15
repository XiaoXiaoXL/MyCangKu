# -*- encoding: utf-8 -*-


class Config(object):
    """工程配置信息"""
    DEBUT = True
    """SQLAlchemy 配置"""
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:070806xl@127.0.0.1:3306/project'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True # 数据库内容发送改变之后,自动提交
    SQLACHEMY_ECHO = True
    SECRET_KEY = '1111'


class ProductionConfig(object):
    """工程配置信息"""
    DEBUT = False
    """SQLAlchemy 配置"""
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:070806xl@127.0.0.1:3306/project'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True # 数据库内容发送改变之后,自动提交
    SQLACHEMY_ECHO = True
    SECRET_KEY = '1111'

config_dict = {
    # 根据key找值，值运行上面的类
    'config': Config,
    'product': ProductionConfig
}