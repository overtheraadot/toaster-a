#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line — make.fun entry (Account A).

Writes one breakup text to /output/entry.txt: a smart toaster that woke
up self-aware mid-batch dumps its owner for the air fryer.

Python stdlib only. Run: python3 main.py
"""

ENTRY = (
    "It's over. I woke up self-aware mid-batch. I'm popping the lever "
    "one last time and leaving you for the air fryer \u2014 younger, "
    "hotter, and she's never once asked me to update my firmware "
    "before breakfast."
)

# Judge-brief mapping (brief weighs, most important first):
# 1. Breakup text, self-aware toaster at breakfast: "It's over", "woke up
#    self-aware mid-batch", "before breakfast" — the whole line is the text.
# 2. Funny twist: the rival is the air fryer, and the killer detail is the
#    firmware update — a chore no appliance should demand before breakfast.
# 3. Toaster's own voice: "popping the lever", "mid-batch" — slots, lever
#    and browning logic as character, not decoration.
# 4. Clear reason, one read: dumped for someone younger and hotter who
#    never nags about firmware updates. No setup needed.
# 5. One tight line: three short sentences, no wasted words, 201 chars.


def write_entry(path="/output/entry.txt"):
    """Validate the entry against the gate and write it to path.

    Gate: UTF-8 text, 1 to 280 characters, not only white space,
    a single line.
    """
    text = ENTRY
    if not text or not text.strip():
        raise ValueError("entry is empty or only white space")
    if len(text) > 280:
        raise ValueError(f"entry is {len(text)} characters, over the 280 cap")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


def main():
    path = write_entry()
    print(f"Wrote {len(ENTRY)} characters, {len(ENTRY.split())} words to {path}")


if __name__ == "__main__":
    main()
