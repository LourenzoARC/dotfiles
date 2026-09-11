# 🐧 Dotfiles do Arch Linux

Configurações avançadas e personalizadas para o meu ambiente Arch Linux com Hyprland e Kernel CachyOS.

## 🛠️ Stack & Ferramentas
| Componente | Ferramenta |
| :--- | :--- |
| **OS** | Arch Linux (Kernel CachyOS BORE/LTO) |
| **WM** | Hyprland (Caelestia) |
| **Terminal** | Kitty |
| **Shell** | Fish Shell |
| **Editor** | Neovim (Nvim) |
| **Barra** | Waybar |
| **Lançador** | Rofi |
| **Info do Sistema** | Fastfetch |
| **Monitor** | Btop |

## ⚡ Instalação Automatizada (All-in-One)

O script \`install.sh\` configura automaticamente o repositório do CachyOS, instala o kernel otimizado, puxa todos os pacotes oficiais e do AUR, implanta as configs do Hyprland e aplica suas modificações customizadas em Python do Caelestia.

```bash
git clone [https://github.com/LourenzoARC/dotfiles.git](https://github.com/LourenzoARC/dotfiles.git) ~/dotfiles
cd ~/dotfiles
./install.sh
```

## 📂 Estrutura do Repositório
- \`config/hypr/\`: Configurações do Hyprland e animações
- \`config/fish/\`: Atalhos, plugins e prompt do Fish
- \`config/nvim/\`: Configurações e plugins do Neovim
- \`config/kitty/\`: Tema e fontes do terminal Kitty
- \`config/waybar/\`: Barra de status customizada
- \`config/rofi/\`: Menu de aplicativos
- \`config/fastfetch/\`: Perfil visual de boas-vindas do terminal
- \`config/btop/\`: Monitor de recursos do sistema
- \`config/caelestia/utils/\`: Modificações Python customizadas
- \`install.sh\`: Script de automação total
