#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '
# ====================================================
# PROMPT CUSTOMIZADO COM BORDAS (Sem imagens)
# ====================================================

# Definindo cores
VERDE="\[\033[01;32m\]"
AZUL="\[\033[01;34m\]"
CIANO="\[\033[01;36m\]"
ROXO="\[\033[01;35m\]"
RESET="\[\033[00m\]"

# Desenhando o prompt com caracteres de borda (╭ e ╰)
PS1="\n${CIANO}╭─[${VERDE}\u@\h${CIANO}]─[${ROXO}\w${CIANO}]\n╰─> ${RESET}"

# Deixa o WezTerm quase transparente
limpo() {
    wezterm cli set-window-background-opacity 0.05
}

# Restaura o WezTerm ao normal
stop() {
    wezterm cli set-window-background-opacity 1.0
}