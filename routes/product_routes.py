from flask import Blueprint, request, jsonify
from models.database import db
from models.product import Product

product_bp = Blueprint('product_route', __name__)

# GET /products - Récupérer tous les produits
@product_bp.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    if not products:
        return jsonify([]), 204

    return jsonify([product.to_dict() for product in products]), 200

# GET /products/<id> - Récupérer un produit par ID
@product_bp.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'message': 'Produit non trouvé'}), 404
    
    return jsonify(product.to_dict()), 200

# POST /products - Créer un nouveau produit
@product_bp.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    name = data.get('name')
    price = data.get('price')
    stock = data.get('stock')

    # Validation des données
    if not name or not price or not stock:
        return jsonify({'message': 'Nom, prix et stock sont requis'}), 400

    product = Product(name=name, price=price, stock=stock)
    db.session.add(product)
    db.session.commit()

    return jsonify(product.to_dict()), 201

# PUT /products/<id> - Mettre à jour un produit par ID
@product_bp.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'message': 'Produit non trouvé'}), 404

    data = request.get_json()
    name = data.get('name')
    price = data.get('price')
    stock = data.get('stock')

    if name is not None:
        product.name = name

    if price is not None:
        product.price = price

    if stock is not None:
        product.stock = stock

    if name is None and price is None and stock is None:
        return jsonify({'message': 'Aucune données fournies'}), 400

    db.session.commit()
    return jsonify(product.to_dict()), 200