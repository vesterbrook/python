from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'Secretkey'
random.randint(0,101)

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/low', methods=['POST'])
def too_low():

    guess= request.form['guess']
    
    print random.randint

    return render_template('index.html', guess=guess)





app.run(debug=True)
