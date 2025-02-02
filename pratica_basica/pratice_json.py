import json
import os

# Crear un archivo JSON con una lista de diccionarios
datos_a_guardar = [
    {"nombre": "Juan", "apellido": "Perez", "edad": 25},
    {"nombre": "Maria", "apellido": "Gomez", "edad": 30},
    {"nombre": "Jose", "apellido": "Garcia", "edad": 45},
    {"nombre": "Ana", "apellido": "Gutierrez", "edad": 35}
]

# Guardar los datos en el archivo JSON
with open("data.json", "w") as f:
    json.dump(datos_a_guardar, f)  # Guarda la lista completa
    print("Archivo creado correctamente.")

# Verificar si el archivo existe
if not os.path.exists('data.json'):
    print('El archivo "data.json" no existe.')
    exit()

# Leer el archivo JSON
try:
    with open('data.json', "r") as archivo:
        datos = json.load(archivo)
        print("El archivo fue leído correctamente.")
except json.JSONDecodeError:
    print("Error: El archivo no tiene un formato JSON válido.")
    exit()
except Exception as e:
    print(f"Error inesperado: {e}")
    exit()

# Procesar los datos
if isinstance(datos, list):  # Verificar si es una lista
    for item in datos:  # Iterar sobre cada diccionario en la lista
        print("\n---")
        for clave, valor in item.items():  # Iterar sobre cada clave-valor del diccionario
            print(f"{clave}: {valor}")
else:
    print("El archivo JSON no contiene una lista de objetos.")