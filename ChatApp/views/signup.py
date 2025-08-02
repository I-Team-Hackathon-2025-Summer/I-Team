#Blueprintはアプリケーションを複数のモジュールに分割することを可能にする
from flask import request, redirect, render_template, session, flash, url_for, Blueprint
import hashlib
#MySQLの一般的な機能
import pymysql
import uuid
import re
import os
from models.user import User

#Blueprintオブジェクト作成
#Blueprintオブジェクト作成
signup = Blueprint('signup', __name__, template_folder = 'templates', static_folder = 'static')

# 定数定義
EMAIL_PATTERN = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

signup.secret_key = os.getenv('SECRET_KEY', uuid.uuid4().hex)


#ログイン画面
@signup.route('/signup', methods=['GET'])
def signup_view():
    return render_template('auth/signup.html')

# サインアップ処理
@signup.route('/signup', methods=['POST'])
def signup_process():
    user_name = request.form.get('user_name')
    email = request.form.get('email')
    password = request.form.get('password')
    passwordConfirmation = request.form.get('password-confirmation')

    if user_name == '' or email =='' or password == '' or passwordConfirmation == '':
        flash('空のフォームがあるようです')
    elif password != passwordConfirmation:
        flash('二つのパスワードの値が違っています')
    elif re.match(EMAIL_PATTERN, email) is None:
        flash('正しいメールアドレスの形式ではありません')
    else:
        user_id = uuid.uuid4()
        password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        registered_user = User.find_by_email(email)

        if registered_user != None:
            flash('既に登録されているようです')
        else:
            User.create(user_id, user_name, email, password)
            UserId = str(user_id)
            session['user_id'] = UserId
            return redirect(url_for('home.home_view'))
    return redirect(url_for('signup_process'))
