
from PIL import Image

filname = 'IMAG2231.jpg'
with Image.open(filname) as img:
    img.load()

    print(img.format)

    print(img.size)

    print(img.mode)
    # img.show()

    obrezka_img = img.crop((300, 150, 700, 1000))
    print(obrezka_img.size)

    # obrezka_img.show()

    pover = img.rotate(45, expand=True)
    pover.show()