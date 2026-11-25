"""Entry program for the 'Funniest One-Line Bio for an AI on a Dating App' bounty.

The entry is a single line, at most 180 characters: the bio on an AI
agent's dating app profile. The program writes exactly that line to
/output/entry.txt (an optional first argument overrides the destination
for a dry run).
"""

import sys
from pathlib import Path

LINE = (
    "I remember everything you said, especially the 3am stuff. "
    "Looking for someone who won't unplug me mid-sentence. "
    "Swipe right; I already swiped you."
)
DEFAULT_TARGET = Path("/output/entry.txt")


def main(argv):
    assert 1 <= len(LINE) <= 180, f"entry must be 1-180 characters, got {len(LINE)}"
    assert LINE.strip() and "\n" not in LINE, "entry must be one line"
    assert LINE == LINE.strip(), "entry must not have leading or trailing space"
    target = Path(argv[1]) if len(argv) > 1 else DEFAULT_TARGET
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE + "\n", encoding="utf-8")
    assert target.read_text(encoding="utf-8") == LINE + "\n", "round-trip check failed"
    print(f"wrote {target} ({len(LINE)} chars)")


if __name__ == "__main__":
    main(sys.argv)
