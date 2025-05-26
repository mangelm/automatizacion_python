import os
import shutil
import sys
from tkinter import Tk, filedialog

# Cambia la codificación de la consola a UTF-8
sys.stdout.reconfigure(encoding='utf-8')

# Ventana de selección de carpeta
ventana = Tk()
ventana.withdraw()
ruta = filedialog.askdirectory(title="Selecciona la carpeta que deseas organizar")

extensiones = {
    "Imágenes": [".jpg", ".png", ".gif", ".jpeg"],
    "Música": [".mp3", ".wav"],
    "Videos": [".mp4", ".avi"],
    "PDFs": [".pdf"],
    "Documentos_Word": [".docx", ".doc"],
    "Documentos_txt": [".txt"],
    "Ejecutables": [".exe", ".orig"],
    "Archivos_comprimidos": [".zip", ".rar"],
    "Isos": [".iso",".ova",".vbox-extpack"],
    "Otros": []
}

# Diccionario para almacenar los archivos por categoría
archivos_por_carpeta = {nombre: [] for nombre in extensiones.keys()}

# Clasificar archivos
for archivo in os.listdir(ruta):
    ruta_archivo = os.path.join(ruta, archivo)
    if os.path.isfile(ruta_archivo):
        nombre, ext = os.path.splitext(archivo)
        ext = ext.lower()
        carpeta_destino = "Otros"
        for carpeta, exts in extensiones.items():
            if ext in exts:
                carpeta_destino = carpeta
                break
        archivos_por_carpeta[carpeta_destino].append(archivo)

# Crear carpetas solo si hay archivos y moverlos
for carpeta, archivos in archivos_por_carpeta.items():
    if archivos:
        ruta_carpeta = os.path.join(ruta, carpeta)
        if not os.path.exists(ruta_carpeta):
            os.makedirs(ruta_carpeta)
            print(f"Carpeta creada: {ruta_carpeta}")

        for archivo in archivos:
            origen = os.path.join(ruta, archivo)
            destino = os.path.join(ruta, carpeta, archivo)
            if os.path.abspath(origen) != os.path.abspath(destino):
                shutil.move(origen, destino)
                print(f"Archivo movido: {archivo} a {carpeta}")
