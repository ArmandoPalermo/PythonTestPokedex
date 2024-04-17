import json
import os
from JsonTest.PokedexGames import PokedexGames

absolute_path = os.path.dirname(__file__)
relative_path = "..\\Risorse\\pokedex.json"
full_path = os.path.join(absolute_path, relative_path)

with open(full_path) as json_file :
    pokedex = json.load(json_file)

gioco = PokedexGames(pokedex)
print('Scegli il minigioco a cui vuoi giocare: ')
print('1) Trova il Pokemon dal numero del Pokedex')
print('2) Indovina il Pokemon dal Tipo')
scelta = input()
print(scelta)
if scelta == '1':
    gioco.GuessThePokemonByNumber()
else:
    gioco.GuessThePokemonByTyping()