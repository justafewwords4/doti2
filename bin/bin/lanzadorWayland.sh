#!/usr/bin/env sh

OUPUT=$(printf "Kanban\nProyectos\nSites" | wofi -show -dmenu -i)

echo "$OUPUT"

case $OUPUT in

  Kanban)
    ~/bin/lanzaKanbanWayland.sh
    ;;
  Proyectos)
    ~/bin/lanzaProyWayland.sh
    ;;
  Sites)
    ~/bin/lanzaSitesWayland.sh
    ;;

esac
