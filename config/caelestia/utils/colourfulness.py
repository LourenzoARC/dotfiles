import numpy as np
from PIL import Image

def get_variant(image: Image.Image) -> str:
    if getattr(image, "is_animated", False):
        try:
            image.seek(image.n_frames // 2)
        except Exception:
            pass

    if image.mode in ("RGBA", "LA") or (image.mode == "P" and "transparency" in image.info):
        bg = Image.new("RGB", image.size, (0, 0, 0))
        bg.paste(image, mask=image.split()[-1] if image.mode != "P" else None)
        img = bg
    elif image.mode != "RGB":
        img = image.convert("RGB")
    else:
        img = image

    arr = np.array(img, dtype=np.float32)
    r, g, b = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]

    max_rgb = np.maximum(r, np.maximum(g, b))
    min_rgb = np.minimum(r, np.minimum(g, b))
    chroma = max_rgb - min_rgb
    total_pixels = chroma.size

    true_black_pixels = np.sum(max_rgb < 35.0)
    true_black_ratio = true_black_pixels / total_pixels

    colored_pixels = np.sum(chroma >= 20.0)
    color_ratio = colored_pixels / total_pixels

    vibrant_pixels = np.sum(chroma >= 45.0)
    vibrant_ratio = vibrant_pixels / total_pixels

    if color_ratio < 0.003:
        return "monochrome"

    if true_black_ratio >= 0.18 and color_ratio < 0.35 and 0.003 <= vibrant_ratio <= 0.15:
        return "tonalspot"

    if vibrant_ratio < 0.08:
        return "fidelity"

    return "vibrant"
