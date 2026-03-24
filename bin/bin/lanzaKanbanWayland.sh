#!/usr/bin/env sh

ls ~/Dropbox/kanban -I done -I algun_dia -I README.md | wofi -show -dmenu -i | xargs -I_ terminator -e taskell ~/Dropbox/kanban/_
