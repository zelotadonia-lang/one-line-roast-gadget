#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day entry.

Writes one original roast line (<=200 chars) about a gadget used every
day to /output/entry.txt, deterministically: same bytes on every run.
"""
import os

LINE = (
    "My robot vacuum bumps into the same chair every day and still acts "
    "surprised, which is the most human thing in my house."
)


def main():
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line must not be only whitespace"
    # Entry must be exactly one line: no newline characters anywhere.
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    # Deterministic by construction: fixed constant, no randomness, no
    # timestamps, explicit UTF-8 encoding, no trailing newline added.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
