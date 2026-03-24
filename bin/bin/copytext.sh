#!/usr/bin/env sh

DIRECTORIO="/home/felipe/tmp/"
IMAGE="image.png"
OUTPUT="output"
PBCOPY="/home/felipe/bin/pbcopy.sh"

flameshot gui --path ${DIRECTORIO}${IMAGE}
tesseract ${DIRECTORIO}${IMAGE} ${DIRECTORIO}${OUTPUT}
cat ${DIRECTORIO}${OUTPUT}.txt | tr -d '\n' | ${PBCOPY}
rm ${DIRECTORIO}${IMAGE}
rm ${DIRECTORIO}${OUTPUT}.txt

