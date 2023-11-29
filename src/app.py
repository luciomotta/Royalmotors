from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()  # Carrega as variáveis do arquivo .env

# Definindo a rota para renderizar o HTML
@app.route('/')
def index():
    return render_template('templates/index.html')

# Endpoint para lidar com o formulário
@app.route('/submit', methods=['POST'])
def submit_task():
    name = request.form['name']
    cpf = request.form['cpf']
    birthdate = request.form['birthdate']
    phone = request.form['phone']
    hasCar = request.form['hasCar']

    # Dados necessários para fazer a requisição à API do Trello
    url = "https://api.trello.com/1/cards"
    params = {
        'key': os.getenv('API_KEY'),
        'token': os.getenv('TOKEN'),
        'idList': os.getenv('LIST_ID'),
        'name': f"{name} - {cpf}",  # Altere conforme desejado para o título do card
        'desc': f"Data de Nascimento: {birthdate}\nTelefone: {phone}\nPossui carro? {hasCar}"  # Adapte para a descrição do card
    }

    # Fazendo a chamada POST para criar um novo card no Trello
    response = requests.post(url, params=params)

    if response.status_code == 200:
        return "Tarefa criada com sucesso no Trello!"
    else:
        return "Erro ao criar tarefa no Trello"

if __name__ == '__main__':
    app.run(debug=True)
