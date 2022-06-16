# Ao abrir o GitPod, execute:
# pip install -r requirements.txt

from flask import Flask, render_template, redirect, request
from uuid import uuid4
import csv 
app = Flask(__name__)

#games = [
#    {'id': uuid4(), 'jogo': 'Red Dead Redemption 2', 'comentario': 'Perfeito com gráficos maravilhosos', 'avaliacao': '9.8'},
#    {'id': uuid4(), 'jogo': 'Borderlands 3', 'comentario': 'Bom mas paia', 'avaliacao': '8.7'},
#    {'id': uuid4(), 'jogo': 'Cyberpunk 2077', 'comentario': 'Jogo ruim KKKKKKK', 'avaliacao': '6.5'},
#]

def ler():
    with open('jogos.csv', 'rt') as file_out:
        leitor = csv.DictReader(file_out)
        games = []
        for row in leitor:
            game = {}
            for key, value in row.items():
                game[key] = value
            games.append(game)
    return games


@app.route('/')
def index():
    games = ler()
    return render_template('index.html', games = games)

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/save', methods=['POST'])
def save():
    games = ler()
    jogo = request.form['jogo']
    comentario = request.form['comentario']
    avaliacao = request.form['avaliacao']
    games.append({"id": uuid4(), "jogo": jogo, "comentario": comentario, "avaliacao": avaliacao})
    with open('jogos.csv', 'wt') as file_out:
        escritor = csv.DictWriter(file_out, ['id', 'jogo', 'comentario', 'avaliacao'])
        escritor.writeheader()
        escritor.writerows(games)
    return redirect('/')

@app.route('/edit/<id>')
def edit(id):
    games = ler()
    for game in games:
        if id == str(game['id']):
            return render_template('update.html', game = game)

@app.route('/edit/game/<id>', methods=['POST'])
def salvar_edicao(id):
    games = ler()
    for game in games:
        if (id == str(game['id'])):
            n = games.index(game)
            edit_id = game['id']
            
    edit_jogo = request.form['jogo']
    edit_comentario = request.form['comentario']
    edit_avaliacao = request.form['avaliacao']
    games[n] = {'id': edit_id, 'jogo': edit_jogo, 'comentario': edit_comentario, 'avaliacao': edit_avaliacao}
    with open('jogos.csv', 'wt') as file_out:
        escritor = csv.DictWriter(file_out, ['id', 'jogo', 'comentario', 'avaliacao'])
        escritor.writeheader()
        escritor.writerows(games)
    return redirect('/')

@app.route('/delete/<id>')
def delete(id):
    games = ler()
    for game in games:
        if (id == str(game['id'])):
            n = games.index(game)
            del games[n]
            with open('jogos.csv', 'wt') as file_out:
                escritor = csv.DictWriter(file_out, ['id', 'jogo', 'comentario', 'avaliacao'])
                escritor.writeheader()
                escritor.writerows(games)
            return redirect('/')

app.run(debug=True)