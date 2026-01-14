from PIL import Image, ImageDraw

img = Image.new("RGB", (800, 600), "white")
draw = ImageDraw.Draw(img)

img.show()