"""Write the make.fun bounty entry text to disk."""

import os
import sys
from pathlib import Path

TEXT = (
    "One star. My phone fell off the bed at 3 a.m.; gravity landed it "
    "exactly where I'd have to get up."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 280, f"entry text must be 1-280 characters, got {len(TEXT)}"
    out_dir = Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8", newline="")
    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
