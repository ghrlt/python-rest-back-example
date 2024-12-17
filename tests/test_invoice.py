import unittest
import json
from app import create_app
from models.database import db
from models.user import User
from models.invoice import Invoice

class InvoiceTestCase(unittest.TestCase):
    def setUp(self):
        """Initialisation avant chaque test"""
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

        # Créer la base de données et ajouter un utilisateur de test
        db.create_all()
        user = User(name='Test User', email='test@example.com', password='password')
        db.session.add(user)
        db.session.commit()
        self.user_id = user.id

    def tearDown(self):
        """Nettoyage après chaque test"""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_invoice(self):
        """Test de la création d'une nouvelle facture"""
        data = {
            'amount': 150.75,
            'user_id': self.user_id
        }
        response = self.client.post('/invoices', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.get_json())

    def test_get_invoices(self):
        """Test de récupération de toutes les factures"""
        # Créer une facture de test
        invoice = Invoice(amount=200.50, user_id=self.user_id)
        db.session.add(invoice)
        db.session.commit()

        response = self.client.get('/invoices')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json(), list)
        self.assertGreaterEqual(len(response.get_json()), 1)

    def test_get_invoice_by_id(self):
        """Test de récupération d'une facture par ID"""
        # Créer une facture de test
        invoice = Invoice(amount=300.00, user_id=self.user_id)
        db.session.add(invoice)
        db.session.commit()

        response = self.client.get(f'/invoices/{invoice.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['amount'], 300.00)

    def test_update_invoice(self):
        """Test de la mise à jour d'une facture"""
        # Créer une facture de test
        invoice = Invoice(amount=400.00, user_id=self.user_id)
        db.session.add(invoice)
        db.session.commit()

        updated_data = {
            'amount': 450.00
        }
        response = self.client.put(f'/invoices/{invoice.id}', data=json.dumps(updated_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['amount'], 450.00)

    def test_delete_invoice(self):
        """Test de la suppression d'une facture"""
        # Créer une facture de test
        invoice = Invoice(amount=500.00, user_id=self.user_id)
        db.session.add(invoice)
        db.session.commit()

        response = self.client.delete(f'/invoices/{invoice.id}')
        try:
            self.assertEqual(response.status_code, 200)
        except:
            self.assertEqual(response.status_code, 404)

        # Vérifier que la facture n'existe plus
        response = self.client.get(f'/invoices/{invoice.id}')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()