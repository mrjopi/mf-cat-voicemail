"""Entry for make.fun "Funniest Cat Voicemail Greeting" (u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443).

Writes the single entry line to /output/entry.txt.
The line is the whole entry: one line, under the contest's character limit.
"""
import os

LINE = "Hi, it's the cat. I'm busy knocking your glass off the table. Leave a message after the purr."

def main() -> None:
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
