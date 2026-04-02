#!/bin/bash

# INSTALACIONES
# sudo apt install rsync
# sudo apt install inotify-tools
# sudo apt install libnotify-bin
# Este script sincroniza los directorios especificados en una unidad USB
# cuando detecta cambios en los directorios de origen.

# Directorio de destino para los respaldos
DEST_DIR="/media/felipe/5A38DA46158C100F/backups"
# DEST_DIR="/run/media/felipe/5A38DA46158C100F/backups"

# Directorios de origen que se respaldarán
SOURCE_DIRS=(
  "$HOME/Documents"
  "$HOME/Music"
  "$HOME/Images"
  "$HOME/Videos"
  "$HOME/zettelkasten"
  "$HOME/Public"
  "$HOME/wallpapers"
  "$HOME/Dropbox"
  "$HOME/Sync"
)

# # Verificar si el disco está montado. Si no, intentar montarlo.
# if ! findmnt -M "$DEST_DIR" >/dev/null; then
#   dunstify "Disco no montado" "Por favor, conecta el disco externo para iniciar la sincronización."
#   mount "$DEST_DIR"
#   if ! findmnt -M "$DEST_DIR" >/dev/null; then
#     dunstify "Error" "No se pudo montar el disco. Abortando script." -u critical
#     exit 1
#   fi
# fi

# Archivo de exclusión
EXCLUDE_FILE="/home/felipe/bin/.rsyncignore"

# Crear el directorio de destino si no existe
mkdir -p "$DEST_DIR"

# Función para sincronizar los directorios
sync_dirs() {
  for SOURCE_DIR in "${SOURCE_DIRS[@]}"; do
    if [ -d "$SOURCE_DIR" ]; then
      echo "Sincronizando $SOURCE_DIR en $DEST_DIR"
      rsync -av --delete --exclude-from="$EXCLUDE_FILE" "$SOURCE_DIR" "$DEST_DIR"
    else
      echo "El directorio de origen $SOURCE_DIR no existe, se omite."
    fi
  done
  echo "Sincronización completada."
  # dunstify "Sincronización completada" "Tus archivos han sido sincronizados."
  notify-send "Sincronización completada" "Tus archivos han sido sincronizados."
}

# Sincronizar una vez al iniciar el script
sync_dirs

# Monitorear cambios en los directorios de origen
while true; do
  # Filtrar solo los directorios que existen para evitar errores en inotifywait
  EXISTING_DIRS=()
  for DIR in "${SOURCE_DIRS[@]}"; do
    if [ -d "$DIR" ]; then
      EXISTING_DIRS+=("$DIR")
    fi
  done

  if [ ${#EXISTING_DIRS[@]} -eq 0 ]; then
    echo "No hay directorios válidos para monitorear. Reintentando en 60s..."
    sleep 60
    continue
  fi

  # Monitorear. Si inotifywait termina con éxito (código 0), ejecutamos la sincronización.
  if inotifywait -r -e modify,create,delete,move "${EXISTING_DIRS[@]}"; then
    sync_dirs
  else
    echo "inotifywait falló o fue interrumpido. Reintentando en 5s..."
    sleep 5
  fi
done
