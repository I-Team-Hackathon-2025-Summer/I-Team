#オペレーションシステムとの対話を可能にする
#環境変数を操作する
import os
#PythonでMySQLを操作する
import pymysql
#pymysqlpool.poolはPyMySQLを使用する際にDB接続を効率的に管理する為の便利なツール
from pymysqlpool.pool import Pool


class DB:
  @classmethod
  def init_db_pool(cls):
      pool = Pool(
          #環境変数からデータベースのホスト名を取得
          host=os.getenv('DB_HOST'),
          #環境変数からデータベースユーザーの値を取得
          user=os.getenv('DB_USER'),
          #環境変数からデータベースパスワードを取得
          password=os.getenv('DB_PASSWORD'),
          #環境変数からデータベースの値を取得
          database=os.getenv('DB_DATABASE'),
          #最大接続数が5
          max_size=5,
          #文字コードを設定
          charset="utf8mb4",
          #クエリ結果をPythonの辞書（Dictionary）のリストとして取得するための設定
          cursorclass=pymysql.cursors.DictCursor
      )
      #コネクションプールの初期化
      pool.init()
      return pool