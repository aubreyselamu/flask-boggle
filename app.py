from boggle import Boggle
from flask import Flask, session, request, redirect, render_template, jsonify



app = Flask(__name__)
app.config['SECRET_KEY'] = "abc123"

boggle_game = Boggle()

@app.route('/')
def homepage():
    board = boggle_game.make_board()
    session['board'] = board
    highscore = session.get('highscore', 0)
    nplays = session.get('nplays', 0)
    return render_template('index.html', board = board, highscore = highscore, nplays = nplays)

@app.route('/check-word')
def check_word():
    '''Check if word is in dictionary'''
    
    word = request.args['word']
    board = session['board']
    
    response = boggle_game.check_valid_word(board, word)

    return jsonify({'result' : response})

@app.route('/post-game', methods = ['POST'])
def post_gmae():
    '''Receive score, update nplays, update high score if appropriate.'''

    score = request.json['score']
    highscore = session.get('highscore', 0)
    nplays = session.get('nplays', 0)

    session[highscore] = max(score, highscore)
    session[nplays] = nplays + 1

    return jsonify(brokeRecord = score > highscore)

