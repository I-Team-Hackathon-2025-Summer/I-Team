from flask import abort
import pymysql
from models.DB import DB


# 初期起動時にコネクションプールを作成し接続を確立
db_pool = DB.init_db_pool()


# ユーザークラス
class User:
   @classmethod
   def create(cls, user_id, user_name, email, password):
       # データベース接続プールからコネクションを取得する
       conn = db_pool.get_conn()
       try:
            # コネクションからカーソル（操作用のオブジェクト）を取得する
            # cursorはデータの接続やクエリ文を実行するためのインターフェイスの役割をしてる
           with conn.cursor() as cur:
               sql = "INSERT INTO users (user_id, user_name, email, password) VALUES (%s, %s, %s, %s);"
               # SQLを実行し、パラメータ（uid, name, email, password）を埋め込む
               cur.execute(sql, (user_id, user_name, email, password,))
               # データベースに変更を反映（保存）する
               conn.commit()
       except pymysql.Error as e:
           print(f'エラーが発生しています：{e}')
           abort(500)
       finally:
           db_pool.release(conn)


   @classmethod
   def find_by_email(cls, email):
       conn = db_pool.get_conn()
       try:
               with conn.cursor() as cur:
                   sql = "SELECT * FROM users WHERE email=%s;"
                   cur.execute(sql, (email,))
                   user = cur.fetchone()
               return user
       except pymysql.Error as e:
           print(f'エラーが発生しています：{e}')
           abort(500)
       finally:
           db_pool.release(conn)
