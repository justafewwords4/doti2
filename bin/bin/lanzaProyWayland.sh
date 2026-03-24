#!/usr/bin/env sh

ls ~/dev/ | wofi -show -dmenu -i | xargs -I_ code ~/dev/_
