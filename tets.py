import requests
from dotenv import load_dotenv
import os

# Carregar variáveis do arquivo .env
load_dotenv()

# Obter as chaves e tokens do arquivo .env
API_KEY = os.getenv('API_KEY')
TOKEN = os.getenv('TOKEN')

# URL base da API do Trello
base_url = "https://api.trello.com/1"

# Nome do board e da lista onde deseja adicionar o cartão
board_name = "Royal motors"  # Substitua pelo nome do seu board
list_name = "Clientes"   # Substitua pelo nome da sua lista

# Encontrar o ID do board pelo nome
boards_url = f"{base_url}/members/me/boards"
boards_params = {
    'key': API_KEY,
    'token': TOKEN
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
    lists_url = f"{base_url}/boards/{board_id}/lists"
    lists_params = {
        'key': API_KEY,
        'token': TOKEN
    }
    response = requests.get(lists_url, params=lists_params)
    lists = response.json()
    list_id = None
    for trello_list in lists:
        if trello_list['name'] == list_name:
            list_id = trello_list['id']
            break

    if list_id:
        # Dados do cartão a serem criados
        card_data = {
            'key': API_KEY,
            'token': TOKEN,
            'idList': list_id,
            'name': 'Novo Cartão',      # Nome do cartão
            'desc': 'Descrição do cartão'  # Descrição do cartão
        }

        # Criar um novo cartão no Trello
        cards_url = f"{base_url}/cards"
        
        # Usar 'json' em vez de 'params' para enviar os dados do cartão corretamente
        response = requests.post(cards_url, json=card_data)

        # Verificar se a operação foi bem-sucedida
        if response.status_code == 200:
            print("Cartão criado com sucesso!")
            card_info = response.json()
            print("ID do cartão:", card_info['id'])
        else:
            print("Erro ao criar o cartão no Trello.")
            print("Status Code:", response.status_code)
            print("Resposta:", response.text)
    else:
        print(f"Lista '{list_name}' não encontrada no board '{board_name}'.")
else:
    print(f"Board '{board_name}' não encontrado.")
