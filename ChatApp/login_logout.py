from flask import Frask, request, redirect, render_template, session, flash,url_for

app = Flask(__name__)

#ログインページ
@app.route('/login', methods=['GET'])
def login_view():
    return render_template('auth/login.html')

#ログイン処理
@app.route('/login', methods=['POST'])
def login_process():
    email = request.form.get('email')
    password = request.form.get('password')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login_view'))