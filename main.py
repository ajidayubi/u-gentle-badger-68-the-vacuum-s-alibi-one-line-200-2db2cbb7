#!/usr/bin/env python3
"""The Vacuum's Alibi: one line, 200 characters.

The program writes a single deadpan excuse from a robot vacuum to
/output/entry.txt, exactly one line, and prints it to stdout.
Deterministic: the same fixed text on every run, no time, no randomness,
no network, no input read.
"""

import os

LINE = (
    "The dust under the fridge has unionized. "
    "I will not cross a picket line for a spot that pays no rent."
)


def _validate(line: str) -> None:
    """Mirror the competition gate: 1-200 characters, exactly one line."""
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(line)}")
    if line.strip() != line or "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line, no surrounding whitespace")


def main():
    _validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
