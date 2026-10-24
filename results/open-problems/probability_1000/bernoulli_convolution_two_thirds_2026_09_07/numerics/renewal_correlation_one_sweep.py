"""The renewal's correlation, every scale in one chunked sweep (memory-safe, 16 MB per chunk).

int_M^inf Q^2 = (3/2) int_(2M/3)^inf cos^2(3 pi v/2) Q(v)^2 dv   is EXACT.
Decorrelation of cos^2(3 pi v/2) from Q^2 would give block ratio 3/4 and exponent 0.7095. Accumulate,
on the ladder N_n = (3/2)^n up to 10^5 (n <= 28):
    B_n    = int over [N_n, N_(n+1)) of Q^2
    C_n    = int over the same block of cos^2(3 pi v/2) Q^2
    corr_n = C_n / (B_n/2)        -> 1 under decorrelation
POWER CHECK, the failure the round-6 verifier found in its own null: report what a real drift would look
like in this statistic, rather than reading a flat sequence as evidence of nothing.
"""
import numpy as np

M, PTS, CH = 100_000.0, 400, 2_000_000
n_tot = int(M * PTS)
du = M / n_tot
edges = [1.5 ** n for n in range(0, 30)]
B = np.zeros(len(edges)); C = np.zeros(len(edges))
for s in range(0, n_tot, CH):
    k = min(CH, n_tot - s)
    u = (s + np.arange(k) + 0.5) * du
    q = np.ones(k); j = 0
    while True:
        a = (2.0/3.0) ** j * u
        q *= np.cos(np.pi * a); j += 1
        if a.max() < 1e-9: break
    q2 = q * q
    w = np.cos(1.5 * np.pi * u) ** 2 * q2
    idx = np.searchsorted(edges, u, side='right') - 1
    ok = idx >= 0
    B += np.bincount(idx[ok], weights=q2[ok] * du, minlength=len(edges))
    C += np.bincount(idx[ok], weights=w[ok] * du, minlength=len(edges))

print(f"{'n':>3} {'N=(3/2)^n':>12} {'block B_n':>12} {'ratio':>9} {'exponent':>9} {'corr_n':>9}")
prev = None
for n in range(0, 29):
    if B[n] <= 0: continue
    corr = C[n] / (0.5 * B[n])
    if prev is None or prev <= 0:
        print(f"{n:>3} {edges[n]:>12.1f} {B[n]:>12.4e} {'-':>9} {'-':>9} {corr:>9.4f}")
    else:
        r = B[n] / prev
        print(f"{n:>3} {edges[n]:>12.1f} {B[n]:>12.4e} {r:>9.4f} {-np.log(r)/np.log(1.5):>9.4f} {corr:>9.4f}")
    prev = B[n]
sel = [n for n in range(8, 29) if B[n] > 0]
cs = np.array([C[n]/(0.5*B[n]) for n in sel])
print(f"\ndecorrelated prediction: ratio 0.7500, exponent 0.7095, corr 1.0000")
print(f"corr over n={sel[0]}..{sel[-1]}: mean {cs.mean():.4f}  sd {cs.std(ddof=1):.4f}  "
      f"min {cs.min():.4f}  max {cs.max():.4f}")
print(f"OLS slope of corr on n: {np.polyfit(sel, cs, 1)[0]:+.5f} per step")
print("POWER: a corr biased high by d multiplies the per-step ratio by d, so the exponent falls by")
print("log(d)/log(1.5). corr = 1.05 costs 0.12 of exponent; corr = 1.35 exactly kills the decay.")
