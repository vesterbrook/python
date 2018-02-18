from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def default():
    return render_template('index.html')

@app.route('/ninja')

return render_template('four.html')