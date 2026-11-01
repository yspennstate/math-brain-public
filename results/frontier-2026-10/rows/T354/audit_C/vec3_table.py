"""Table of vec3_out/*.txt: per family G_j at beta2 0.9995/0.999/0.998, the linear extrapolation of G to d = 0 and the
largest relative change of G over the halvings; the noM control at the three beta2."""
import glob, re
import numpy as np
rows = {}
for f in glob.glob("vec3_out/H*.txt"):
    t = open(f).read()
    m = re.search(r"H (\w) beta1 ([\d.]+) beta2 ([\d.]+) eps ([\d.]+).*\| G \[([^\]]+)\] \| noM \[([^\]]+)\] \| MR vs grad ([\de.+-]+) \| resid ([\de.+-]+)", t, re.S)
    if not m:
        print("UNPARSED", f); continue
    H, b1, b2, e = m.group(1), m.group(2), float(m.group(3)), m.group(4)
    rows.setdefault((H, b1, e), {})[b2] = (np.array(m.group(5).split(), float), np.array(m.group(6).split(), float),
                                            float(m.group(7)), float(m.group(8)))
print("| H | beta1 | eps | G at beta2 0.9995 | 0.999 | 0.998 | G(0.998)-G(0.9995) | noM at 0.9995 / 0.999 / 0.998 (coord 1) | MR vs grad | max resid |")
print("|---|---|---|---|---|---|---|---|---|---|")
for k in sorted(rows):
    r = rows[k]
    if len(r) < 3:
        print("| %s | %s | %s | incomplete (%d of 3) |" % (k + (len(r),))); continue
    G = [r[b][0] for b in (0.9995, 0.999, 0.998)]; N = [r[b][1][0] for b in (0.9995, 0.999, 0.998)]
    fmt = lambda v: "[" + " ".join("%.3f" % x for x in v) + "]"
    print("| %s | %s | %s | %s | %s | %s | %s | %.0f / %.0f / %.0f | %.1e | %.0e |" % (k[0], k[1], k[2], fmt(G[0]), fmt(G[1]), fmt(G[2]),
          fmt(G[2] - G[0]), N[0], N[1], N[2], max(r[b][2] for b in r), max(r[b][3] for b in r)))
