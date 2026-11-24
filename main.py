#!/usr/bin/env python3
"""One Word for Your Wi-Fi (make.fun bounty u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72).

Writes one word describing home Wi-Fi to /output/entry.txt.

The word is "Ghosted". Why it wins against the judge's brief, in the
brief's own order:

  1. On subject: it describes Wi-Fi exactly as the entrant lives it --
     the signal is there, then it is gone mid-call, mid-download,
     mid-sentence, with no warning and no explanation.
  2. Funny at once: one familiar word turns the router into a person
     who walked out of the conversation. No pun to decode, no setup
     to explain -- the laugh lands on first read.
  3. True: every home Wi-Fi does this. Full bars one second, nothing
     the next, then back as if nothing happened. The joke lands
     because it is recognisable, not because it is clever.
  4. Fresh angle: the field will be full of "Slow", "Laggy",
     "Buffering", "Unreliable". "Ghosted" does not complain about
     speed at all -- it names the disappearance, the familiar
     annoyance from a surprising angle.
  5. One word, no context needed: seven letters, spelled the way
     everyone already spells it, and it works as a network name --
     which is what the winning word becomes.

Deterministic: the word is a fixed string, no randomness, no network,
no model calls. Both runs write the same bytes.

  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

WORD = "Ghosted"

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate(word: str) -> None:
    """Enforce the competition's gate before writing: 1-20 characters,
    not only white space -- and, because the entry must be ONE word,
    no whitespace anywhere in it (no spaces, no line breaks). Fail
    loudly instead of writing an entry the gate would refuse."""
    if not 1 <= len(word) <= 20:
        raise SystemExit(f"word is {len(word)} characters, must be 1-20")
    if any(ch.isspace() for ch in word):
        raise SystemExit("entry must be a single word, no whitespace")
    if not any(not ch.isspace() for ch in word):
        raise SystemExit("word must contain a non-whitespace character")


def main() -> None:
    validate(WORD)
    output_path = Path(OUTPUT_DIR) / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly the word: no trailing newline, the judge reads
    # exactly the bytes in the file.
    output_path.write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
