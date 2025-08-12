from flask import request, redirect, render_template, session, flash,url_for, Blueprint
#MySQLの一般的な機能
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
     channels = Channel.channels_get_all()
  return render_template('channels/channels.html', channels=channels)