from datetime import datetime

class Libro:
    def __init__(self, titulo):
        self.titulo = titulo

    def __str__(self):
        return self.titulo


class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre


class Prestamo:
    def __init__(self, libro, usuario):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = datetime.now()

    def __str__(self):
        return f"Préstamo: {self.libro} a {self.usuario} el {self.fecha_prestamo}"


class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []  # Lista de libros disponibles
        self.usuarios = []  # Lista de usuarios registrados
        self.prestamos = []  # Lista de préstamos activos

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro}' agregado a la biblioteca '{self.nombre}'.")

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"Usuario '{usuario}' registrado en la biblioteca '{self.nombre}'.")

    def prestar_libro(self, libro, usuario):
        if libro in self.libros and usuario in self.usuarios:
            prestamo = Prestamo(libro, usuario)
            self.prestamos.append(prestamo)
            self.libros.remove(libro)  # El libro ya no está disponible
            print(f"Préstamo registrado: {prestamo}")
        else:
            print(f"No se puede prestar. Verifica que el libro y el usuario estén registrados.")

    def devolver_libro(self, libro, usuario):
        for prestamo in self.prestamos:
            if prestamo.libro == libro and prestamo.usuario == usuario:
                self.prestamos.remove(prestamo)
                self.libros.append(libro)  # El libro está disponible nuevamente
                print(f"Devolución registrada: {libro} devuelto por {usuario}.")
                return
        print(f"No se encontró un préstamo activo de {libro} a {usuario}.")
        
        
    def listar_prestamos(self):
        if not self.prestamos:
            print("No hay préstamos activos en este momento.")
        else:
            print("Préstamos activos:")
            for prestamo in self.prestamos:
                print(prestamo)
        
    #Buscar libro
    def buscar_libro(self, titulo):
        # Buscar en libros disponibles
        for libro in self.libros:
            if libro.titulo == titulo:
                print(f"Libro encontrado: {libro} (disponible).")
                return
            
            
# Crear objetos
libro1 = Libro("Python3 con Inteligencia Artificial")
libro2 = Libro("Python3 con Machine Learning")
usuario = Usuario("Roberth Silva")
biblioteca = Biblioteca("Biblioteca Central")

# Agregar libros y usuarios a la biblioteca
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_usuario(usuario)

# Prestar y devolver libros
biblioteca.prestar_libro(libro1, usuario)
biblioteca.devolver_libro(libro1, usuario)
# Listar préstamos
biblioteca.listar_prestamos()

# Buscar libros
biblioteca.buscar_libro("Python3 con Inteligencia Artificial")
biblioteca.buscar_libro("Python3 con Machine Learning")


biblioteca.prestar_libro(libro2, usuario)
print(len(biblioteca.libros))
