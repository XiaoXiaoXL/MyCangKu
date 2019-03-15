# -*- encoding: utf-8 -*-
from flask import Blueprint,render_template,request,redirect,url_for,session

index_blue = Blueprint('index_blue',import_name=__name__,template_folder='../../templates')




@index_blue.route('/')
def index():
    return 'ok'









