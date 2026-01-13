# importar para manejo de archivos y sistema
import os
import shutil
import sys

# Importar módulos de tkinter para la selección de carpetas
from tkinter import Tk, filedialog

# importar para manejo de fechas
from datetime import datetime

# importar para obtener el nombre del usuario actual
import getpass

# Cambia la codificación de la consola a UTF-8
sys.stdout.reconfigure(encoding='utf-8')

# Ventana de selección de carpeta
ventana = Tk()
ventana.withdraw()

# Abrir el diálogo para seleccionar la carpeta
ruta = filedialog.askdirectory(title="Selecciona la carpeta que deseas organizar")

# Definir las extensiones de archivo y sus carpetas correspondientes
extensiones = {
    ".jpg": "Imágenes",
    ".png": "Imágenes", 
    ".gif": "Imágenes",
    ".jpeg": "Imágenes",
    ".webp": "Imágenes",
    ".mp3": "Música",
    ".wav": "Música",
    ".mp4": "Videos",
    ".avi": "Videos",
    ".pdf": "PDFs",
    ".docx": "Documentos_Word",
    ".doc": "Documentos_Word",
    ".txt": "Documentos_txt",
    ".exe": "Ejecutables",
    ".orig": "Ejecutables",
    ".zip": "Archivos_comprimidos",
    ".rar": "Archivos_comprimidos",
    ".iso": "Isos",
    ".ova": "Isos"
}

# Obtener el nombre del usuario actual
usuario = getpass.getuser()

# Clasificar archivos
for archivo in os.listdir(ruta):
    
    ruta_archivo = os.path.join(ruta, archivo)
    
    # Verificar si es un archivo
    if os.path.isfile(ruta_archivo):
        nombre, ext = os.path.splitext(archivo)
        ext = ext.lower()

        if ext in extensiones:
            carpeta_destino = extensiones[ext]
            ruta_carpeta = os.path.join(ruta, carpeta_destino)

            # ✅ Crear la carpeta SOLO si se va a usar
            if not os.path.exists(ruta_carpeta):
                os.makedirs(ruta_carpeta)

            #Obtener la fecha de ultima modificacion
            fecha_mod = datetime.fromtimestamp(os.path.getmtime(ruta_archivo))
            # Crear subcarpeta por año-mes
            subcarpeta_fecha = fecha_mod.strftime("%Y-%m")

            # Ruta completa de la subcarpeta por tipo
            carpeta_tipo = os.path.join(ruta, extensiones[ext])
            #ruta completa de la subcarpeta
            carpeta_fecha = os.path.join(carpeta_tipo, subcarpeta_fecha)

            #crear la subcarpeta si no existe
            if not os.path.exists(carpeta_fecha):
                os.makedirs(carpeta_fecha)
            
            # Ruta de destino final del archivo
            destino = os.path.join(carpeta_fecha, archivo)
            
            # Mover el archivo
            shutil.move(ruta_archivo, destino)

            # Registrar el movimiento
            with open(os.path.join(ruta, "registro_organizacion.txt"), "a", encoding="utf-8") as registro:
                registro.write(
                    f"{datetime.now()}: Usuario: {usuario} - archivo movido: "
                    f"'{archivo}' a '{carpeta_destino}'\n"
                )
