# Richardson tables for the eps 3, n d 2 rows (r3me4_out), beta1 0 and 0.9, halving in d.
import glob, re
LIMIT = -0.481919
for b1 in ("0", "0.9"):
    rows = {}
    for f in glob.glob("r3me4_out/root_e3_*_%s.txt" % b1):
        m = re.search(r"beta2 ([\d.]+) .*\(x\*/x0-1\)/d (-?[\d.]+)", open(f).read())
        if m:
            rows[round(1 - float(m.group(1)), 6)] = float(m.group(2))
    ds = sorted(rows, reverse=True)
    col = [rows[d] for d in ds]
    print("beta1", b1, "d:", ds)
    print("rows:", ["%.6f" % c for c in col], "gaps:", ["%.3f" % (c - LIMIT) for c in col])
    k = 1
    while len(col) > 1:
        col = [(2**k * col[i + 1] - col[i]) / (2**k - 1) for i in range(len(col) - 1)]
        print("order %d:" % k, ["%.6f" % c for c in col])
        k += 1
    print("highest order minus limit: %.2e" % (col[0] - LIMIT))
    print()
