#!/usr/bin/env python3
"""Office Joke Open entry: write one line of office comedy to /output/entry.txt.

The joke is a reply-all gag in three beats: a reasonable request ("remove
me from this thread"), the office's signature self-defeating response (47
people replying-all to agree), and the payoff — the thread they all wanted
dead is now immortal. The humour lands in the last few words, and the whole
line stays well under the 200-character gate.
"""

import os

JOKE = (
    "I asked to be removed from this email thread, so 47 people "
    "replied-all to agree \u2014 congratulations, the thread is now immortal."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
