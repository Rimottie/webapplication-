# Ao abrir o GitPod, execute:
# pip install -r requirements.txt

from flask import Flask, render_template, request
from uuid import uuid4
import csv 

app = Flask(__name__)

games = [
    {'id': 1, 'nome': 'Red Dead Redemption 2', 'comentario': 'Perfeito com gráficos maravilhosos', 'avaliacao': '9.8'},
    {'id': 2, 'nome': 'Borderlands 3', 'comentario': 'Bom mas paia', 'avaliacao': '8.7'},
    {'id': 3, 'nome': 'Cyberpunk 2077', 'comentario': 'Jogo ruim KKKKKKK', 'avaliacao': '6.5'},
]


@app.route('/')
def index():
    with open('games.csv', 'rt') as file_in:
        leitor = csv.reader(file_in)
        for linha in leitor:
            print(linha)
    return render_template('index.html', games=games)

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/save', methods=['POST'])
def save():
    nome = request.form['nome']         # <input name="nome" ...
    comentario = request.form['comentario']       # Sempre será uma string!
    avaliacao = request.form['avaliacao']
    games.append({"id": uuid4(), "nome": nome, "comentario": comentario, "avaliacao": avaliacao})

    with open('games.csv', 'wt') as file_out:
     escritor = csv.writer(file_out)
     escritor.writerows(games)
    return render_template('index.html', games=games)

# Trabalho Final da Disciplina:
# Implementar o delete 
# Implementar o update (rota para mostrar os dados no form e outra para salvar os dados)
# Salvar os dados, conforme forem sendo manipulados, em um arquivo CSV.

@app.route('/delete/<id>')
def delete(id):
    return id

@app.route('/update/<id>')
def update(id):
    return id

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


