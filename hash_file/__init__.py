from flask import Flask, render_template,flash,redirect,url_for
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user


app=Flask(__name__)
app.config['SECRET_KEY'] = '4684384f67h43g46j35vh59f21g54e32'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)


from hash_file import routes
