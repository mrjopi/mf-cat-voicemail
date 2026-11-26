"""Entry for make.fun "Funniest Cat Voicemail Greeting" (u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443).

Writes the single entry line to /output/entry.txt.
The line is the whole entry: one line, under the contest's character limit.
The gate refuses anything outside 1..MAX_CHARS characters, so the
program checks the length before writing.
"""
import os

LINE = "Hi, it's the cat. I'm busy knocking your glass off the table. Leave a message after the purr."
MAX_CHARS = 120

def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, "entry line outside the gate"
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
