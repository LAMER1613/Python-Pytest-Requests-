import requests

# 'Content-Type': 'application/json'
# 'trainer_token': token

token = '89e982e933066fa628e8361dd90a47c2'
url_api = 'https://api.pokemonbattle.me:9104'


test1 = requests.post(f'{url_api}/pokemons',
                    headers={'Content-Type': 'application/json',
                             'trainer_token': token},
                    json={"name": "Abubakar",
                          "photo": "https://dolnikov.ru/pokemons/albums/804.png"})
print(test1.text)

test2 = requests.put(f'{url_api}/pokemons',
                    headers={'Content-Type': 'application/json',
                              'trainer_token': token},
                    json={"pokemon_id": "11112",
                          "name": "abubakar ressurecter",
                          "photo": "https://dolnikov.ru/pokemons/albums/911.png"})
print(test2.text)

test3 = requests.post(f'{url_api}/trainers/add_pokeball',
                    headers={'Content-Type': 'application/json',
                               'trainer_token': token},
                    json={"pokemon_id": "6891"})
print(test3.text)