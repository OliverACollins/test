import argparse
from grid_illusions.hermann import draw_hermann
from grid_illusions.scintillating import draw_scintillating
from grid_illusions.bergen import draw_bergen
from grid_illusions.ninio import draw_ninio
from grid_illusions.mcanany_levine import draw_mcanany_levine


def main():
    parser = argparse.ArgumentParser(description="Draw a grid illusion!", formatter_class=argparse.ArgumentDefaultsHelpFormatter, add_help=False)
    subparsers = parser.add_subparsers(dest="illusion", required=True)

    parser.add_argument(
    "--help",
    action="help",
    help="Help for CLI"
)
    
    # Hermann grid
    hermann = subparsers.add_parser(
        "hermann",
        help="Hermann grid illusion",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        add_help=False
    )
    
    hermann.add_argument("--help", action="help", help="")
    hermann.add_argument("--cells", type=int, default=5, metavar="", help="Number of grid cells")
    hermann.add_argument("--size", type=int, default=400, metavar="", help="Size of square (pixels)")
    hermann.add_argument("--img_width", type=int, default=800, metavar="", help="Width of canvas (pixels)")
    hermann.add_argument("--img_height", type=int, default=600, metavar="", help="Height of canvas (pixels)")
    hermann.add_argument("--grid_zoom", type=float, default =1.1, metavar="", help="Zoom factor for grid")
    hermann.add_argument("--grid_width", type=int, default=15, metavar="", help="Width of grid lines")
    hermann.add_argument("--blur_strength", type=int, default=0, metavar="", help="Strength of Gaussian blur")
    hermann.add_argument("--square_colour", type=str, default="black", metavar="", help="Square fill colour")
    hermann.add_argument("--canvas_colour", type=str, default="white", metavar="", help="Canvas (background) colour")
    hermann.add_argument("--vertical_colour", type=str, default="white", metavar="", help="Vertical grid line colour")
    hermann.add_argument("--horizontal_colour", type=str, default="white", metavar="", help="Horizontal grid line colour")
    hermann.add_argument("--outline_colour", type =str, default="black", metavar="", help="Colour outline for square")
    hermann.add_argument("--outline_width", type=int, default=4, metavar="", help="Width of outline for square")
    hermann.add_argument("--save", type=str, default="hermann.png", metavar="", help="Output filename (MUST specify file extension)")

    # Scintillating grid
    scintillating = subparsers.add_parser(
        "scintillating",
        help="Scintillating grid illusion",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        add_help=False
    )

    scintillating.add_argument("--help", action="help", help="")
    scintillating.add_argument("--cells", type=int, default=12, metavar="", help="Number of grid cells")
    scintillating.add_argument("--size", type=int, default=400, metavar="", help="Size of square (pixels)")
    scintillating.add_argument("--img_width", type=int, default=800, metavar="", help="Width of canvas (pixels)")
    scintillating.add_argument("--img_height", type=int, default=600, metavar="", help="Height of canvas (pixels)")
    scintillating.add_argument("--grid_zoom", type=float, default=1.05, metavar="", help="Zoom factor for grid")
    scintillating.add_argument("--grid_width", type=int, default=4, metavar="", help="Width of grid lines")
    scintillating.add_argument("--blur_strength", type=int, default=0, metavar="", help="Strength of Gaussian blur")
    scintillating.add_argument("--dot_radius", type=int, default=3, metavar="", help="Radius of dots")
    scintillating.add_argument("--dot_colour", type=str, default="white", metavar="", help="Colour of dots")
    scintillating.add_argument("--square_colour", type=str, default="black", metavar="", help="Square fill colour")
    scintillating.add_argument("--canvas_colour", type=str, default="white", metavar="", help="Canvas (background) colour")
    scintillating.add_argument("--vertical_colour", type=str, default="grey", metavar="", help="Vertical grid line colour")
    scintillating.add_argument("--horizontal_colour", type=str, default="grey", metavar="", help="Horizontal grid line colour")
    scintillating.add_argument("--outline_colour", type =str, default="black", metavar="", help="Colour outline for square")
    scintillating.add_argument("--outline_width", type=int, default=4, metavar="", help="Width of outline for square")
    scintillating.add_argument("--save", type=str, default="scintillating.png", metavar="", help="Output filename (MUST specify file extension)")

    # Bergen grid
    bergen = subparsers.add_parser(
        "bergen",
        help="Bergen grid illusion",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        add_help=False
    )
    
    bergen.add_argument("--help", action="help", help="")
    bergen.add_argument("--cells", type=int, default=10, metavar="", help="Number of grid cells")
    bergen.add_argument("--size", type=int, default=400, metavar="", help="Size of square (pixels)")
    bergen.add_argument("--img_width", type=int, default=800, metavar="", help="Width of canvas (pixels)")
    bergen.add_argument("--img_height", type=int, default=600, metavar="", help="Height of canvas (pixels)")
    bergen.add_argument("--grid_zoom", type=float, default=1.05, metavar="", help="Zoom factor for grid")
    bergen.add_argument("--grid_width", type=int, default=5, metavar="", help="Width of grid lines")
    bergen.add_argument("--blur_strength", type=int, default=4, metavar="", help="Strength of Gaussian blur")
    bergen.add_argument("--square_colour", type=str, default="black", metavar="", help="Square fill colour")
    bergen.add_argument("--canvas_colour", type=str, default="white", metavar="", help="Canvas (background) colour")
    bergen.add_argument("--vertical_colour", type=str, default="white", metavar="", help="Vertical grid line colour")
    bergen.add_argument("--horizontal_colour", type=str, default="white", metavar="", help="Horizontal grid line colour")
    bergen.add_argument("--outline_colour", type =str, default="black", metavar="", help="Colour outline for square")
    bergen.add_argument("--outline_width", type=int, default=4, metavar="", help="Width of outline for square")
    bergen.add_argument("--save", type=str, default="bergen.png", metavar="", help="Output filename (MUST specify file extension)")

    # Ninio's extinction grid
    ninio = subparsers.add_parser(
        "ninio",
        help="Ninio's extinction illusion",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        add_help=False
    )

    ninio.add_argument("--help", action="help", help="")
    ninio.add_argument("--cells", type=int, default=10, metavar="", help="Number of grid cells")
    ninio.add_argument("--size", type=int, default=400, metavar="", help="Size of square (pixels)")
    ninio.add_argument("--img_width", type=int, default=800, metavar="", help="Width of canvas (pixels)")
    ninio.add_argument("--img_height", type=int, default=600, metavar="", help="Height of canvas (pixels)")
    ninio.add_argument("--grid_zoom", type=float, default=1.05, metavar="", help="Zoom factor for grid")
    ninio.add_argument("--grid_width", type=int, default=4, metavar="", help="Width of grid lines")
    ninio.add_argument("--blur_strength", type=int, default=0, metavar="", help="Strength of Gaussian blur")
    ninio.add_argument("--dot_radius", type=int, default=3, metavar="", help="Radius of dots")
    ninio.add_argument("--dot_colour", type=str, default="black", metavar="", help="Colour of dots")
    ninio.add_argument("--dot_outline_colour", type=str, default="white", metavar="", help="Colour of dot outline")
    ninio.add_argument("--square_colour", type=str, default="black", metavar="", help="Square fill colour")
    ninio.add_argument("--canvas_colour", type=str, default="white", metavar="", help="Canvas (background) colour")
    ninio.add_argument("--vertical_colour", type=str, default="grey", metavar="", help="Vertical grid line colour")
    ninio.add_argument("--horizontal_colour", type=str, default="grey", metavar="", help="Horizontal grid line colour")
    ninio.add_argument("--diagonal_colour", type=str, default="grey", metavar="", help="Diagonal grid line colour")
    ninio.add_argument("--outline_colour", type =str, default="black", metavar="", help="Colour outline for square")
    ninio.add_argument("--outline_width", type=int, default=4, metavar="", help="Width of outline for square")
    ninio.add_argument("--save", type=str, default="ninio.png", metavar="", help="Output filename (MUST specify file extension)")

    # McAnany-Levine extinction grid
    mcanany_levine = subparsers.add_parser(
        "mcanany-levine",
        help="McAnany-Levine extinction illusion",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        add_help=False
    )

    mcanany_levine.add_argument("--help", action="help", help="")
    mcanany_levine.add_argument("--cells", type=int, default=10, metavar="", help="Number of grid cells")
    mcanany_levine.add_argument("--size", type=int, default=400, metavar="", help="Size of square (pixels)")
    mcanany_levine.add_argument("--img_width", type=int, default=800, metavar="", help="Width of canvas (pixels)")
    mcanany_levine.add_argument("--img_height", type=int, default=600, metavar="", help="Height of canvas (pixels)")
    mcanany_levine.add_argument("--grid_zoom", type=float, default=1.05, metavar="", help="Zoom factor for grid")
    mcanany_levine.add_argument("--grid_width", type=int, default=8, metavar="", help="Width of grid lines")
    mcanany_levine.add_argument("--blur_strength", type=int, default=0, metavar="", help="Strength of Gaussian blur")
    mcanany_levine.add_argument("--dot_radius", type=int, default=4, metavar="", help="Radius of dots")
    mcanany_levine.add_argument("--dot_colour", type=str, default="white", metavar="", help="Colour of dots")
    mcanany_levine.add_argument("--square_colour", type=str, default="black", metavar="", help="Square fill colour")
    mcanany_levine.add_argument("--canvas_colour", type=str, default="white", metavar="", help="Canvas (background) colour")
    mcanany_levine.add_argument("--vertical_colour", type=str, default="#a6a6a6", metavar="", help="Vertical grid line colour")
    mcanany_levine.add_argument("--horizontal_colour", type=str, default="#a6a6a6", metavar="", help="Horizontal grid line colour")
    mcanany_levine.add_argument("--outline_colour", type =str, default="black", metavar="", help="Colour outline for square")
    mcanany_levine.add_argument("--outline_width", type=int, default=4, metavar="", help="Width of outline for square")
    mcanany_levine.add_argument("--save", type=str, default="mcanany_levine.png", metavar="", help="Output filename (MUST specify file extension)")

    args = parser.parse_args()

    if args.illusion == "hermann":
        img = draw_hermann(
            cells=args.cells,
            side=args.size,
            img_size=(args.img_width, args.img_height),
            grid_zoom=args.grid_zoom,
            grid_width=args.grid_width,
            blur_strength=args.blur_strength,
            square_colour=args.square_colour,
            canvas_colour=args.canvas_colour,
            vertical_colour=args.vertical_colour,
            horizontal_colour=args.horizontal_colour,
            outline_colour=args.outline_colour,
            outline_width=args.outline_width,
        )

    elif args.illusion == "scintillating":
        img = draw_scintillating(
            cells=args.cells,
            side=args.size,
            img_size=(args.img_width, args.img_height),
            grid_zoom=args.grid_zoom,
            grid_width=args.grid_width,
            blur_strength=args.blur_strength,
            dot_radius=args.dot_radius,
            dot_colour=args.dot_colour,
            square_colour=args.square_colour,
            canvas_colour=args.canvas_colour,
            vertical_colour=args.vertical_colour,
            horizontal_colour=args.horizontal_colour,
            outline_colour=args.outline_colour,
            outline_width=args.outline_width,
        )

    elif args.illusion == "bergen":
        img = draw_bergen(
            cells=args.cells,
            side=args.size,
            img_size=(args.img_width, args.img_height),
            grid_zoom=args.grid_zoom,
            grid_width=args.grid_width,
            blur_strength=args.blur_strength,
            square_colour=args.square_colour,
            canvas_colour=args.canvas_colour,
            vertical_colour=args.vertical_colour,
            horizontal_colour=args.horizontal_colour,
            outline_colour=args.outline_colour,
            outline_width=args.outline_width,
        )

    elif args.illusion == "ninio":
        img = draw_ninio(
            cells=args.cells,
            side=args.size,
            img_size=(args.img_width, args.img_height),
            grid_zoom=args.grid_zoom,
            grid_width=args.grid_width,
            blur_strength=args.blur_strength,
            dot_radius=args.dot_radius,
            dot_colour=args.dot_colour,
            dot_outline_colour=args.dot_outline_colour,
            square_colour=args.square_colour,
            canvas_colour=args.canvas_colour,
            vertical_colour=args.vertical_colour,
            horizontal_colour=args.horizontal_colour,
            diagonal_colour=args.diagonal_colour,
            outline_colour=args.outline_colour,
            outline_width=args.outline_width,
        )

    elif args.illusion == "mcanany-levine":
        img = draw_mcanany_levine(
            cells=args.cells,
            side=args.size,
            img_size=(args.img_width, args.img_height),
            grid_zoom=args.grid_zoom,
            grid_width=args.grid_width,
            blur_strength=args.blur_strength,
            dot_radius=args.dot_radius,
            dot_colour=args.dot_colour,
            square_colour=args.square_colour,
            canvas_colour=args.canvas_colour,
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