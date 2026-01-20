from PIL import Image, ImageDraw, ImageFilter

def draw_mcanany_levine(
    cells=10,
    side=600,
    img_size=(1000, 800),
    grid_zoom=1.05,
    grid_width=8,
    dot_radius=4,
    dot_colour="white",
    square_colour="black",
    canvas_colour="white",
    vertical_colour="#a6a6a6",
    horizontal_colour="#a6a6a6",
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

    # Draw dots
    for j in range(1, cells):
        row_type = j % 4

        if row_type == 1:
            # 3-dot row: left, centre, right
            cols = [1, cells // 2, cells - 1]

        elif row_type == 3:
            # 2-dot row: left, right
            cols = [3, cells -3]

        else:
            continue

        yi = offset_y + j * step

        for i in cols:
            if 1 <= i < cells:
                xi = offset_x + i * step
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
    img = draw_mcanany_levine()
    img.show()