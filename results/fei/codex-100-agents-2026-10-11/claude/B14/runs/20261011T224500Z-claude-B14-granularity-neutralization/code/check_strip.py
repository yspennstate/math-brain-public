# Supplementary (floating, support only): cost of stripping a padding point defect by one restriction.
# f'_N = pad(f) * (1 - 2*1{x=all+}); restrict padding coordinate j=n (0-based) ; x_j=-1 removes the defect.
import sys, json, math
import numpy as np
sys.path.insert(0, __import__("os").path.dirname(__file__))
from b14lib import fwht  # same FWHT as the main check (module body guarded below)
def H(f, m):
    W = fwht(np.array(f, dtype=np.int64)).astype(np.float64) / float(1 << m)
    q = W * W; q = q[q > 0]
    return float(-(q * np.log2(q)).sum())
def base():
    yield "x1", 1, [1, -1]
    yield "AND2", 2, [1, 1, 1, -1]
    yield "Maj3", 3, [1 if sum(1 - 2 * ((b >> i) & 1) for i in range(3)) > 0 else -1 for b in range(8)]
    yield "addr2", 6, [1 - 2 * ((b >> (2 + (b & 3))) & 1) for b in range(64)]
out = {}
for name, n, f0 in base():
    rows = []
    for N in range(n + 2, min(n + 9, 15)):
        fp = [f0[b & ((1 << n) - 1)] for b in range(1 << N)]; fp[0] = -fp[0]
        pad1 = [f0[b & ((1 << n) - 1)] for b in range(1 << (N - 1))]
        fp1 = list(pad1); fp1[0] = -fp1[0]
        dec = H(fp, N) - 0.5 * (H(pad1, N - 1) + H(fp1, N - 1))
        infl = 2.0 / (1 << N)
        rows.append({"N": N, "decrement_bits": dec, "queried_influence": infl, "ratio": dec / infl})
    out[name] = rows
json.dump(out, open(sys.argv[1], "w"), indent=1)
for k, v in out.items():
    print(k, [(r["N"], round(r["ratio"], 3)) for r in v])
