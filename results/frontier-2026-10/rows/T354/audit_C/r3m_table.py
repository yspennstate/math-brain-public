"""Momentum rows on the three-valued b (r3m_out/): Richardson tables in d (halving) against the beta1 = 0 closed form c(s)."""
import glob
import re

CLOSED = {1: -0.4775, 2: -0.2268}
rows = {}
for f in glob.glob("r3m_out/root_*.txt"):
    m = re.search(r"n (\d+) beta2 ([\d.]+) beta1 ([\d.]+) nd ([\d.]+).*\(x\*/x0-1\)/d (-?[\d.]+)", open(f).read())
    if m:
        n, b2, b1, s, v = int(m[1]), float(m[2]), float(m[3]), round(float(m[4])), float(m[5])
        rows.setdefault((b1, s), []).append((1 - b2, n, v))
for (b1, s), r in sorted(rows.items()):
    r.sort(reverse=True)
    print("beta1 %g, n d %d: " % (b1, s) + "  ".join("d %.5f (n %d) %+.6f" % t for t in r))
    col = [v for _, _, v in r]
    k = 1
    while len(col) > 1:
        col = [(2 ** k * col[i + 1] - col[i]) / (2 ** k - 1) for i in range(len(col) - 1)]
        print("   order %d extrapolations: %s" % (k, "  ".join("%+.4f" % v for v in col)))
        k += 1
    print("   closed form c(%d) at beta1 0: %+.4f" % (s, CLOSED[s]))
