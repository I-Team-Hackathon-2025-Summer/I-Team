from flask import abort
import pymysql
from models.DB import DB


# 初期起動時にコネクションプールを作成し接続を確立
db_pool = DB.init_db_pool()

# ユーザークラス
class Chat:
   @classmethod
   #clsはPythonのクラスメソッドにおいて、クラス自体を指す特別な引数
   #clsの役割①：クラスを使いたい時インスタス化をしなくていい(new User的なのが要らない)
   #役割②：使い回しができる。同クラス内の他関数にclsを使えば、clsを介してそのクラスのクラス変数やクラスメソッドにアクセスできる
   def create(cls, message_id, user_id, message, created_at):
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
               sql = "INSERT INTO open_messages (message_id, user_id, message, created_at) VALUES (%s, %s, %s, %s);"
               # SQLを実行し、パラメータ（uid, name, email, password）を埋め込む
               #executeはSQLクエリを実行するために使う
               cur.execute(sql, (message_id, user_id, message, created_at,))
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