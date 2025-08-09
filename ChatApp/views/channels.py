from flask import request, redirect, render_template, session, flash,url_for, Blueprint
#MySQLの一般的な機能
import pymysql

#Blueprintオブジェクト作成
channels = Blueprint('channels', __name__, template_folder = 'templates', static_folder = 'static')


#チャンネル画面(都道府県選択画面)
@channels.route('/home/<area_id>/channels', methods=['GET'])
def channels_view():
  return render_template('channels.html')