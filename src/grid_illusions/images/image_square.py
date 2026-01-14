from PIL import Image, ImageDraw

img = Image.new("RGBA", (800, 600), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Square parameters
x, y = 400, 300     
side = 200
cells = 4          # logical grid resolution

# Center the square
x = (img.size[0] - side) // 2
y = (img.size[1] - side) // 2

# Draw outer square
draw.rectangle([x, y, x + side, y + side], width=2, fill="black")

# Zoom factor: >1 = zoom in, <1 = zoom out
zoom = 1.15

# Compute new step size to "zoom" the grid
step = (side / cells) * zoom

img.show()