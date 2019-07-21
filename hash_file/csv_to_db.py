
import csv
from flask import Flask, render_template,flash,redirect,url_for
from flask_sqlalchemy import SQLAlchemy



app=Flask(__name__)
app.config['SECRET_KEY'] = '4684384f67h43g46j35vh59f21g54e32'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class md(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    hash=db.Column(db.String(400),nullable=True)
    date_created=db.Column(db.String(400),nullable=True)
    size=db.Column(db.String(400),nullable=True)
    source=db.Column(db.String(100),nullable=True)

    def __repr__(self):
        return f"md('{self.id}','{self.hash}','{self.date_created}','{self.size}','{self.source}')"

class sha1(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    hash=db.Column(db.String(400),nullable=True)
    date_created=db.Column(db.String(400),nullable=True)
    size=db.Column(db.String(400),nullable=True)
    source=db.Column(db.String(100),nullable=True)

    def __repr__(self):
        return f"sha1('{self.id}','{self.hash}','{self.date_created}','{self.size}','{self.source}')"

class sha256(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    hash=db.Column(db.String(400),nullable=True)
    date_created=db.Column(db.String(400),nullable=True)
    size=db.Column(db.String(400),nullable=True)
    source=db.Column(db.String(100),nullable=True)

    def __repr__(self):
        return f"sha256('{self.id}','{self.hash}','{self.date_created}','{self.size}','{self.source}')"

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30),nullable=True)
    username=db.Column(db.String(20),unique=True,nullable=True)
    email=db.Column(db.String(30),unique=True,nullable=True)
    password=db.Column(db.String(40),unique=True,nullable=False)

    def __repr__(self):
        return f"User('{self.username}','{self.email}')"


db.create_all()
try:
    with open('/Users/shivanshu.singh/Documents/assessment/hash_file/scrap_virus.csv','r') as csv_file,open('/Users/shivanshu.singh/Documents/assessment/hash_file/scrap.csv','r') as csv_file1:
        csv_reader =csv.reader(csv_file)
        for row in csv_reader:
            inp=md(hash=row[4],date_created=row[2],size=row[3],source=row[12])
            db.session.add(inp)


        csv_reader =csv.reader(csv_file1)
        for row in csv_reader:
            inp=md(hash=row[1],date_created=row[5],size=row[10],source=row[13])
            db.session.add(inp)

except:
    db.session.rollback()




try:
    with open('/Users/shivanshu.singh/Documents/assessment/hash_file/scrap_virus.csv','r') as csv_file:
        csv_reader =csv.reader(csv_file)
        for row in csv_reader:

            inp=sha1(hash=row[5],date_created=row[2],size=row[3],source=row[12])
            db.session.add(inp)


except:
    db.session.rollback()

try:
    with open('/Users/shivanshu.singh/Documents/assessment/hash_file/scrap.csv','r') as csv_file:
        csv_reader =csv.reader(csv_file)
        for row in csv_reader:
            inp=sha1(hash=row[2],date_created=row[5],size=row[10],source=row[13])
            db.session.add(inp)


except:
    db.session.rollback()

try:
    with open('/Users/shivanshu.singh/Documents/assessment/hash_file/scrap_totalhash.csv','r') as csv_file:
        csv_reader =csv.reader(csv_file)
        for row in csv_reader:
            inp=sha1(hash=row[1],date_created=row[2],size="",source=row[3])
            db.session.add(inp)


except:
    db.session.rollback()


try:
    with open('/Users/shivanshu.singh/Documents/assessment/hash_file/scrap_virus.csv','r') as csv_file:
        csv_reader =csv.reader(csv_file)
        for row in csv_reader:

            inp=sha256(hash=row[6],date_created=row[2],size=row[3],source=row[12])
            db.session.add(inp)


except:
    db.session.rollback()

try:
    with open('/Users/shivanshu.singh/Documents/assessment/hash_file/scrap.csv','r') as csv_file:
        csv_reader =csv.reader(csv_file)
        for row in csv_reader:

            inp=sha256(hash=row[3],date_created=row[5],size=row[10],source=row[13])
            db.session.add(inp)
        db.session.commit()

except:
    db.session.rollback()
