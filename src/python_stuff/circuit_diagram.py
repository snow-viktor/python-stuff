from pathlib import Path

import schemdraw
from schemdraw.elements import Battery, Lamp, Line, MeterA, MeterV

from python_stuff._paths import project_root


def draw(output_dir: Path | None = None) -> None:
    output_dir = output_dir or project_root() / "outputs"
    output_dir.mkdir(parents=True, exist_ok=True)
    parallel = output_dir / "parallel.svg"
    series = output_dir / "series.svg"

    with schemdraw.Drawing(file=str(parallel), show=False) as d:
        Line().right(1)
        d.push()
        Line().up(0.75)
        Battery().right(2)
        Line().down(0.75)
        d.pop()
        Line().down(0.75)
        Battery().right(2)
        Line().up(0.75)
        Line().right(1)

        Line().up(2)
        d.push()
        MeterA().left(2)
        Lamp().left(2)

        d.pop()
        Line().up(2)
        MeterV().left(4)
        Line().to(d.elements[0].start)

    with schemdraw.Drawing(file=str(series), show=False) as d:
        Line().right(1)
        Battery().right(1)
        Battery().right(1)
        Line().right(1)

        Line().up(2)
        d.push()
        MeterA().left(2)
        Lamp().left(2)

        d.pop()
        Line().up(2)
        MeterV().left(4)
        Line().to(d.elements[0].start)


def main() -> None:
    output_dir = project_root() / "outputs"
    draw(output_dir)
    print(f"Generated {output_dir / 'parallel.svg'} and {output_dir / 'series.svg'}")


if __name__ == "__main__":
    main()
