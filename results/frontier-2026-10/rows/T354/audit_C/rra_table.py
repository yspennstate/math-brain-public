"""Table of rra_runs.txt: gap to the predictions over d, and the extrapolation to d = 0."""
import re, collections
rows = collections.defaultdict(dict)
pat = re.compile(r"RRA eps (\S+) a (\[.*?\]) b .*? beta1 (\S+) beta2 (\S+) nodes (\d+):.*?x\* (\S+)\s+\(x\*/x0-1\)/d (\S+)\s+guess (\S+)\s+withr1 (\S+)")
for line in open("rra_runs.txt", encoding="utf-8"):
    m = pat.search(line)
    if not m:
        continue
    eps, a, b1, b2, nodes, xs, val, guess, w = m.groups()
    rows[(a, float(eps), float(b1), int(nodes))][float(b2)] = (float(val), float(guess), float(w), xs)
print("| a | eps | beta1 | nodes | exact at beta2 0.9995 / 0.999 / 0.998 | guess | withr1 | gap to withr1 / d | extrap - withr1 | extrap - guess |")
print("|---|---|---|---|---|---|---|---|---|---|")
for key in sorted(rows):
    a, eps, b1, nodes = key
    r = rows[key]
    b2s = sorted(r, reverse=True)
    vals = [r[k][0] for k in b2s]
    g, w = r[b2s[0]][1], r[b2s[0]][2]
    gaps = ["%.2f" % ((r[k][0] - r[k][2]) / (1 - k)) for k in b2s]
    if len(b2s) >= 2:
        d1, d2 = 1 - b2s[0], 1 - b2s[1]
        ex = vals[0] + (vals[0] - vals[1]) * d1 / (d2 - d1)
        e1, e2 = "%+.1e" % (ex - w), "%+.1e" % (ex - g)
    else:
        e1 = e2 = "-"
    print("| %s | %g | %g | %d | %s | %.6f | %.6f | %s | %s | %s |" % (a, eps, b1, nodes, " / ".join("%.6f" % v for v in vals), g, w, " / ".join(gaps), e1, e2))
print()
for key in sorted(rows):
    if key[3] == 240:
        twin = (key[0], key[1], key[2], 160)
        for b2 in rows[key]:
            print("nodes 240 vs 160", key[:3], b2, "x*", rows[key][b2][3], rows[twin][b2][3])
