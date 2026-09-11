# Dotfiles - Arch Linux

Configurações avançadas e otimizadas para o ambiente Arch Linux com Hyprland e o kernel CachyOS (BORE/LTO).

## Stack e Ferramentas

| Componente | Ferramenta |
| :--- | :--- |
| **Sistema Operacional** | Arch Linux |
| **Kernel** | CachyOS (BORE / LTO) |
| **Gerenciador de Janelas** | Hyprland (Caelestia) |
| **Terminal** | Kitty |
| **Shell** | Fish Shell |
| **Editor de Texto** | Neovim |
| **Barra de Status** | Waybar |
| **Lançador de Aplicativos** | Rofi |
| **Informações do Sistema** | Fastfetch |
| **Monitor de Recursos** | Btop |

## Instalação Automatizada

O script de instalação automatizada configura o repositório do CachyOS, instala o kernel otimizado, gerencia a instalação de pacotes oficiais e do AUR, implanta as configurações do sistema e restaura os utilitários Python personalizados.

\`\`\`bash
git clone https://github.com/LourenzoARC/dotfiles.git ~/dotfiles
cd ~/dotfiles
./install.sh
\`\`\`

## Estrutura do Repositório

- \`config/hypr/\`: Configurações e gerenciamento do Hyprland.
- \`config/fish/\`: Configurações e plugins do Fish Shell.
- \`config/nvim/\`: Arquivos de configuração do Neovim.
- \`config/kitty/\`: Configurações do terminal Kitty.
- \`config/waybar/\`: Layout e estilos da barra de status.
- \`config/rofi/\`: Configurações do menu de aplicativos.
- \`config/fastfetch/\`: Perfil do sistema.
- \`config/btop/\`: Tema e configurações do monitor de recursos.
- \`config/caelestia/utils/\`: Utilitários e customizações em Python.
- \`install.sh\`: Script de automação e implantação completa.
