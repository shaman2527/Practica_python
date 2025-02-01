class Perro:
    # Atributos (se define en la Constructor __init__)
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
       
     # Metodos
    def ladrar(self):
        print(f"{self.nombre} dice: Guau, guau")
        
        
# Crear un objeto (instanciar la clase)

mi_perro = Perro("Rex", 3)
mi_perro.ladrar()           
        