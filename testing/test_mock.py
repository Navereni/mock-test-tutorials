from request.mock
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_football(self):
    # We will mock a response of 1 and test that we get football returned.
        with request_mock.Mocker() as g:
            g.get('http://api:5000/get/number', text='1')
            g.get('http://api:5000/get/letter', text='a')
            response = self.client.get(url_for('sport'))
            self.assertIn(b'Football', response.data)
    
    def test_badminton(self):
    # We will mock a response of 1 and test that we get badminton returned.
        with request_mock.Mocker() as g:
            g.get('http://api:5000/get/number', text='1')
            g.get('http://api:5000/get/letter', text='b')
            response = self.client.get(url_for('sport'))
            self.assertIn(b'Badminton', response.data)
    
    def test_hockey(self):
    # We will mock a response of 1 and test that we get hockey returned.
        with request_mock.Mocker() as g:
            g.get('http://api:5000/get/number', text='1')
            g.get('http://api:5000/get/letter', text='c')
            response = self.client.get(url_for('sport'))
            self.assertIn(b'Hockey', response.data)
    def test_Boxing(self):
    # We will mock a response of 1 and test that we get hBoxingockey returned.
        with patch('requests.get') as g:
            g.return_value.text = "4"
            response = self.client.get(url_for('sport'))
            self.assertIn(b'Boxing', response.data)