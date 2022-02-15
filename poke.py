import requests
pokeNum = 1
pokeWeights = {}
# res = requests.get('https://pokeapi.co/api/v2/pokemon/'+str(1))
# pokemon = res.json()
# print(pokemon)

for i in range(1,20):
  res = requests.get('https://pokeapi.co/api/v2/pokemon/'+str(i))
  pokemon = res.json()
  name = pokemon['forms'][0]['name']
  weight = pokemon['weight']
  pokeWeights[name] = weight
  print(name, weight)

print(pokeWeights)
