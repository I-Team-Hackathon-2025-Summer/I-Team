from flask import request, redirect, render_template, session, flash, url_for, Blueprint
import pymysql
from models.channels import Channel

home = Blueprint('home', __name__, template_folder = 'templates', static_folder = 'static')

#ホーム画面(地方選択)の表示
#templates/channels/homeがホーム画面の場所
@home.route('/home', methods=['GET'])
def home_view():
    user_id = session.get('user_id')
    if user_id is None:
        return redirect(url_for('login_logout.login_view'))
    else:
        areas = Channel.areas_get_all()
        #areas.reverse()
        return render_template('channels/home.html', areas=areas, page='home')




