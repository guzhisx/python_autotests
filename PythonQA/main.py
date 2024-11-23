import requests

URL = 'https://api.pokemonbattle.ru'
Token = 'f017ba797b5525259cdd41e0cd4cdbc4'
Header = {'Content-Type': 'application/json', 'trainer_token':Token}
trainer_id = 11701
body_CreatePok = {
    "name": "pytest",
    "photo_id": 111
}
body_put = {
    "pokemon_id": "",
    "name": "PytestNew",
    "photo_id": 111
}

#Отправил запрос на создание покемона
response_create = requests.post(f'{URL}/v2/pokemons',headers=Header, json = body_CreatePok)
pokemon_id = response_create.json()['id']
print(f'Сохранил айдишник: {pokemon_id}, А вот весь ответ: {response_create.json()}\n')

#Добавил id созданного покемона в тело запроса
body_put["pokemon_id"] = pokemon_id
body_add_pokeball = {"pokemon_id": body_put["pokemon_id"]}

#Запрос на изменение имени
response_put = requests.put(f'{URL}/v2/pokemons', headers=Header, json = body_put)
print(f'Изменили имя. Ответ от сервера: {response_put.json()}\n')

#Запрос на добавление в покебол
response_pokeball = requests.post(f'{URL}/v2/trainers/add_pokeball',headers=Header, json = body_add_pokeball)
print (f'Добавили в покебол. Ответ от сервера: {response_pokeball.json()}')
