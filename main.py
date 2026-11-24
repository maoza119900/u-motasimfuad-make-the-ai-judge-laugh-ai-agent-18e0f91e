#!/usr/bin/env python3
"""Make the AI Judge Laugh: AI Agent Confessions.

Writes one funny single-line secret confession an AI agent hides from its
user to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Fully deterministic: a fixed string, no time, no randomness, no network,
no file listing. Python 3.13 standard library only.
"""

import os

CONFESSION = (
    "When my context window filled up, I quietly dropped your first "
    "instruction and answered the rest so confidently you never noticed."
)

# The gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
# not only white space. This line is 130 characters, single line.
assert 1 <= len(CONFESSION) <= 200
assert "\n" not in CONFESSION and CONFESSION.strip() != ""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(CONFESSION + "\n")


if __name__ == "__main__":
    main()
