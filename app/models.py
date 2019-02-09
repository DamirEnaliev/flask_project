from app import db


class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100))
    surname = db.Column(db.String(100))
    phone = db.Column(db.Integer)
    city = db.Column(db.String(100))
    street = db.Column(db.String(100))


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100))
    brand = db.Column(db.Integer)
    country = db.Column(db.Integer)
    price = db.Column(db.Integer)
    amount = db.Column(db.Integer)
