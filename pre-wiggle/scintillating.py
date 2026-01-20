from PIL import Image, ImageDraw, ImageFilter

def draw_scintillating(
    cells=12,
    side=400,
    img_size=(800, 600),
    grid_zoom=1.05,
    grid_width=4,
    dot_radius=3,
    dot_colour="white",
    square_colour="black",
    canvas_colour="white",
    vertical_colour="grey",
    horizontal_colour="grey",
    outline_colour="black",
    outline_width=4,
    blur_strength=0,
):

    # Anti-aliasing
    aa_scale = 4
    aa = aa_scale
    hi_size = (img_size[0] * aa, img_size[1] * aa)

    # Scale spatial parameters
    side *= aa
    grid_width *= aa
    dot_radius *= aa
    outline_width *= aa

    img = Image.new("RGB", hi_size, canvas_colour)
    draw = ImageDraw.Draw(img)

    # Centre the square
    x = (img.size[0] - side) // 2
    y = (img.size[1] - side) // 2

    # Fill the square with black
    draw.rectangle([x, y, x + side, y + side], fill=square_colour)

    # Scale zoom
    step = (side / cells) * grid_zoom

    # Centre the grid
    total_grid_size = step * cells
    offset_x = x + (side - total_grid_size) / 2
    offset_y = y + (side - total_grid_size) / 2

    # Draw vertical grid lines
    for i in range(1, cells):
        xi = offset_x + i * step
        draw.line(
            [xi, y, xi, y + side],
            fill=vertical_colour,
            width=grid_width
        )

    # Draw horizontal grid lines
    for i in range(1, cells):
        yi = offset_y + i * step
        draw.line(
            [x, yi, x + side, yi],
            fill=horizontal_colour,
            width=grid_width
        )

    # Draw dots at grid line intersections
    for i in range(1, cells):
        for j in range(1, cells):
            xi = offset_x + i * step
            yi = offset_y + j * step
            draw.ellipse(
                [
                    xi - dot_radius,
                    yi - dot_radius,
                    xi + dot_radius,
                    yi + dot_radius
                ],
                fill=dot_colour
            )

    # Draw outer square outline
    draw.rectangle(
        [x, y, x + side, y + side],
        outline=outline_colour,
        width=outline_width
    )

    # Apply blur
    if blur_strength > 0:
        img = img.filter(ImageFilter.GaussianBlur(blur_strength * aa))

    # Downsample for anti-aliasing
    img = img.resize(img_size, Image.LANCZOS)

    return img

# Testing
if __name__ == "__main__":
    img = draw_scintillating()
    img.show()