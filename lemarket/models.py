from lemarket import db

class postData(db.Model):  #SQL cxrili python klasis formashi
    id = db.Column(db.Integer(), primary_key=True)
    content = db.Column(db.String(length=200), nullable=False)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))
    

 
class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    items = db.relationship('postData', backref='posted_by_user', lazy=True)
    

