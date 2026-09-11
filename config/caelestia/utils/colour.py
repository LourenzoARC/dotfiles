from __future__ import annotations
import colorsys

class Colour:
    _rgb_vals: tuple[int, ...]
    _hex_vals: tuple[str, ...]

    def __init__(self, hex_str: str):
        clean = hex_str.lstrip("#").ljust(8, "f")
        self._hex_vals = tuple(clean[i : i + 2] for i in range(0, 7, 2))
        self._rgb_vals = tuple(int(h, 16) for h in self._hex_vals)

    @property
    def r(self) -> int: return self._rgb_vals[0]
    @property
    def g(self) -> int: return self._rgb_vals[1]
    @property
    def b(self) -> int: return self._rgb_vals[2]

    @property
    def hex(self) -> str:
        return "".join(self._hex_vals[:-1])

    @property
    def hexalpha(self) -> str:
        return "".join(self._hex_vals)

    @property
    def rgb(self) -> str:
        return f"rgb({','.join(map(str, self._rgb_vals[:-1]))})"

    @property
    def rgbalpha(self) -> str:
        return f"rgba({','.join(map(str, self._rgb_vals))})"

    @property
    def hypr(self) -> str:
        return f"rgba({self.hex}{self._hex_vals[-1]})"

    def with_alpha(self, alpha: float) -> Colour:
        alpha_hex = f"{int(max(0.0, min(1.0, alpha)) * 255):02x}"
        return Colour(f"{self.hex}{alpha_hex}")

    def lighten(self, factor: float = 0.1) -> Colour:
        h, l, s = colorsys.rgb_to_hls(self.r / 255.0, self.g / 255.0, self.b / 255.0)
        l = min(1.0, max(0.0, l + factor))
        r, g, b = colorsys.hls_to_rgb(h, l, s)
        return Colour(f"{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}{self._hex_vals[-1]}")

    def darken(self, factor: float = 0.1) -> Colour:
        return self.lighten(-factor)

    def saturate(self, factor: float = 0.1) -> Colour:
        h, l, s = colorsys.rgb_to_hls(self.r / 255.0, self.g / 255.0, self.b / 255.0)
        s = min(1.0, max(0.0, s + factor))
        r, g, b = colorsys.hls_to_rgb(h, l, s)
        return Colour(f"{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}{self._hex_vals[-1]}")

    @property
    def luminance(self) -> float:
        def norm(c: int) -> float:
            v = c / 255.0
            return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
        return 0.2126 * norm(self.r) + 0.7152 * norm(self.g) + 0.0722 * norm(self.b)

    @property
    def is_dark(self) -> bool:
        return self.luminance < 0.4

    @property
    def foreground(self) -> str:
        return "ffffff" if self.is_dark else "141414"


def get_dynamic_colours(colours: dict[str, str]) -> dict[str, Colour]:
    return {name: Colour(code) for name, code in colours.items()}
