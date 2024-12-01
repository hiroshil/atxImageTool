#!/usr/bin/python

import sys
import json
import shutil
from pathlib import Path
from PIL import Image, ImageDraw
from zipfile import ZipFile

def rebuild_sprite(json_data, texture_path):
    canvas_width = json_data["Canvas"]["Width"]
    canvas_height = json_data["Canvas"]["Height"]
    sprites = []

    blocks = sorted(json_data["Block"], key=lambda k: k['priority'], reverse=True)
    for block in blocks:
        base_image = f"{blocks[0]['filename']}_" if block != blocks[0] else ''
        sprite = Image.new("RGBA", (canvas_width, canvas_height), (0, 0, 0, 0))
        offset_x = block["offsetX"]
        offset_y = block["offsetY"]
        for mesh in block["Mesh"]:
            tex_no = mesh["texNo"]
            src_offset_x = mesh["srcOffsetX"]
            src_offset_y = mesh["srcOffsetY"]
            tex_u1 = mesh["texU1"]
            tex_v1 = mesh["texV1"]
            tex_u2 = mesh["texU2"]
            tex_v2 = mesh["texV2"]
            view_x = mesh["viewX"]
            view_y = mesh["viewY"]
            
            texture = Image.open(texture_path.replace('[tex_no]', str(tex_no))).convert("RGBA")

            cropped_texture = texture.crop((
                round(tex_u1 * texture.width),
                round(tex_v1 * texture.height),
                round(tex_u2 * texture.width),
                round(tex_v2 * texture.height)
            ))

            sprite.paste(cropped_texture, (round(src_offset_x) + round(offset_x), round(src_offset_y) + round(offset_y)))
        sprites.append((sprite, f"{base_image}{block['filename']}"))
    return sprites

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("> Usage: python atlas_to_png.py <file>")
        exit(1)
    file = sys.argv[1]
    with ZipFile(file, 'r') as zip_ref:
        zip_ref.extractall('temp')
    with open(f'temp/atlas.json', "r") as json_file:
        json_data = json.load(json_file)
    if Path('temp/tex0.png').exists():
        tex_path = f"temp/tex[tex_no].png"
    else:
        tex_path = f"temp/tex[tex_no].webp"
    sprites = rebuild_sprite(json_data, tex_path)
    len_path = 5 if "l" in file else 4
    output_path = Path(file).parent / Path(file).stem[:len_path]
    output_path.mkdir(parents=True, exist_ok=True)
    if len(sprites):
        for sprite in sprites:
            file_name = output_path / (sprite[1] + ".png")
            sprite[0].save(file_name, "PNG")
            print(f'> Reconstructed CG saved as {file_name.name}')
    shutil.rmtree('temp')
    
