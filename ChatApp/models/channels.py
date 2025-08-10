from flask import abort
import pymysql
from models.DB import DB


# 初期起動時にコネクションプールを作成し接続を確立
db_pool = DB.init_db_pool()

# チャンネルクラス(エリア＆チャンネル)
class Channel:
   @classmethod
   #エリア表示
   def areas_get_all(cls):
       conn = db_pool.get_conn()
       try:
           with conn.cursor() as cur:
               sql = "SELECT * FROM areas ORDER BY;"
               cur.execute(sql)
               #fetchallはSQLクエリの結果からすべての行を取得する
               areas = cur.fetchall()
               return areas
       except pymysql.Error as e:
           print(f'エラーが発生しています：{e}')
           abort(500)
       finally:
           db_pool.release(conn)