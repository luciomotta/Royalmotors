from flask import Flask, request
import requests
from dotenv import load_dotenv
import os
#pip install Flask ---> Instalar
#python app.py ----->Iniciar
#Abra um navegador e vá para http://127.0.0.1:5000/ (ou o link fornecido pelo Flask)

app = Flask(__name__)
load_dotenv()  # Carrega as variáveis do arquivo .env

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
