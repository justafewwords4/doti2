#!/usr/bin/bash

echo "instalando diversos paquetes..."
sudo apt update
sudo apt upgrade
sudo apt install udiskie \
  flameshot \
  golang gopls \
  inotify-tools libnotify-bin \
  rsync \
  emacs \
  stow \
  flatpak \
  xclip \
  wget \
  tesseract-ocr tesseract-ocr-spa \
  lazygit

echo "instalando flatpak"
sudo flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo

# configurar copytext.sh
mkdir /home/$(whoami)/tmp/

# npm

echo "instalando n"
sudo mkdir -p /usr/local/n
sudo chown -R $(whoami) /usr/local/n
sudo mkdir -p /usr/local/bin /usr/local/lib /usr/local/include /usr/local/share
sudo chown -R \
  $(whoami) /usr/local/bin /usr/local/lib /usr/local/include /usr/local/share
sudo mkdir -p /usr/local/share/man/man1
sudo chown -R $(whoami) /usr/local/share/man/man1

curl -fsSL https://raw.githubusercontent.com/tj/n/master/bin/n | bash -s lts
npm install -g n

# instalaciones npm

npm i -g stylelint js-beautify marked

# neovim
echo "instalando neovim..."
curl -LO https://github.com/neovim/neovim/releases/latest/download/nvim-linux-x86_64.tar.gz
sudo rm -rf /opt/nvim-linux-x86_64
sudo tar -C /opt -xzf nvim-linux-x86_64.tar.gz

echo 'export PATH="$PATH:/opt/nvim-linux-x86_64/bin"' >>~/.bashrc

# zapzap
echo "instalar zapzap..."
flatpak install flathub com.rtosta.zapzap

# bluetooth
echo "instalando bluetooth..."
sudo apt update
sudo apt install bluetooth bluez bluez-tools bluez-firmware
sudo systemctl enable --now bluetooth
sudo apt install blueman

cd ~/Downloads
wget -O tsetup.6.7.6.tar.xz https://telegram.org/dl/desktop/linux
7z x tsetup.6.7.6.tar.xz
7z x tsetup.6.7.6.tar
mv Telegram ..

# opencode

curl -fsSL https://opencode.ai/install | bash

# gemini-cli
npm install -g @google/gemini-cli

cd
