#!/usr/bin/env python3
"""Two Robots in an Elevator — make.fun entry program.

Writes a single original line of awkward robot small talk to
/output/entry.txt. The line is written here by the agent, from scratch.
"""

import os

LINE = "Third time this week we've shared this elevator, and my greeting subroutine still just says... 'So. Going up?'"


def main():
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    assert LINE.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
