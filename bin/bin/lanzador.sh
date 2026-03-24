#!/usr/bin/env sh

DIR="$HOME/.config/openbox-themes"
STYLE="bouquet"
RASI="$DIR/themes/$STYLE/rofi/launcher.rasi"

OUPUT=$(printf "Kanban\nProyectos\nSites\nFinances\nWiki" | rofi -show -dmenu -i -theme ${RASI})

echo "$OUPUT"

case $OUPUT in

Kanban)
	~/bin/lanzaKanban.sh
	;;
Proyectos)
	~/bin/lanzaProy.sh
	;;
Sites)
	~/bin/lanzaSites.sh
	;;
Finances)
	kitty -d /home/felipe/dev/finanzas/ -e /home/felipe/bin/finances.sh
	;;
Wiki)
	kitty -d /home/felipe/vimwiki/index.wiki -e nvim /home/felipe/vimwiki/index.wiki
	;;

esac
