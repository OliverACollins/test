import argparse
from .hermann_grid import draw_grid

def main():
    parser = argparse.ArgumentParser(description="Draw a grid image")
    parser.add_argument("--cells", type=int, default=4, help="Number of grid cells")
    parser.add_argument("--side", type=int, default=200, help="Size of the square (pixels)")
    parser.add_argument("--img_width", type=int, default=800, help="Width of canvas")
    parser.add_argument("--img_height", type=int, default=600, help="Height of canvas")
    parser.add_argument("--grid_zoom", type=float, default=1.0, help="Zoom factor for the grid")
    parser.add_argument("--grid_width", type=int, default=10, help="Width of grid lines")
    parser.add_argument("--output", type=str, default="grid.png", help="Output filename")
    
    args = parser.parse_args()
    
    img = draw_grid(
        cells=args.cells,
        side=args.side,
        img_size=(args.img_width, args.img_height),
        grid_zoom=args.grid_zoom,
        grid_width=args.grid_width
    )
    
    img.save(args.output)
    print(f"Grid image saved to {args.output}")
    img.show()

if __name__ == "__main__":
    main()
