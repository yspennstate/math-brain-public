import numpy as np, sys, itertools
exec(open(r'~/AppData/Local/Temp/prob/h0020_search.py').read().split('best = (-np.inf, None)')[0])
rng = np.random.default_rng(int(sys.argv[1]))
def worst_over_orderings(R, lam):
    d = R.shape[0]; vals = []
    for perm in itertools.permutations(range(d)):
        Rp = R[np.ix_(perm, perm)].astype(float)
        vals.append(lam_max(Rp, lam, d - 1))
    return min(vals), max(vals)
found = {}
for t in range(int(sys.argv[2])):
    d = int(sys.argv[3]) if len(sys.argv) > 3 else rng.integers(3, 5); lam = int(rng.integers(1, 7))
    R = np.zeros((d, d), dtype=int)
    for i in range(d):
        off = rng.integers(0, lam + 2, size=d - 1) * (rng.random(d - 1) < rng.uniform(0.2, 1.0))
        R[i, [j for j in range(d) if j != i]] = off
        R[i, i] = lam - off.sum()
    if np.any(np.diag(R) < 0) or not irreducible(R): continue
    lo, hi = worst_over_orderings(R, lam)
    key = d
    if key not in found or lo > found[key][0]: found[key] = (lo, hi, R.copy(), lam)
for d in sorted(found):
    lo, hi, R, lam = found[d]
    print(f"d={d}: best min-over-orderings lambda_max = {lo:.5f} (max over orderings {hi:.5f}), balance {lam}\n{R}")
