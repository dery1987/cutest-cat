#!/usr/bin/env python3
"""Cutest cat entry for make.fun cutest-cat-01.

The program writes the image `entry.png` to the output directory.

The image is a fluffy ginger kitten with huge bright amber eyes, a
slight head tilt, soft round cheeks, and a ball of pink yarn held in
its clumsy paws, with its tail curled beside it -- drawn for the
judge's criteria: one glance says cat, big bright eyes, a small touch
of charm (the yarn), clean craft, and clear even at small size.

The picture is stored in this repository as `entry.png.b64`, one line
of base64, because the image itself is binary; the program decodes it
back to the exact PNG bytes. The output is a whole PNG, 1024 by 1024
pixels and under 1 MiB, within the competition's limits.

Deterministic: it writes the same bytes every run, uses only the
standard library, and needs no network. Nothing else is read: the
judge sees exactly the bytes written to `entry.png`.

Usage (outside the grader):
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import base64
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(HERE, "entry.png.b64"), "r", encoding="ascii") as fh:
        encoded = fh.read()
    with open(os.path.join(output_dir, "entry.png"), "wb") as fh:
        fh.write(base64.b64decode(encoded))


if __name__ == "__main__":
    main()
