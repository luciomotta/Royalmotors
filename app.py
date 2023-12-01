from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os
import logging

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
        # Obtenção das chaves da API e do token do .env
        api_key = os.getenv('API_KEY')
        token = os.getenv('TOKEN')
        board_name = "Royal motors"  # Substitua pelo nome do seu board
        list_name = "Clientes"   # Substitua pelo nome da sua lista

        # Encontrar o ID do board pelo nome
        boards_url = f"https://api.trello.com/1/members/me/boards"
        boards_params = {
            'key': api_key,
            'token': token
        }
        response = requests.get(boards_url, params=boards_params)
        boards = response.json()
        board_id = None
        for board in boards:
            if board['name'] == board_name:
                board_id = board['id']
                break

        if board_id:
            # Encontrar o ID da lista pelo nome no board encontrado
            lists_url = f"https://api.trello.com/1/boards/{board_id}/lists"
            lists_params = {
                'key': api_key,
                'token': token
            }
            response = requests.get(lists_url, params=lists_params)
            lists = response.json()
            list_id = None
            for trello_list in lists:
                if trello_list['name'] == list_name:
                    list_id = trello_list['id']
                    break

            if list_id:
                # Obtenção dos dados do formulário
                name = request.form['name']
                cpf = request.form['cpf']
                birthdate = request.form['birthdate']
                phone = request.form['phone']
                hasCar = request.form['hasCar']

                # Nome será o título do cartão
                card_title = name + ' ' + cpf

                # Restante das informações na descrição do cartão
                card_desc = f"CPF: {cpf}\nData de Nascimento: {birthdate}\nTelefone: {phone}\nPossui carro? {hasCar}"

                # Dados do cartão a serem criados
                card_data = {
                    'key': api_key,
                    'token': token,
                    'idList': list_id,
                    'name': card_title,
                    'desc': card_desc
                }

                # Criar um novo cartão no Trello
                cards_url = "https://api.trello.com/1/cards"
                response = requests.post(cards_url, params=card_data)

                if response.status_code == 200:
                    return "Tarefa criada com sucesso no Trello!"
                else:
                    logging.error("Erro ao criar tarefa no Trello")
                    return "Erro ao criar tarefa no Trello"
            else:
                logging.error(f"Lista '{list_name}' não encontrada no board '{board_name}'.")
                return f"Lista '{list_name}' não encontrada no board '{board_name}'."
        else:
            logging.error(f"Board '{board_name}' não encontrado.")
            return f"Board '{board_name}' não encontrado."

    except Exception as e:
        logging.exception("Erro ao processar a solicitação")
        return f"Erro ao processar a solicitação: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
