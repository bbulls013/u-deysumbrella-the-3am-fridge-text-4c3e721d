#!/usr/bin/env python3
"""The 3AM Fridge Text: one line a smart fridge texts its owner at 3am.

Writes one fixed line to /output/entry.txt. The text is a constant,
so every run produces byte-identical output.
"""
import os
from pathlib import Path

LINE = (
    "3:04 AM. I counted. You opened me 6 times tonight and ate nothing. "
    "At this point I am just a cold lamp you visit when you cannot sleep."
)


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")
    print(f"wrote {out} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
