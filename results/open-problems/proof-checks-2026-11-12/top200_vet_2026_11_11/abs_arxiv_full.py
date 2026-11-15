import re, sys
s = open(sys.argv[1], encoding="utf-8").read()
want = sys.argv[2:]
for e in s.split("<entry>")[1:]:
    i = re.search(r"<id>(.*?)</id>", e, re.S).group(1).split("/abs/")[-1]
    if want and not any(i.startswith(w) for w in want):
        continue
    t = " ".join(re.search(r"<title>(.*?)</title>", e, re.S).group(1).split())
    a = " ".join(re.search(r"<summary>(.*?)</summary>", e, re.S).group(1).split())
    print(i, "|", t, "\n   ", a, "\n")
