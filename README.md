# Instrucciones

## Generar llave ssh

```sh
ssh-keygen -t ed25519 -C "justafewwords4@gmail.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
cat ~/.ssh/id_ed25519.pub
```

## El programa stow

Se requiere el programa `stow`.

Dentro del directorio `~/doti`

```sh
stow `directorio`
```

Crea los enlaces para el directorio.

```sh
stow *
```

Crea los enlaces para todos los directorios.

## Comando para copiar clave ssh a otra computadora

```sh
ssh-copy-id root@10.10.0.5
```

## Configurar copytext.sh

```sh
mkdir /home/$(whoami)/tmp/
```

## Instalar n (npm)

```sh
sudo mkdir -p /usr/local/n
sudo chown -R $(whoami) /usr/local/n
sudo mkdir -p /usr/local/bin /usr/local/lib /usr/local/include /usr/local/share
sudo chown -R \
  $(whoami) /usr/local/bin /usr/local/lib /usr/local/include /usr/local/share
sudo mkdir -p /usr/local/share/man/man1
sudo chown -R $(whoami) /usr/local/share/man/man1

curl -fsSL https://raw.githubusercontent.com/tj/n/master/bin/n | bash -s lts
npm install -g n
```

### Instalaciones npm

```sh
npm i -g stylelint js-beautify marked
```

## autoenv

<https://github.com/hyperupcall/autoenv>

Es una aplicación para el shell, que permite ejecutar ciertos comandos que se
encuentren en cierto archivo.

Instalación:

```sh
curl \
-#fLo- \
'https://raw.githubusercontent.com/hyperupcall/autoenv/master/scripts/install.sh' \
| sh
```

Poner lo siguiente en el `.zshrc`

```sh
export AUTOENV_ENV_FILENAME=.autoenv
export AUTOENV_ENV_LEAVE_FILENAME=.autoenv.leave
```

Y para usarlo, por ejemplo en un directorio con un ambiente virtual python,
crear un archivo llamado `.autoenv` con el siguiente contenido:

```sh
source .venv/bin/activate
```
