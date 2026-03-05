import os
import json

import organism
import quotes
import poster


def loadhistory():

    if not os.path.exists("history.json"):
        return {"count": 0}

    with open("history.json") as f:
        return json.load(f)


def savehistory(data):

    with open("history.json", "w") as f:
        json.dump(data, f, indent=2)


def run():

    os.makedirs("art", exist_ok=True)
    os.makedirs("poster", exist_ok=True)

    history = loadhistory()

    index = history["count"] + 1

    # generate background
    bg = organism.generate()

    artpath = f"art/{index}.png"

    bg.save(artpath)

    # ambil 1 quote
    quote, ref = quotes.get()

    # render poster
    posterpath = poster.render(bg, quote, ref, index)

    history["count"] = index

    savehistory(history)

    print("art:", artpath)
    print("poster:", posterpath)


if __name__ == "__main__":
    run()
