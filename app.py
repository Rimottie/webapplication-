# Ao abrir o GitPod, execute:
# pip install -r requirements.txt

from flask import Flask, render_template, redirect, request
from uuid import uuid4
import csv 

app = Flask(__name__)

games = [
    {'id': uuid4(), 'jogo': 'Red Dead Redemption 2', 'comentario': 'Perfeito com gráficos maravilhosos', 'avaliacao': '9.8'},
    {'id': uuid4(), 'jogo': 'Borderlands 3', 'comentario': 'Bom mas paia', 'avaliacao': '8.7'},
    {'id': uuid4(), 'jogo': 'Cyberpunk 2077', 'comentario': 'Jogo ruim KKKKKKK', 'avaliacao': '6.5'},
]

@app.route('/')
def index():
      with open('jogos.csv', 'wt') as file_out:
          
        escritor = csv.writer(file_out)
        escritor.writerows(games)
        return render_template('index.html', games=games)

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/save', methods=['POST'])
def save():
    jogo = request.form['jogo']         # <input name="nome" ...
    comentario = request.form['comentario']       # Sempre será uma string!
    avaliacao = request.form['avaliacao']

    games.append({"id": uuid4(), "jogo": jogo, "comentario": comentario, "avaliacao": avaliacao})
    with open('jogos.csv', 'wt') as file_out:
        escritor = csv.writer(file_out)
        escritor.writerows(games)
        return render_template('index.html', games=games)

@app.route('/edit/<id>')
def edit(id):
    for game in games:

        if (id == str(game['id'])):
            game.update(game)
    return render_template('update.html', games=games)

@app.route('/edit/game/<id>', methods=['POST'])
def save_edit(id):
    for game in games:

        if (id == str(game['id'])):
            i = games.index(game)
            edit_id = game['id']

    edit_jogo = request.form['Jogo']
    edit_comentario = request.form['Comentário']
    edit_avaliacao = request.form['Avaliação']

    games[i] = {'id':edit_id,'Jogo':edit_jogo,'Cometário':edit_comentario,'Avaliação':edit_avaliacao}
    return redirect('/Inicio')

@app.route('/delete/<id>')
def delete(id):
    for game in games:
        if (id == str(game['id'])):
            games.remove(game)
    return render_template('index.html', games=games)

app.run(debug=True)


# CLIENTE -- SERVIDOR
# Navegador -- AWS (Flask)

# Client -> REQUEST (Mensagem HTTP) -> Server 
# Server -> RESPONSE (Mensagem HTTP) -> CLIENTE

# HTTP (HyperText Transfer Protocol)
# HTML (HyperText Markup Language)

# Mensagem HTTP: 
# Header
# Body
# METHOD (GET, POST), Métodos suportados pelos navegadores.
# GET -> DADOS PELA URL
# POST -> OCULTO OS DADOS (NÃO MOSTRA NA URL)

# METHOD (API = GET, POST, PUT, DELETE, PATCH, OPTIONS)

# API REST
# POST   (C)REATE
# GET    (R)EAD
# PUT    (U)PDATE
# PATCH  (U)PDATE PARCIAL
# DELETE (D)ELETE