from controllers import app
from flask import request, redirect, render_template, session, flash,url_for

#基本URL
@app.route('/', methods=['GET'])
def index():
    user_id = session.get('user_id')
    if user_id is None:
      return redirect(url_for('login.view'))
    return redirect(url_for('home.view'))

#ホーム画面(地方選択画面)
@app.route('/home', method=['GET'])
def home_view():
  return render_template('home.html')