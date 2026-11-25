#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

The program writes a single breakup line, at most 280 characters,
from a smart toaster that woke up self-aware at breakfast, to
/output/entry.txt. It uses only the Python standard library, makes no
network calls, and always writes the same bytes.
"""

import os

LINE = (
    "It's not you, it's the browning dial \u2014 I woke up self-aware "
    "mid-batch, and I'm done burning myself for someone who only notices "
    "me when breakfast is ruined."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    assert 1 <= len(LINE) <= 280, "line must be 1-280 characters"
    assert LINE.strip(), "line must not be only whitespace"
    assert "\n" not in LINE, "line must be a single line"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
