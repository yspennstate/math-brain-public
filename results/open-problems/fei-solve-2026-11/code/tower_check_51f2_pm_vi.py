"""Tower with PM(K33) and its negation variants (input flip: evaluate at 1-p; output flip: p' -> 1-p').
W(p) = max_variant [G(p_in) + W(p')] / J(p_in).  Value iteration on a log-odds grid, then an exact rollout from 1/2."""
import itertools, math
import numpy as np

perms = list(itertools.permutations(range(3)))
N = 1 << 9
bits = np.array([[(x >> e) & 1 for e in range(9)] for x in range(N)], dtype=float)
pm = np.array([any(all((x >> (3 * i + s[i])) & 1 for i in range(3)) for s in perms) for x in range(N)])
F = np.where(pm, -1.0, 1.0)
sizes = bits.sum(1)

def stats(p):
    s = math.sqrt(p * (1 - p))
    w = np.prod(np.where(bits == 1, p, 1 - p), axis=1)
    phi = (bits - p) / s
    chi = np.prod(np.where(bits[None, :, :] == 1, phi[:, None, :], 1.0), axis=2)
    coef = (w * F) @ chi
    var = 1 - coef[0] ** 2
    q = coef[1:] ** 2 / var
    q = q[q > 1e-300]
    return float(w[F < 0].sum()), float(-(q * np.log2(q)).sum()), float((coef[1:] ** 2 * sizes[1:]).sum() / var)

# fixed point of P(p)=Pr_p[PM]
lo, hi = 0.3, 0.6
for _ in range(60):
    m = (lo + hi) / 2
    if stats(m)[0] < m: lo = m
    else: hi = m
ps, gs, js = stats(lo)
print("fixed point p*=%.9f  G=%.9f J=%.9f  stationary G/(J-1)=%.9f" % (lo, gs, js, gs / (js - 1)))

L = np.linspace(-9, 9, 1601)
grid = 1 / (1 + np.exp(-L))
S = np.array([stats(p) for p in grid])          # P, G, J at each grid p
def interp(W, p):
    return np.interp(math.log(p / (1 - p)) if 0 < p < 1 else (99 if p >= 1 else -99), L, W)
W = np.zeros(len(grid))
for sweep in range(200):
    Wn = np.empty_like(W)
    for k, p in enumerate(grid):
        best = -1e9
        for kin in (k, len(grid) - 1 - k):       # input flip: grid is symmetric, 1-p sits at the mirrored index
            P, G, J = S[kin]
            for pn in (P, 1 - P):
                pn = min(max(pn, grid[0]), grid[-1])
                best = max(best, (G + interp(W, pn)) / J)
        Wn[k] = best
    if np.max(np.abs(Wn - W)) < 1e-12:
        break
    W = Wn
print("VI sweeps %d  W(1/2) grid = %.9f" % (sweep, interp(W, 0.5)))

# exact rollout: greedy on the grid W, true quantities
p, Gt, Jt = 0.5, 0.0, 1.0
for step in range(60):
    best = None
    for pin in (p, 1 - p):
        P, G, J = stats(pin)
        for pn in (P, 1 - P):
            v = (G + interp(W, min(max(pn, grid[0]), grid[-1]))) / J
            if best is None or v > best[0]:
                best = (v, G, J, pn)
    _, G, J, pn = best
    Gt, Jt = G + J * Gt, J * Jt
    p = pn
    if step < 4 or step % 10 == 9:
        print("  step %2d p=%.9f G/J=%.10f" % (step, p, Gt / Jt))
print("rollout G/J = %.10f" % (Gt / Jt))
