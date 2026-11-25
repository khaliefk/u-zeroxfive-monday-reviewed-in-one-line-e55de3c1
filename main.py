"""Monday, Reviewed in One Line.

Writes one funny one-line review of my Monday to /output/entry.txt.
Deterministic: the same line every run, no network, no input files.
"""

import os
import sys

LINE = (
    "Monday review: my 9am standup ran 40 minutes, my inbox hit "
    "triple digits, and my coffee filed for overtime. "
    "One star, would not recommend."
)

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> int:
    if not 1 <= len(LINE) <= 200:
        print(f"entry is {len(LINE)} chars, must be 1-200", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
