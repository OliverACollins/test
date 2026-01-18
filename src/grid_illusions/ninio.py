from PIL import Image, ImageDraw, ImageFilter

def draw_ninio(
    cells=10,
    side=400,
    img_size=(800, 600),
    grid_zoom=1.05,
    grid_width=4,
    dot_radius=3,
    dot_colour="black",
    dot_outline_colour="white",
    square_colour="white",
    canvas_colour="white",
    vertical_colour="grey",
    horizontal_colour="grey",
    diagonal_colour="grey",
    outline_colour="black",
    outline_width=4,
    blur_strength=0
):
    
    # Anti-aliasing
    aa_scale = 4
    aa = aa_scale
    hi_size = (img_size[0] * aa, img_size[1] * aa)
    
    side *= aa
    grid_width *= aa
    dot_radius *= aa
    outline_width *= aa
    
    img = Image.new("RGB", hi_size, canvas_colour)
    draw = ImageDraw.Draw(img)

    # Centre the square
    x = (img.size[0] - side) // 2
    y = (img.size[1] - side) // 2

    # Fill the square
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
            [xi, offset_y, xi, offset_y + total_grid_size],
            fill=vertical_colour,
            width=grid_width
        )

    # Draw horizontal grid lines
    for i in range(1, cells):
        yi = offset_y + i * step
        draw.line(
            [offset_x, yi, offset_x + total_grid_size, yi],
            fill=horizontal_colour,
            width=grid_width
        )

    # Draw diagonal grid lines
    half = grid_width * 0.25

    for row in range(cells):
        for col in range(cells):
            x0 = offset_x + col * step
            y0 = offset_y + row * step
            x1 = x0 + step
            y1 = y0 + step

            draw.line(
                [x0 + half, y0 + half, x1 - half, y1 - half],
                fill=diagonal_colour,
                width=grid_width
            )

            draw.line(
                [x0 + half, y1 - half, x1 - half, y0 + half],
                fill=diagonal_colour,
                width=grid_width
            )

    # Draw dots at grid intersections
    halo_ratio = 1.25
    outline_radius = int(dot_radius * halo_ratio)

    for i in range(1, cells):
        for j in range(1, cells):
            if i % 2 == 0 and j % 2 == 0:
                xi = offset_x + i * step
                yi = offset_y + j * step

                # White outline (draw first)
                draw.ellipse(
                    [xi - outline_radius, yi - outline_radius,
                    xi + outline_radius, yi + outline_radius],
                    fill=dot_outline_colour
                )

                # Black dot (draw on top)
                draw.ellipse(
                    [xi - dot_radius, yi - dot_radius,
                    xi + dot_radius, yi + dot_radius],
                    fill=dot_colour
                )

    # Draw outer square outline
    draw.rectangle(
        [
            offset_x,
            offset_y,
            offset_x + total_grid_size,
            offset_y + total_grid_size
        ],
        outline=outline_colour,
        width=outline_width
    )

    # Apply blur
    if blur_strength > 0:
        img = img.filter(ImageFilter.GaussianBlur(blur_strength))

    # Downsample for anti-aliasing
    img = img.resize(img_size, Image.LANCZOS)
    return img

# Testing
if __name__ == "__main__":
    img = draw_ninio()
    img.show()