from flask import Flask, render_template
from views.login_logout import login_logout
from views.signup import signup
from views.home import home



app = Flask(__name__)

#Blueprint登録
#Blueprint登録
app.register_blueprint(login_logout)
app.register_blueprint(signup)
app.register_blueprint(home)


@app.route('/', methods=['GET'])
def index():
    return render_template('auth/login.html')

#if __name__ == '__main__':は、Pythonスクリプトが直接実行されたときに、そのブロック内のコードを実行するための条件文
#スクリプトは、特定のタスクを自動化するために書かれた一連の命令やコードのこと
#直接実行とは、スクリプトやプログラムをコマンドラインやターミナルから直接呼び出して実行することを指す
#他のモジュールからインポートされると、直接実行とは見なされない
##host="0.0.0.0"は誰でもアクセスできますよって意味。絶対に記載するもの
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)