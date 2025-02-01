import os

carpeta = r"C:\Users\ROBER\Pictures\img"  # Ruta corregida
contador = 1

for archivo in os.listdir(carpeta):
    if archivo.lower().endswith(".jpg"):  # Aseguramos que detecte .JPG, .jPg, etc.
        nuevo_nombre = f"foto_{contador:03d}.jpg"
        # Renombramos el archivo
        os.rename(
            os.path.join(carpeta, archivo),
            os.path.join(carpeta, nuevo_nombre)
        )
        contador += 1

print("¡Archivos renombrados con éxito!")