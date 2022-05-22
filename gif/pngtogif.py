from PIL import Image
import glob2


frames = []

imgs = glob2.glob("*.png")

for i in imgs:
    new_frame = Image.open(i)
    frames.append(new_frame)


frames[0].save('dnaGif.gif', format="gif", append_images=frames[1:], save_all=True, duration=200, loop=0)
