import datetime


def create_log(data, status):
    """
    printa o texto informado na chamada da função
    abre o arquilo LOG salva o texto no arquivo
    :param data:
    :param status:
    """
    data_name = datetime.datetime.today()
    datahora_name = data_name.strftime("%d_%m_%Y_%H_%M_%S")

    file_log = open(fr"log\LOG_{datahora_name}.txt", "a")
    file_log.write(f'{datetime.datetime.today()} - inicio')
    file_log.write(f'\n')
    file_log.write(f'{data}')
    file_log.write(f'\n')
    file_log.write(f'{status}')
    file_log.write(f'\n')
    file_log.close()


if __name__ == '__main__':
    create_log('{ "userId": 1, "id": 1, "title": "delectus aut autem", "completed": false }', 200)
