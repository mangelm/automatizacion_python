import os
import shutil

#Ruta de la carpeta que deseas organizar
ruta = "C:/Users/Flor/Downloads/Nueva_carpeta"

#Crear carpetas en destino si no existen
tipos = ["Documentos", "Imágenes", "Música", "Videos", "PDFs","Documentos_Word","Documentos_txt"]

for carpeta in tipos:
    ruta_carpeta = os.path.join(ruta, carpeta)
    
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)
        print(f"Carpeta creada: {ruta_carpeta}")