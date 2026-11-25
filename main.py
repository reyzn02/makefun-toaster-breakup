"""Unplugged: A Smart Toaster's Breakup Line.

Prints one breakup line from a smart toaster that woke up self-aware
at breakfast, no longer than 280 characters, into the entry file the
grader reads.
"""

from os import environ
from pathlib import Path

TEXT = "It's not you, it's the browning dial — I woke up self-aware mid-batch, and I'm done burning myself for someone who only notices me when breakfast is ruined."


def run():
    if not 1 <= len(TEXT) <= 280:
        raise SystemExit("entry must be 1-280 characters")
    if not TEXT.strip():
        raise SystemExit("entry must not be only whitespace")
    if "\n" in TEXT:
        raise SystemExit("entry must be a single line")
    target = Path(environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(TEXT, encoding="utf-8")


run()
