from flask import abort
#DBと接続するために使うドライバー
import pymysql
from models.DB import DB


# 初期起動時にコネクションプールを作成し接続を確立
db_pool = DB.init_db_pool()

# チャンネルクラス(エリア＆チャンネル)
class Channel:
    #エリア表示
    @classmethod
    def areas_get_all(cls):
        conn = db_pool.get_conn()
        try:
            with conn.cursor() as cur:
                sql = "SELECT * FROM areas;"
                cur.execute(sql)
                #fetchallはSQLクエリの結果からすべての行を取得する
                #fetconeでもOK
                areas = cur.fetchall()
                return areas
        except pymysql.Error as e:
            print(f'エラーが発生しています：{e}')
            abort(500)
        finally:
            db_pool.release(conn)

    #チャンネル表示
    @classmethod
    def channels_get_all(cls, area_id):
        conn = db_pool.get_conn()
        try:
            with conn.cursor() as cur:
                sql = "SELECT * FROM open_channels WHERE area_id=%s;"
                cur.execute(sql, (area_id,))
                #fetchallはSQLクエリの結果からすべての行を取得する
                channels = cur.fetchall()
                return channels
        except pymysql.Error as e:
            print(f'エラーが発生しています：{e}')
            abort(500)
        finally:
            db_pool.release(conn)

    #エリアname表示
    @classmethod
    def find_by_area_name(cls, area_id):
        conn = db_pool.get_conn()
        try:
            with conn.cursor() as cur:
                sql = "SELECT * FROM areas WHERE area_id=%s;"
                cur.execute(sql,(area_id,))
                #area_idに対して1行だけ取得できればいいからfetchoneでOK
                areas = cur.fetchone()
                return areas
        except pymysql.Error as e:
            print(f'エラーが発生しています：{e}')
            abort(500)
        finally:
            db_pool.release(conn)
