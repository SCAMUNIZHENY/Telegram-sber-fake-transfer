from PIL import Image, ImageDraw, ImageFont
from datetime import datetime


async def translate(id_user, name, price):
    sber = Image.open("images/sber.jpg")

    idraw = ImageDraw.Draw(sber)
    time = f"{datetime.now().strftime('%H:%M')}"
    price = price[::-1]
    price = ' '.join([price[i:i+3] for i in range(0, len(price), 3)])[::-1]
    sx = 208
    for i in range(len(price)):
        sx -= 10
    price = f"{price} ₽"
    sy = 208
    for i in range(len(name)):
        sy -= 4

    font = ImageFont.truetype("arial.ttf", size=20)
    font2 = ImageFont.truetype("arialbd.ttf", size=50)
    font3 = ImageFont.truetype("arial.ttf", size=20)

    idraw.text((10, 7), time, font=font)
    idraw.text((sx, 310), price, font=font2)
    idraw.text((sy, 390), name, font=font3)
    sber.save(f'images/{id_user}.jpg')
    img = open(f'images/{id_user}.jpg', "rb")
    return img
