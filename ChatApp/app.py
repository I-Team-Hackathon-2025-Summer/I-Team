from flask import Flask, render_template, session, redirect, url_for
from views.login_logout import login_logout
from views.signup import signup
from views.home import home

import uuid
import os

app = Flask(__name__)

app.secret_key = os.getenv('SECRET_KEY', uuid.uuid4().hex)

#Blueprint登録
app.register_blueprint(login_logout)
app.register_blueprint(signup)
app.register_blueprint(home)


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
##host="0.0.0.0"は誰でもアクセスできますよって意味。絶対に記載するもの
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)