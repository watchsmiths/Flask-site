from app import db  

class Brands(db.Model):
    brand_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True, nullable=False)
    logo = db.Column(db.String(255), index=True, unique=True, nullable=True)
    products = db.relationship('Products', backref='brand', lazy='dynamic')

    def __repr__(self):
        return '<Brand {}>'.format(self.name)

class Products(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    brand_name = db.Column(db.String, db.ForeignKey('brands.name'), nullable=False)
    name = db.Column(db.String(240), index=True, unique=True, nullable=False)
    thumb_name = db.Column(db.String(240), nullable=True)
    price = db.Column(db.Numeric(11,2), nullable=False)
    discount_price = db.Column(db.Numeric(10,2), nullable=True)
    sale = db.Column(db.Boolean, default=False, nullable=True)
    cart_thumb = db.Column(db.String(255), nullable=True)
    product_large_1 = db.Column(db.String(255), nullable=True)
    product_large_2 = db.Column(db.String(255), nullable=True)
    product_large_3 = db.Column(db.String(255), nullable=True)
    product_thumb_1 = db.Column(db.String(255), nullable=True)
    product_thumb_2 = db.Column(db.String(255), nullable=True)
    product_thumb_3 = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return '<Product {}>'.format(self.name)

db.create_all()