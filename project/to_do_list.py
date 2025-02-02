import tkinter as tk
from tkinter import messagebox

tk.Tk().withdraw()
messagebox.showinfo("Bienvenido", "Bienvenido a la lista de tareas")



tareas = []

# funcion para mostrar el menu

def mostrar_menu():
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Salir")
    
    
    

# Funcion para ver tareas
def ver_tareas():
    if not tareas:
        print("no hay tareas")
    else:
        print("Tareas:")
        for i, tarea in enumerate(tareas, 1):
            estado = "✓" if tarea["completada"] else "✗"
            print(f"{i}. [{estado}] {tarea['descripcion']}")
            
                
            
# funcion para agregar tarea

def agregar_tarea():
    descripcion = input("Descripcion de la tarea: ")
    tarea = ({"descripcion": descripcion, "completada": False})
    tareas.append(tarea)
    print(f"La tarea '{descripcion}' ha sido agregada")
    
    
    
    
# funcion para eliminar tarea

def eliminar_tarea():
    ver_tareas()
    try:
        indice = int(input("Ingrese el numero de la tarea a eliminar: ")) - 1
        if 0<= indice < len(tareas):
            tarea_eliminada = tareas.pop(indice)
            print(f"La tarea '{tarea_eliminada['descripcion']}' ha sido eliminada")
        else:
            print("Numero de tarea invalido")
    except ValueError:
        print("Numero de tarea invalido")
        
        
        
# Bucle principal del programa

print("Bienvenido a la lista de tareas")
print(mostrar_menu())

while True:
    mostrar_menu
    opcion = input("Seleccione una opcion: ")
    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        ver_tareas()
    elif opcion == "3":
        eliminar_tarea()
    elif opcion == "4":
        break
    else:
        print("Opcion invalida")  
        
                            