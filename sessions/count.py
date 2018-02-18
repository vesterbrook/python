from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'Secretkey'


@app.route('/')
def index():

    request.session['generate'] = request.POST['generate']
    if 'counter' not in session:
        session['counter'] =0
    session['counter'] += 1

    return render_template('index.html', count=session['counter'])

@app.route('/plustwo')
def level():
    session['counter'] += 1

    return redirect('/')


@app.route('/reset')
def clear():
    if 'counter' in session:
        session['counter'] > 0
    session['counter'] =0

    return redirect()

app.run(debug=True) 

