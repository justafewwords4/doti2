#!/usr/bin/env sh

ls ~/sites | rofi -show -dmenu -i | xargs -I_ code ~/sites/_
