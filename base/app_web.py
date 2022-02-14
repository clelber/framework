from flask import Flask, render_template
from get_api import get_data
from set_log import create_log


app = Flask(__name__)


@app.route('/')
def get_data():
    """
    chama a função get_dados, que é responsável pelo 'requests' das informações da api informada
    :return: renderiza os dados no arquivo 'show_data.html'
    """
    todos, status = get_data()
    create_log(f'{todos}', f'{status}')
    return render_template('show_data.html', dados=todos)


app.run()
