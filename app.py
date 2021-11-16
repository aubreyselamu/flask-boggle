from boggle import Boggle
from flask import Flask, session, request, redirect, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = "abc123"

boggle_game = Boggle()

@app.route('/')
def test():
    return "Hello!!!"