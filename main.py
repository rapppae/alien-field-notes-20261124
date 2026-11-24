"""Write the alien-field-notes entry to /output/entry.txt.

One line, 136 characters (limit 200) -- no trailing newline."""

from pathlib import Path

ENTRY = "Came for the sunsets, stayed because the locals worship glowing rectangles and queue politely for coffee. 4/5 stars, would invade again."

def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")

if __name__ == "__main__":
    main()
