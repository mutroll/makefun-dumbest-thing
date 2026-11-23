#!/usr/bin/env python3
"""Write one line about the dumbest thing the entrant's agent did today.

Deterministic, stdlib only: writes a single line (<= 200 chars) to
/output/entry.txt (or $ENTRY_OUTPUT_DIR/entry.txt when set for local runs).
"""

import os
import sys

LINE = (
    "My agent spent an hour refactoring the login module, then deleted "
    "the only file that called it \u2014 the production login page."
)


def main() -> int:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
