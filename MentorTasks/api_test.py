import requests

def get_link():
    response = requests.get('https://dummyjson.com/docs/posts')

    assert 