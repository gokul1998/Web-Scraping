from flask import render_template,url_for,redirect,session
from flask_wtf import FlaskForm
from hash_file import app,db
from hash_file.forms import RegistrationForm, LoginForm
from hash_file.models import User,md,sha1,sha256
from datetime import timedelta
import csv
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user, UserMixin

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/",methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        app.permanent_session_lifetime = timedelta(minutes=15)
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('basic'))
    return render_template('sign_in.html',title= 'Sign in',form=form)


@app.route("/basic",methods=['GET','POST'])
def basic():

    try:
        return render_template('basic.html',title = 'HASH WORLD',name=current_user.username)
    except:
        return redirect(url_for('error'))

@app.route("/error",methods=['GET','POST'])
def error():
    return render_template('error.html',title = 'ERROR')



@app.route("/source1_md5",methods=['GET','POST'])
def source1_md5():
    try:
        data=md.query.filter(md.source=='virus_sign')
        return render_template('index.html',title = 'HASH WORLD',data=data,str='MD5 HASH OF SOURCE VIRUS_SIGN',name=current_user.username)
    except:
        return redirect(url_for('error'))

@app.route("/source1_md5_sort",methods=['GET','POST'])
def source1_md5_sort():
    try:
        data=md.query.filter(md.source=='virus_sign').order_by(md.hash)
        return render_template('index.html',title = 'HASH WORLD',data=data,str='MD5 HASH OF SOURCE VIRUS_SIGN',name=current_user.username)
    except:
        return redirect(url_for('error'))


@app.route("/source1_sha1",methods=['GET','POST'])
def source1_sha1():
    try:
        data=sha1.query.filter(sha1.source=='virus_sign')
        return render_template('index1.html',title = 'HASH WORLD',data=data,str='SHA-1 HASH OF SOURCE VIRUS_SIGN',name=current_user.username)
    except:
        return redirect(url_for('error'))


@app.route("/source1_sha1_sort",methods=['GET','POST'])
def source1_sha1_sort():
    try:
        data=sha1.query.filter(sha1.source=='virus_sign').order_by(sha1.hash)
        return render_template('index1.html',title = 'HASH WORLD',data=data,str='SHA-1 HASH OF SOURCE VIRUS_SIGN',name=current_user.username)
    except:
        return redirect(url_for('error'))


@app.route("/source1_sha256",methods=['GET','POST'])
def source1_sha256():
    try:
        data=sha256.query.filter(sha256.source=='virus_sign')
        return render_template('index2.html',title = 'HASH WORLD',data=data,str='SHA-256 HASH OF SOURCE VIRUS_SIGN',name=current_user.username)
    except:
        return redirect(url_for('error'))


@app.route("/source1_sha256_sort",methods=['GET','POST'])
def source1_sha256_sort():
    try:
        data=sha256.query.filter(sha256.source=='virus_sign').order_by(sha256.hash)
        return render_template('index2.html',title = 'HASH WORLD',data=data,str='SHA-256 HASH OF SOURCE VIRUS_SIGN',name=current_user.username)
    except:
        return redirect(url_for('error'))


@app.route("/source2_md5",methods=['GET','POST'])
def source2_md5():
    try:
        data=md.query.filter(md.source=='avcaeser.malware.lu')
        return render_template('index.html',title = 'HASH WORLD',data=data,str='MD5 HASH OF SOURCE MALWARE.LU',name=current_user.username)
    except:
        return redirect(url_for('error'))

@app.route("/source2_md5_sort",methods=['GET','POST'])
def source2_md5_sort():
    try:
        data=md.query.filter(md.source=='avcaeser.malware.lu').order_by(md.hash)
        return render_template('index.html',title = 'HASH WORLD',data=data,str='MD5 HASH OF SOURCE MALWARE.LU',name=current_user.username)
    except:
        return redirect(url_for('error'))


@app.route("/source2_sha1",methods=['GET','POST'])
def source2_sha1():
    try:
        data=sha1.query.filter(sha1.source=='avcaeser.malware.lu')
        return render_template('index1.html',title = 'HASH WORLD',data=data,str='SHA-1 HASH OF SOURCE MALWARE.LU',name=current_user.username)
    except:
        return redirect(url_for('error'))


@app.route("/source2_sha1_sort",methods=['GET','POST'])
def source2_sha1_sort():
    try:
        data=sha1.query.filter(sha1.source=='avcaeser.malware.lu').order_by(sha1.source)
        return render_template('index1.html',title = 'HASH WORLD',data=data,str='SHA-1 HASH OF SOURCE MALWARE.LU',name=current_user.username)
    except:
        return redirect(url_for('error'))


@app.route("/source2_sha256",methods=['GET','POST'])
def source2_sha256():
    try:
        data=sha256.query.filter(sha256.source=='avcaeser.malware.lu')
        return render_template('index2.html',title = 'HASH WORLD',data=data,str='SHA-256 HASH OF SOURCE MALWARE.LU',name=current_user.username)
    except:
        return redirect(url_for('error'))


@app.route("/source2_sha256_sort",methods=['GET','POST'])
def source2_sha256_sort():
    try:
        data=sha256.query.filter(sha256.source=='avcaeser.malware.lu').order_by(sha256.hash)
        return render_template('index2.html',title = 'HASH WORLD',data=data,str='SHA-256 HASH OF SOURCE MALWARE.LU',name=current_user.username)
    except:
        return redirect(url_for('error'))


@app.route("/source3_sha1",methods=['GET','POST'])
def source3_sha1():
    try:
        data=sha1.query.filter(sha1.source=='https://totalhash.cymru.com/')
        return render_template('index1.html',title = 'HASH WORLD',data=data,str='SHA1 HASH OF SOURCE TOTAL HASH',name=current_user.username)
    except:
        return redirect(url_for('error'))


@app.route("/source3_sha1_sort",methods=['GET','POST'])
def source3_sha1_sort():
    try:
        data=sha1.query.filter(sha1.source=='https://totalhash.cymru.com/').order_by(sha1.hash)
        return render_template('index1.html',title = 'HASH WORLD',data=data,str='SHA1 HASH OF SOURCE TOTAL HASH',name=current_user.username)
    except:
        return redirect(url_for('error'))


@app.route("/md",methods=['GET','POST'])
def about():
    try:
        data=md.query.all()
        return render_template('index.html',title = 'MD',data=data,str='MD5 HASH OF ALL SOURCES',name=current_user.username)
    except:
        return redirect(url_for('error'))


@app.route("/md_sort",methods=['GET','POST'])
def md_sort():
    try:
        data=md.query.order_by(md.hash).all()
        return render_template('index.html',title = 'MD',data=data,str='MD5 HASH OF ALL SOURCES',name=current_user.username)
    except:
        return redirect(url_for('error'))


@app.route("/sha1",methods=['GET','POST'])
def about1():
    try:
        data=sha1.query.all()
        return render_template('index1.html',title = 'SHA-1',data=data,str='SHA-1 HASH OF ALL SOURCE',name=current_user.username)
    except:
        return redirect(url_for('error'))


@app.route("/sha1_sort",methods=['GET','POST'])
def sha1_sort():
    try:
        data=sha1.query.order_by(sha1.hash).all()
        return render_template('index1.html',title = 'SHA-1',data=data,str='SHA-1 HASH OF ALL SOURCE',name=current_user.username)
    except:
        return redirect(url_for('error'))


@app.route("/sha256",methods=['GET','POST'])
def about2():
    try:
        data=sha256.query.all()
        return render_template('index2.html',title = 'SHA-256',data=data,str='SHA-256 HASH OF ALL SOURCE',name=current_user.username)
    except:
        return redirect(url_for('error'))


@app.route("/sha256_sort",methods=['GET','POST'])
def sha256_sort():
    try:
        data=sha256.query.order_by(sha256.hash).all()
        return render_template('index2.html',title = 'SHA-256',data=data,str='SHA-256 HASH OF ALL SOURCE',name=current_user.username)
    except:
        return redirect(url_for('error'))


@app.route("/signup",methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))
    return render_template('sign_up.html',title='Main',form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
