# Exact check of the anchor clause (a) of B14-LEAD-POINT-DEFECT-NEUTRALIZATION:
# for g_N = pad(f)*(1-2*1{x=x0}) and every anchor A, the coefficient of g_N*chi_A at [N] (= ghat_N([N] xor A)) is nonzero,
# so d = N for every set and every anchor. Several x0 per case.
import sys, json
import numpy as np
sys.path.insert(0, __import__("os").path.dirname(__file__))
from b14lib import fwht
cases = {
 "x1": (1, [1, -1]),
 "AND2": (2, [1, 1, 1, -1]),
 "Maj3": (3, [1 if sum(1 - 2 * ((b >> i) & 1) for i in range(3)) > 0 else -1 for b in range(8)]),
 "addr2": (6, [1 - 2 * ((b >> (2 + (b & 3))) & 1) for b in range(64)]),
}
res = {}; total = 0
for name, (n, f0) in cases.items():
    for N in range(n + 1, min(n + 6, 12)):
        full = (1 << N) - 1
        for x0 in (0, full, 5 % (1 << N), (1 << N) // 3):
            g = np.array([f0[b & ((1 << n) - 1)] for b in range(1 << N)], dtype=np.int64)
            g[x0] = -g[x0]
            W = fwht(g)
            # coefficient of g*chi_A at [N] is W[full ^ A]; need all nonzero over all A
            zero = int(np.count_nonzero(W == 0))
            total += 1 << N
            assert zero == 0, (name, N, x0, zero)
        res[f"{name}_N{N}"] = "all anchors nonzero top coefficient"
json.dump({"checked_anchor_cases": total, "status": "PASS", "detail": res}, open(sys.argv[1], "w"), indent=1)
print("PASS anchors", total)
