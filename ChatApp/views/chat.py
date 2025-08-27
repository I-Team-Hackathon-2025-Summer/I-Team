from flask import request, redirect, render_template, session, flash, url_for, Blueprint

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
    else:
        #チャンネル名とチャンネルID
        channels = Chat.find_by_channel(channel_id)
        #メッセージとユーザー名表示
        messages = Chat.messages_get_all(channel_id)
        return render_template('chat/chat.html', channels=channels, messages=messages, user_id=user_id, page='chat')

#メッセージ作成
@chat.route('/channels/<channel_id>/chat', methods=['POST'])
def create_messages(channel_id):
    user_id = session.get('user_id')
    if user_id is None:
        return redirect(url_for('login_logout.login_view'))
    
    message = request.form.get('message')
    if message:
        Chat.create_message(user_id, channel_id, message)
        return redirect(url_for('chat.chat_view', channel_id=channel_id))

#メッセージ削除
@chat.route('/<channel_id>/chat/delete/<message_id>', methods=['POST'])
def delete_messages(channel_id, message_id):
    user_id = session.get('user_id')
    if user_id is None:
        return redirect(url_for('login_logout.login_view'))
    
    if message_id:
        Chat.delete_message(message_id)
        return redirect(url_for('chat.chat_view', channel_id=channel_id))



