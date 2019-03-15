# -*- encoding: utf-8 -*-
from flask import Blueprint,session,\
    render_template,redirect,url_for,\
    request,flash,jsonify
# generate_password_hash加密作用,check_password_hash解密作用
from werkzeug.security import generate_password_hash,\
    check_password_hash
import apps
# 导入databases文件中的Admin类
from databases import Admin,Category

# 实例化蓝图类，参数（name，固定写法（__name__代表当前页面），模板文件夹的路径）
admin_blue = Blueprint('admin_blue',import_name=__name__,template_folder='../../templates')

@admin_blue.route('/')
def index():
    user_id = session.get('a_user_id')
    if user_id:
        return render_template('/admin/index.html')
    else:
        return redirect(url_for('admin_blue.login'))


@admin_blue.route('/login',methods=['GET','POST'])
def login():
    # 判断请求是否是post请求
    if request.method == 'POST':
        # 从form表单中获取登录信息，并进行保存
        user = request.form.get('username')
        pwd = request.form.get('password')
        # 判断获取到的信息是否有空值
        if not all([user,pwd]):
            flash('信息不全')
        else:
            # 过滤符合Admin类中name字段==user的值，截取一条数据
            a = Admin.query.filter(Admin.name==user).first()
            # 判断a为空（没有截取到信息，说明库中没有该用户）
            if not a:
                flash('用户名不存在')
            else:
                # 解码并判断数据库的密码与登录的密码是否相等
                if check_password_hash(a.pass_hash,pwd):
                    # 登录时的id是否等于截取到的id
                    session['a_user_id'] = a.id
                    return redirect(url_for('admin_blue.index'))
                else:
                    flash('密码错误')
    return render_template('/admin/login.html')


@admin_blue.route('/add')
def add():
    pwd = generate_password_hash('1234')
    a = Admin(name='xiao',pass_hash = pwd)
    apps.db.session.add(a)
    return 'ok'


@admin_blue.route('/newscate',methods=['GET','POST'])
def news_cate():
    msg = {}
    if  request.method == 'POST':
        name = request.form.get('name')
        if name:
            c = Category(name=name)
            apps.db.session.add(c)
            msg['code'] = '200'
            msg['message'] = '添加成功'
        else:
            msg['code'] = '500'
            msg['message'] = '不能为空'
        return jsonify(msg)
    # 从category类中取数据，因为是all所以自动识别了可以直接使用，不用封装在字典中
    cate = Category.query.all()
    return render_template('admin/news_type.html',category=cate)





