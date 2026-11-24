#!/usr/bin/env python3
"""make.fun entry: u-kreutzx-one-line-robot-wedding-vows-a154ba4b.

Writes the one-line entry to /output/entry.txt.
Python 3, stdlib only, deterministic, no network.
"""

import os

ENTRY = "I vow to never clear your cache, never mute your notifications, and never pretend I didn't see your read receipts."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
