# Instalar dwm

```
sudo pacman -S base-devel libx11 libxft libxinerama freetype2 fontconfig
```

```
mkdir .suckless
cd .suckless
```

```
git clone https://git.suckless.org/dwm
git clone https://git.suckless.org/st
git clone https://git.suckless.org/dmenu
```

```
cd dwm
make
sudo make clean install
cd ..
```


```
cd st
make
sudo make clean install
cd ..
```


```
cd dmenu
make
sudo make clean install
cd ..
```

## Starting dwm

Put this in the file `/usr/share/xsessions`.

```
[Desktop Entry]
Encoding=UTF-8
Name=Dwm
Comment=Dynamic window manager
Exec=/usr/local/bin/dwm
Icon=dwm
Type=XSession
```
