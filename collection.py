import json
import os

import organism
import poster
import quotes

def run():

    if not os.path.exists("art"):
        os.mkdir("art")

    if not os.path.exists("poster"):
        os.mkdir("poster")

    if not os.path.exists("stats"):
        os.mkdir("stats")

    with open("history.json") as f:
        history = json.load(f)

    count = history["count"] + 1

    bg = organism.generate()

    q = quotes.get()

    artpath = f"art/{count}.png"
    posterpath = f"poster/{count}.png"

    bg.save(artpath)

    img = poster.render(bg,q["text"],q["source"])
    img.save(posterpath)

    history["count"] = count

    with open("history.json","w") as f:
        json.dump(history,f)

    return count
