from flask_testing import TestCase
from flask import current_app, url_for
from main import app
from urllib.parse import urlparse

class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        
        return app
    
    def test_app_exists(self):
        self.assertIsNotNone(current_app)
        
    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])
        
    def test_index_redirects(self):
        response = self.client.get(url_for('cookie'))
        parsed_location = urlparse(response.location)

    def test_hello_get(self):
        response = self.client.get(url_for('marisol'))
        self.assert200(response)
        
    def test_hello_post(self):
        fake_form = {
            'username': 'fake',
            'password': 'fake-password'
        }
        response = self.client.post(url_for('marisol'), data=fake_form)
        parsed_location = urlparse(response.location)
        self.assertEqual(parsed_location.path, url_for('cookie'))