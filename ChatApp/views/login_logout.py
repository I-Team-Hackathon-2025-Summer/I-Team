#Blueprintはアプリケーションを複数のモジュールに分割することを可能にする
from flask import request, redirect, render_template, session, flash, url_for, Blueprint
import hashlib
#MySQLの一般的な機能
import pymysql
from models.user import User

#Blueprintオブジェクト作成
login_logout = Blueprint('login_logout', __name__, template_folder = 'templates', static_folder = 'static')

#ログイン画面
@login_logout.route('/login', methods=['GET'])
def login_view():
    return render_template('auth/login.html')

#ログイン処理
@login_logout.route('/login', methods=['POST'])
def login_process():
    email = request.form.get('email')
    password = request.form.get('password')

    if email =='' or password == '':
        flash('空のフォームがあるようです')
    else:
        user = User.find_by_email(email)
        if user is None:
            flash('このユーザーは存在しません')
        else:
            hashPassword = hashlib.sha256(password.encode('utf-8')).hexdigest()
            print(hashPassword)
            if hashPassword != user["password"]:
                flash('パスワードが間違っています！')
            else:
                #ログイン時sessionに値を保存
                session['user_id'] = user["user_id"]
                #ユーザー名表示のために必要
                session['user_name'] = user["user_name"]
                return redirect(url_for('home.home_view'))
    return redirect(url_for('login_logout.login_view'))    

#ログアウト処理
@login_logout.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login_logout.login_view'))