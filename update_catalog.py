#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import glob
import urllib.parse

def update_readme():
    readme_path = "README.md"
    static_dir = "wallpapers/static"
    
    extensions = ("*.jpg", "*.jpeg", "*.png", "*.webp")
    image_files = []
    for ext in extensions:
        image_files.extend(glob.glob(os.path.join(static_dir, ext)))
    
    # Ordena do MAIOR para o MENOR arquivo (em bytes)
    image_files.sort(key=lambda x: os.path.getsize(x), reverse=True)
    
    if not image_files:
        print("[!] Nenhum wallpaper encontrado em wallpapers/static/")
        return

    raw_base = "https://raw.githubusercontent.com/LourenzoARC/dotfiles/main"

    catalog_html = '<div align="center">\n'
    for img in image_files:
        rel_path = img.replace("\\", "/")
        # Codifica espaços e caracteres especiais para a URL raw funcionar perfeitamente
        encoded_path = urllib.parse.quote(rel_path, safe='/')
        raw_url = f"{raw_base}/{encoded_path}"
        catalog_html += f'<a href="{raw_url}" target="_blank"><img src="{raw_url}" width="200px" style="border-radius: 8px; margin: 6px;" /></a>\n'
    catalog_html += '</div>'

    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()
    else:
        content = "# Dotfiles\n\n## 🖼️ Wallpaper Catalog\n"

    start_marker = "<!-- WALLPAPER_CATALOG_START -->"
    end_marker = "<!-- WALLPAPER_CATALOG_END -->"
    
    block = f"{start_marker}\n{catalog_html}\n{end_marker}"

    if start_marker in content and end_marker in content:
        start_idx = content.find(start_marker)
        end_idx = content.find(end_marker) + len(end_marker)
        new_content = content[:start_idx] + block + content[end_idx:]
    else:
        new_content = content + f"\n\n## 🖼️ Wallpaper Catalog\n{block}\n"

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    print(f"[✓] Catálogo ordenado por tamanho e atualizado com {len(image_files)} wallpapers!")

if __name__ == "__main__":
    update_readme()