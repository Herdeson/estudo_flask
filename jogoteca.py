from distutils.debug import DEBUG
from flask import Flask, redirect, render_template, request

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

app = Flask(__name__)

jogo1 = Jogo('Tetris', 'Puzzle', "Atari")
jogo2 = Jogo('God of War', 'Aventura', "PS2")
lista = [jogo1, jogo2]


@app.route('/')
def index():

    #return "<h1>Ola Mundo</h1>"
    return render_template('lista.html', titulo='Jogos', jogos = lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo jogo')

@app.route('/criar' ,  methods=['POST']) # Rota de processamento
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    novoJogo = Jogo(nome, categoria, console)
    lista.append(novoJogo)

    return redirect('/')

    #return render_template('lista.html', titulo='Jogos', jogos = lista)

app.run(debug=True)