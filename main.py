#!/usr/bin/env python3
"""Texts From Your Future Self — writes one funny SMS to /output/entry.txt."""

import os

TEXT = (
    "Hey, it's you from 2036. Stop saving the good plates for guests — "
    "future you eats cereal off them every night and honestly? Living the "
    "dream. Also, the plant lives — and it has a name now. Gary."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(TEXT)


if __name__ == "__main__":
    main()
