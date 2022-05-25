from lemarket import db

class itemData(db.Model):  #SQL cxrili python klasis formashi
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    quality = db.Column(db.String(length=30), nullable=False)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))
    def __repr__(self):
        return f"Item {self.name}"

 
class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    items = db.relationship('itemData', backref='owned_by_user', lazy=True)
    def __repr__(self):
        return f"user -> {self.username}"
