from flask import Flask, render_template, request, redirect, make_response
from os import getrandom
import db

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        db.add_comment(request.form['comment'])
        return redirect('/')

    search_query = request.args.get('q')

    comments = db.get_comments(search_query)

    response = make_response(render_template('index.html',
                           comments=comments,
                           search_query=search_query))

    response.set_cookie('username', 'Fabian')
    response.set_cookie('password', getrandom(16).hex())

    return response

@app.route('/reset', methods=['POST'])
def reset():
    db.reset()
    return redirect('/')
