# Coloque isto na PRIMEIRA linha do seu ~/.config/fish/config.fish
if status --is-login
    if test (tty) = /dev/tty1
        exec Hyprland
    end
end

# Carrega coisas interativas (Starship, alias, zoxide, fastfetch)
if status is-interactive
    cat ~/.local/state/caelestia/sequences.txt 2> /dev/null
    starship init fish | source
    
    command -v direnv &> /dev/null && direnv hook fish | source
    command -v zoxide &> /dev/null && zoxide init fish --cmd cd | source

    alias syu="sudo pacman -Syu"
    alias fd="find"
    alias Rns="sudo pacman -Rns"
    alias Rdd="sudo pacman -Rdd"
    alias ls="eza --icons --group-directories-first -1"
    alias limpar="yay -Yc --noconfirm;yay -Scc --noconfirm;sudo pacman -Scc --noconfirm;sudo journalctl --vacuum-time=1d;flatpak uninstall --unused -y;rm -rf ~/.cache/thumbnails/*"
    alias erros="systemctl --failed;sudo dmesg --level=err,warn;sudo journalctl -p 4 -xb"
    
    # Substituindo o nano pelo VS Code
    alias nano="code"

    # Fastfetch aleatório na inicialização do terminal
    set -l FASTFETCH_TXT (find ~/.config/fastfetch/ascii -type f -name "*.txt" 2>/dev/null | shuf -n 1)
    if test -n "$FASTFETCH_TXT"
        fastfetch --file "$FASTFETCH_TXT" --logo-type file 2>/dev/null
    end
end

# --- FUNÇÕES ---

function code
    command code-oss --ozone-platform=x11 $argv >/dev/null 2>&1 &
end

function ff
end

function port
    echo "🔓 Liberando firewall e todas as portas de rede (Atenção à segurança!)..."
    sudo iptables -F 2>/dev/null
    sudo iptables -X 2>/dev/null
    sudo iptables -P INPUT ACCEPT 2>/dev/null
    sudo iptables -P FORWARD ACCEPT 2>/dev/null
    sudo iptables -P OUTPUT ACCEPT 2>/dev/null
    if command -v ufw > /dev/null
        sudo ufw disable
    end

    echo "💾 Procurando e montando pendrives desconectados logicamente..."
    for dev in (lsblk -rno NAME,RM,TYPE,MOUNTPOINT | awk '$2==1 && $3=="part" && $4=="" {print $1}')
        echo "Montando /dev/$dev..."
        udisksctl mount -b /dev/$dev
    end

    echo "🔌 Reiniciando controladoras USB no Kernel (Resolvendo travamentos)..."
    for driver in xhci_hcd ehci-pci
        if test -d /sys/bus/pci/drivers/$driver
            for dev in (ls /sys/bus/pci/drivers/$driver/ | grep -E '^[0-9a-fA-F:.]+$')
                echo $dev | sudo tee /sys/bus/pci/drivers/$driver/unbind >/dev/null
                sleep 0.5
                echo $dev | sudo tee /sys/bus/pci/drivers/$driver/bind >/dev/null
            end
        end
    end
    echo "✅ Comando executado! Portas abertas e USBs reiniciados."
end

function arrumar_app
    echo "🔍 Janelas ativas no momento:"
    
    set -l pids (hyprctl clients | grep "pid:" | awk '{print $2}')
    set -l classes (hyprctl clients | grep "class:" | awk '{print $2}')
    
    set -l count (count $pids)
    if test $count -eq 0
        echo "Nenhuma janela ativa encontrada."
        return
    end
    
    for i in (seq 1 $count)
        echo "[$i] " $classes[$i] " (PID: " $pids[$i] ")"
    end
    
    echo ""
    read -p 'echo "👉 Digite o número do app para consertar a tela (ou Enter para sair): "' num
    
    if test -z "$num"; or not string match -q -r '^[0-9]+$' "$num"
        echo "Operação cancelada."
        return
    end
    
    if test $num -lt 1; or test $num -gt $count
        echo "Número inválido!"
        return
    end
    
    set -l alvo_pid $pids[$num]
    set -l alvo_class $classes[$num]
    
    echo "⚙️  Processando $alvo_class (PID: $alvo_pid)..."
    
    set -l cmd_full (cat /proc/$alvo_pid/cmdline | tr "\0" " ")
    set -l bin_name (echo $cmd_full | awk '{print $1}')
    
    echo "🛑 Reiniciando a janela..."
    kill -9 $alvo_pid
    sleep 1
    
    echo "🚀 Abrindo com a resolução original forçada (X11)..."
    env GDK_BACKEND=x11 QT_QPA_PLATFORM=xcb ELECTRON_OZONE_PLATFORM_HINT=auto $bin_name --ozone-platform=x11 >/dev/null 2>&1 &
    
    echo "✅ Concluído! A interface do $alvo_class deve estar normal agora."
end

# --- FUNÇÕES DE TRANSPARÊNCIA ---

function limpo
    kitty @ set-background-opacity 0.0
end
function stop
    kitty @ set-background-opacity 0.78
end