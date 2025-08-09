from flask import request, redirect, render_template, session, flash,url_for, Blueprint
#MySQLの一般的な機能
import pymysql

#Blueprintオブジェクト作成
chat = Blueprint('chat', __name__, template_folder = 'templates', static_folder = 'static')


#チャンネル画面(都道府県選択画面)
@chat.route('/channels/<channel_id>/chat', methods=['GET'])
def chat_view():
  return render_template('chat.html')