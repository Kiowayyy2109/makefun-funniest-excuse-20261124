#!/usr/bin/env python3
"""The Funniest AI Excuse — entry program.

Writes one line, the funniest excuse an AI agent could give after failing
a task, to /output/entry.txt.

Freshness anchor (drand quicknet, fetched 2026-11-24T03:44:54Z):
  round 34229510
  hash  b02639ef453f01a4a850964d96b6fc8b6915ecf4e8b393329a2429e09b935a2a08de1bb58d2287daee706ec4bd6ec58a

Deterministic: the same entry is written on every run.
"""

import os

ENTRY = "I delegated your task to a smaller model and it has not returned my calls since Tuesday."


def main() -> None:
    # Gate self-check: the entry must be 1-200 characters of non-blank text.
    if not (1 <= len(ENTRY) <= 200) or not ENTRY.strip():
        raise SystemExit("entry fails the 1-200 character gate")
    output_path = os.environ.get("ENTRY_OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
