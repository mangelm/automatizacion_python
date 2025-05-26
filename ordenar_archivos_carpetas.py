import os
import shutil
import sys

# Cambia la codificación de la consola a UTF-8
sys.stdout.reconfigure(encoding='utf-8')

#Ruta de la carpeta que deseas organizar
ruta = "C:/Users/Flor/Downloads/Nueva_carpeta"

#Crear carpetas en destino si no existen
#tipos = ["Documentos", "Imágenes", "Música", "Videos", "PDFs","Documentos_Word","Documentos_txt","Ejecutables","Archivos_comprimidos"]

extensiones = {
    "Imágenes": [".jpg", ".png", ".gif", ".jpeg"],
    "Música": [".mp3", ".wav"],
    "Videos": [".mp4", ".avi"],
    "PDFs": [".pdf"],
    "Documentos_Word": [".docx", ".doc"],
    "Documentos_txt": [".txt"],
    "Ejecutables": [".exe", ".orig"],
    "Archivos_comprimidos": [".zip", ".rar"],
    "Ejecutables": [".exe", ".orig"],
    "Otros": []
}

#Creacion de carpetas
# for carpeta in tipos:
#     ruta_carpeta = os.path.join(ruta, carpeta)
    
    
#     if not os.path.exists(ruta_carpeta):
#         os.makedirs(ruta_carpeta)
#         print(f"Carpeta creada: {ruta_carpeta}")

for carpeta in extensiones.keys():
    ruta_carpeta = os.path.join(ruta, carpeta)
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)
        print(f"Carpeta creada: {ruta_carpeta}")
#Ordenar archivos
for archivo in os.listdir(ruta):

    # if archivo.endswith(".jpg") or archivo.endswith(".png") or archivo.endswith(".gif") or archivo.endswith(".jpeg"):
    #     #De la carpeta de origen a la carpeta de destino
    #     shutil.move(os.path.join(ruta, archivo), os.path.join(ruta, "Imágenes", archivo))
    #     print(f"Archivo movido: {archivo} a Imágenes")

    # elif archivo.endswith(".mp3") or archivo.endswith(".wav"):
    #     shutil.move(os.path.join(ruta, archivo), os.path.join(ruta, "Música", archivo))
    #     print(f"Archivo movido: {archivo} a Música")

    # elif archivo.endswith(".mp4") or archivo.endswith(".avi"):
    #     shutil.move(os.path.join(ruta, archivo), os.path.join(ruta, "Videos", archivo))
    #     print(f"Archivo movido: {archivo} a Videos")

    # elif archivo.endswith(".pdf"):
    #     shutil.move(os.path.join(ruta, archivo), os.path.join(ruta, "PDFs", archivo))
    #     print(f"Archivo movido: {archivo} a PDFs")
    
    # elif archivo.endswith(".docx") or archivo.endswith(".doc"):
    #     shutil.move(os.path.join(ruta, archivo), os.path.join(ruta, "Documentos_Word", archivo))
    #     print(f"Archivo movido: {archivo} a Documentos_Word")

    # elif archivo.endswith(".txt"):
    #     shutil.move(os.path.join(ruta, archivo), os.path.join(ruta, "Documentos_txt", archivo))
    #     print(f"Archivo movido: {archivo} a Documentos_txt")

    # elif archivo.endswith(".exe") or archivo.endswith(".orig"): 
    #     shutil.move(os.path.join(ruta, archivo), os.path.join(ruta, "Ejecutables", archivo))
    #     print(f"Archivo movido: {archivo} a Ejecutables")

    # elif archivo.endswith(".zip") or archivo.endswith(".rar"):
    #     shutil.move(os.path.join(ruta, archivo), os.path.join(ruta, "Archivos_comprimidos", archivo))
    #     print(f"Archivo movido: {archivo} a Archivos_comprimidos")

    ruta_archivo = os.path.join(ruta, archivo)

    if os.path.isfile(ruta_archivo):  # Verifica si es un archivo
        # Obtener la extensión del archivo
        nombre,ext= os.path.splitext(archivo)
        ext= ext.lower()
        carpeta_destino = "Otros" 
        
        for carpeta, exts in extensiones.items():
            if ext in exts:
                carpeta_destino = carpeta
        destino = os.path.join(ruta, carpeta_destino, archivo)
        # Evita mover archivos que ya están en la carpeta destino
        if os.path.abspath(ruta_archivo) != os.path.abspath(destino):
            shutil.move(ruta_archivo, destino)
            print(f"Archivo movido: {archivo} a {carpeta_destino}")