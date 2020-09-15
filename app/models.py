from app import db

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     firstname = db.Column(db.String(80), unique=False, nullable=False)
#     lastname = db.Column(db.String(80), unique=False, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(180), unique=False, nullable=False)
#     profile = db.Column(db.String(180), unique=False, nullable=False, default='profile.jpg')

#     def __repr__(self):
#         return '<User %r>' % self.firstname


# class sellwatch(db.Model):
#     # id = db.Column(db.Integer)

class Brands(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True, nullable=False)
    logo = db.Column(db.String(255), index=True, unique=True, nullable=True)
    products = db.relationship('Product', backref='brand', lazy='dynamic')

    def __repr__(self):
        return '<Brand {}>'.format(self.name)

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_brand = db.Column(db.Integer, db.ForeignKey('brands.id'))
    name = db.Column(db.String(240), index=True, unique=True, nullable=False)
    price = db.Column(db.Numeric(11,2), index=True, nullable=False)
    discount_price = db.Column(db.Numeric(10,2), index=True, nullable=True)
    image_1 = db.Column(db.String(255), nullable=False)
    image_2 = db.Column(db.String(255), nullable=False)
    image_3 = db.Column(db.String(255), nullable=False)
    image_4 = db.Column(db.String(255), nullable=False)
    image_5 = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<Product {}>'.format(self.name)

db.create_all()