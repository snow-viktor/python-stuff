from __future__ import annotations

import importlib
import sys
from collections.abc import Callable

SCRIPTS: dict[str, str] = {
    "cipher": "python_stuff.cipher:main",
    "circuit-diagram": "python_stuff.circuit_diagram:main",
    "is-prime": "python_stuff.is_prime:main",
    "number-guessing": "python_stuff.number_guessing:main",
    "password": "python_stuff.password:main",
    "roger-2486": "python_stuff.roger_2486:main",
    "runway-number": "python_stuff.runway_number:main",
    "taiwan-aqi": "python_stuff.taiwan_aqi:main",
}


def _load_entry(entry: str) -> Callable[[], None]:
    module_name, _, attr = entry.partition(":")
    return getattr(importlib.import_module(module_name), attr)


def _show_menu() -> None:
    for index, slug in enumerate(SCRIPTS, start=1):
        print(f" {index:>2}. {slug}")
    print("  q. quit")


def main() -> None:
    if len(sys.argv) > 1:
        slug = sys.argv[1].lower()
        if slug not in SCRIPTS:
            print(f"Unknown script: {slug}")
            print("Available scripts:")
            _show_menu()
            sys.exit(1)
        _run(slug)
        return

    while True:
        print("\npython-stuff — pick a script:\n")
        _show_menu()
        choice = input("\n> ").strip().lower()
        if choice in {"q", "quit", "exit"}:
            break

        if choice not in SCRIPTS and choice.isdigit():
            index = int(choice)
            names = list(SCRIPTS)
            if 1 <= index <= len(names):
                choice = names[index - 1]

        if choice not in SCRIPTS:
            print(f"Unknown script: {choice}")
            continue

        _run(choice)


def _run(slug: str) -> None:
    print(f"\n=== {slug} ===")
    _load_entry(SCRIPTS[slug])()
