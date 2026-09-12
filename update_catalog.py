#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import glob

def update_readme():
    readme_path = "README.md"
    static_dir = "wallpapers/static"
    
    extensions = ("*.jpg", "*.jpeg", "*.png", "*.webp")
    image_files = []
    for ext in extensions:
        image_files.extend(glob.glob(os.path.join(static_dir, ext)))
    image_files.sort()
    
    if not image_files:
        print("[!] Nenhum wallpaper encontrado em wallpapers/static/")
        return

    # HTML compactado em uma linha por item para evitar falhas no parser do GitHub
    catalog_html = '<div align="center">\n'
    for img in image_files:
        rel_path = img.replace("\\", "/")
        catalog_html += f'<a href="{rel_path}" target="_blank"><img src="{rel_path}" width="200px" style="border-radius: 8px; margin: 6px;" /></a>\n'
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
    
    print(f"[✓] Sucesso! Catálogo atualizado com {len(image_files)} wallpapers.")

if __name__ == "__main__":
    update_readme()