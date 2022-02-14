from base import get_api


def test_get_api():
    """
    teste para a função 'get_api'
    :return:resultado do teste com preencimento do response
    """
    resp = get_api.get_data()
    assert resp
