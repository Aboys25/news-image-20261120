"""Decode the bundled poster image to the grader output directory.

The entry image sums up the world news of Friday 20 November 2026:
Cyclone Akvan bearing down on Odisha, Trump pushing any Iran decision
to 2027, European leaders ready for Ukraine peace talks with Russia,
GTA VI's $1.84bn launch day, and World Children's Day.

The image ships in this repository as base64 text (entry.png.b64),
so the repository stays text-only and can be pushed over a text-only
channel. The base64 payload is ASCII (one line), and decoding it
reproduces the exact PNG bytes that were encoded. This program decodes
it back to entry.png in the output directory, using only the Python
standard library, with no network access. It runs twice and writes
identical bytes both times.

The source file is located relative to this script (not the working
directory), so the program works no matter where it is invoked from.
"""

import base64
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png.b64")

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DEST = os.path.join(OUT_DIR, "entry.png")

if not os.path.isfile(SOURCE):
    raise SystemExit("entry.png.b64 missing next to main.py")

with open(SOURCE, "rb") as fh:
    raw = base64.b64decode(fh.read(), validate=True)

os.makedirs(OUT_DIR, exist_ok=True)
with open(DEST, "wb") as fh:
    fh.write(raw)

# Sanity check: the written file must be a whole PNG within the limits.
if os.path.getsize(DEST) > 1048576:
    raise SystemExit("entry.png exceeds the 1 MiB limit")
