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