from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    

    return render_template('index.html')


@app.route('/process', methods=['POST'])
def two():
    
    name= request.form['name']
    print name
    return render_template('process.html', pname=name)
    

app.run(debug=True)
