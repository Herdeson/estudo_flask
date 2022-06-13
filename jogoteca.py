from distutils.debug import DEBUG
from tkinter.messagebox import RETRY
from flask import Flask, redirect, render_template, request, session, flash, url_for

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

app = Flask(__name__)
app.secret_key = 'ljflkasjdfopiuw0e98r7082754oh43jk52h08rytw'

jogo1 = Jogo('Tetris', 'Puzzle', "Atari")
jogo2 = Jogo('God of War', 'Aventura', "PS2")
lista = [jogo1, jogo2 ]

def validar_acesso():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=novo')

@app.route('/')
def index():

    #return "<h1>Ola Mundo</h1>"
    return render_template('lista.html', titulo='Jogos', jogos = lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=novo')
    return render_template('novo.html', titulo='Novo jogo')

@app.route('/criar' ,  methods=['POST']) # Rota de processamento
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    novoJogo = Jogo(nome, categoria, console)
    lista.append(novoJogo)

    return redirect(url_for('index'))

    #return render_template('lista.html', titulo='Jogos', jogos = lista)
@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST'])
def autenticar():
    if 'thisistheway' == request.form['senha']:
        proxima_pagina = request.form['proxima']
        session['usuario_logado'] = request.form['usuario']
        flash('Usuario Logado com Sucesso')
        return redirect(proxima_pagina)
    else:
        flash('Usuario Logado com Sucesso')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso')
    return redirect(url_for('login'))


app.run(debug=True)