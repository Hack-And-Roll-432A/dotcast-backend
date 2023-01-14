import json

with open("data/mrt.txt", "r") as f:
    st = [ l.strip() for l in f ]
    sts = {}
    for s in st:
        data = s.split(",")
        sts[data[0]] = data[1].strip() + " MRT"
    with open("mrt.json", "w") as outfile:
        json.dump(sts, outfile)