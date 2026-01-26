from PIL import Image, ImageDraw, ImageFilter

def draw_ninio(
    cells=(16, 16), #w, h
    grid_size=(800, 575), #w, h
    img_size=(1000, 800), #w, h
    grid_zoom=1.2,
    grid_width=6,
    dot_radius=4.5,
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
    supersample = 4
    SCALE = supersample
    big_size = (img_size[0] * SCALE, img_size[1] * SCALE)

    img_big = Image.new("RGB", big_size, canvas_colour)

    grid_layer = Image.new("RGBA", big_size, (0, 0, 0, 0))
    grid_draw = ImageDraw.Draw(grid_layer)

    grid_w, grid_h = grid_size
    grid_w *= SCALE
    grid_h *= SCALE

    grid_width *= SCALE
    dot_radius *= SCALE
    outline_width *= SCALE

    # Centre the square
    x = (big_size[0] - grid_w) // 2
    y = (big_size[1] - grid_h) // 2

    # Fill the square
    grid_draw.rectangle([x, y, x + grid_w, y + grid_h], fill=square_colour)

    cols, rows = cells

    # --- COVER scaling: grid ALWAYS fills the frame ---
    cell_size = max(
        grid_w / cols,
        grid_h / rows
    ) * grid_zoom

    step_x = step_y = cell_size

    total_w = step_x * cols
    total_h = step_y * rows

    # Anchor grid to the frame (no centering = no margins)
    offset_x = x + (grid_w - total_w) / 2
    offset_y = y + (grid_h - total_h) / 2

    # Draw vertical grid lines
    for i in range(1, cols):
        xi = offset_x + i * step_x
        if xi >= offset_x + total_w:
            break
        grid_draw.line(
            [xi, offset_y, xi, offset_y + total_h],
            fill=vertical_colour,
            width=grid_width
        )


    # Draw horizontal grid lines
    for j in range(1, rows):
        yi = offset_y + j * step_y
        if yi >= offset_y + total_h:
            break
        grid_draw.line(
            [offset_x, yi, offset_x + total_w, yi],
            fill=horizontal_colour,
            width=grid_width
        )


    half = grid_width * 0.25
    
    for row in range(rows):
        for col in range(cols):
            x0 = offset_x + col * step_x
            y0 = offset_y + row * step_y

            if x0 >= offset_x + total_w or y0 >= offset_y + total_h:
                continue

            x1 = x0 + step_x
            y1 = y0 + step_y

            if (row + col) % 2 == 0:
                # ↘ diagonal
                grid_draw.line(
                    [x0 + half, y0 + half,
                    x1 - half, y1 - half],
                    fill=diagonal_colour,
                    width=grid_width
                )
            else:
                # ↗ diagonal
                grid_draw.line(
                    [x0 + half, y1 - half,
                    x1 - half, y0 + half],
                    fill=diagonal_colour,
                    width=grid_width
                )

    # --- Draw dots at diagonal + orthogonal intersections ---
    halo_ratio = 1.25
    outline_radius = dot_radius * halo_ratio

    dots_per_row = 4

    dot_stride_x = cols // dots_per_row
    dot_stride_y = rows // dots_per_row

    for j in range(0, rows, dot_stride_y):
        for i in range(0, cols, dot_stride_x):

            xi = offset_x + (i + 2) * step_x
            yi = offset_y + j * step_y

            if xi >= offset_x + total_w or yi >= offset_y + total_h:
                continue

            grid_draw.ellipse(
                [xi - outline_radius, yi - outline_radius,
                xi + outline_radius, yi + outline_radius],
                fill=dot_outline_colour
            )

            grid_draw.ellipse(
                [xi - dot_radius, yi - dot_radius,
                xi + dot_radius, yi + dot_radius],
                fill=dot_colour
            )




    mask = Image.new("L", big_size, 0)
    mask_draw = ImageDraw.Draw(mask)

    mask_draw.rectangle(
        [x, y, x + grid_w, y + grid_h],
        fill=255
    )

    grid_layer.putalpha(mask)

    img_big = Image.alpha_composite(
    img_big.convert("RGBA"),
    grid_layer
    ).convert("RGB")
    

    ImageDraw.Draw(img_big).rectangle(
    [x, y, x + grid_w, y + grid_h],
    outline=outline_colour,
    width=outline_width
    )

    # Apply blur
    if blur_strength > 0:
        img_big = img_big.filter(ImageFilter.GaussianBlur(blur_strength))

    # Downsample for anti-aliasing
    img = img_big.resize(img_size, Image.LANCZOS)
    return img

# Testing
if __name__ == "__main__":
    img = draw_ninio()
    img.show()