from PIL import Image, ImageDraw, ImageFilter

def draw_bergen_grid(cells=10, side=400, img_size=(800, 600), grid_zoom=1.05,
                      grid_width=5, square_colour="black",
                      vertical_colour="white", horizontal_colour="white",
                      outline_colour="orange", outline_width=4,
                      blur_strength=4):
    """
    Draw a square with a grid inside, optionally applying a blur.
    """
    img = Image.new("RGB", img_size, "white")
    draw = ImageDraw.Draw(img)

    # Centre the square
    x = (img.size[0] - side) // 2
    y = (img.size[1] - side) // 2

    # Draw outer square
    draw.rectangle([x, y, x + side, y + side], width=2, fill=square_colour)

    # Scale zoom
    step = (side / cells) * grid_zoom

    # Centre the grid
    total_grid_size = step * cells
    offset_x = x + (side - total_grid_size) / 2
    offset_y = y + (side - total_grid_size) / 2

    # Draw vertical grid lines
    for i in range(1, cells):
        xi = offset_x + i * step
        draw.line([xi, y, xi, y + side], fill=vertical_colour, width=grid_width)

    # Draw horizontal grid lines
    for i in range(1, cells):
        yi = offset_y + i * step
        draw.line([x, yi, x + side, yi], fill=horizontal_colour, width=grid_width)

    # Draw outer square outline
    draw.rectangle([x, y, x + side, y + side], outline=outline_colour, width=outline_width)

    # Apply blur
    if blur_strength > 0:
        img = img.filter(ImageFilter.GaussianBlur(blur_strength))

    return img

# Testing
#if __name__ == "__main__":
    #img = draw_bergen_grid()
    #img.show()