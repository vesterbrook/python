from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/ninjas')
def info_ninja():
    return render_template('ninjas.html') 

@app.route('/dojos/new', methods=['POST'])
def dojo_new():


    name = request.form['name']
    email = request.form['email']

    return render_template('dojos.html')

   
app.run(debug=True)