from PIL import Image, ImageDraw, ImageFilter

def draw_scintillating_grid(
    cells=12,
    side=400,
    img_size=(800, 600),
    grid_zoom=1.05,
    grid_width=4,
    dot_radius=3,
    dot_colour="white",
    square_colour="black",
    vertical_colour="grey",
    horizontal_colour="grey",
    outline_colour="black",
    outline_width=4,
    blur_strength=0
):
    # Create image
    img = Image.new("RGB", img_size, "white")
    draw = ImageDraw.Draw(img)

    # Centre the square
    x = (img.size[0] - side) // 2
    y = (img.size[1] - side) // 2

    # Fill the square with black
    draw.rectangle([x, y, x + side, y + side], fill=square_colour)

    # Calculate step size with zoom
    step = (side / cells) * grid_zoom

    # Total grid size and offsets for centering
    total_grid_size = step * cells
    offset_x = x + (side - total_grid_size) / 2
    offset_y = y + (side - total_grid_size) / 2

    # Grid bounds (constrain lines to grid area)
    grid_x0 = offset_x
    grid_x1 = offset_x + total_grid_size
    grid_y0 = offset_y
    grid_y1 = offset_y + total_grid_size

    # Draw vertical grid lines inside grid bounds
    for i in range(1, cells):
        xi = offset_x + i * step
        draw.line([xi, grid_y0, xi, grid_y1], fill=vertical_colour, width=grid_width)

    # Draw horizontal grid lines inside grid bounds
    for i in range(1, cells):
        yi = offset_y + i * step
        draw.line([grid_x0, yi, grid_x1, yi], fill=horizontal_colour, width=grid_width)

    # Draw dots at grid line intersections
    for i in range(1, cells):
        for j in range(1, cells):
            xi = offset_x + i * step
            yi = offset_y + j * step
            draw.ellipse(
                [xi - dot_radius, yi - dot_radius, xi + dot_radius, yi + dot_radius],
                fill=dot_colour
            )

    # Draw outer square outline
    draw.rectangle([x, y, x + side, y + side], outline=outline_colour, width=outline_width)

    # Apply optional blur
    if blur_strength > 0:
        img = img.filter(ImageFilter.GaussianBlur(blur_strength))

    return img

# Example usage
#if __name__ == "__main__":
#    img = draw_scintillating_grid()
#    img.show()
