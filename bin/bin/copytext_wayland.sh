#!/usr/bin/env sh

DIRECTORIO="/home/felipe/tmp/"
IMAGE="image.png"
OUTPUT="output"

# Aseguramos que el directorio temporal existe
mkdir -p "${DIRECTORIO}"

# 1. Seleccionar región con slurp y capturar con grim
grim -g "$(slurp)" "${DIRECTORIO}${IMAGE}"

# 2. OCR con Tesseract (puedes añadir '-l spa' si el texto es español)
tesseract "${DIRECTORIO}${IMAGE}" "${DIRECTORIO}${OUTPUT}"

# 3. Limpiar saltos de línea y copiar al portapapeles de Wayland (wl-copy)
cat "${DIRECTORIO}${OUTPUT}.txt" | wl-copy

# 4. Limpieza de archivos temporales
rm "${DIRECTORIO}${IMAGE}"
rm "${DIRECTORIO}${OUTPUT}.txt"
