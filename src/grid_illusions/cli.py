import argparse
from grid_illusions.hermann_grid import draw_hermann_grid
from grid_illusions.scintillating_grid import draw_scintillating_grid

# Per-illusion default settings
ILLUSION_DEFAULTS = {
    "hermann": {
        "cells": 4,
        "size": 400,
        "grid_zoom": 1.1,
        "grid_width": 10,
    },
    "scintillating": {
        "cells": 12,
        "size": 400,
        "grid_zoom": 1.05,
        "grid_width": 4,
        "dot_radius": 3
    }
}

def main():
    parser = argparse.ArgumentParser(description="Draw a grid or illusion image")

    parser.add_argument("--illusion", type=str, default="hermann",
                        choices=ILLUSION_DEFAULTS.keys(),
                        help="Type of illusion to draw")
    parser.add_argument("--cells", type=int, help="Number of grid cells")
    parser.add_argument("--size", type=int, help="Size of the square (pixels)")
    parser.add_argument("--img_width", type=int, default=800, help="Width of canvas")
    parser.add_argument("--img_height", type=int, default=600, help="Height of canvas")
    parser.add_argument("--grid_zoom", type=float, help="Zoom factor for the grid")
    parser.add_argument("--grid_width", type=int, help="Width of grid lines")
    parser.add_argument("--dot_radius", type=int, help="Radius of dots (for scintillating grid)")
    parser.add_argument("--outline", type = str, default = "orange", help = "Colour outline for square")
    parser.add_argument("--save", type=str, default="grid.png", help="Output filename")

    args = parser.parse_args()

    # Apply per-illusion defaults for any argument that was not provided
    defaults = ILLUSION_DEFAULTS[args.illusion]
    for key, value in defaults.items():
        if getattr(args, key) is None:
            setattr(args, key, value)

    # Dispatch
    if args.illusion == "hermann":
        img = draw_hermann_grid(
            cells=args.cells,
            side=args.size,
            img_size=(args.img_width, args.img_height),
            grid_zoom=args.grid_zoom,
            grid_width=args.grid_width,
            outline=args.outline
        )
    elif args.illusion == "scintillating":
        img = draw_scintillating_grid(
            cells=args.cells,
            side=args.size,
            img_size=(args.img_width, args.img_height),
            grid_zoom=args.grid_zoom,
            grid_width=args.grid_width,
            dot_radius=args.dot_radius,
            outline=args.outline
        )

    img.save(args.save)
    print(f"Saved {args.illusion} illusion to {args.save}")
    img.show()

if __name__ == "__main__":
    main()
