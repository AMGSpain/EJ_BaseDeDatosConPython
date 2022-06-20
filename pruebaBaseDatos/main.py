import json

with open('baseDeDatosJSON') as file:
    data = json.load(file)
    #dataDump = json.dumps(file)

entrada = input("¿Eres un usuario nuevo?: ")


def userCheck(password,nombre):
    if passwordInput == password:
        print("Bienvenido",nombre)
    else:
        print("Password Erroneo.")

def registro():
    userName = input("Elige un nombre de Usuario: ")
    password = input("Elige un Password: ")
    nombre = input("¿Cual es tu nombre?: ")
    edad = int(input("¿Cual es tu edad?: "))
    altura = float(input("¿Cual es tu altura?: "))
    
    data['user'].append({
        'userName' : userName,
        'password' : password,
	    'nombre' : nombre,
	    'edad' : edad,
	    'altura' : altura
    })
    
    if edad >= 18:
        print("Hola",nombre,"te has registrado como usuario con:", userName)
        with open("baseDeDatosJSON", "w") as json_file:
            json.dump(data, json_file)
    else:
        print("Eres menor de edad")
        
if entrada.lower() == "si":
    registro()
else:
    userInput = input("¿Cual es tu nombre de usuario?: ")
    passwordInput = input("¿Cual es tu password?: ")
    
    for user in data['user']:
        userName = user['userName']  
        password = user['password']
        nombre = user['nombre']
        if userInput == userName:
            print("Hola",userName)
            userCheck(password,nombre)
            break
    else:
        print("El usuario no esta registrado.")
    

