#!/bin/bash

# Nombre del monitor interno de la laptop
IN="eDP-1"

# Encuentra el primer monitor externo conectado
# Esto hace el script más robusto si el nombre del puerto cambia (ej. de HDMI-1 a HDMI-2)
EXT=$(xrandr | grep " connected" | grep -v "^$IN" | head -n 1 | cut -d ' ' -f 1)

# Si no se encuentra un monitor externo, simplemente activa el monitor interno y sale.
if [ -z "$EXT" ]; then
  xrandr --output "$IN" --auto --primary
  exit 0
fi

# Verifica si el monitor interno está actualmente activo (tiene una resolución asignada)
# El patrón [0-9]x[0-9] busca algo como "1920x1080".
if xrandr | grep "^$IN" | grep -q "[0-9]x[0-9]"; then
  # Si el monitor interno está ACTIVO, lo apaga y enciende el externo.
  xrandr --output "$IN" --off --output "$EXT" --auto --primary
else
  # Si el monitor interno está INACTIVO, lo enciende y apaga el externo.
  xrandr --output "$IN" --auto --primary --output "$EXT" --off
fi

# Establecer un fondo de pantalla aleatorio utilizando feh
feh --randomize --bg-fill ~/wallpapers/*
