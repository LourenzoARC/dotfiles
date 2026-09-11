import os, json

SCHEME_PATH = os.path.expanduser("~/.local/state/caelestia/scheme.json")
CONFIG_PATH = os.path.expanduser("~/.config/fastfetch/config.jsonc")

def pegar_cor():
    try:
        if not os.path.exists(SCHEME_PATH): return "a6c8ff"
        with open(SCHEME_PATH, "r") as f:
            data = json.load(f)
            return data["colours"]["primary"].lstrip("#")
    except: return "a6c8ff"

def gerar_degrade(hex_base, passos=8):
    r, g, b = int(hex_base[0:2], 16), int(hex_base[2:4], 16), int(hex_base[4:6], 16)
    degrade = []
    for i in range(passos):
        f = i / (passos - 1) if passos > 1 else 0
        nr, ng, nb = int(r + (255 - r) * f), int(g + (255 - g) * f), int(b + (255 - b) * f)
        degrade.append(f"38;2;{nr};{ng};{nb}")
    return degrade

cores = gerar_degrade(pegar_cor())

config = {
    "$schema": "https://github.com/fastfetch-cli/fastfetch/raw/dev/doc/json_schema.json",
    "logo": {
        "type": "file",
        "source": "$(ls ~/.config/fastfetch/ascii/*.txt 2>/dev/null | shuf -n 1)",
        "color": { "1": cores[0] },
        "padding": { "top": 1, "left": 2 }
    },
    "display": {
        "separator": "  ›  "
    },
    "modules": [
        { "type": "title", "color": { "user": cores[0], "at": cores[1], "host": cores[2] } },
        { "type": "custom", "format": "──────────────────────────────" },
        { "key": "  🕇 OS", "keyColor": cores[0], "type": "os" },
        { "key": "  🕇 Kernel", "keyColor": cores[1], "type": "kernel" },
        { "key": "  🕇 Uptime", "keyColor": cores[2], "type": "uptime" },
        { "key": "  🕇 Shell", "keyColor": cores[3], "type": "shell" },
        { "key": "  🕇 WM", "keyColor": cores[4], "type": "wm" },
        { "key": "  🕇 Memory", "keyColor": cores[5], "type": "memory" },
        { "type": "custom", "format": "──────────────────────────────" },
        { "type": "colors", "symbol": "circle" }
    ]
}

with open(CONFIG_PATH, "w") as f:
    json.dump(config, f, indent=2)

