#!/bin/bash
set -e
echo "🚀 Iniciando a instalação completa do ambiente LourenzoARC..."

# 1. Configurar Repositório CachyOS e Kernel
echo "⚙️ Configurando o repositório do CachyOS..."
if ! grep -q "cachyos" /etc/pacman.conf; then
    curl https://mirror.cachyos.org/cachyos-repo.tar.xz -o cachyos-repo.tar.xz
    tar xvf cachyos-repo.tar.xz
    cd cachyos-repo
    sudo ./cachyos-repo.sh
    cd ..
    rm -rf cachyos-repo cachyos-repo.tar.xz
    sudo pacman -Sy
fi

# 2. Instalar Pacotes Oficiais
echo "📦 Instalando pacotes oficiais e kernel CachyOS..."
sudo pacman -S --needed - < pacotes-arch.txt

# 3. Instalar Pacotes AUR
if command -v yay &> /dev/null; then
    echo "📦 Instalando pacotes do AUR..."
    yay -S --needed - < pacotes-aur.txt
fi

# 4. Aplicar Dotfiles (.config)
echo "📂 Aplicando dotfiles (Hyprland, Fish, Kitty, etc.)..."
mkdir -p ~/.config
cp -rf config/* ~/.config/

# 5. Restaurar Utilitários Python do Caelestia
echo "🐍 Aplicando modificações Python customizadas..."
if [ -d "config/caelestia/utils" ]; then
    sudo cp -rf config/caelestia/utils/* /usr/lib/python3.14/site-packages/caelestia/utils/
fi

# 6. Sincronizar Extensões do VS Code
if command -v code &> /dev/null && [ -f "vscode-extensions.txt" ]; then
    echo "🧩 Instalando extensões do VS Code..."
    while read -r ext; do
        [ -n "$ext" ] && code --install-extension "$ext"
    done < vscode-extensions.txt
fi

echo "✨ Tudo pronto! Reinicie o sistema para carregar o Kernel CachyOS e o Hyprland."
