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

# --- Configurar Repositório CachyOS ---
echo "⚙️ Configurando o repositório do CachyOS..."
if ! grep -q "cachyos" /etc/pacman.conf; then
    curl https://mirror.cachyos.org/cachyos-repo.tar.xz -o cachyos-repo.tar.xz
    tar xvf cachyos-repo.tar.xz
    cd cachyos-repo
    sudo ./cachyos-repo.sh
    cd ..
    rm -rf cachyos-repo cachyos-repo.tar.xz
fi
