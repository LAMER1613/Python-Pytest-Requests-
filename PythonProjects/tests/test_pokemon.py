import pytest
import requests

url_api = 'https://api.pokemonbattle.me:9104'

def test_get_trainer():
    response = requests.get(f'{url_api}/trainers', params={'trainer_id' : '1552'})
    assert response.status_code == 200
    
def test_get_trainer_id():
    response = requests.get(f'{url_api}/trainers', params={'trainer_id' : '1552'})
    assert response.json()['trainer_name'] == 'Тлен'