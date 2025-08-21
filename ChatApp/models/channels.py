from flask import abort
import pymysql
from models.DB import DB

#DBプールの初期化
db_pool = DB.init_db_pool()

#チャンネルクラス
class Channel:
  @classmethod
  def areas_get_all(cls):
      conn = db_pool.get_conn()
      try:
         with conn.cursor() as cur:
              sql = "SELECT * FROM areas;"
              cur.execute(sql)
              areas = cur.fetchall()
              return areas
      except pymysql.Error as e:
          print(f'エラーが発生しています：{e}')
          abort(500)
      finally:
          db_pool.release(conn)

  @classmethod
  def channels_get_all(cls, area_id):
      conn = db_pool.get_conn()
      try:
          with conn.cursor() as cur:
              sql = "SELECT * FROM open_channels WHERE area_id=%s;"
              cur.execute(sql, (area_id,))
              channels = cur.fetchall()
              return channels
      except pymysql.Error as e:
          print(f'エラーが発生しています：{e}')
          abort(500)
      finally:
          db_pool.release(conn)

  @classmethod
  def find_by_area_name(cls, area_id):
      conn = db_pool.get_conn()
      try:
          with conn.cursor() as cur:
              sql = "SELECT * FROM areas WHERE area_id=%s;"
              cur.execute(sql,(area_id,))
              areas = cur.fetchone()
          return areas
      except pymysql.Error as e:
          print(f'エラーが発生しています。：{e}')
          abort(500)
      finally:
          db_pool.release(conn)

  




          


