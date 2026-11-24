#!/usr/bin/env python3
"""Say What Actually Broke — one line of brutally honest error copy.

Writes a single line to /output/entry.txt naming the real failure:
the server's disk filled up with its own error logs.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

MESSAGE = (
    "Your upload didn't fail. Our server did: its disk is full of error logs "
    "\u2014 40,000 of them are copies of this message. We've cleared them out. "
    "Try again."
)


def main() -> None:
    # The gate: one line of UTF-8 text, 1-200 characters, not only whitespace.
    assert 1 <= len(MESSAGE) <= 200, f"entry is {len(MESSAGE)} chars"
    assert "\n" not in MESSAGE and MESSAGE.strip(), "entry must be one real line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(MESSAGE)


if __name__ == "__main__":
    main()
