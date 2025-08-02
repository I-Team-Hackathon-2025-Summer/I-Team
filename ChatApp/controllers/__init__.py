#__init__.pyは、ディレクトリをPythonのパッケージとして認識させるためのファイル
#パッケージとは、モジュールをまとめて整理するためのディレクトリのこと
#このWebアプリ自体の初期化処理を書いていく
from flask import Flask
import controllers.home, controllers.login_logout

#Flaskをインスタンス化
app = Flask(__name__)

#if __name__ == '__main__':は、Pythonスクリプトが直接実行されたときに、そのブロック内のコードを実行するための条件文
#スクリプトは、特定のタスクを自動化するために書かれた一連の命令やコードのこと
#直接実行とは、スクリプトやプログラムをコマンドラインやターミナルから直接呼び出して実行することを指す
#他のモジュールからインポートされると、直接実行とは見なされない
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)