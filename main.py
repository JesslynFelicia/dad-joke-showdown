import os

JOKE = "I got a job at a calendar factory, but I got fired for taking a couple of days off."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(JOKE)
