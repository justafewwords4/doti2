#!/usr/bin/env sh

ls ~/sites | wofi -show -dmenu -i | xargs -I_ code ~/sites/_
