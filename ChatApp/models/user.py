from flask import abort
import pymysql
from models.DB import DB


# 初期起動時にコネクションプールを作成し接続を確立
#プールは限られた数の接続を管理し、再利用する為の仕組み
#DB接続プール: DB接続をあらかじめ確保し、アプリケーションが必要なときに接続を取得し、使用後にプールに戻す仕組み
db_pool = DB.init_db_pool()


# ユーザークラス
class User:
   @classmethod
   #clsはPythonのクラスメソッドにおいて、クラス自体を指す特別な引数
   #clsの役割①：クラスを使いたい時インスタス化をしなくていい(new User的なのが要らない)
   #役割②：使い回しができる。同クラス内の他関数にclsを使えば、clsを介してそのクラスのクラス変数やクラスメソッドにアクセスできる
   def create(cls, user_id, user_name, email, password):
       #DB接続プールからコネクションを取得する
       conn = db_pool.get_conn()
       #try-except文はPythonにおけるエラーハンドリングのための構文
       #try: エラーが発生する可能性のあるコードを含むブロック
       try:
            # コネクションからカーソル（操作用のオブジェクト）を取得する
            # cursorはデータの接続やクエリ文を実行するためのインターフェイスの役割をしてる
            #withはcursorで取得したカーソルが自動的に閉じられる。withを抜けるとカーソルが自動的に解放されるため、close()を呼び出す必要がない
            #closeはリソースを完全に閉じて使用できなくする。cursorを閉じることで、他のプロセスがそのcursorにアクセスできるようにする
            #with内でエラーが発生した場合でも,カーソルは自動的に解放される
           with conn.cursor() as cur:
               sql = "INSERT INTO users (user_id, user_name, email, password) VALUES (%s, %s, %s, %s);"
               # SQLを実行し、パラメータ（uid, name, email, password）を埋め込む
               #executeはSQLクエリを実行するために使う
               cur.execute(sql, (user_id, user_name, email, password,))
               # データベースに変更を反映（保存）する
               conn.commit()
        #except: 特定のエラーを捕捉し、そのエラーに対する処理を記述
       except pymysql.Error as e:
           #abortは特定のHTTPステータスコードを返してリクエストを中断することができる
           print(f'エラーが発生しています：{e}')
           abort(500)
        #finally: エラーの有無に関わらず必ず実行されるコードを記述。リソースの解放などに使われる
       finally:
           #releaseは使用済みのリソースをプールに戻す事。DB接続をプールに戻すことで、他のリクエストがその接続を再利用できるようになる
           #リソース（データベース接続やスレッドなど）
           db_pool.release(conn)


   @classmethod
   def find_by_email(cls, email):
       conn = db_pool.get_conn()
       try:
            with conn.cursor() as cur:
                sql = "SELECT * FROM users WHERE email=%s;"
                cur.execute(sql, (email,))
                #fetchoneは実行したSQLクエリの結果から1行だけを取得するために使う
                user = cur.fetchone()
            return user
       except pymysql.Error as e:
           print(f'エラーが発生しています：{e}')
           abort(500)
       finally:
           db_pool.release(conn)
