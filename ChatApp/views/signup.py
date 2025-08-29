from flask import request, redirect, render_template, session, flash, url_for, Blueprint
import hashlib

import pymysql
import uuid
import re
from models.user import User

#Blueprintオブジェクト作成
signup = Blueprint('signup', __name__, template_folder = 'templates', static_folder = 'static')

#定数定義
EMAIL_PATTERN = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

#サインアップ画面表示
@signup.route('/signup', methods=['GET'])
def signup_view():
    return render_template('auth/signup.html')

#サインアップ処理
@signup.route('/signup', methods=['POST'])
def signup_process():
    #request.form.get()で、POSTのデータを取得
    user_name = request.form.get('user_name')
    email = request.form.get('email')
    password = request.form.get('password')

    if user_name == '' or email == '' or password == '':
        flash('空のフォームがあるようです')
        #reモジュールのmatch関数、文字列の先頭がマッチするかチェック
    elif re.match(EMAIL_PATTERN, email) is None:
        flash('正しいメールアドレスの形式ではありません')
    else:
        #UUIDを生成し、ueser_idに代入
        user_id = uuid.uuid4()
        #hashlibでパスワードをハッシュ化
        password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        registered_user = User.find_by_email(email)

        if registered_user != None:
            flash('既に登録されているようです')
        else:
            #データベースにユーザー情報を登録
            User.create(user_id, user_name, email, password)
            UserId = str(user_id)
            #ユーザー情報をセッションに保存
            session['user_id'] = UserId
            return redirect(url_for('home.home_view'))
    return redirect(url_for('signup.signup_process'))

