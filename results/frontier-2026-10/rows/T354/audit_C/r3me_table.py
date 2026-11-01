"""eps 1 momentum rows on the three-valued b (r3me_out/): Richardson tables in d (halving) against the eps > 0 closed form c(s)
of cclosed_eps_3v.py. The rows are (x*/(r x0) - 1)/d with r = sqrt(B2)/(sqrt(B2) + eps)."""
import glob
import re

CLOSED = {1: -0.539035, 2: -0.408672}  # cclosed_eps_3v.py 1
rows = {}
for f in glob.glob("r3me_out/root_e1_*.txt"):
    m = re.search(r"n (\d+) beta2 ([\d.]+) beta1 ([\d.]+) eps ([\d.]+) nd ([\d.]+).*\(x\*/x0-1\)/d (-?[\d.]+)", open(f).read())
    if m:
        n, b2, b1, s, v = int(m[1]), float(m[2]), float(m[3]), round(float(m[5])), float(m[6])
        rows.setdefault((b1, s), []).append((1 - b2, n, v))
for (b1, s), r in sorted(rows.items()):
    r.sort(reverse=True)
    print("eps 1, beta1 %g, n d %d: " % (b1, s) + "  ".join("d %.5f (n %d) %+.6f" % t for t in r))
    col = [v for _, _, v in r]
    k = 1
    while len(col) > 1:
        col = [(2 ** k * col[i + 1] - col[i]) / (2 ** k - 1) for i in range(len(col) - 1)]
        print("   order %d extrapolations: %s" % (k, "  ".join("%+.4f" % v for v in col)))
        k += 1
    print("   eps 1 closed form c(%d): %+.4f" % (s, CLOSED[s]))
