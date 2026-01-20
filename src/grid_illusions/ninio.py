from PIL import Image, ImageDraw, ImageFilter
import math

def distort_point(
    x, y,
    t,
    orientation,
    strength,
    frequency,
):
    offset = strength * math.sin(2 * math.pi * frequency * t)

    if orientation == "vertical":
        return x + offset, y

    elif orientation == "horizontal":
        return x, y + offset

    elif orientation == "diag_pos":  # ↘
        # perpendicular is (1, -1)
        d = offset / math.sqrt(2)
        return x + d, y - d

    elif orientation == "diag_neg":  # ↗
        # perpendicular is (1, 1)
        d = offset / math.sqrt(2)
        return x + d, y + d

def draw_distorted_line(
    draw,
    start,
    end,
    width,
    fill,
    orientation,
    strength=2,
    frequency=2,
    samples=800,
):
    r = width / 2
    x1, y1 = start
    x2, y2 = end

    for i in range(samples + 1):
        t = i / samples

        # ---- ADD THIS ----
        if orientation == "vertical":
            phase = x1
        elif orientation == "horizontal":
            phase = y1
        else:  # diagonals
            phase = x1 + y1

        t_eff = t + phase * 0.002
        # ------------------

        x = x1 + (x2 - x1) * t
        y = y1 + (y2 - y1) * t

        x, y = distort_point(
            x, y,
            t=t_eff,
            orientation=orientation,
            strength=strength,
            frequency=frequency
        )

        draw.ellipse(
            (x - r, y - r, x + r, y + r),
            fill=fill
        )
        
def draw_ninio(
    cells=8,
    side=600,
    img_size=(1000, 800),
    grid_zoom=1.05,
    grid_width=6,
    wiggle_strength=1,
    wiggle_frequency=2,
    blur_strength=0,
    dot_radius=4.5,
    dot_colour="black",
    dot_outline_colour="white",
    square_colour="white",
    canvas_colour="white",
    vertical_colour="grey",
    horizontal_colour="grey",
    diagonal_colour="grey",
    outline_colour="black",
    outline_width=4
):
    
    # Anti-aliasing
    supersample = 4
    SCALE = supersample
    big_size = (img_size[0] * SCALE, img_size[1] * SCALE)

    img_big = Image.new("RGB", big_size, canvas_colour)
    draw = ImageDraw.Draw(img_big)

    grid_layer = Image.new("RGBA", big_size, (0, 0, 0, 0))
    grid_draw = ImageDraw.Draw(grid_layer)

    side *= SCALE
    grid_width *= SCALE
    dot_radius *= SCALE
    outline_width *= SCALE
    raw_wiggle = wiggle_strength
    wiggle_strength *= SCALE

    # Centre the square
    x = (big_size[0] - side) // 2
    y = (big_size[1] - side) // 2

    # Draw square background
    grid_draw.rectangle([x, y, x + side, y + side], fill=square_colour)

    # Scale zoom
    step = (side / cells) * grid_zoom

    # Centre the grid
    total = step * cells
    offset_x = x + (side - total) / 2
    offset_y = y + (side - total) / 2

    # Draw vertical grid lines
    for i in range(1, cells):
        xi = offset_x + i * step

        if raw_wiggle == 0:
            grid_draw.line(
                [xi, y, xi, y + side],
                fill=vertical_colour,
                width=grid_width
            )
        else:
            draw_distorted_line(
                grid_draw,
                (xi, y),
                (xi, y + side),
                width=grid_width,
                fill=vertical_colour,
                orientation="vertical",
                strength=wiggle_strength,
                frequency=wiggle_frequency,
            )

    # Draw horizontal grid lines
    for i in range(1, cells):
        yi = offset_y + i * step

        if raw_wiggle == 0:
            grid_draw.line(
                [x, yi, x + side, yi],
                fill=horizontal_colour,
                width=grid_width
            )
        else:
            draw_distorted_line(
                grid_draw,
                (x, yi),
                (x + side, yi),
                width=grid_width,
                fill=horizontal_colour,
                orientation="horizontal",
                strength=wiggle_strength,
                frequency=wiggle_frequency,
            )

    # Draw diagonal grid lines
    for row in range(cells):
        for col in range(cells):
            x0 = offset_x + col * step
            y0 = offset_y + row * step
            x1 = x0 + step
            y1 = y0 + step

            if raw_wiggle == 0:
                grid_draw.line(
                    [x0, y0, x1, y1],
                    fill=diagonal_colour,
                    width=grid_width
                )
                grid_draw.line(
                    [x0, y1, x1, y0],
                    fill=diagonal_colour,
                    width=grid_width
                )
            else:
                draw_distorted_line(
                    grid_draw,
                    (x0, y0),
                    (x1, y1),
                    width=grid_width,
                    fill=diagonal_colour,
                    orientation="diag_pos",
                    strength=wiggle_strength,
                    frequency=wiggle_frequency * math.sqrt(2),
                )

                draw_distorted_line(
                    grid_draw,
                    (x0, y1),
                    (x1, y0),
                    width=grid_width,
                    fill=diagonal_colour,
                    orientation="diag_neg",
                    strength=wiggle_strength,
                    frequency=wiggle_frequency * math.sqrt(2),
                )

    # Draw dots at grid intersections
    halo_ratio = 1.25
    outline_radius = int(dot_radius * halo_ratio)

    for i in range(1, cells):
        for j in range(1, cells):
            if i % 2 == 0 and j % 2 == 0:
                xi0 = offset_x + i * step
                yi0 = offset_y + j * step

                xd, yd = xi0, yi0

                for _ in range(3):
                    ty = (yd - y) / side
                    tx = (xd - x) / side

                    xd, _ = distort_point(
                        xi0, yd,
                        t=ty,
                        orientation="vertical",
                        strength=wiggle_strength,
                        frequency=wiggle_frequency
                    )

                    _, yd = distort_point(
                        xd, yi0,
                        t=tx,
                        orientation="horizontal",
                        strength=wiggle_strength,
                        frequency=wiggle_frequency
                    )

                # halo
                grid_draw.ellipse(
                    [xd - outline_radius, yd - outline_radius,
                    xd + outline_radius, yd + outline_radius],
                    fill=dot_outline_colour
                )

                # dot
                grid_draw.ellipse(
                    [xd - dot_radius, yd - dot_radius,
                    xd + dot_radius, yd + dot_radius],
                    fill=dot_colour
                )

    # Fill the square
    mask = Image.new("L", big_size, 0)
    mask_draw = ImageDraw.Draw(mask)

    mask_draw.rectangle(
        [x, y, x + side, y + side],
        fill=255
    )

    # Clip the grid to the square
    grid_layer.putalpha(mask)

    # Alpha-composite grid over square
    img_big = Image.alpha_composite(
        img_big.convert("RGBA"),
        grid_layer
    ).convert("RGB")

    # Draw outer square outline
    final_draw = ImageDraw.Draw(img_big)
    final_draw.rectangle(
        [x, y, x + side, y + side],
        outline=outline_colour,
        width=outline_width,
    )

    # Apply blur
    if blur_strength > 0:
        img_big = img_big.filter(
            ImageFilter.GaussianBlur(blur_strength * SCALE)
        )

    # Downsample for anti-aliasing
    img = img_big.resize(img_size, Image.LANCZOS)
    return img

# Testing
if __name__ == "__main__":
    img = draw_ninio()
    img.show()