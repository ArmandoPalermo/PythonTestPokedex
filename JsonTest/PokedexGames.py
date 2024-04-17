'''
Created on 27 set 2023

@author: Armando
'''
import random 
from _overlapped import NULL

class PokedexGames:
    def __init__(self, jsonFileConverted):
        self.jsonf = jsonFileConverted
        
       
    def FindPokemonNumber(self, idEstratto,nomePokemon):
        find = 2
        
        for i in self.jsonf:
            nPokemon = i['name']['english']
            if nPokemon.lower() == nomePokemon.lower():
                find = 0
                
        for i in self.jsonf:
            
            nPokemon = i['name']['english']
            currentId = i['id']
            
            
            if nPokemon.lower() == nomePokemon.lower() and str(idEstratto) == str(currentId):
                find = 1
        
                
        return find
        
    
        
        
    def GuessThePokemonByNumber(self):
        extractedPokemon = random.choice(self.jsonf)
        extractedId = str(extractedPokemon['id'])
        print('Indovina il pokemon che ha questo Id nel pokedex : '+ extractedId)
        playerGuess = input()
        
        if  self.FindPokemonNumber(extractedId,playerGuess) == 1:
            print('Bravo hai indovinato!!!')
        elif self.FindPokemonNumber(extractedId, playerGuess) == 2:
            print('il pokemon che hai inserito non esiste :(')
        else:
            print('sbagliatoo')
        
        
        
        
    def GuessThePokemonByTyping(self):
        extractedPokemon = random.choice(self.jsonf) # Ho estratto una riga intera dal json
        extractedType = extractedPokemon["type"]
        extractedName = extractedPokemon["name"]["english"] 
        extractedId = str(extractedPokemon['id'])
        
        types = '-'.join(extractedType)
    
        print('Indovina il pokemon che ha questo/i tipi : ' + types)
        playerGuess = input()
        
        if playerGuess.lower() == extractedName.lower() :
            print('Bravo, hai indovinato!!!') 
        else:
            print('Ultima possibilità. Suggerimento : il suo id nel pokedex è ' + extractedId)
            
        playerGuess = input()
        
        if playerGuess.lower() == extractedName.lower() :
            print('Bravo, hai indovinato!!!')
        else: 
            print('Hai sbagliato :( , era ' + extractedName)
        
         
        