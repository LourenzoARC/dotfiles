# Dotfiles - Arch Linux

Configurações para o ambiente Arch Linux com Hyprland e o kernel CachyOS (BORE/LTO).

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

## Modos de Instalação e Uso

### Opção 1: Apenas Aplicar Configurações e Customizações
Para quem já possui o ambiente configurado e deseja apenas clonar e aplicar os dotfiles e utilitários Python:

```bash
git clone https://github.com/LourenzoARC/dotfiles.git ~/dotfiles && cd ~/dotfiles && mkdir -p ~/.config && cp -rf config/* ~/.config/ && sudo cp -rf config/caelestia/utils/* /usr/lib/python3.14/site-packages/caelestia/utils/
```

### Opção 2: Instalação Completa do Zero 
Para clonar e executar a instalação completa automatizada (kernel CachyOS, pacotes, configs e utilitários):

```bash
git clone https://github.com/LourenzoARC/dotfiles.git ~/dotfiles && cd ~/dotfiles && ./install.sh
```

## Estrutura do Repositório

- `config/hypr/`: Configurações e gerenciamento do Hyprland.
- `config/fish/`: Configurações e plugins do Fish Shell.
- `config/nvim/`: Arquivos de configuração do Neovim.
- `config/kitty/`: Configurações do terminal Kitty.
- `config/waybar/`: Layout e estilos da barra de status.
- `config/rofi/`: Configurações do menu de aplicativos.
- `config/fastfetch/`: Perfil do sistema.
- `config/btop/`: Tema e configurações do monitor de recursos.
- `config/caelestia/utils/`: Utilitários e customizações em Python.
- `install.sh`: Script de automação e implantação completa.
