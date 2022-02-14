import requests
import json


def get_data():
    """
    utiliza o a biblioteca 'requests' para obter os dados da api informada
    salva as informações no arquilo 'LOG_' dentro da pasta 'log' da aplicação
    :return: retorna os 5 primeiros registros
    """

    resp = requests.get("https://jsonplaceholder.typicode.com/todos")
    if resp.status_code == 200:
        status = resp.status_code
        todos = json.loads(resp.content)
        todos = todos[:5]
        todos_j = json.dumps(todos, indent=2)
    else:
        status = resp.status_code
        todos_j = '{"error": {"reason": "página não encontrada"}}'

    return todos_j, status


if __name__ == '__main__':
    get_data()
