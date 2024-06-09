from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define the models
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80), nullable=False)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def in_stock(self):
        return self.quantity > 0

class ProductCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

    product = db.relationship('Product', backref=db.backref('product_categories', lazy=True))
    category = db.relationship('Category', backref=db.backref('product_categories', lazy=True))


