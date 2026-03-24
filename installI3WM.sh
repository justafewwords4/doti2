#!/usr/bin/bash

# install main components

sudo apt install xorg i3-wm i3status i3lock -y

# instalar aplicaciones esenciales

sudo apt install feh maim xclip wget curl git pipx \
  python3-pip timeshift thunar network-manager blueman pavucontrol \
  brightnessctl btop dunst mate-polkit mesa-vulkan-drivers mesa-utils \
  pipewire pipewire-audio wireplumber redshift -y

# Install and get flatpak ready for you fav apps

sudo apt install flatpak -y
flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo -y

# instalar fuentes

sudo apt install fonts-dejavu fonts-noto fonts-noto-color-emoji fonts-font-awesome -y

# copiar wallpapers

sudo cp ~/i3wm_files/assets/wallpapers/*.jpg /usr/share/wallpapers/

# Install Assets & fonts (for those `cp` step make sure you `cd` in debian_i3 folder first)

sudo apt install fonts-dejavu fonts-noto fonts-noto-color-emoji fonts-font-awesome -y

# Install Basic Fonts
sudo apt install fonts-dejavu fonts-noto fonts-noto-color-emoji fonts-font-awesome -y

# Install `FontAwesome 7` that use for **Polybar icons**

sudo mkdir -p /usr/share/fonts/fontawesome-7/
sudo cp ~/i3wm_files/assets/fontawesome-free-7.0.0-desktop/*.otf /usr/share/fonts/fontawesome-7/
sudo fc-cache -f -v

# Install JetBrain Nerd Font for rofi theme

wget -P ~/.local/share/fonts https://github.com/ryanoasis/nerd-fonts/releases/download/v3.0.2/JetBrainsMono.zip
cd ~/.local/share/fonts
unzip JetBrainsMono.zip
rm JetBrainsMono.zip
fc-cache -fv

# Additional configs

# Install `polybar` (MAIN) for main status bar

sudo apt install polybar -y

# Install `rofi` (MAIN) for app launcher also theming it

sudo apt install rofi

sudo cp configs/rofi/DarkYellow.rasi /usr/share/rofi/themes/

# Install `picom` (OPTIONAL) for composition fade, rounded-corner, transparency

sudo apt install picom
