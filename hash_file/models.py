
from hash_file import db
from flask_login import UserMixin

class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30),nullable=True)
    username=db.Column(db.String(20),unique=True,nullable=True)
    email=db.Column(db.String(30),unique=True,nullable=True)
    password=db.Column(db.String(40),unique=True,nullable=False)

    def __repr__(self):
        return f"User('{self.username}','{self.email}')"


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
