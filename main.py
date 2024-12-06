import os
from PIL import Image, ImageDraw, ImageFont, ImageColor, ImageFilter


def new_photo(name):
    image = Image.open(name)
    w, h = image.size

    return image.resize((w//2, h//2))

im = new_photo('dog.jpg')
im2 = new_photo('i.webp')

w, h = im.size

blurred_im2 = im.filter(ImageFilter.EDGE_ENHANCE)
im.paste(im2,(0, 0))


draw = ImageDraw.Draw(im)
font = ImageFont.truetype("SmoothRelief-Regular.ttf", size =30)
draw.text((750, 630), 'By, Aleksandr.', font = font, fill = 'green')
font = ImageFont.truetype("SmoothRelief-Regular.ttf", size =40)
draw.text((780, 590), 'Desing.', font = font, fill = 'red')
font = ImageFont.truetype("ALSFinlandiaScript.otf", size =40)
draw.text((650, 100), 'Пишу письмо, чего же проще.\n Ах нет печатаю уже.', font = font, fill = 'gold')

im.show()

"""
Или с помощью класса
__________________________________________________________________________________________
class PostCardMaker:

    def __init__(self, name, template=None, font_path=None):
        self.name = name
        self.template = "post_card.jpg" if template is None else template
        if font_path is None:
            self.font_path = os.path.join("fonts", "ofont_ru_DS Eraser2.ttf")
        else:
            self.font_path = font_path

    def make(self, resize=False, out_path=None):
        im = Image.open(self.template)
        if resize:
            w, h = im.size
            im = im.resize((w // 2, h // 2))
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype(self.font_path, size=26)

        y = im.size[1] - 10 - (10 + font.size) * 2
        message = f"Привет, {self.name}!"
        draw.text((10, y), message, font=font, fill=ImageColor.colormap['red'])

        y = im.size[1] - 20 - font.size
        message = f"С ужасным праздником тебя!"
        draw.text((10, y), message, font=font, fill=ImageColor.colormap['red'])

        # im.show()
        out_path = out_path if out_path else 'probe.jpg'
        im.save(out_path)
        print(f'Post card saved az {out_path}')


if __name__ == '__main__':
    maker = PostCardMaker(name='Оля')
    maker.make(resize=True)
"""

