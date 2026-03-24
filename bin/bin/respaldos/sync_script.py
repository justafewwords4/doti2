#!/usr/bin/env python3
import os
import subprocess
import time
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# --- CONFIGURACIÓN ---
# 1. Lista de directorios a monitorear (equivalente a WATCH_DIRS en bash)
WATCH_DIRS = [
    "/home/felipe/zettelkasten/",
    "/home/felipe/Documents/",
    "/home/felipe/Videos/",
    "/home/felipe/Music/",
    "/home/felipe/Pictures/",
    "/home/felipe/Public/",
]

# 2. Directorio raíz donde se guardarán todos los respaldos (equivalente a BACKUP_PARENT_DIR)
BACKUP_PARENT_DIR = "/media/felipe/5A38DA46158C100F/backups/"

# 3. (Opcional) Segundos a esperar después de detectar un cambio antes de iniciar rsync.
#    Esto ayuda a agrupar múltiples cambios rápidos en una sola operación de respaldo.
DEBOUNCE_SECONDS = 10

# --- LÓGICA DEL SCRIPT ---

# Usamos un threading.Event para comunicar de forma segura que "un cambio ha ocurrido"
# desde el hilo del observador de archivos al hilo principal del script.
change_detected_event = threading.Event()


class ChangeHandler(FileSystemEventHandler):
    """Un manejador de eventos simple que simplemente activa nuestro Event cuando algo sucede."""

    def on_any_event(self, event):
        # Ignoramos los eventos que ocurren en el propio directorio de respaldo para evitar bucles.
        if not event.src_path.startswith(BACKUP_PARENT_DIR):
            # print(f"-> Evento detectado: {event.event_type} en {event.src_path}")
            change_detected_event.set()


def run_full_sync():
    """
    Ejecuta rsync para cada directorio monitoreado.
    Esta función es el equivalente al bucle 'for' dentro de tu script de bash.
    """
    print(f"\n[{time.ctime()}] Se detectó un cambio. Iniciando respaldo...")

    for watch_dir in WATCH_DIRS:
        # Asegurarse de que el directorio de origen exista antes de intentar sincronizar
        if not os.path.isdir(watch_dir):
            print(
                f"  - [Advertencia] El directorio de origen no existe, omitiendo: {watch_dir}"
            )
            continue

        # Extraer el nombre base del directorio (ej: /home/user/Docs/ -> Docs)
        # os.path.normpath se asegura de que se manejen las barras finales (/)
        target_subdir_name = os.path.basename(os.path.normpath(watch_dir))
        backup_dest_path = os.path.join(BACKUP_PARENT_DIR, target_subdir_name)

        # La barra final en el origen es importante para que rsync copie el *contenido* del directorio
        source_path = os.path.join(watch_dir, "")

        print(f"  - Sincronizando: {source_path} -> {backup_dest_path}")

        try:
            # Ejecutar el comando rsync.
            # -a: modo archivo (recursivo, preserva permisos, etc.)
            # --delete: borra archivos en el destino que ya no están en el origen.
            subprocess.run(
                ["rsync", "-a", "--delete", source_path, backup_dest_path],
                check=True,  # Lanza una excepción si rsync devuelve un error
                capture_output=True,  # No mostrar la salida de rsync a menos que haya un error
                text=True,
            )
        except subprocess.CalledProcessError as e:
            print(f"  - [ERROR] rsync falló para {watch_dir}.")
            print(f"  - Salida de error: {e.stderr}")
        except FileNotFoundError:
            print(
                "  - [ERROR] No se encontró el comando 'rsync'. Asegúrate de que esté instalado y en tu PATH."
            )
            # Si rsync no se encuentra, no tiene sentido continuar.
            return False

    print(f"[{time.ctime()}] Respaldo completado. Esperando nuevos cambios.")
    return True


if __name__ == "__main__":
    # --- CONFIGURACIÓN INICIAL ---
    # Crear el directorio principal de respaldo si no existe
    os.makedirs(BACKUP_PARENT_DIR, exist_ok=True)
    # Crear los directorios a monitorear si no existen (mismo comportamiento que el script bash)
    for directory in WATCH_DIRS:
        os.makedirs(directory, exist_ok=True)

    print("--- Script de Respaldo Automático con rsync ---")
    print("\nMonitoreando los siguientes directorios:")
    for directory in WATCH_DIRS:
        print(f" - {directory}")
    print(f"\nLos respaldos se guardarán en: {BACKUP_PARENT_DIR}")
    print("Presiona Ctrl+C para detener el script.")

    # --- INICIAR MONITOREO ---
    event_handler = ChangeHandler()
    observer = Observer()
    for directory in WATCH_DIRS:
        if os.path.isdir(directory):
            observer.schedule(event_handler, directory, recursive=True)
        else:
            print(f"\n[Advertencia] El directorio a monitorear no existe: {directory}")

    observer.start()

    # Realizar una sincronización inicial al arrancar el script
    print("\nRealizando sincronización inicial...")
    if not run_full_sync():
        observer.stop()  # Detener si rsync no fue encontrado
        observer.join()
        exit(1)

    # --- BUCLE PRINCIPAL ---
    try:
        while True:
            # 1. El hilo principal se bloquea aquí hasta que el ChangeHandler llame a .set()
            change_detected_event.wait()

            # 2. Debounce: una vez detectado un cambio, espera un poco más.
            #    Si ocurren más cambios en este tiempo, el evento seguirá seteado, pero
            #    solo ejecutaremos rsync una vez.
            print(
                f"\n[{time.ctime()}] Cambio detectado. Esperando {DEBOUNCE_SECONDS}s por si hay más cambios..."
            )
            time.sleep(DEBOUNCE_SECONDS)

            # 3. Limpiar el evento y ejecutar la sincronización.
            change_detected_event.clear()
            run_full_sync()

    except KeyboardInterrupt:
        print("\n\nSe recibió interrupción (Ctrl+C). Deteniendo el monitoreo...")
    finally:
        observer.stop()
        observer.join()
        print("Monitoreo detenido. Adiós.")
