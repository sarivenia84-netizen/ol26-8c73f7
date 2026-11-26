"""Synchronized Apologizing: two athletes perform a flawless routine of 'no, you first'
until one runs out of patience. No one has ever won."""
import os


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    LINE = "Synchronized Apologizing: two athletes perform a flawless routine of 'no, you first' until one runs out of patience. No one has ever won."
    with open(entry_path, "w") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()