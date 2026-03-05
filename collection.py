import json
import os

import organism
import poster
import quotes

def run():

    os.makedirs("art",exist_ok=True)
    os.makedirs("poster",exist_ok=True)
    os.makedirs("stats",exist_ok=True)

    with open("history.json") as f:
        history = json.load(f)

    count = history["count"] + 1

    bg = organism.generate()

    q = quotes.get()

    artpath = f"art/{count}.png"
    posterpath = f"poster/{count}.png"

    bg.save(artpath)

    img = poster.render(bg,q["text"],q["source"])
    img.save(posterpath,optimize=True)

    history["count"] = count

    with open("history.json","w") as f:
        json.dump(history,f)

    print("generated",count)

if __name__=="__main__":
    run()
