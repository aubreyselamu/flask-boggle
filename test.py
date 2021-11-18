from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):
    
    def setUp(self):
        app.config['TESTING'] = True
    
    def test_homepage(self):
        with app.test_client() as client:
            response = client.get('/')
            self.assertIn('board', session)
            self.assertNotIn('highscore', session)
            self.assertNotIn('nplays', session)
            self.assertIn(b'<p>High Score:', response.data)
            self.assertIn(b'Score:', response.data)
            self.assertIn(b'Seconds Left:', response.data)
    
    











