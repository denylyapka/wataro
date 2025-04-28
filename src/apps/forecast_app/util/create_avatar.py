import random

from PIL import Image, ImageDraw, ImageFont


def generate_avatar_user(tg_id: int, letter: str):
    colors = ["#758BFF"]
    color = random.choice(colors)
    print(color)

    img = Image.new("RGBA", (140, 140), color=color)
    idraw = ImageDraw.Draw(img)

    headline = ImageFont.truetype("arial.ttf", 30)

    idraw.text((38, 52), letter, spacing=20, font=headline, fill="white")

    img.save(f"avatar_{tg_id}.png")
    return "ok"

generate_avatar_user(tg_id=123123, letter="soon")