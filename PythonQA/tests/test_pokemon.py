import requests
import pytest

URL = 'https://api.pokemonbattle.ru'
Token = 'f017ba797b5525259cdd41e0cd4cdbc4'
Header = {'Content-Type': 'application/json', 'trainer_token':Token}
trainer_id = 11701

@pytest.fixture
def General_response():
    return requests.get(f'{URL}/v2/trainers',params={"trainer_id": trainer_id})

def test_status_code(General_response):
    assert General_response.status_code == 200
   
def test_trainer_name(General_response):
    assert General_response.json()["data"][0]["trainer_name"] == "string"
