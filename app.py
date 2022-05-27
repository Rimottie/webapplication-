# Ao abrir o GitPod, execute:
# pip install -r requirements.txt

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'

app.run()
