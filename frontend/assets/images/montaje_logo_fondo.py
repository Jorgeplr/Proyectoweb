from PIL import Image, ImageDraw
import os

# Rutas de las imágenes (ajusta si es necesario)
background_path = 'frontend/assets/images/fondo.png'
logo_path = 'frontend/assets/images/logofondo.png'
output_path = 'frontend/assets/images/montaje.png'

# Abrir imágenes
background = Image.open(background_path).convert('RGBA')
logo = Image.open(logo_path).convert('RGBA')

# Añadir margen transparente alrededor del logo antes de recortar
def add_transparent_margin(im, margin_ratio=0.35):
    w, h = im.size
    margin_w = int(w * margin_ratio)
    margin_h = int(h * margin_ratio)
    new_w = w + 2 * margin_w
    new_h = h + 2 * margin_h
    new_im = Image.new('RGBA', (new_w, new_h), (0, 0, 0, 0))
    new_im.paste(im, (margin_w, margin_h))
    return new_im

# Hacer el logo circular sin borde blanco
def make_circle(im):
    size = min(im.size)
    mask = Image.new('L', (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)
    output = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    im = im.resize((size, size), Image.LANCZOS)
    output.paste(im, (0, 0), mask)
    return output

# Añadir margen al logo antes de hacerlo circular
logo_with_margin = add_transparent_margin(logo, margin_ratio=0.35)

# Aumentar el tamaño del logo (70% de la altura del fondo)
logo_size = int(background.height * 0.7)
logo_circular = logo_with_margin.resize((logo_size, logo_size), Image.LANCZOS)
logo_circular = make_circle(logo_circular)

# Posición: margen
margin = 40
position = (margin, margin)

# Pegar el logo circular sobre el fondo
background.paste(logo_circular, position, logo_circular)

# Guardar el resultado
background.save(output_path)
print(f'Montaje guardado en: {output_path}')
