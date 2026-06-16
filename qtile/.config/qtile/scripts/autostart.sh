#!/bin/sh

# polkit
lxpolkit &

# background
feh --bg-fill /home/drew/.config/qtile/wallpaper/wallhaven-218x7m_3440x1440.png &

# GTK live theme updates
xsettingsd &

# compositor
picom --config ~/.config/qtile/picom/picom.conf -b &

# Notifications
dunst -config ~/.config/qtile/dunst/dunstrc &

nm-applet &
# mis agregados
blueman-applet &
# flatpak run com.rtosta.zapzap &
# whatsie &
brave-browser --app=https://web.whatsapp.com/ &
brave-browser --app=https://chat.google.com/app/home &
~/Telegram/Telegram &
emacs --daemon &
udiskie &
~/bin/backup.sh &
localsend_app --hidden &
# flatpak run org.localsend.localsend_app &
# First-login welcome (shown once, dismissable)
if [ ! -f "$HOME/.cache/qtile/welcomed" ]; then
  mkdir -p "$HOME/.cache/qtile"
  touch "$HOME/.cache/qtile/welcomed"
  (
    sleep 3
    notify-send -u normal -t 15000 \
      "Welcome to Qtile" \
      "Press Super + / anytime to see all keybindings.&#10;See ~/QUICKSTART-qtile.md for a cheat sheet."
  ) &
fi
