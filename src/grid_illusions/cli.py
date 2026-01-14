import argparse
from grid_illusions.hermann_grid import draw_hermann_grid
from grid_illusions.scintillating_grid import draw_scintillating_grid
from grid_illusions.bergen_grid import draw_bergen_grid


def add_common_args(p):
    p.add_argument("--size", type=int, default=400)
    p.add_argument("--img-width", type=int, default=800)
    p.add_argument("--img-height", type=int, default=600)
    p.add_argument("--grid-zoom", type=float, default=1.05)
    p.add_argument("--square-colour", default="black")
    p.add_argument("--outline-colour", default="black")
    p.add_argument("--outline-width", type=int, default=4)
    p.add_argument("--save", default="illusion.png")


def main():
    parser = argparse.ArgumentParser(description="Draw a grid illusion!")
    subparsers = parser.add_subparsers(dest="illusion", required=True)

    # ---- Hermann ----
    hermann = subparsers.add_parser("hermann", help="Hermann grid illusion")
    add_common_args(hermann)
    hermann.add_argument("--cells", type=int, default=5)
    hermann.add_argument("--grid-width", type=int, default=15)
    hermann.add_argument("--blur-strength", type=int, default=0)
    hermann.add_argument("--vertical-colour", default="white")
    hermann.add_argument("--horizontal-colour", default="white")

    # ---- Scintillating ----
    scint = subparsers.add_parser("scintillating", help="Scintillating grid illusion")
    add_common_args(scint)
    scint.add_argument("--cells", type=int, default=12)
    scint.add_argument("--grid-width", type=int, default=4)
    scint.add_argument("--blur-strength", type=int, default=0)
    scint.add_argument("--dot-radius", type=int, default=3)
    scint.add_argument("--dot-colour", default="white")
    scint.add_argument("--vertical-colour", default="grey")
    scint.add_argument("--horizontal-colour", default="grey")

    # ---- Bergen ----
    bergen = subparsers.add_parser("bergen", help="Bergen grid illusion")
    add_common_args(bergen)
    bergen.add_argument("--cells", type=int, default=10)
    bergen.add_argument("--grid-width", type=int, default=5)
    bergen.add_argument("--blur-strength", type=int, default=4)
    bergen.add_argument("--vertical-colour", default="white")
    bergen.add_argument("--horizontal-colour", default="white")

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