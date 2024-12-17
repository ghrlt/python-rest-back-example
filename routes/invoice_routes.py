from flask import Blueprint, request, jsonify
from models.database import db
from model.user import User
from model.invoice import Invoice

invoice_bp = Blueprint('invoice_route', __name__)

# GET /invoices - Récupérer toutes les factures
@invoice_bp.route('/invoices', methods=['GET'])
def get_invoices():
    invoices = Invoice.query.all()
    return jsonify([invoice.to_dict() for invoice in invoices]), 200

# GET /invoices/<id> - Récupérer une facture par ID
@invoice_bp.route('/invoices/<int:invoice_id>', methods=['GET'])
def get_invoice(invoice_id):
    invoice = Invoice.query.get(invoice_id)
    if not invoice:
        return jsonify({'message': 'Facture non trouvée'}), 404
    
    return jsonify(invoice.to_dict()), 200

# POST /invoices - Créer une nouvelle facture
@invoice_bp.route('/invoices', methods=['POST'])
def create_invoice():
    data = request.get_json()
    amount = data.get('amount')
    date = data.get('date')  # Optionnel, sinon utilise la date actuelle
    user_id = data.get('user_id')

    # Validation des données
    if not amount or not user_id:
        return jsonify({'message': 'Montant et user_id sont requis'}), 400

    # Vérifier si l'utilisateur existe
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'Utilisateur non trouvé'}), 404

    invoice = Invoice(amount=amount, user_id=user_id)
    if date:
        try:
            invoice.date = datetime.fromisoformat(date)
        except ValueError:
            return jsonify({'message': 'Format de date invalide'}), 400

    db.session.add(invoice)
    db.session.commit()

    return jsonify(invoice.to_dict()), 201

# PUT /invoices/<id> - Mettre à jour une facture
@invoice_bp.route('/invoices/<int:invoice_id>', methods=['PUT'])
def update_invoice(invoice_id):
    invoice = Invoice.query.get(invoice_id)
    if not invoice:
        return jsonify({'message': 'Facture non trouvée'}), 404

    data = request.get_json()
    amount = data.get('amount')
    date = data.get('date')
    user_id = data.get('user_id')

    if amount is not None:
        invoice.amount = amount
    
    if date is not None:
        try:
            invoice.date = datetime.fromisoformat(date)
        except ValueError:
            return jsonify({'message': 'Format de date invalide'}), 400
    
    if user_id is not None:
        user = User.query.get(user_id)
        if not user:
            return jsonify({'message': 'Utilisateur non trouvé'}), 404
    
        invoice.user_id = user_id

    db.session.commit()
    return jsonify(invoice.to_dict()), 200

# DELETE /invoices/<id> - Supprimer une facture
@invoice_bp.route('/invoices/<int:invoice_id>', methods=['DELETE'])
def delete_invoice(invoice_id):
    invoice = Invoice.query.get(invoice_id)
    if not invoice:
        # On pourrait très bien retourner un code 200 ici, mais un code 404 est plus
        # approprié pour indiquer que la ressource n'existe pas, et ce même si l'objectif
        # est atteint (la facture n'existe plus (pas))
        return jsonify({'message': 'Facture non trouvée'}), 404

    db.session.delete(invoice)
    db.session.commit()
    return jsonify({'message': f'Facture {invoice_id} supprimée avec succès'}), 200