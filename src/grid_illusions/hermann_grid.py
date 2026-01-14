# src/grid_illusions/hermann_grid.py
from PIL import Image, ImageDraw

def draw_hermann_grid(cells=4, side=400, img_size=(800, 600), grid_zoom=1.1, grid_width=10):
    """
    Draw a square with a grid inside.

    Parameters:
        cells (int): Number of grid cells (resolution).
        side (int): Size of the square.
        img_size (tuple): Size of the canvas (width, height).
        grid_zoom (float): Zoom factor for the grid.
        grid_width (int): Width of the grid lines.

    Returns:
        PIL.Image: The generated image.
    """
    img = Image.new("RGB", img_size, "white")
    draw = ImageDraw.Draw(img)

    # Center the square
    x = (img.size[0] - side) // 2
    y = (img.size[1] - side) // 2

    # Draw outer square
    draw.rectangle([x, y, x + side, y + side], width=2, fill="black")

    # Step size for grid lines, scaled by zoom
    step = (side / cells) * grid_zoom

    # Offset to center the grid
    total_grid_size = step * cells
    offset_x = x + (side - total_grid_size) / 2
    offset_y = y + (side - total_grid_size) / 2

    # Draw vertical grid lines
    for i in range(1, cells):
        xi = offset_x + i * step
        draw.line([xi, y, xi, y + side], fill="white", width=grid_width)

    # Draw horizontal grid lines
    for i in range(1, cells):
        yi = offset_y + i * step
        draw.line([x, yi, x + side, yi], fill="white", width=grid_width)

    # Draw outer square outline
    draw.rectangle([x, y, x + side, y + side], outline="pink", width=4)

    return img

# Example usage
if __name__ == "__main__":
    img = draw_hermann_grid()
    img.show()
