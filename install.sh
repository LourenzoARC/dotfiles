#!/bin/bash
echo "Instalando pacotes do Arch..."
sudo pacman -S --needed - < pacotes-arch.txt
echo "Restaurando configurações..."
cp -a .config/* ~/.config/
echo "Concluído!"

# Restaurar utilitários Python customizados do Caelestia
if [ -d "config/caelestia/utils" ]; then
    sudo cp -rf config/caelestia/utils/* /usr/lib/python3.14/site-packages/caelestia/utils/
fi
