import os
import random


def random_images():
    directorio = os.getcwd()
    # Listar todos los archivos en el directorio
    archivos = os.listdir(directorio)

    # Filtrar solo los archivos con extensión .png
    imagenes_png = [
        archivo for archivo in archivos if archivo.endswith('.png')]

    # Comprobar si hay imágenes PNG en el directorio
    if not imagenes_png:
        print("No se encontraron imágenes PNG en el directorio.")
        return None

    # Seleccionar una imagen aleatoria
    imagen_seleccionada = random.choice(imagenes_png)
    return imagen_seleccionada


if __name__ == "__main__":

    # Definir el directorio actual
    imagen_aleatoria = random_images()

    if imagen_aleatoria:
        print(f"Imagen seleccionada aleatoriamente: {imagen_aleatoria}")
