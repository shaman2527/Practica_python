# Objetivo: mostrar la escritura de archivos de texto en python

with open("nuevo.txt", "w") as f:
    f.write("Hola mundo\n")
    f.write("Adios mundo\n")
    f.write("Hola de nuevo\n")
    f.writelines(["Hola mundo\n", "Adios mundo\n", "Hola de nuevo\n"])
    print("El archivo se ha creado")
    
    
    #verificamos si el archivo existe
    
    import os
    if os.path.exists("nuevo.txt"):
        print("El archivo existe")
        
# os.rename("nuevo.txt", "nuevo2.txt")

if os.path.exists("nuevo.txt"):
    os.remove("nuevo.txt")
    print("El archivo fue eliminado")        
    