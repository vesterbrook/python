from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('indexx.html')

@app.route('/projects')
def proj():
    return render_template('projects.html')

@app.route('/about')
def abou():
    return render_template('about.html')

app.run(debug=True)