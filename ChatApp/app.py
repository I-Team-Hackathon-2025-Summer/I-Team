from flask import Flask, render_template, request, flash, redirect, url_for, session
import re
import uuid
import hashlib

from models import User

EMAIL_PATTERN = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
SESSION_DAYS = 30

app = Flask(__name__)

@app.route('/signup', methods=['GET'])
def sign_view():
    return render_template('auth/signup.html')

@app.route('/signup', methods=['POST'])
def signup_process():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    passwordConfirmation = request.form.get('password-confirmation')

    if name == '' or email == '' or password == '' or passwordConfirmation == '':
        flash('空のフォームがあります')
    elif password != passwordConfirmation:
        flash('二つのパスワードの値が違います')
    elif re.match(EMAIL_PATTERN, email) is None:
        flash('正しいメールアドレスの形式ではありません')
    else:
        uid = uuid.uuid4()
        password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        registered_user = User.find_by_email(email)

        if registered_user != None:
            flash('既に登録されています')
        else:
            User.create(uid, name, email, password)
            UserId = str(uid)
            session['uid'] = UserId
            return redirect(url_for('home_view'))
    return redirect(url_for('signup_process'))

        

