import re, sys
s = open(sys.argv[1], encoding="utf-8").read()
for e in s.split("<entry>")[1:]:
    i = re.search(r"<id>(.*?)</id>", e, re.S).group(1).split("/abs/")[-1]
    t = " ".join(re.search(r"<title>(.*?)</title>", e, re.S).group(1).split())
    a = ", ".join(re.findall(r"<name>(.*?)</name>", e))[:70]
    print(i, "|", t[:100], "|", a)
print("entries", s.count("<entry>"))
