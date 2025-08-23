from flask import redirect, render_template, session,url_for, Blueprint
#DBと接続するために使うドライバー
import pymysql
from models.channels import Channel

#Blueprintオブジェクト作成
home = Blueprint('home', __name__, template_folder = 'templates', static_folder = 'static')


#ホーム画面(地方選択画面)
@home.route('/home', methods=['GET'])
def home_view():
  user_id = session.get('user_id')
  if user_id is None:
      return redirect(url_for('login_logout.login_view'))
  else:
     areas = Channel.areas_get_all()
     #reverseはリストの要素の順序を逆にする
     #areas.reverse()
  return render_template('channels/home.html', areas=areas, page='home')