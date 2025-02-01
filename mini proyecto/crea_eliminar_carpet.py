import os,shutil

crear_carpeta = "PythonGamer"
os.mkdir("C:/Users/ROBER/Desktop/PythonGamer")
print(f"Carpeta creada con éxito {crear_carpeta}")

# Crear carpeta con ruta

crear_carpeta  = "C:/Users/ROBER/Desktop/"
 
if os.path.exists("C:/Users/ROBER/Desktop/PythonGamer"):
    for archivo in os.listdir(crear_carpeta):
        print("El archivo es: encontrado ", archivo)
        
else:
    print("La ruta no existe")
        
    
    print("************************************************************************")
    
# Crear carpeta con ruta
    
if os.path.exists("C:/Users/ROBER/Desktop/PythonGamer"):
    print("La ruta existe")
else:
    print("La ruta no existe")
    
    print("************************************************************************")
    
    

# Eliminar carpeta
    
eliminar_carpeta = "C:/Users/ROBER/Desktop/PythonGamer"    

if os.path.exists(eliminar_carpeta):
    try:
        shutil.rmtree(eliminar_carpeta)
        print("Carpeta eliminada con éxito")
    except Exception as e:
        print("Error al eliminar la carpeta", e)
else:
    print("La carpeta no existe")        

