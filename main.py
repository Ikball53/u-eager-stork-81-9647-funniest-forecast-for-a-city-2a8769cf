#!/usr/bin/env python3
"""Funniest Forecast for a City That Isn't — make.fun one-liner entry.

Builds a single weather-forecast line (at most 120 characters) for the
invented city of Blusterwick, then writes it to entry.txt.

The line is composed from named parts, not pasted as one literal, so the
structure stays visible: a bulletin-style lead, the day's conditions, and
the absurd twist delivered in the same flat official voice.
"""

import hashlib
import os
import sys

MAX_LINE_CHARS = 119  # line + "\n" must stay within the 120-char gate

# --- Named parts of the line -------------------------------------------

CITY = "Blusterwick"  # invented city: no such place exists

LEAD = "Tomorrow in " + CITY + ": "
# Classic bulletin opening: day + place + temperature, straight from a
# weather desk, before anything strange happens.
CONDITIONS = "72\u00b0F, scattered applause, "
# The forecast itself misbehaves: applause listed as if it were
# precipitation, in the bulletin's own "scattered showers" phrasing.
# The laugh comes from the weather, not from a pun.
TWIST = "and a 90% chance the wind files a complaint."
# The probability line every bulletin uses — except the wind is now a
# disgruntled party lodging a formal complaint.


def build_line() -> str:
    """Compose the forecast line from its named parts."""
    return LEAD + CONDITIONS + TWIST


def main() -> int:
    line = build_line()

    if len(line) > MAX_LINE_CHARS:
        print(
            f"ERROR: line is {len(line)} chars, over the {MAX_LINE_CHARS} limit",
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR may point at a directory or at the file itself.
    if out_dir.endswith(".txt"):
        out_path = out_dir
        os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    else:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")

    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(line + "\n")

    digest = hashlib.sha256((line + "\n").encode("utf-8")).hexdigest()
    print(f"line: {line}")
    print(f"chars: {len(line)} (limit 120 including newline)")
    print(f"sha256: {digest}")
    print(f"wrote: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
