import csv
import os


# Escribir en un archivo csv

with open("nuevo.csv", "w") as f:
    escritor = csv.writer(f)
    escritor.writerow(["nombre ", "apellido ", "edad "])
    escritor.writerow(["Juan", "Perez", 25])
    escritor.writerow(tuple([["Maria", "Gomez", 30], ["Jose", "Garcia", 45]]))
    print(escritor.__str__())
    
 # Leer el archivo   
    
with open("nuevo.csv", "r") as f:
    lector = csv.reader(f)
    for linea in lector:
        print(linea)    
    
    
#elimar el archivo

if os.path.exists("nuevo2.csv"):
    os.remove("nuevo2.csv")
    print("Archivo eliminado")
else:
    print("El archivo no existe")
    
    
print("Fin del programa")

