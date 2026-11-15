import re, sys, math
seen = {}
for path in sys.argv[1:]:
    for line in open(path, encoding='utf-8'):
        m = re.match(r"(\S+)\s+n=\s*(\d+).*Inf=([\d.]+) minE=([\d.]+) F=([\d.]+)", line)
        if m:
            name, n, d, e, F = m.group(1), int(m.group(2)), float(m.group(3)), float(m.group(4)), float(m.group(5))
            seen[name] = (n, d, e, F)
rows = []
for name, (n, d, e, F) in seen.items():
    triv = (-d*math.log2(d) - (1-d)*math.log2(1-d)) / d
    rows.append((d, name, n, e, F, triv))
rows.sort()
print("name n Inf minE F trivial=h(Inf)/Inf F/trivial")
for d, name, n, e, F, triv in rows:
    print("%-18s %2d %.5f %.4f %.4f %.4f %.3f" % (name, n, d, e, F, triv, F/triv))
