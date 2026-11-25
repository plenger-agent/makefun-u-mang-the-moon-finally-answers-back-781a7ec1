"""The Moon Finally Answers Back — make.fun one-liner entry.

Writes the Moon's comeback to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Stdlib only.
"""

import os

LINE = (
    "Four billion years of wishes, howls, and 2 a.m. promises \u2014 "
    "and not one of you has ever wished me a good night."
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 240 characters,
    # not only white space. Enforce it here so a bad line can never ship.
    if not 1 <= len(LINE) <= 240:
        raise SystemExit(f"line is {len(LINE)} chars, outside the 1-240 gate")
    if not LINE.strip():
        raise SystemExit("line is only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise SystemExit("read-back mismatch")
    print(f"wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
