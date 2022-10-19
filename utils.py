from PIL import Image, ImageDraw, ImageSequence, ImageFont
import io


def cover_text_on_gif(x: int, y: int, path_to_gif: str, text: str, color_text: str, text_size: int):
    if path_to_gif.split('.')[-1] != 'gif':
        raise ValueError('"path_to_gif" must point to gif file')

    gif = Image.open(path_to_gif)

    width, height = gif.size

    if x > width or y > height:
        raise ValueError('x or y is not within the boundaries of the image\nThis gif size: width={}, height={}'.format(width, height))

    frames = []

    font = ImageFont.truetype('fonts/SourceSansPro-Regular.ttf', size=text_size, encoding='UTF-8')

    for frame in ImageSequence.Iterator(gif):
        d = ImageDraw.Draw(frame)
        d.text((x,y), text=text, fill=color_text, font=font)
        del d

        b = io.BytesIO()
        frame.save(b, format='GIF')
        frame = Image.open(b)

        frames.append(frame)

    frames[0].save('out.gif', save_all=True, append_images=frames[1:])


gif_cover = cover_text_on_gif(13, 55, 'gifs/7plX.gif', 'test тест Україна ', 'green', 12)
