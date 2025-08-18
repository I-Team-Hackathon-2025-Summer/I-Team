#Blueprintはアプリケーションを複数のモジュールに分割することを可能にする
from flask import request, redirect, render_template, session, flash, url_for, Blueprint
#hashlibモジュールはPythonに組み込まれている標準ライブラリの一部でさまざまなハッシュ関数を提供
#ハッシュ関数は、任意の長さのデータを固定長のハッシュ値に変換するための関数
import hashlib
#DBと接続するために使うドライバー
import pymysql
#uuidモジュールはPythonに組み込まれている標準ライブラリの一部でUUID（Universally Unique Identifier）を生成するための機能を提供
import uuid
#reは正規表現（Regular Expressions）を使用して文字列の検索や操作を行うための機能
import re
from models.user import User

#Blueprintオブジェクト作成
signup = Blueprint('signup', __name__, template_folder = 'templates', static_folder = 'static')

# 定数定義
EMAIL_PATTERN = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"


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
    # passwordConfirmation = request.form.get('password-confirmation')

    if user_name == '' or email =='' or password == '':
        flash('空のフォームがあるようです')
    # elif password != passwordConfirmation:
    #     flash('二つのパスワードの値が違っています')

    #matchは文字列の先頭から特定の正規表現パターンにマッチするかどうかを確認するための便利な関数
    elif re.match(EMAIL_PATTERN, email) is None:
        flash('正しいメールアドレスの形式ではありません')
    else:
        #uuid4は衝突の可能性が非常に低いかつランダムに生成されたUUID（Universally Unique Identifier）を作成
        #一意に識別するための128ビットの値
        user_id = uuid.uuid4()
        #sha256はハッシュアルゴリズム
        #UTF-8エンコーディングでバイト列に変換(エンコード)
        #hexdigestはハッシュ値を16進数の文字列として取得
        password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        registered_user = User.find_by_email(email)

        if registered_user != None:
            flash('既に登録されているようです')
        else:
            User.create(user_id, user_name, email, password)
            #多分uuidをstringとして保存して欲しいから記載
            UserId = str(user_id)
            session['user_id'] = UserId
            return redirect(url_for('home.home_view'))
    return redirect(url_for('signup.signup_process'))
