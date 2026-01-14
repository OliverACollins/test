from PIL import Image, ImageDraw

img = Image.new("RGB", (800, 600), "white")
draw = ImageDraw.Draw(img)

# Square parameters
x, y = 400, 300     
side = 250
cells = 15          # logical grid resolution

# Center the square
x = (img.size[0] - side) // 2
y = (img.size[1] - side) // 2

# Draw outer square
draw.rectangle([x, y, x + side, y + side], width=2, fill="black")

# Zoom factor: >1 = zoom in, <1 = zoom out
zoom = 1.1

# Compute new step size to "zoom" the grid
step = (side / cells) * zoom

# Compute offset to keep grid centered
total_grid_size = step * cells
offset_x = x + (side - total_grid_size) / 2
offset_y = y + (side - total_grid_size) / 2

grid_width = 8

# Vertical grid lines
for i in range(1, cells):
    xi = offset_x + i * step
    draw.line([xi, y, xi, y + side], fill="white", width=grid_width)

# Horizontal grid lines
for i in range(1, cells):
    yi = offset_y + i * step
    draw.line([x, yi, x + side, yi], fill="white", width=grid_width)

# Draw outer square again for outline
draw.rectangle([x, y, x + side, y + side], outline="orange", width=3)

img.show()