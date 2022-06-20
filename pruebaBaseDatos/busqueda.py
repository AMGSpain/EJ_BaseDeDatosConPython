import json

with open('baseDeDatosJSON') as file:
    data = json.load(file)
    
    
for user in data['user']:
    altura = user['altura']
    nombre = user['nombre']
    while altura >= 1.0:
        print(f"{nombre} es humano.")
        break