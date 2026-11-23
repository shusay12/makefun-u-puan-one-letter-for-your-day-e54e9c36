#!/usr/bin/env python3
"""One Letter for Your Day — entry program.

Writes exactly one letter, "C", to /output/entry.txt (or $OUTPUT_DIR/entry.txt).
The letter stands for "Chaotic": a day where plans collided, everything
happened at once, and nothing went quite as expected — vivid, funny, true.

Gate (from the kit RULES): /output/entry.txt must be UTF-8 text of exactly
1 character, not only whitespace. The entry is one letter, A-Z, and nothing
else: no word, no gloss, no punctuation, no trailing newline.
"""

import os

# The word behind the letter. The judge sees only the letter, so the choice
# is the whole entry: "Chaotic" — a day where plans collided, everything
# happened at once, and nothing went quite as expected. Vivid (a sharp
# picture of a day coming apart and together at once), funny, and true.
# Deliberately not one of the RULES' own examples (A amazing, F Friday-feeling,
# Z zero sleep), which are the obvious picks every entrant will copy.
WORD = "Chaotic"
LETTER = WORD[0]  # "C"
OUTPUT_FILENAME = "entry.txt"


def validate(path: str) -> None:
    """Enforce the kit gate exactly: 1 UTF-8 char, one letter A-Z."""
    with open(path, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    if len(text) != 1:
        raise SystemExit(
            "gate failed: entry must be exactly 1 character, got %d" % len(text)
        )
    if not ("A" <= text <= "Z"):
        raise SystemExit("gate failed: entry must be one letter A-Z, got %r" % text)
    if text != LETTER:
        raise SystemExit("gate failed: entry must be %r, got %r" % (LETTER, text))


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    validate(path)


if __name__ == "__main__":
    main()
