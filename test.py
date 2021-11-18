from unittest import TestCase
from app import app
from flask import session, request
from boggle import Boggle


class FlaskTests(TestCase):
    
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()
    
    def test_homepage(self):
        '''Make sure information is in the session and HTML is displayed'''
        
        with self.client as client:
            response = client.get('/')
            self.assertIn('board', session)
            self.assertNotIn('highscore', session)
            self.assertNotIn('nplays', session)
            self.assertIn(b'<p>High Score:', response.data)
            self.assertIn(b'Score:', response.data)
            self.assertIn(b'Seconds Left:', response.data)
    
    def test_valid_word(self):
        '''Test if the board is valid by modify the board in session'''
        
        with self.client as client:
            with client.session_transaction() as sess:
                sess['board'] = [["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"]]
        response = self.client.get('/check-word?word=cat')
        self.assertEqual(response.json['result'], 'ok')
    
    def test_invalid_word(self):
        '''Test if word is in the dictionary'''
        self.client.get('/')

        response = self.client.get('/check-word?word=impossible')
        self.assertEqual(response.json['result'], 'not-on-board')
    
    def test_non_english_word(self):
        '''Test if word is on board'''
        
        self.client.get('/')
        response = self.client.get('/check-word?word=gfndjhgjsgh')
        self.assertEqual(response.json['result'], 'not-word')



        
  





