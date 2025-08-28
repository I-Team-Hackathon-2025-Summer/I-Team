from flask import Flask, session, redirect, url_for
from views.login_logout import login_logout
from views.signup import signup
from views.home import home
from views.channels import channels
from views.chat import chat

#uuidモジュールはPythonに組み込まれている標準ライブラリの一部でUUID（Universally Unique Identifier）を生成するための機能を提供
import uuid
#OS（オペレーティングシステム）との対話を可能にするための標準ライブラリ
#環境変数の操作ができる
import os

app = Flask(__name__)

#SECRET_KEYはセッション情報(Cookie)を暗号化する際に使用する秘密鍵(文字列)
#Cookieはユーザのログイン情報が記録されたデータのことで、クライアント側(ブラウザや端末)に直接保存されるもの
#Flaskでは必要
#hexは
app.secret_key = os.getenv('SECRET_KEY', uuid.uuid4().hex)

#Blueprint登録
app.register_blueprint(login_logout)
app.register_blueprint(signup)
app.register_blueprint(home)
app.register_blueprint(channels)
app.register_blueprint(chat)


@app.route('/', methods=['GET'])
def index():
    user_id = session.get('user_id')
    if user_id is None:
        return redirect(url_for('login_logout.login_view'))
    return redirect(url_for('home.home_view'))

#if __name__ == '__main__':は、Pythonスクリプトが直接実行されたときに、そのブロック内のコードを実行するための条件文
#スクリプトは、特定のタスクを自動化するために書かれた一連の命令やコードのこと
#直接実行とは、スクリプトやプログラムをコマンドラインやターミナルから直接呼び出して実行することを指す
#他のモジュールからインポートされると、直接実行とは見なされない
#host="0.0.0.0"は誰でもアクセスできますよって意味。絶対に記載するもの
#簡易版のWebサーバとWebアプリケーションサーバを立ち上げるためのコード
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)