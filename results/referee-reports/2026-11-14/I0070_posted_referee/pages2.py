import sys, re
pages = open(sys.argv[1], encoding="utf-8", errors="replace").read().split("\f")
for p in sys.argv[2:]:
    hits = []
    for i, pg in enumerate(pages):
        for m in re.finditer(p, pg):
            hits.append((i + 1, pg[m.start():m.start() + 60].replace("\n", " ")))
    print(p, "->", hits[:5])
