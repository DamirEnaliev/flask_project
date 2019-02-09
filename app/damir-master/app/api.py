from app import app
from models import Brand
from models import Country
from models import Customer
from models import Product
from flask import jsonify
from flask import request
from flask import render_template
from app import db

#api's for BRAND
@app.route('/api/brand', methods=['GET'])
def api_brand_get():
    brands = Brand.query.all()
    brands_json = [{"id_brand": brand.id, "name_brand": brand.name}
                  for brand in brands]
    return jsonify(brands_json)

@app.route('/api/brand/<id>', methods=['GET'])
def api_brand_get_id(id):
    brands = Brand.query.filter_by(id=id)
    if not brands:
        abort(404)
    brand = brands[0]
    brand_json = {"id_brand": brand.id, "name_brand": brand.name}
    return jsonify(brand_json)

@app.route('/api/brand', methods=['POST'])
def api_brand_insert():
    new_brand = request.get_json()
    brand = Brand(id=new_brand['id'], name=new_brand['name'])
    db.session.add(brand)
    db.session.commit()
    brand_json = {"id": brand.id, "name": brand.name}
    return jsonify(brand_json)

@app.route('/api/brand/<id>', methods=['DELETE'])
def api_brand_delete(id):
    brands = Brand.query.filter_by(id=id)
    if not brands:
        abort(404)
    brand = brands[0]
    db.session.delete(brand)
    db.session.commit()
    return jsonify()

#api's for COUNTRY
@app.route('/api/country', methods=['GET'])
def api_country_get():
    countrys = Country.query.all()
    countrys_json = [{"id_country": country.id, "name_country": country.name}
                  for country in countrys]
    return jsonify(countrys_json)

@app.route('/api/country/<id>', methods=['GET'])
def api_country_get_id(id):
    countrys = Country.query.filter_by(id=id)
    if not countrys:
        abort(404)
    country = countrys[0]
    country_json = {"id_country": country.id, "name_country": country.name}
    return jsonify(country_json)

@app.route('/api/country', methods=['POST'])
def api_country_insert():
    new_country = request.get_json()
    country = Country(id=new_country['id'], name=new_country['name'])
    db.session.add(country)
    db.session.commit()
    country_json = {"id": country.id, "name": country.name}
    return jsonify(country_json)

@app.route('/api/country/<id>', methods=['DELETE'])
def api_country_delete(id):
    countrys = Country.query.filter_by(id=id)
    if not countrys:
        abort(404)
    country = countrys[0]
    db.session.delete(country)
    db.session.commit()
    return jsonify()

#api's for CUSTOMER
@app.route('/api/customer', methods=['GET'])
def api_customer_get():
    customers = Customer.query.all()
    customers_json = [{"id_customer": customer.id, "name_customer": customer.firstname, "surname_customer": customer.surname, "phone_customer": customer.phone, "city_customer": customer.city, "street_customer": customer.street}
                  for customer in customers]
    return jsonify(customers_json)

@app.route('/api/customer/<id>', methods=['GET'])
def api_customer_get_id(id):
    customers = Customer.query.filter_by(id=id)
    if not customers:
        abort(404)
    customer = customers[0]
    customer_json = {"id_customer": customer.id, "name_customer": customer.firstname, "surname_customer": customer.surname, "phone_customer": customer.phone, "city_customer": customer.city, "street_customer": customer.street}
    return jsonify(customer_json)

@app.route('/api/customer', methods=['POST'])
def api_customer_insert():
    new_customer = request.get_json()
    customer = Customer(id=new_customer['id'], firstname=new_customer['firstname'], surname=new_customer['surname'], phone=new_customer['phone'], city=new_customer['city'], street=new_customer['street'])
    db.session.add(customer)
    db.session.commit()
    customer_json = {"id_customer": customer.id, "name_customer": customer.firstname, "surname_customer": customer.surname, "phone_customer": customer.phone, "city_customer": customer.city, "street_customer": customer.street}
    return jsonify(customer_json)

@app.route('/api/customer/<id>', methods=['DELETE'])
def api_customer_delete(id):
    customers = Customer.query.filter_by(id=id)
    if not customers:
        abort(404)
    customer = customers[0]
    db.session.delete(customer)
    db.session.commit()
    return jsonify()

#api's for PRODUCT
@app.route('/api/product', methods=['GET'])
def api_product_get():
    products = Product.query.all()
    products_json = [{"id_product": product.id, "type_product": product.type, "brand_product": product.brand, "country_product": product.country, "price_product": product.price, "amount_product": product.amount}
                  for product in products]
    return jsonify(products_json)

@app.route('/api/product/<id>', methods=['GET'])
def api_product_get_id(id):
    products = Product.query.filter_by(id=id)
    if not products:
        abort(404)
    product = products[0]
    product_json = {"id_product": product.id, "type_product": product.type, "brand_product": product.brand, "country_product": product.country, "price_product": product.price, "amount_product": product.amount}
    return jsonify(product_json)

@app.route('/api/product', methods=['POST'])
def api_product_insert():
    new_product = request.get_json()
    product = Product(id=new_product['id'], type=new_product['type'], brand=new_product['brand'], country=new_product['country'], price=new_product['price'], amount=new_product['amount'])
    db.session.add(product)
    db.session.commit()
    product_json = {"id_product": product.id, "type_product": product.type, "brand_product": product.brand, "country_product": product.country, "price_product": product.price, "amount_product": product.amount}
    return jsonify(product_json)

@app.route('/api/product/<id>', methods=['DELETE']) 	
def api_product_delete(id):
    products = Product.query.filter_by(id=id)
    if not products:
        abort(404)
    product = products[0]
    db.session.delete(product)
    db.session.commit()
    return jsonify()

@app.route('/')
def index():
	return render_template('index.html')

