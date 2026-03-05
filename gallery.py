import json

def update():

    with open("history.json") as f:
        history = json.load(f)

    count = history["count"]

    lines = []

    lines.append("# Islamic Quote Posters\n")

    for i in range(count,0,-1):
        lines.append(f"![](poster/{i}.png)\n")

    with open("README.md","w") as f:
        f.write("\n".join(lines))

if __name__=="__main__":
    update()
