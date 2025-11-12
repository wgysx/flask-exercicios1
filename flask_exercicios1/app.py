from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, Flask !!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
