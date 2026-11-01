"""Referee checks for Corollaries G1, G2, the product-law value of U, and the read-once composition formula.

G1: U <= H(W) + sum_{k>=1} W_k log2 E[binom(|S|,k)]           (all f, n <= 4; equality for symmetric f)
G2: U <= log2 E(1+lam)^{|S|} - I log2 lam   for lam > 0          (all f, n <= 4, lam grid)
Product laws (any marginals theta): U = sum_i (1-theta_i) log2(1/(1-theta_i)) <= I log2 e.
Composition: f = g(h_1..h_k) on disjoint blocks: U(f) = U(P_g^mu) + sum_j P(j in J) U(q_j)  (brute force).
"""
import math, json, itertools
import numpy as np
from rlib import Spec, all_tables, walsh, popcounts, plogq, LOG2E

rng = np.random.default_rng(99)
res = {}

# ---------------- G1 and G2 exhaustively
for n in [2, 3, 4]:
    sp = Spec.from_tables(all_tables(n))
    U = sp.U(); I = sp.I(); H = sp.H(); Var = sp.Var()
    pc = popcounts(n)
    Wk = np.stack([sp.p[:, pc == k].sum(-1) for k in range(n + 1)], -1)
    HW = -plogq(Wk, Wk).sum(-1)
    G1 = HW.copy()
    for k in range(1, n + 1):
        mk = (sp.p * np.array([math.comb(int(s), k) for s in pc])).sum(-1)
        G1 += plogq(Wk[:, k], np.where(mk > 0, mk, 1))
    g1_viol = int((U > G1 + 1e-12).sum())
    g2_worst = -1e9
    for lam in [0.01, 0.1, 0.3, 1.0, 3.0, 10.0, 100.0]:
        Z = (sp.p * (1 + lam) ** pc).sum(-1)
        g2 = np.log2(Z) - I * math.log2(lam)
        g2_worst = max(g2_worst, float((U - g2).max()))
    res[f'G1G2_n{n}'] = dict(G1_violations=g1_viol, G2_worst_U_minus_bound=g2_worst)

# ---------------- G1 equality for symmetric functions (all symmetric f on n bits, n <= 9)
sym_err = 0.0
for n in range(2, 10):
    N = 1 << n
    pc = popcounts(n)
    combs = [np.array([math.comb(int(s), k) for s in pc], dtype=np.float64) for k in range(n + 1)]
    codes = np.arange(1 << (n + 1))
    tabs = 1 - 2 * ((codes[:, None] >> pc[None, :]) & 1)
    sp = Spec.from_tables(tabs)
    U = sp.U()
    Wk = np.stack([sp.p[:, pc == k].sum(-1) for k in range(n + 1)], -1)
    G1 = -plogq(Wk, Wk).sum(-1)
    for k in range(1, n + 1):
        mk = (sp.p * combs[k]).sum(-1)
        G1 += plogq(Wk[:, k], np.where(mk > 0, mk, 1))
    sym_err = max(sym_err, float(np.abs(U - G1).max()))
res['G1_equality_symmetric_max_abs_err'] = sym_err

# ---------------- product laws
pe = 0.0; ratio_max = 0.0
for trial in range(200):
    n = int(rng.integers(1, 9)); th = rng.random(n) ** 3
    N = 1 << n; idx = np.arange(N)
    p = np.ones(N)
    for i in range(n):
        b = (idx >> i) & 1
        p *= np.where(b == 1, th[i], 1 - th[i])
    sp = Spec(p)
    U = float(sp.U()[0]); pred = float(sum((1 - t) * math.log2(1 / (1 - t)) for t in th))
    pe = max(pe, abs(U - pred)); ratio_max = max(ratio_max, U / (sum(th) * LOG2E))
res['product_law_U_formula_err'] = pe
res['product_law_max_U_over_IlogE'] = ratio_max

# ---------------- composition formula (brute force)
def biased_coeffs(gtab, k, mus):
    """mu-biased Fourier coefficients of g:{-1,1}^k -> {-1,1} (index bit j = 1 iff y_j = -1)."""
    sig = [math.sqrt(1 - m * m) for m in mus]
    out = np.zeros(1 << k)
    for J in range(1 << k):
        s = 0.0
        for y in range(1 << k):
            w = 1.0; ph = 1.0
            for j in range(k):
                yj = -1 if (y >> j) & 1 else 1
                w *= (1 + mus[j] * yj) / 2
                if (J >> j) & 1:
                    ph *= (yj - mus[j]) / sig[j]
            s += w * gtab[y] * ph
        out[J] = s
    return out

def U_of_law(p):
    return float(Spec(p).U()[0])

comp_err = 0.0; compH_err = 0.0; compI_err = 0.0; ntest = 0
for trial in range(120):
    k = int(rng.integers(2, 4))
    sizes = [int(rng.integers(1, 4)) for _ in range(k)]
    if sum(sizes) > 11:
        continue
    gtab = rng.choice([-1, 1], size=1 << k)
    hs = []
    for m in sizes:
        while True:
            h = rng.choice([-1, 1], size=1 << m)
            if abs(h.sum()) < (1 << m):  # nonconstant
                break
        hs.append(h)
    n = sum(sizes); N = 1 << n
    # build f
    offs = np.cumsum([0] + sizes[:-1])
    f = np.zeros(N, dtype=np.int64)
    for x in range(N):
        y = 0
        for j in range(k):
            sub = (x >> int(offs[j])) & ((1 << sizes[j]) - 1)
            if hs[j][sub] == -1:
                y |= (1 << j)
        f[x] = gtab[y]
    if abs(f.sum()) == N:
        continue
    spf = Spec.from_tables(f)
    Uf = float(spf.U()[0]); Hf = float(spf.H()[0]); If = float(spf.I()[0])
    mus = [float(h.mean()) for h in hs]
    gb = biased_coeffs(gtab, k, mus); Pg = gb ** 2
    pin = []  # P(j in J)
    for j in range(k):
        pin.append(float(sum(Pg[J] for J in range(1 << k) if (J >> j) & 1)))
    Upred = U_of_law(Pg); Hpred = float(Spec(Pg).H()[0]); Ipred = 0.0
    for j, h in enumerate(hs):
        sh = Spec.from_tables(h)
        p = sh.p[0].copy(); p0 = p[0]; q = p.copy(); q[0] = 0.0; q = q / (1 - p0)
        sq = Spec(q)
        Upred += pin[j] * float(sq.U()[0]); Hpred += pin[j] * float(sq.H()[0]); Ipred += pin[j] * float(sq.I()[0])
    comp_err = max(comp_err, abs(Uf - Upred)); compH_err = max(compH_err, abs(Hf - Hpred)); compI_err = max(compI_err, abs(If - Ipred))
    ntest += 1
res['composition_tests'] = ntest
res['composition_U_err'] = comp_err; res['composition_H_err'] = compH_err; res['composition_I_err'] = compI_err
print(json.dumps(res, indent=1))
with open('g1g2_comp_results.json', 'w', encoding='utf-8') as fh:
    json.dump(res, fh, indent=1)
