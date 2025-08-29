from flask import Flask, session, redirect, url_for
from views.login_logout import login_logout
from views.channels import channels
from views.signup import signup
from views.home import home
from views.chat import chat

import uuid
import os

#Flaskクラスのインスタンスを作成し、appに代入
app = Flask(__name__)

#セッションデータを暗号化(secret_key)して、安全に管理するための設定
app.secret_key = os.getenv('SECRET_KEY', uuid.uuid4().hex)

#Blueprintをアプリケーションに登録
app.register_blueprint(login_logout)
app.register_blueprint(channels)
app.register_blueprint(signup)
app.register_blueprint(home)
app.register_blueprint(chat)

#ルートページのリダイレクト処理
#セッションがない場合、ログイン画面に、ある場合はホーム画面(地方選択)に遷移する
@app.route('/', methods=['GET'])
def index():
    user_id = session.get('user_id')
    if user_id is None:
        return redirect(url_for('login_logout.login_view'))
    return redirect(url_for('home.home_view'))

#このファイルが、コマンドラインからスクリプトとして実行された場合のみ、処理を実行する
#host="0.0.0.0"は、誰でもアクセス可能という意味
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True) 


