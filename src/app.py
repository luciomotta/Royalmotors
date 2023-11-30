from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os
import traceback

app = Flask(__name__, static_folder='static')
load_dotenv()  # Carrega as variáveis do arquivo .env

# Definindo a rota para renderizar o HTML
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint para lidar com o formulário
@app.route('/submit', methods=['POST'])
def submit_task():
    try:
        name = request.form['name']
        cpf = request.form['cpf']
        birthdate = request.form['birthdate']
        phone = request.form['phone']
        hasCar = request.form['hasCar']

        # Nome será o título do cartão
        card_title = name

        # Restante das informações na descrição do cartão
        card_desc = f"Nome: {name} \nCPF: {cpf}\nData de Nascimento: {birthdate}\nTelefone: {phone}\nPossui carro? {hasCar}"

        # Dados necessários para fazer a requisição à API do Trello
        api_key = os.getenv('API_KEY')
        token = os.getenv('TOKEN')
        list_id = os.getenv('LIST_ID')

        # Dados necessários para fazer a requisição à API do Trello
        url = "https://api.trello.com/1/cards"
        params = {
            'key': os.getenv('API_KEY'),
            'token': os.getenv('TOKEN'),
            'idList': os.getenv('LIST_ID'),
            'name': card_title,
            'desc': card_desc
        }

        # Fazendo a chamada POST para criar um novo card no Trello
        response = requests.post(url, params=params)

        if response.status_code == 200:
            return "Tarefa criada com sucesso no Trello!"
        else:
            return "Erro ao criar tarefa no Trello"
    except Exception as e:
        traceback.print_exc()  # Isso imprimirá o rastreamento da pilha para ajudar a identificar o erro
        return f"Erro ao processar a solicitação: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
