import os

MAX_CHARS = 200

JOKE = "I tried dating a broom, but I just couldn't sweep her off her feet."


def write_entry(text, path="/output/entry.txt"):
    text = text.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"joke must be 1 to {MAX_CHARS} characters, got {len(text)}")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    write_entry(JOKE)
