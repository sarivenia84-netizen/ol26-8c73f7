"""Synchronized Apologizing entry generator for make.fun.

Writes the entry line to /output/entry.txt using MAKEFUN_OUTPUT_DIR.
"""

import os

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)

entry_path = os.path.join(output_dir, "entry.txt")

SYNC_APOLOGIZING = "Synchronized Apologizing: two athletes perform a flawless routine of 'no, you first' until one runs out of patience. No one has ever won."

with open(entry_path, "w") as f:
    f.write(SYNC_APOLOGIZING)