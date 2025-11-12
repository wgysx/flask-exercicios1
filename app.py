from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, Flask !!</h1>'

@app.route('/versao')
def versao():
    versao = "1.1.0"
    return f"App v{versao}"

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/saudar/<nome>')
def saudar(nome):
    return f'Olá, {nome.capitalize()}!'

@app.route('/quadrado/<int:n>')
def quadrado(n):
    return f'{n}² = {n*n}'


@app.route('/pagina')
def pagina():
    return render_template('pagina.html')
