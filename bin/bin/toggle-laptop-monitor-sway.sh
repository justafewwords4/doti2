#!/bin/bash

# Este script es para Sway (Wayland) y gestiona la alternancia entre monitor interno y externo.
# Optimizado para Sway 1.10.1 y versiones que entregan salida en JSON.

# Nombre del monitor interno de la laptop
IN="eDP-1"

# Obtenemos la información de las salidas una sola vez para mayor eficiencia
OUTPUTS=$(swaymsg -t get_outputs)

# 1. Buscamos el nombre del primer monitor que NO sea el interno ($IN).
EXT=$(echo "$OUTPUTS" | jq -r ".[] | select(.name != \"$IN\") | .name" | head -n 1)

# REQUISITO 1: Si no se encuentra un monitor externo (está vacío), no hacemos nada y salimos.
if [ -z "$EXT" ]; then
  exit 0
fi

# 2. Verificamos si el monitor EXTERNO está actualmente activo.
IS_EXT_ACTIVE=$(echo "$OUTPUTS" | jq -r ".[] | select(.name == \"$EXT\") | .active")

# REQUISITO 2: Lógica de alternancia (Toggle)
if [ "$IS_EXT_ACTIVE" = "true" ]; then
  # Si el monitor externo está ACTIVO, lo apaga y enciende el interno.
  swaymsg "output '$EXT' disable"
  swaymsg "output '$IN' enable"
  TARGET="$IN"
else
  # Si el monitor externo está INACTIVO (o apagado), lo enciende y apaga el interno.
  swaymsg "output '$IN' disable"
  swaymsg "output '$EXT' enable"
  TARGET="$EXT"
fi

# --- Gestión de mako (notificaciones) ---
# Matamos mako para asegurar que se reinicie en la salida (output) correcta
pkill mako || true
mako --output "$TARGET" &

# --- Gestión del fondo de pantalla ---
# Matamos cualquier instancia previa de swaybg
pkill swaybg || true

# Seleccionamos una imagen aleatoria si el directorio existe
if [ -d "$HOME/wallpapers" ]; then
  WALLPAPER=$(find "$HOME/wallpapers" -type f | shuf -n 1)
  if [ -n "$WALLPAPER" ]; then
    swaybg -i "$WALLPAPER" -m fill &
  fi
fi
