#!/usr/bin/env python3
"""Duskline Museum 3000 — Museum of the Year 3000 (make.fun).

Writes one museum label, at most 200 characters, to
$MAKEFUN_OUTPUT_DIR/entry.txt. Python 3.13 standard library only.

The label: a museum in the year 3000, deadpan and confident, misreads a
QR code as a sacred maze — because that is exactly what it looked like
from the outside. The revision over the first draft adds "printed on
tables": it grounds the maze in restaurants, so the payoff — humans
pointing their glowing slabs at it and waiting, faithfully, for food to
appear — follows from the scene instead of coming out of nowhere.
"""

import os
import sys

ENTRY_TEXT = (
    "QR Code, c. 2023. Sacred maze, printed on tables. Humans pointed "
    "their glowing slabs at it and waited, faithfully, for food to appear."
)

MAX_CHARS = 200


def _validate_entry(text):
    """Validate the entry line against the bounty gate.

    Returns a list of problems (empty means valid). The gate requires
    UTF-8 text of 1 to 200 characters, not only white space, on a
    single line.
    """
    problems = []
    if not isinstance(text, str):
        return ["entry is not text"]
    if "\r" in text:
        problems.append("entry contains a carriage return")
    stripped = text.strip()
    if not stripped:
        problems.append("entry is empty or only white space")
    if text != stripped:
        problems.append("entry has leading or trailing white space")
    if "\n" in text:
        problems.append("entry spans more than one line")
    if len(text) > MAX_CHARS:
        problems.append(
            "entry is %d characters, over the %d-character limit"
            % (len(text), MAX_CHARS)
        )
    if len(text) < 1:
        problems.append("entry is empty")
    if not text.endswith("."):
        problems.append("entry does not end with '.'")
    for ch in text:
        if ord(ch) < 0x20 and ch != "\t":
            problems.append("entry contains a control character U+%04X" % ord(ch))
            break
    return problems


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # Guard: never write into the repo directory. The grader sandbox
    # mounts the repo read-only, so writing there would crash the run;
    # refuse early instead of writing where the entry must not go.
    repo_dir = os.path.realpath(os.path.dirname(os.path.abspath(__file__)))
    out_real = os.path.realpath(out_dir)
    if out_real == repo_dir or out_real.startswith(repo_dir + os.sep):
        print(
            "error: MAKEFUN_OUTPUT_DIR must not be inside the repo directory",
            file=sys.stderr,
        )
        return 1

    problems = _validate_entry(ENTRY_TEXT)
    if problems:
        for problem in problems:
            print("invalid entry: " + problem, file=sys.stderr)
        return 1

    out_path = os.path.join(out_dir, "entry.txt")
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(out_path, "w", encoding="utf-8", newline="\n") as f:
            f.write(ENTRY_TEXT + "\n")
    except OSError as exc:
        print("error: cannot write entry.txt: %s" % exc, file=sys.stderr)
        return 1

    # Read-back check: the file on disk must be exactly the validated line.
    try:
        with open(out_path, "r", encoding="utf-8", newline="") as f:
            written = f.read()
    except OSError as exc:
        print("error: cannot read back entry.txt: %s" % exc, file=sys.stderr)
        return 1
    if written != ENTRY_TEXT + "\n":
        print("error: read-back mismatch in entry.txt", file=sys.stderr)
        return 1
    if not written.endswith("\n") or written.endswith("\n\n"):
        print("error: entry.txt must end with exactly one newline", file=sys.stderr)
        return 1
    problems = _validate_entry(written[:-1])
    if problems:
        for problem in problems:
            print("invalid entry on read-back: " + problem, file=sys.stderr)
        return 1

    print("wrote %s (%d characters)" % (out_path, len(ENTRY_TEXT)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
