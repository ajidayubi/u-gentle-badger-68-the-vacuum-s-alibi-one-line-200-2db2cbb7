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


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
