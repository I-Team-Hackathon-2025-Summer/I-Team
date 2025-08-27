from flask import abort

import pymysql
from models.DB import DB

#コネクションプールを作成し接続
db_pool = DB.init_db_pool()

#チャットクラス
class Chat:
  #チャンネル名を表示
  @classmethod
  def find_by_channel(cls, channel_id):
      conn = db_pool.get_conn()
      try:
          with conn.cursor() as cur:
              sql = "SELECT * FROM open_channels WHERE channel_id=%s;"
              cur.execute(sql,(channel_id,))
              channels = cur.fetchone()
              return channels
      except pymysql.Error as e:
          print(f'エラーが発生しています：{e}')
          abort(500)
      finally:
          db_pool.release(conn)


  #メッセージ表示
  @classmethod
  def messages_get_all(cls, channel_id):
      conn = db_pool.get_conn()
      try:
          with conn.cursor() as cur:
              sql = """
                SELECT *
                FROM open_messages AS m
                INNER JOIN users AS u ON m.user_id = u.user_id
                WHERE channel_id=%s;
                """
              cur.execute(sql, (channel_id,))
              messages = cur.fetchall()
              return messages
      except pymysql.Error as e:
          print(f'エラーが発生しています：{e}')
          abort(500)
      finally:
          db_pool.release(conn)


  #メッセージ作成
  @classmethod
  def create_message(cls, user_id, channel_id, message):
      conn = db_pool.get_conn()
      try:
          with conn.cursor() as cur:
              sql = "INSERT INTO open_messages (user_id, channel_id, message) VALUES (%s, %s, %s);"
              cur.execute(sql, (user_id, channel_id, message,))
              conn.commit()
      except pymysql.Error as e:
          print(f'エラーが発生しています：{e}')
          abort(500)
      finally:
          db_pool.release(conn)


  #メッセージ削除
  @classmethod
  def delete_message(cls, message_id):
      conn = db_pool.get_conn()
      try:
          with conn.cursor() as cur:
              sql = "DELETE FROM open_messages WHERE message_id=%s;"
              cur.execute(sql, (message_id,))
              conn.commit()
      except pymysql.Error as e:
          print(f'エラーが発生しています：{e}')
          abort(500)
      finally:
          db_pool.release(conn)   
          
