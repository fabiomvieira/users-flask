from app import app, db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    email = db.Column(db.String(30))
    phone = db.Column(db.Integer)

    def __init__(self, name, age, email, phone):
        self.name = name
        self.age = age
        self.email= email
        self.phone = phone