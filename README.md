# python-stuff

Small Python tools, games, and algorithms, managed with [uv](https://docs.astral.sh/uv/).

## Install

```sh
uv sync --all-groups
```

## Usage

Run the menu launcher:

```sh
uv run python-stuff
```

Or run any tool directly:

| Command                    | What it does                          |
| -------------------------- | ------------------------------------- |
| `uv run cipher`            | Caesar / Vigenère cipher demo         |
| `uv run circuit-diagram`   | Generate circuit SVGs to `outputs/`   |
| `uv run is-prime`          | Prime number checker                  |
| `uv run number-guessing`   | Number guessing game                  |
| `uv run password`          | Random password generator             |
| `uv run roger-2486`        | The mysterious one...                 |
| `uv run runway-number`     | Angle → runway number                 |
| `uv run taiwan-aqi`        | Download Taiwan AQI data to `outputs/AQI.csv` |
