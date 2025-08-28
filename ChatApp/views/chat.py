from flask import request, redirect, render_template, session, flash,url_for, Blueprint
#DBと接続するために使うドライバー
import pymysql
from models.chat import Chat

#Blueprintオブジェクト作成
chat = Blueprint('chat', __name__, template_folder = 'templates', static_folder = 'static')


#チャット画面
#/<area_id>がないと前のチャンネル画面に戻れない
@chat.route('/<area_id>/channels/<channel_id>/chat', methods=['GET'])
#area_idを引数として渡さないとエラーになる(URLで来たarea_idを受け取る場所が必要なのだと思う)
def chat_view(area_id, channel_id):
  user_id = session.get('user_id')
  if user_id is None:
    return redirect(url_for('login_logout.login_view'))
  else:
    #チャンネル名とチャンネルIDのため
    channels = Chat.find_by_channel(channel_id)
    #メッセージとユーザ名表示
    messages = Chat.messages_get_all(channel_id)
    
    return render_template('chat/chat.html',  channels=channels, messages=messages, user_id=user_id, page='chat')

#メッセージ作成
@chat.route('/<area_id>/channels/<channel_id>/chat', methods=['POST'])
#area_idを引数として渡さないとエラーになる(URLで来たarea_idを受け取る場所が必要なのだと思う)
def create_messages(area_id,channel_id):
  user_id = session.get('user_id')
  if user_id is None:
    return redirect(url_for('login_logout.login_view'))
  
  message = request.form.get('message')
  if message:
      Chat.create(user_id, channel_id, message)
  return redirect(url_for('chat.chat_view', area_id=area_id, channel_id=channel_id))

#メッセージ削除
#urlにarea_idとchannel_idがないとurl_forのリダイレクト先に戻れない(/<area_id>/channels/<channel_id>/chat)
@chat.route('/<area_id>/<channel_id>/chat/delete_message/<message_id>', methods=['POST'])
def delete_messages(area_id, channel_id, message_id):
  user_id = session.get('user_id')
  if user_id is None:
    return redirect(url_for('login_logout.login_view'))

  if message_id:
    Chat.delete_message(message_id)
    return redirect(url_for('chat.chat_view', area_id=area_id, channel_id=channel_id))