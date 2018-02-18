from flask import Flask, render_template, request, redirect 

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def survey_sub():

    name= request.form['name']
    dojoloc=request.form['dojoloc']
    fav_lang=request.form['fav_lang']
    comment=request.form['comment']

    return render_template('submit.html', pname=name, dlocal=dojoloc, flang=fav_lang, commentop=comment)


app.run(debug=True)

guess= request.form['guess']