#!/usr/bin/env python3
"""Round-2 entry: one-star review from a house cat about its human.

Writes exactly one single-line review (1-200 chars, no embedded
newline) to /output/entry.txt. Deterministic: fixed text, no network,
no randomness.
"""

import os

LINE = "One star. She sang me lullabies all the way to the vet, then wondered why I filed her under 'untrustworthy'."

def main():
    assert 1 <= len(LINE) <= 200, len(LINE)
    assert "\n" not in LINE and "\r" not in LINE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Self-check: what landed on disk must be exactly the line, one line.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, repr(written)

if __name__ == "__main__":
    main()
