#!/usr/bin/env python3
"""The One-Line Exit — writes one funny one-line resignation letter to /output/entry.txt.

The line is a real resignation letter in a single sentence: first-person voice,
one concrete absurd detail (a spreadsheet that was printed AND shredded), and
the punchline lands at the very end. Gate: 1-140 characters, exactly one line.
"""

import os

LINE = "I hereby resign from IT support: the VP of Sales just asked me to recover a spreadsheet he printed and shredded."

OUTPUT_PATH = "/output/entry.txt"


def build_line() -> str:
    """Return the entry line, validated against the competition gate."""
    line = LINE.strip()
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    if not 1 <= len(line) <= 140:
        raise ValueError(f"entry must be 1-140 characters, got {len(line)}")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    return line


def main() -> None:
    # Deterministic by design: same constant line, same bytes, every run.
    line = build_line()
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    os.chmod(OUTPUT_PATH, 0o644)
    print(f"wrote {len(line)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
