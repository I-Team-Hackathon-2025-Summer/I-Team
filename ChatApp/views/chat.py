from flask import request, redirect, render_template, session, flash,url_for, Blueprint
#MySQLの一般的な機能
import pymysql
from models.chat import Chat

#Blueprintオブジェクト作成
chat = Blueprint('chat', __name__, template_folder = 'templates', static_folder = 'static')


#チャット画面
@chat.route('/channels/<channel_id>/chat', methods=['GET'])
def chat_view(channel_id):
  user_id = session.get('user_id')
  if user_id is None:
    return redirect(url_for('login_logout.login_view'))
  
  return render_template('chat.html')