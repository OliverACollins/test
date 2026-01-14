# src/grid_illusions/cli.py
import argparse
from grid_illusions.hermann_grid import draw_hermann_grid 
from grid_illusions.hermann_grid import draw_scintillating_grid
# from grid_illusions.rodframe import draw_rod_frame  # placeholder for future illusions

def main():
    parser = argparse.ArgumentParser(description="Draw a grid or illusion image")

    # Argument to choose the illusion
    parser.add_argument(
        "--illusion",
        type=str,
        default="hermann",
        choices=["hermann", "scintillating"],  # add other illusions here later
        help="Type of illusion to draw"
    )

    parser.add_argument("--cells", type=int, default=4, help="Number of grid cells")
    parser.add_argument("--size", type=int, default=200, help="Size of the square (pixels)")
    parser.add_argument("--img_width", type=int, default=800, help="Width of canvas")
    parser.add_argument("--img_height", type=int, default=600, help="Height of canvas")
    parser.add_argument("--grid_zoom", type=float, default=1.1, help="Zoom factor for the grid")
    parser.add_argument("--grid_width", type=int, default=10, help="Width of grid lines")
    parser.add_argument("--dot_radius", type=int, default=3, help="Radius of dots for scintillating grid")
    parser.add_argument("--save", type=str, default="hermann.png", help="Output filename")

    args = parser.parse_args()

    # Dispatch to the correct illusion function
    if args.illusion == "hermann":
        img = draw_hermann_grid(
            cells=args.cells,
            size=args.side,
            img_size=(args.img_width, args.img_height),
            grid_zoom=args.grid_zoom,
            grid_width=args.grid_width
        )

    elif args.illusion == "scintillating":
        img = draw_scintillating_grid(
            cells=args.cells,
            side=args.side,
            img_size=(args.img_width, args.img_height),
            grid_zoom=args.grid_zoom,
            grid_width=args.grid_width,
            dot_radius=args.dot_radius
        )
    else:
        raise ValueError(f"Unknown illusion type: {args.illusion}")
    

    img.save(args.output)
    print(f"Saved {args.illusion} illusion to {args.output}")
    img.show()

if __name__ == "__main__":
    main()
