from PIL import Image, ImageDraw

def draw_scintillating_grid(cells=12, side=400, img_size=(800, 600), grid_zoom=1.05, grid_width=4, dot_radius=3, outline_colour="orange", outline_width=4):
    """
    Draw a scintillating grid illusion.
    
    Parameters:
        cells (int): Number of grid cells
        side (int): Size of the square
        img_size (tuple): Size of the canvas
        grid_zoom (float): Zoom factor for the grid
        grid_width (int): Width of grid lines
        dot_radius (int): Radius of the black dots at intersections
    
    Returns:
        PIL.Image: The generated image
    """
    img = Image.new("RGB", img_size, "white")
    draw = ImageDraw.Draw(img)

    # Centre the square
    x = (img.size[0] - side) // 2
    y = (img.size[1] - side) // 2

    # Fill the square with black
    draw.rectangle([x, y, x + side, y + side], fill="black")

    # Scale zoom
    step = (side / cells) * grid_zoom

    # Centre the grid
    total_grid_size = step * cells
    offset_x = x + (side - total_grid_size) / 2
    offset_y = y + (side - total_grid_size) / 2

    # Draw vertical grid lines
    for i in range(1, cells):
        xi = offset_x + i * step
        draw.line([xi, y, xi, y + side], fill="grey", width=grid_width)

    # Draw horizontal grid lines
    for i in range(1, cells):
        yi = offset_y + i * step
        draw.line([x, yi, x + side, yi], fill="grey", width=grid_width)

    # Draw dots at grid line intersections
    for i in range(1, cells):
        for j in range(1, cells):
            xi = offset_x + i * step
            yi = offset_y + j * step
            draw.ellipse(
                [xi - dot_radius, yi - dot_radius, xi + dot_radius, yi + dot_radius],
                fill="white"
            )

    # Draw outer square outline
    draw.rectangle([x, y, x + side, y + side], outline=outline_colour, width=outline_width)

    return img

# Testing
#if __name__ == "__main__":
    #img = draw_scintillating_grid()
    #img.show()
