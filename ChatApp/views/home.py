from flask import request, redirect, render_template, session, flash, url_for, Blueprint
import pymysql

home = Blueprint('home', __name__, template_folder = 'templates', static_folder = 'static')

@home.route('/home', methods=['GET'])
def home_view():
  return render_template('home/home.html')
