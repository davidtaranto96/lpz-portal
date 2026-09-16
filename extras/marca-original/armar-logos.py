"""Logo plano de LPZ Propiedades, a partir del trazo de logo-lpz.png (Grupo LPZ):
la corona y las letras LPZ son el mismo dibujo; cambian los colores y el rótulo de abajo."""
from PIL import Image, ImageDraw, ImageFont
import numpy as np

SRC = "/Users/dt/Documents/DT-System/crm-molins/portal/img/logo-lpz.png"
NARANJA = (243, 122, 31)
GRIS = (110, 104, 97)       # letras sobre fondo claro
GRIS_CLARO = (214, 208, 201) # letras sobre fondo oscuro
CARBON = (46, 44, 40)

base = Image.open(SRC).convert("RGBA")
alfa = np.array(base)[..., 3]

def pieza(y0, y1, color):
    a = alfa[y0:y1]
    arr = np.zeros((a.shape[0], a.shape[1], 4), dtype=np.uint8)
    arr[..., :3] = color
    arr[..., 3] = a
    return Image.fromarray(arr, "RGBA")

def rotulo(texto, ancho, alto_mayus, color):
    fuente_path = "/System/Library/Fonts/Optima.ttc"
    # índice 1 = Optima Bold en la colección
    tam = int(alto_mayus / 0.7)
    f = ImageFont.truetype(fuente_path, tam, index=1)
    glifos = [f.getbbox(c) for c in texto]
    anchos = [b[2] - b[0] for b in glifos]
    esp = (ancho - sum(anchos)) / (len(texto) - 1)
    bb = f.getbbox("PROPIEDADES")
    h = bb[3] - bb[1]
    im = Image.new("RGBA", (ancho, h + 4), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    x = 0.0
    for c, b, w in zip(texto, glifos, anchos):
        d.text((x - b[0], -bb[1]), c, font=f, fill=color + (255,))
        x += w + esp
    return im

def logo(color_letras):
    corona = pieza(15, 282, NARANJA)
    lpz = pieza(310, 630, color_letras)
    rot = rotulo("PROPIEDADES", 694, 64, color_letras)
    W = base.width
    H = corona.height + lpz.height + 52 + rot.height + 20
    lienzo = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    lienzo.alpha_composite(corona, (0, 0))
    lienzo.alpha_composite(lpz, (0, corona.height))
    lienzo.alpha_composite(rot, (18, corona.height + lpz.height + 52))
    return lienzo.crop(lienzo.getbbox())

def marca(color_letras):
    """Corona + LPZ, sin rótulo: para los lugares chicos y cuadrados."""
    corona = pieza(15, 282, NARANJA)
    lpz = pieza(310, 630, color_letras)
    im = Image.new("RGBA", (base.width, corona.height + lpz.height), (0, 0, 0, 0))
    im.alpha_composite(corona, (0, 0)); im.alpha_composite(lpz, (0, corona.height))
    return im.crop(im.getbbox())

oscuro = logo(GRIS); oscuro.save("logo-lpz-propiedades.png", optimize=True)
claro = logo(GRIS_CLARO); claro.save("logo-lpz-propiedades-claro.png", optimize=True)

# escudo cuadrado: ocupa el lugar de logo-molins.png (316x320, fondo lleno)
E = 320
esc = Image.new("RGBA", (E, E), CARBON + (255,))
m = marca(GRIS_CLARO)
esc_ancho = 208
m = m.resize((esc_ancho, round(m.height * esc_ancho / m.width)), Image.LANCZOS)
esc.alpha_composite(m, ((E - m.width) // 2, (E - m.height) // 2))
esc.convert("RGB").save("escudo-lpz.png", optimize=True)

# vista previa al compartir, 1200x630
og = Image.new("RGBA", (1200, 630), CARBON + (255,))
c = claro.resize((round(claro.width * 470 / claro.height), 470), Image.LANCZOS)
og.alpha_composite(c, ((1200 - c.width) // 2, (630 - c.height) // 2))
og.convert("RGB").save("og-lpz.jpg", quality=90)

# hoja de control: los dos logos sobre sus fondos
hoja = Image.new("RGB", (1500, 760), (240, 236, 231))
hoja.paste((46, 44, 40), (750, 0, 1500, 760))
a = oscuro.resize((round(oscuro.width * 620 / oscuro.height), 620), Image.LANCZOS)
b = claro.resize((round(claro.width * 620 / claro.height), 620), Image.LANCZOS)
hoja.paste(a, ((750 - a.width)//2, 70), a); hoja.paste(b, (750 + (750 - b.width)//2, 70), b)
hoja.save("control.png")
print(oscuro.size, claro.size)
