# The C1 ratio (Delta_v / Inf_v at a most influential coordinate) for f = OR of k disjoint copies of a small monotone g,
# exactly, for every monotone g on 1..4 variables and k = 1..40. For an OR of independent parts h_i with g_i = 1 - h_i,
# P(S) = 4 prod_i w_i(S_i) for S nonempty (w_i = squared coefficients of g_i, total p_i = Pr[h_i = 0]), so
#   H(f) = -8 prod p + 4 sum_i (prod_{j != i} p_j) H_i - phi(4 prod w_i(empty)) + phi((2 prod p - 1)^2).
# Restricting v inside copy 1 replaces that copy by its restriction; Inf_v(f) = Inf_v(copy) * p^(k-1).
import math, numpy as np
from mono_enum import monotone_masks
def phi(t): return 0.0 if t <= 0 else -t * math.log2(t)
def fwht_vec(v):
    a = v.astype(float).copy(); N = len(a); h = 1
    while h < N:
        a = a.reshape(-1, 2, h); u = a[:, 0, :].copy(); w = a[:, 1, :]; a[:, 0, :] = u + w; a[:, 1, :] = u - w; a = a.reshape(N); h *= 2
    return a / N
def part_stats(tt):
    """tt: bool array of h over {0,1}^m. Returns (p, Hpart, w_empty) for g = 1 - h in the 0/1 convention."""
    g = (~tt).astype(float)
    c = fwht_vec(g); w = c * c
    p = float(g.mean()); Hp = float(sum(phi(x) for x in w)); return p, Hp, float(w[0])
def H_or(parts):
    prodp = 1.0; prodw = 1.0
    for p, h, we in parts: prodp *= p; prodw *= we
    tot = -8 * prodp
    for i, (p, h, we) in enumerate(parts):
        if p > 0: tot += 4 * (prodp / p) * h
    return tot - phi(4 * prodw) + phi((2 * prodp - 1) ** 2)
best = (0, None)
rows = []
for m in range(1, 5):
    masks = monotone_masks(m); N = 1 << m; x = np.arange(N)
    for mk in masks:
        tt = ((int(mk) >> x) & 1).astype(bool)
        if tt.all() or not tt.any(): continue
        # influences within the copy
        infs = [float((tt[x[((x >> v) & 1) == 0]] != tt[x[((x >> v) & 1) == 0] | (1 << v)]).mean()) for v in range(m)]
        if max(infs) == 0: continue
        full = part_stats(tt); p = full[0]
        for v in range(m):
            if infs[v] < max(infs) - 1e-12: continue
            lo = x[((x >> v) & 1) == 0]
            r0 = part_stats(tt[lo]); r1 = part_stats(tt[lo | (1 << v)])
            for k in range(1, 41):
                Hk = H_or([full] * k); H0 = H_or([r0] + [full] * (k - 1)); H1 = H_or([r1] + [full] * (k - 1))
                inf = infs[v] * p ** (k - 1)
                if inf < 1e-9: break
                r = (Hk - 0.5 * (H0 + H1)) / inf
                if r > best[0]: best = (r, (m, int(mk), v, k))
                rows.append(r)
print('OR of k copies of g, all monotone g on <= 4 variables, k <= 40: largest ratio at a most influential coordinate %.5f' % best[0])
print('attained by m=%d mask=%d v=%d k=%d' % best[1])
m, mk, v, k = best[1]; N = 1 << m
print('g truth table (bit x = g(x)):', format(mk, '0%db' % N)[::-1])
