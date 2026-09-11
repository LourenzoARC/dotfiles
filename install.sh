#!/bin/bash
echo "Instalando pacotes do Arch..."
sudo pacman -S --needed - < pacotes-arch.txt
echo "Restaurando configurações..."
cp -a .config/* ~/.config/
echo "Concluído!"
