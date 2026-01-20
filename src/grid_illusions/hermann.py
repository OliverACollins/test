from PIL import Image, ImageDraw, ImageFilter
import math

def draw_distorted_line(
    draw,
    start,
    end,
    width,
    fill,
    strength=2,
    frequency=2,
    samples=800,
):
    r = width / 2

    x1, y1 = start
    x2, y2 = end

    for i in range(samples + 1):
        t = i / samples
        x = x1 + (x2 - x1) * t
        y = y1 + (y2 - y1) * t

        offset = strength * math.sin(2 * math.pi * frequency * t)

        if abs(x2 - x1) < abs(y2 - y1):  # vertical distorted grid line
            x += offset
        else:                            # horizontal distorted grid line
            y += offset

        draw.ellipse(
            (x - r, y - r, x + r, y + r),
            fill=fill,
            outline=None
        )

def draw_hermann(
    cells=5,
    side=600,
    img_size=(1000, 800),
    grid_zoom=1.1,
    grid_width=15,
    wiggle_strength=0,
    wiggle_frequency=0,
    blur_strength=0,
    square_colour="black",
    canvas_colour="white",
    vertical_colour="white",
    horizontal_colour="white",
    outline_colour="black",
    outline_width=4,
):
    # Anti-aliasing
    supersample=4
    SCALE = supersample
    big_size = (img_size[0] * SCALE, img_size[1] * SCALE)

    img_big = Image.new("RGB", big_size, canvas_colour)
    draw = ImageDraw.Draw(img_big)

    grid_layer = Image.new("RGBA", big_size, (0, 0, 0, 0))
    grid_draw = ImageDraw.Draw(grid_layer)

    side *= SCALE
    grid_width *= SCALE
    outline_width *= SCALE
    raw_wiggle = wiggle_strength
    wiggle_strength *= SCALE

    # Centre the square
    x = (big_size[0] - side) // 2
    y = (big_size[1] - side) // 2

    # Fill the square with black
    draw.rectangle([x, y, x + side, y + side], fill=square_colour)

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
                strength=wiggle_strength,
                frequency=wiggle_frequency,
            )

    mask = Image.new("L", big_size, 0)
    mask_draw = ImageDraw.Draw(mask)

    mask_draw.rectangle(
        [x, y, x + side, y + side],
        fill=255
    )

    img_big = Image.composite(
    grid_layer,
    img_big,
    mask
)

    # Draw outer square outline
    final_draw = ImageDraw.Draw(img_big)
    final_draw.rectangle(
        [x, y, x + side, y + side],
        outline=outline_colour,
        width=outline_width
    )

    # Apply blur
    if blur_strength > 0:
        img_big = img_big.filter(
            ImageFilter.GaussianBlur(blur_strength * SCALE)
        )

    # Downsample
    img = img_big.resize(img_size, Image.LANCZOS)
    return img

# Testing
if __name__ == "__main__":
    img = draw_hermann()
    img.show()