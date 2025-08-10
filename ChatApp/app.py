from flask import Flask, render_template
#from views.login_logout import login_logout
from views.signup import signup
from views.home import home

import uuid
import os

app = Flask(__name__)

app.secret_key = os.getenv('SECRET_KEY', uuid.uuid4().hex)

#app.register_blueprint(login_logout)
app.register_blueprint(signup)
app.register_blueprint(home)

@app.route('/', methods=['GET'])
def index():
    return render_template('auth/login.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True) 


