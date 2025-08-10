#OS（オペレーティングシステム）との対話を可能にするための標準ライブラリ
#環境変数の操作ができる
import os
import pymysql
#pymysqlpool.poolはPyMySQLを使用する際にDB接続を効率的に管理する為の便利なツール
from pymysqlpool.pool import Pool

class DB:
  #クラスメソッドを定義するためのデコレータ(特別な関数)
  @classmethod
  #clsはPythonのクラスメソッドにおいて、クラス自体を指す特別な引数
  #clsの役割①：クラスを使いたい時インスタス化をしなくていい(new User的なのが要らない)
  #役割②：使い回しができる。同クラス内の他関数にclsを使えば、clsを介してそのクラスのクラス変数やクラスメソッドにアクセスできる
  def init_db_pool(cls):
       pool = Pool(
           # データベースホスト
           host=os.getenv('DB_HOST'),
           # データベースユーザー
           user=os.getenv('DB_USER'),
           # データベースパスワード  
           password=os.getenv('DB_PASSWORD'),
           # データベース名
           database=os.getenv('DB_DATABASE'),
           # 最大コネクション数
           #何をコネクション？
           max_size=5,
           # 文字コード
           charset="utf8mb4",
           # カーソルクラス（辞書型でフェッチ）
           #PyMySQLライブラリで使用されるカーソルの一種。このカーソルを使うと、クエリの結果を辞書形式で取得できる
           #カーソルは、データベースとのやり取りを行うためのオブジェクトで、SQLクエリを実行したり、結果を取得したりするために使用される
           cursorclass=pymysql.cursors.DictCursor
       )
       # コネクションプールの初期化
       pool.init()
       return pool