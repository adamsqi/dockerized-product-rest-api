import os

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # stop from complaining in the console

db = SQLAlchemy(app)

ma = Marshmallow(app)


class Product(db.Model):
    sku = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(255))
    qty = db.Column(db.Integer)
    price = db.Column(db.Float)

    def __init__(self, sku, name, qty, price):
        self.sku = sku
        self.name = name
        self.qty = qty
        self.price = price


db.drop_all()
db.create_all()


class ProductSchema(ma.Schema):
    class Meta:
        fields = ('sku', 'name', 'qty', 'price')


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)


@app.route('/product/register', methods=['POST'])
def register_product():
    sku = request.json['sku']
    name = request.json['name']
    qty = request.json['qty']
    price = request.json['price']
    new_product = Product(sku, name, qty, price)
    db.session.add(new_product)
    db.session.commit()
    return product_schema.jsonify(new_product)


@app.route('/product/<sku>', methods=['GET'])
def get_product(sku):
    product = Product.query.filter(Product.sku == sku)
    result = products_schema.dump(product)
    return jsonify(result)


@app.route('/products/available', methods=['GET'])
def get_all_available_products():
    all_products = Product.query.filter(Product.qty > 0)
    result = products_schema.dump(all_products)
    return jsonify(result)


@app.route('/products/sold_out', methods=['GET'])
def get_all_sold_products():
    all_products = Product.query.filter(Product.qty == 0)
    result = products_schema.dump(all_products)
    return jsonify(result)


@app.route('/product/<sku>/set_new_qty/<qty>', methods=['PUT'])
def register_quantity_change(sku, qty):
    product = Product.query.filter(Product.sku == sku).first()
    product.qty = qty
    db.session.commit()
    return product_schema.jsonify(product)


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
