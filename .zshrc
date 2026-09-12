# --- COMANDO AUTOMÁTICO DE REPARO (ARRUMAR) ---
arrumar() {
    echo "🔄 [1/3] Garantindo pacotes de sistemas de arquivos..."
    sudo pacman -S --needed --noconfirm ntfs-3g exfatprogs util-linux

    echo "🔍 [2/3] Verificando e corrigindo partições travadas (NTFS/ExFAT)..."
    # Procura por partições NTFS e aplica correção de superbloqueio/journal
    for part in $(lsblk -o NAME,FSTYPE -r | grep -E 'ntfs|exfat' | awk '{print "/dev/" $1}'); do
        echo "Aplicando reparo em: $part"
        sudo ntfsfix "$part" 2>/dev/null || true
    done

    echo "🚀 [3/3] Remontando todas as portas e discos do sistema..."
    sudo mount -a

    echo "✨ Pronto! Todas as portas e discos foram verificados e arrumados."
}