import argparse
from grid_illusions.hermann_grid import draw_hermann_grid
from grid_illusions.scintillating_grid import draw_scintillating_grid
from grid_illusions.bergen_grid import draw_bergen_grid


def main():
    parser = argparse.ArgumentParser(description="Draw a grid illusion!", formatter_class=argparse.ArgumentDefaultsHelpFormatter, add_help=False)
    subparsers = parser.add_subparsers(dest="illusion", required=True)

    parser.add_argument(
    "--help",
    action="help",
    help="Help for CLI"
)
    
    # ---- Hermann ----
    hermann = subparsers.add_parser(
        "hermann",
        help="Hermann grid illusion",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    hermann.add_argument("--cells", type=int, default=5, metavar="", help="Number of grid cells")
    hermann.add_argument("--size", type=int, default=400, metavar="", help="Size of the square (pixels)")
    hermann.add_argument("--img_width", type=int, default=800, metavar="", help="Width of canvas")
    hermann.add_argument("--img_height", type=int, default=600, metavar="", help="Height of canvas")
    hermann.add_argument("--grid_zoom", type=float, default =1.1, metavar="", help="Zoom factor for the grid")
    hermann.add_argument("--grid_width", type=int, default=15, metavar="", help="Width of grid lines")
    hermann.add_argument("--blur_strength", type=int, default=0, metavar="", help="Strength of Gaussian blur")
    hermann.add_argument("--square_colour", type=str, default="black", metavar="", help="Square fill colour")
    hermann.add_argument("--vertical_colour", type=str, default="white", metavar="", help="Vertical grid line colour")
    hermann.add_argument("--horizontal_colour", type=str, default="white", metavar="", help="Horizontal grid line colour")
    hermann.add_argument("--outline_colour", type =str, default="black", metavar="", help="Colour outline for square")
    hermann.add_argument("--outline_width", type=int, default=4, metavar="", help="Width of square outline")
    hermann.add_argument("--save", type=str, default="hermann.png", metavar="", help="Output filename (MUST specify file extension)")

    # ---- Scintillating ----
    scintillating = subparsers.add_parser(
        "scintillating",
        help="Scintillating grid illusion",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    scintillating.add_argument("--cells", type=int, default=12, metavar="", help="Number of grid cells")
    scintillating.add_argument("--size", type=int, default =400, metavar="", help="Size of the square (pixels)")
    scintillating.add_argument("--img_width", type=int, default=800, metavar="", help="Width of canvas")
    scintillating.add_argument("--img_height", type=int, default=600, metavar="", help="Height of canvas")
    scintillating.add_argument("--grid_zoom", type=float, default=1.05, metavar="", help="Zoom factor for the grid")
    scintillating.add_argument("--grid_width", type=int, default=4, metavar="", help="Width of grid lines")
    scintillating.add_argument("--blur_strength", type=int, default=0, metavar="", help="Strength of Gaussian blur")
    scintillating.add_argument("--dot_radius", type=int, default=3, metavar="", help="Radius of dots")
    scintillating.add_argument("--dot_colour", type=str, default="white", metavar="", help="Colour of dots")
    scintillating.add_argument("--square_colour", type=str, default="black", metavar="", help="Square fill colour")
    scintillating.add_argument("--vertical_colour", type=str, default="grey", metavar="", help="Vertical grid line colour")
    scintillating.add_argument("--horizontal_colour", type=str, default="grey", metavar="", help="Horizontal grid line colour")
    scintillating.add_argument("--outline_colour", type =str, default="black", metavar="", help="Colour outline for square")
    scintillating.add_argument("--outline_width", type=int, default=4, metavar="", help="Width of square outline")
    scintillating.add_argument("--save", type=str, default="scintillating.png", metavar="", help="Output filename (MUST specify file extension)")

    # ---- Bergen ----
    bergen = subparsers.add_parser(
        "bergen",
        help="Bergen grid illusion",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    bergen.add_argument("--cells", type=int, default=10, metavar="", help="Number of grid cells")
    bergen.add_argument("--size", type=int, default=400, metavar="", help="Size of the square (pixels)")
    bergen.add_argument("--img_width", type=int, default=800, metavar="", help="Width of canvas")
    bergen.add_argument("--img_height", type=int, default=600, metavar="", help="Height of canvas")
    bergen.add_argument("--grid_zoom", type=float, default=1.05, metavar="", help="Zoom factor for the grid")
    bergen.add_argument("--grid_width", type=int, default=5, metavar="", help="Width of grid lines")
    bergen.add_argument("--blur_strength", type=int, default=4, metavar="", help="Strength of Gaussian blur")
    bergen.add_argument("--square_colour", type=str, default="black", metavar="", help="Square fill colour")
    bergen.add_argument("--vertical_colour", type=str, default="white", metavar="", help="Vertical grid line colour")
    bergen.add_argument("--horizontal_colour", type=str, default="white", metavar="", help="Horizontal grid line colour")
    bergen.add_argument("--outline_colour", type =str, default="black", metavar="", help="Colour outline for square")
    bergen.add_argument("--outline_width", type=int, default=4, metavar="", help="Width of square outline")
    bergen.add_argument("--save", type=str, default="bergen.png", metavar="", help="Output filename (MUST specify file extension)")

    args = parser.parse_args()

    if args.illusion == "hermann":
        img = draw_hermann_grid(
            cells=args.cells,
            side=args.size,
            img_size=(args.img_width, args.img_height),
            grid_zoom=args.grid_zoom,
            grid_width=args.grid_width,
            blur_strength=args.blur_strength,
            square_colour=args.square_colour,
            vertical_colour=args.vertical_colour,
            horizontal_colour=args.horizontal_colour,
            outline_colour=args.outline_colour,
            outline_width=args.outline_width,
        )

    elif args.illusion == "scintillating":
        img = draw_scintillating_grid(
            cells=args.cells,
            side=args.size,
            img_size=(args.img_width, args.img_height),
            grid_zoom=args.grid_zoom,
            grid_width=args.grid_width,
            blur_strength=args.blur_strength,
            dot_radius=args.dot_radius,
            dot_colour=args.dot_colour,
            square_colour=args.square_colour,
            vertical_colour=args.vertical_colour,
            horizontal_colour=args.horizontal_colour,
            outline_colour=args.outline_colour,
            outline_width=args.outline_width,
        )

    elif args.illusion == "bergen":
        img = draw_bergen_grid(
            cells=args.cells,
            side=args.size,
            img_size=(args.img_width, args.img_height),
            grid_zoom=args.grid_zoom,
            grid_width=args.grid_width,
            blur_strength=args.blur_strength,
            square_colour=args.square_colour,
            vertical_colour=args.vertical_colour,
            horizontal_colour=args.horizontal_colour,
            outline_colour=args.outline_colour,
            outline_width=args.outline_width,
        )

    img.save(args.save)
    print(f"Saved {args.illusion} illusion to {args.save}")
    img.show()


if __name__ == "__main__":
    main()