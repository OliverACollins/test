import argparse
from grid_illusions.hermann_grid import draw_hermann_grid
from grid_illusions.scintillating_grid import draw_scintillating_grid

ILLUSION_DEFAULTS = {
    "hermann": {
        "cells": 5,
        "size": 400,
        "grid_zoom": 1.1,
        "grid_width": 15,
        "vertical_colour": "white",
        "horizontal_colour": "white",
    },
    "scintillating": {
        "cells": 12,
        "size": 400,
        "grid_zoom": 1.05,
        "grid_width": 4,
        "dot_radius": 3,
        "vertical_colour": "grey",
        "horizontal_colour": "grey",
    }
}

def main():
    parser = argparse.ArgumentParser(description="Draw a grid illusion!", add_help = False)
    parser.add_argument("--help", action="help", help="Help for CLI")
    parser.add_argument("--illusion", type=str, default="hermann", metavar="", help=f"Type of illusion to draw  {{{','.join(ILLUSION_DEFAULTS.keys())}}}")
    parser.add_argument("--cells", type=int, metavar="", help="Number of grid cells")
    parser.add_argument("--size", type=int, metavar="", help="Size of the square (pixels)")
    parser.add_argument("--img_width", type=int, default=800, metavar="", help="Width of canvas")
    parser.add_argument("--img_height", type=int, default=600, metavar="", help="Height of canvas")
    parser.add_argument("--grid_zoom", type=float, metavar="", help="Zoom factor for the grid")
    parser.add_argument("--grid_width", type=int, metavar="", help="Width of grid lines")
    parser.add_argument("--dot_radius", type=int, metavar="", help="Radius of dots (ONLY for scintillating grid)")
    parser.add_argument("--dot_colour", type=str, default="white", metavar="", help="Colour of dots (ONLY for scintillating grid)")
    parser.add_argument("--square_colour", default="black", metavar="", help="Square fill colour")
    parser.add_argument("--vertical_colour", metavar="", help="Vertical grid line colour")
    parser.add_argument("--horizontal_colour", metavar="", help="Horizontal grid line colour")
    parser.add_argument("--outline_colour", type =str, default="orange", metavar="", help="Colour outline for square")
    parser.add_argument("--outline_width", type=int, default=4, metavar="", help="Width of square outline")
    parser.add_argument("--save", type=str, default="illusion.png", metavar="", help="Output filename (MUST specify file extension)")

    args = parser.parse_args()

    defaults = ILLUSION_DEFAULTS[args.illusion]
    for key, value in defaults.items():
        if getattr(args, key) is None:
            setattr(args, key, value)

    if args.illusion == "hermann":
        img = draw_hermann_grid(
            cells=args.cells,
            side=args.size,
            img_size=(args.img_width, args.img_height),
            grid_zoom=args.grid_zoom,
            grid_width=args.grid_width,
            square_colour=args.square_colour,
            vertical_colour=args.vertical_colour,
            horizontal_colour=args.horizontal_colour,
            outline_colour=args.outline_colour,
            outline_width=args.outline_width
        )
    elif args.illusion == "scintillating":
        img = draw_scintillating_grid(
            cells=args.cells,
            side=args.size,
            img_size=(args.img_width, args.img_height),
            grid_zoom=args.grid_zoom,
            grid_width=args.grid_width,
            dot_radius=args.dot_radius,
            dot_colour=args.dot_colour,
            square_colour=args.square_colour,
            vertical_colour=args.vertical_colour,
            horizontal_colour=args.horizontal_colour,
            outline_colour=args.outline_colour,
            outline_width=args.outline_width
        )

    img.save(args.save)
    print(f"Saved {args.illusion} illusion to {args.save}")
    img.show()

if __name__ == "__main__":
    main()
