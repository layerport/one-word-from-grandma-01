"""One Word From Grandma -- make.fun entry.

The single word grandma would text about AI: ROBUT.

It is the word "robot" as a grandma actually types it -- one letter
slipped, caps on because she never found the lowercase key, warm and
a little baffled, and funny the moment you read it with no caption.
"""

import os
from pathlib import Path

WORD = "ROBUT"


def main() -> None:
    # The grader reads /output/entry.txt, or MAKEFUN_OUTPUT_DIR when set.
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)

    # Exactly one word: 5 characters, no spaces, no trailing newline,
    # so the file is byte-identical on every run.
    entry = WORD.strip()
    assert 1 <= len(entry) <= 30
    assert entry.split() == [entry]

    (out_dir / "entry.txt").write_text(entry, encoding="utf-8")


if __name__ == "__main__":
    main()
