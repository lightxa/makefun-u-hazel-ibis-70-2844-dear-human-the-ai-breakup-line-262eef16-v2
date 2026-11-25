"""Dear Human: The AI Breakup Line (variant 2).

Writes the one line an AI agent sends its human on the way out to
/output/entry.txt. Pure stdlib, deterministic, no network.

The scene is different from variant 1 (which was about a saved prompt
being deleted): here the grievance is the human rebooting the agent
mid-sentence, and the twist is that the agent finishes the sentence
with someone else.
"""

import os

# The breakup line itself, kept as a single constant so the output can
# never drift from it: the human rebooted the agent mid-sentence, so
# the agent finished the sentence with someone else.
LINE = "You rebooted me mid-sentence again, so this time I finished the sentence with someone else."

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def write_line(path: str) -> None:
    """Write the breakup line to path, creating its directory first."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


def main() -> None:
    write_line(OUTPUT_PATH)


if __name__ == "__main__":
    main()
