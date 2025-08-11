from flask import request, redirect, render_template, session, flash,url_for, Blueprint
#MySQLの一般的な機能
import pymysql

#Blueprintオブジェクト作成
home = Blueprint('home', __name__, template_folder = 'templates', static_folder = 'static')


#ホーム画面(地方選択画面)
@home.route('/home', methods=['GET'])
def home_view():
  return render_template('channels/home.html')