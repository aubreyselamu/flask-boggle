from boggle import Boggle
from flask import Flask, session, request, redirect, render_template, jsonify
from testing import add


app = Flask(__name__)
app.config['SECRET_KEY'] = "abc123"

boggle_game = Boggle()

@app.route('/')
def homepage():
    board = boggle_game.make_board()
    session['board'] = board
    return render_template('index.html', board = board)

@app.route('/check-word')
def check_word():
    '''Check if word is in dictionary'''
    
    word = request.args['word']
    board = session['board']
    
    response = boggle_game.check_valid_word(board, word)

    return jsonify({'result' : response})