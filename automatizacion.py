# importar para manejo de archivos y sistema
import os
import shutil
import sys

# importar para manejo de tiempo
import time

# Importar módulos de tkinter para la selección de carpetas
from tkinter import Tk, filedialog

# importar para manejo de fechas
from datetime import datetime

# importar para obtener el nombre del usuario actual
import getpass

# importar para monitoreo de cambios en el sistema de archivos
from watchdog.observers import Observer
# importar para manejar eventos del sistema de archivos
from watchdog.events import FileSystemEventHandler

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

# Función para esperar hasta que un archivo esté libre para ser movido
def esperar_archivo_libre(ruta_archivo, intentos=10, espera=0.5):
    # Intentar abrir el archivo varias veces
    for _ in range(intentos):
        try:
            # Intentar abrir el archivo en modo lectura/escritura
            with open(ruta_archivo, 'rb'):
                return True
        
        # Si no se puede abrir, capturar las excepciones de permiso y esperar
        except (PermissionError , OSError):
            # Esperar antes de intentar de nuevo
            time.sleep(espera)
    return False

# Función para ordenar los archivos
def ordenar_archivos(ruta):
    # Clasificar archivos
    for archivo in os.listdir(ruta):
        
        # Ruta completa del archivo
        ruta_archivo = os.path.join(ruta, archivo)
        
        # Verificar si es un archivo y no el archivo de registro
        if os.path.isfile(ruta_archivo) and archivo != "registro_organizacion.txt":
            
            # Esperar hasta que el archivo esté libre
            if not esperar_archivo_libre(ruta_archivo):
                print(f"No se pudo acceder al archivo: {archivo} porque está en uso.")
                # Si el archivo sigue en uso, saltar al siguiente archivo
                continue
            
            # Obtener la extensión del archivo en minúsculas
            ext = os.path.splitext(archivo)[1].lower()

            # Verificar si la extensión está en el diccionario
            if ext in extensiones:

                carpeta_destino = extensiones[ext]
                ruta_carpeta = os.path.join(ruta, carpeta_destino)

                # Crear la carpeta SOLO si se va a usar
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


# Definir la clase para manejar eventos del sistema de archivos
class ManejadorEventos(FileSystemEventHandler):
    # Método que se ejecuta cuando se crea un archivo
    def on_created(self, evento):
        # Verificar si el evento es la creación de un archivo
        if not evento.is_directory:
            print(f"Nuevo archivo detectado: {evento.src_path}")
            ordenar_archivos(ruta)

# Ordenar los archivos inicialmente al iniciar el script
ordenar_archivos(ruta) 

# Configurar el observador para monitorear la carpeta seleccionada
manejador_eventos = ManejadorEventos()
# instanciar el observador
observador = Observer()
# Agregar la ruta al observador, y que no ordenee subcarpetas porque lo ordenamos en la funcion de antes
observador.schedule(manejador_eventos, ruta, recursive=False)
# Iniciar el observador
observador.start()

print(f"Vigilando la carpeta: {ruta}")
print("Presiona Ctrl+C para detener el programa.")

# Mantener el script en ejecució
try:
    while True:
        # Mantener el script en ejecución
        time.sleep(1)
# Manejar la interrupción del teclado para detener el observador
except (KeyboardInterrupt):
    print("Deteniendo vigilancia")
    # Detener el observador si se interrumpe el script
    observador.stop()

# Esperar a que el observador termine
observador.join()