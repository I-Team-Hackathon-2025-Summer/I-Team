from flask import request, redirect, render_template, session, flash,url_for, Blueprint
#DBと接続するために使うドライバー
import pymysql
from models.channels import Channel

#Blueprintオブジェクト作成
channels = Blueprint('channels', __name__, template_folder = 'templates', static_folder = 'static')


#チャンネル画面(都道府県選択画面)
@channels.route('/home/<area_id>/channels', methods=['GET'])
def channels_view(area_id):
  user_id = session.get('user_id')
  if user_id is None:
      return redirect(url_for('login_logout.login_view'))
  else:
     #エリア名表示
     areas = Channel.find_by_area_name(area_id)
     #チャンネル名表示
     channels = Channel.channels_get_all(area_id)
  return render_template('channels/channels.html', channels=channels, areas=areas, page='ch')