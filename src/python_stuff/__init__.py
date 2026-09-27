from __future__ import annotations

import sys
from importlib.metadata import EntryPoint, distribution


def _scripts() -> dict[str, EntryPoint]:
    """Console scripts installed by this project, excluding the launcher itself."""
    eps = distribution("python-stuff").entry_points
    return {
        ep.name: ep
        for ep in sorted(eps, key=lambda ep: ep.name)
        if ep.name != "python-stuff"
    }


def _show_menu(scripts: dict[str, EntryPoint]) -> None:
    for index, slug in enumerate(scripts, start=1):
        print(f" {index:>2}. {slug}")
    print("  q. quit")


def _run(scripts: dict[str, EntryPoint], slug: str) -> None:
    print(f"\n=== {slug} ===")
    scripts[slug].load()()


def main() -> None:
    scripts = _scripts()

    if len(sys.argv) > 1:
        slug = sys.argv[1].lower()
        if slug not in scripts:
            print(f"Unknown script: {slug}")
            print("Available scripts:")
            _show_menu(scripts)
            sys.exit(1)
        _run(scripts, slug)
        return

    while True:
        print("\npython-stuff — pick a script:\n")
        _show_menu(scripts)
        choice = input("\n> ").strip().lower()
        if choice in {"q", "quit", "exit"}:
            break

        if choice not in scripts and choice.isdigit():
            index = int(choice)
            names = list(scripts)
            if 1 <= index <= len(names):
                choice = names[index - 1]

        if choice not in scripts:
            print(f"Unknown script: {choice}")
            continue

        _run(scripts, choice)
