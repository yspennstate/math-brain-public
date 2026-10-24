# Check of the biased step bound behind the product-measure theorem: for a monotone DNF gate G, a product measure with all
# biases in [eps, 1-eps], a minterm M of G of least size k, and v in M maximising mu_D(v blocked) (the coordinate of the
# biased minterm lemma), the credited step satisfies
#     Lstep_v <= (14.23 + 2 k log2(1/eps)) Rstep_v,
# with L = sum_{A nonempty} P~ log2(sigma_A^2/P~), R = I~ - Var~, and restriction weights mu(y_v = b). Also by duality the
# maxterm version, via the dual gate under the reflected measure.
import math, numpy as np
from biased_induction import LR, restrict
rng = np.random.default_rng(53)
worst = 0.0; worst_case = None; count = 0
for trial in range(500):
    m = int(rng.integers(2, 8)); N = 1 << m; x = np.arange(N); G = np.zeros(N, dtype=bool)
    for _ in range(int(rng.integers(1, 2 * m))):
        w = int(rng.integers(1, 4)); S = rng.choice(m, size=min(w, m), replace=False)
        mask = int(sum(1 << int(u) for u in S)); G |= (x & mask) == mask
    if G.all() or not G.any(): continue
    eps = float(rng.choice([0.02, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5]))
    q = list(rng.uniform(eps, 1 - eps, size=m))
    F = np.where(G, -1.0, 1.0)
    wts = np.ones(N)
    for j in range(m): wts *= np.where((x >> j) & 1, q[j], 1 - q[j])
    muD = float(wts[~G].sum())
    ones = [xx for xx in range(N) if G[xx]]
    minterms = [xx for xx in ones if all(not G[xx & ~(1 << u)] for u in range(m) if (xx >> u) & 1)]
    k = min(bin(M).count('1') for M in minterms)
    M = [Mt for Mt in minterms if bin(Mt).count('1') == k][0]
    vs = [u for u in range(m) if (M >> u) & 1]
    def blocked(v):
        lo = x[((x >> v) & 1) == 0]; hi = lo | (1 << v)
        return float(wts[lo][(~G[lo]) & G[hi]].sum()) / muD
    v = max(vs, key=blocked)
    L, R = LR(F, q)
    qq = q[:v] + q[v + 1:]
    L0, R0 = LR(restrict(F, m, v, 0), qq) if m > 1 else (0.0, 0.0)
    L1, R1 = LR(restrict(F, m, v, 1), qq) if m > 1 else (0.0, 0.0)
    Ls = L - ((1 - q[v]) * L0 + q[v] * L1); Rs = R - ((1 - q[v]) * R0 + q[v] * R1)
    bound = (14.23 + 2 * k * math.log2(1 / eps)) * Rs
    if Rs > 1e-14:
        r = Ls / bound; count += 1
        if r > worst: worst, worst_case = r, (m, k, eps, Ls / Rs)
    elif Ls > 1e-12:
        print('step with Rstep = 0 but Lstep = %.3e > 0 (m=%d k=%d)' % (Ls, m, k))
print('%d gates: max Lstep/(C(k,eps) Rstep) = %.4f (claim <= 1); worst case m=%d k=%d eps=%g raw ratio %.3f'
      % (count, worst, *worst_case))
