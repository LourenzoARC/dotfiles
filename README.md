# 󰣇 Arch Linux Dotfiles

Minhas configurações pessoais para o ambiente Arch Linux com Hyprland (Caelestia).

## 🛠️ Stack & Tools
| Componente | Ferramenta |
| :--- | :--- |
| **OS** | Arch Linux |
| **WM** | Hyprland (Caelestia) |
| **Terminal** | Kitty |
| **Shell** | Fish |
| **Bar** | Waybar |
| **Launcher** | Rofi |

## 📂 Structure
- \`config/\`: Configurações dos aplicativos (\`kitty\`, \`waybar\`, \`rofi\`)
- \`install.sh\`: Script de instalação automatizada
- \`pacotes-arch.txt\`: Lista de pacotes oficiais
- \`pacotes-aur.txt\`: Lista de pacotes do AUR
- \`vscode-extensions.txt\`: Extensões do VS Code

## 🚀 Installation & Restoration

Para clonar e aplicar estas configurações em uma nova instalação:

```bash
git clone [https://github.com/LourenzoARC/dotfiles.git](https://github.com/LourenzoARC/dotfiles.git) ~/dotfiles
cd ~/dotfiles
./install.sh
```

### Restauração Manual (Alternativa)
Se preferir instalar os pacotes por etapa:

```bash
# Pacotes oficiais
sudo pacman -S --needed - < pacotes-arch.txt

# Pacotes AUR (via yay/paru)
yay -S --needed - < pacotes-aur.txt

# Extensões do VS Code
while read -r ext; do code --install-extension "$ext"; done < vscode-extensions.txt
```
