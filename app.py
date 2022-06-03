# Ao abrir o GitPod, execute:
# pip install -r requirements.txt

from flask import Flask, render_template

app = Flask(__name__)

clientes = [
    {'nome': 'Fulano', 'email': 'fulano@email.com', 'telefone': '123123'},
    {'nome': 'Ciclano', 'email': 'ciclano@email.com', 'telefone': '432423'},
    {'nome': 'Beltrano', 'email': 'beltrano@email.com', 'telefone': '6456456'},
]

@app.route('/')
def index():
    return render_template('index.html', clientes=clientes)

@app.route('/create')
def create():
    return render_template('create.html')

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


