from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, Flask !!</h1>'

@app.route('/versao')
def versao():
    versao = "1.1.0"
    return f"App v{versao}"

@app.route('/saudar/<nome>')
def saudar(nome):
    return f'Olá, {nome.capitalize()}!'

@app.route('/quadrado/<int:n>')
def quadrado(n):
    return f'{n}² = {n*n}'

@app.route('/home')
def home():
    return redirect('/')

@app.route('/pagina')
def pagina():
    return render_template('pagina.html')

@app.route('/buscar/<item>')
def buscar(item):
    itens = ['maçã', 'banana', 'laranja', 'uva']
    for i in itens:
        if i == item:
            return f'Item \"{item}\" encontrado.'
    return f'Item \"{item}\" não encontrado.'

if __name__ == '__main__':
    app.run(debug=True)