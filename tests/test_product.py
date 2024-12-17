import unittest
from app import create_app
from models.database import db
from models.product import Product

class ProductTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_product(self):
        data = {
            "name": "Test Product",
            "price": 9.99,
            "stock": 10
        }
        response = self.client.post('/products', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json()['name'], data['name'])
        self.assertEqual(response.get_json()['price'], data['price'])
        self.assertEqual(response.get_json()['stock'], data['stock'])

        product = Product.query.get(response.get_json()['id'])
        self.assertEqual(product.name, data['name'])
        self.assertEqual(product.price, data['price'])
        self.assertEqual(product.stock, data['stock'])
    
    def test_get_products(self):
        response = self.client.get('/products')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 0)

        product = Product(name="Test Product", price=9.99, stock=10)
        db.session.add(product)
        db.session.commit()

        response = self.client.get('/products')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 1)
        self.assertEqual(response.get_json()[0]['name'], product.name)
        self.assertEqual(response.get_json()[0]['price'], product.price)
        self.assertEqual(response.get_json()[0]['stock'], product.stock)

        product2 = Product(name="Test Product 2", price=19.99, stock=20)
        db.session.add(product2)
        db.session.commit()

        response = self.client.get('/products')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 2)
        self.assertEqual(response.get_json()[0]['name'], product.name)
        self.assertEqual(response.get_json()[0]['price'], product.price)
        self.assertEqual(response.get_json()[0]['stock'], product.stock)
        self.assertEqual(response.get_json()[1]['name'], product2.name)
        self.assertEqual(response.get_json()[1]['price'], product2.price)
        self.assertEqual(response.get_json()[1]['stock'], product2.stock)

    def test_get_product_by_id(self):
        product = Product(name="Test Product", price=9.99, stock=10)
        db.session.add(product)
        db.session.commit()

        response = self.client.get(f'/products/{product.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['name'], product.name)
        self.assertEqual(response.get_json()['price'], product.price)
        self.assertEqual(response.get_json()['stock'], product.stock)

        response = self.client.get('/products/999')
        self.assertEqual(response.status_code, 404)

        response = self.client.get('/products/-1')
        self.assertEqual(response.status_code, 404)

    def test_update_product(self):
        product = Product(name="Test Product", price=9.99, stock=10)
        db.session.add(product)
        db.session.commit()

        data = {
            "name": "Updated Product",
            "price": 19.99,
            "stock": 20
        }
        response = self.client.put(f'/products/{product.id}', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['name'], data['name'])
        self.assertEqual(response.get_json()['price'], data['price'])
        self.assertEqual(response.get_json()['stock'], data['stock'])

        product = Product.query.get(product.id)
        self.assertEqual(product.name, data['name'])
        self.assertEqual(product.price, data['price'])
        self.assertEqual(product.stock, data['stock'])

    def test_delete_product(self):
        product = Product(name="Test Product", price=9.99, stock=10)
        db.session.add(product)
        db.session.commit()

        response = self.client.delete(f'/products/{product.id}')
        self.assertEqual(response.status_code, 200)

        response = self.client.get(f'/products/{product.id}')
        self.assertEqual(response.status_code, 404)

        product = Product.query.get(product.id)
        self.assertIsNone(product)