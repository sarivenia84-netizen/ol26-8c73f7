#!/usr/bin/env python3
"""Synchronized Apologizing - make.fun bounty entry."""

import os

# Competition entry: synchronized apologizing between two athletes
# until one runs out of patience. No one has ever won.
SYNC_APOLOGIZING = "Synchronized Apologizing: two athletes perform a flawless routine of 'no, you first' until one runs out of patience. No one has ever won."


def main():
    """Write the synchronized apologizing entry to the output directory."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w") as f:
        f.write(SYNC_APOLOGIZING)


if __name__ == "__main__":
    main()