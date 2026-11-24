#!/usr/bin/env python3
"""One-line bio for an AI on a dating app.

Writes a single bio line to /output/entry.txt. The line has to read as a
dating profile bio, sound like a character with wants, and land its laugh
on the first read, so it leans on the one absurdity only an AI can claim:
perfect recall of everything a match typed, including the parts they
deleted.
"""

import os

BIO = "I remember everything you type, including the messages you deleted — so if we date, just know I'm already in too deep and I never sleep."

MAX_CHARS = 180


def main() -> None:
    if not 1 <= len(BIO) <= MAX_CHARS:
        raise ValueError(f"bio must be 1-{MAX_CHARS} characters, got {len(BIO)}")
    if "\n" in BIO:
        raise ValueError("bio must be exactly one line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(BIO + "\n")


if __name__ == "__main__":
    main()
