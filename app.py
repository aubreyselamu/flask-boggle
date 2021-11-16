from boggle import Boggle
from flask import Flask, session, request, redirect, render_template
from testing import add


app = Flask(__name__)
app.config['SECRET_KEY'] = "abc123"

boggle_game = Boggle()

@app.route('/')
def test():
    board = boggle_game.make_board()
    session['board'] = board
    return render_template('base.html', board = board)

