#!/usr/bin/env sh

ls ~/dev/ | rofi -show -dmenu -i | xargs -I_ kitty -e lvim ~/dev/_
