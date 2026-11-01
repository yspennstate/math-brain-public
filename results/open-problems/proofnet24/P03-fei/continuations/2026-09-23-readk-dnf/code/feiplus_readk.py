"""Audit of the uniform FEI+ proof for read-k DNFs, piece by piece, on random (non-)monotone redundant formulas.
Quantities (log base 2, beta = 3):
  R0 = H^{>=1} / (I - Var)                     true FEI+ ratio
  R1 = sum_{|S|>=2} P log2(1/Q1) / J           reduced Gibbs term, Q1 = term reference with pi_t = 2^{-|V_t|}
  R2 = W * Lambda / J        (proof: <= 4k)
  R3 = max_i nu_i(empty) / sum_{s ni i} 2^{-(w_s-1)}   (proof: <= 1)
  R4 = sum_i Inf_i w_i nu_i(sparse & T nonempty) / J  (proof: <= max(log2 k + 2, 2 k C_3))
  R5 = dense part  E[1{|S|>=2} * sum_{t in D(S)} |V_t|] / J   (proof: <= beta k)
"""
import math, numpy as np
from feicore import spectrum, popcounts, polite, wht
from termref import superset_sum
from readk_nonmono import random_nonmono
polite()
LN2 = math.log(2); BETA = 3.0; C3 = 13 * 299 / 4096

def audit(n, terms):
    N = 1 << n; xs = np.arange(N, dtype=np.int64); pc = popcounts(n)
    m = len(terms)
    sat = np.array([((xs & mm) == v) for (mm, v) in terms])
    fval = sat.any(axis=0)
    g = np.where(fval, -1.0, 1.0)
    P = spectrum(g)
    nz = P > 1e-300
    H = float(-(P[nz] * np.log2(P[nz])).sum())
    Hp = H - (P[0] * math.log2(1 / P[0]) if P[0] > 0 else 0.0)
    I = float((P * pc).sum()); Var = 1 - float(P[0])
    big = pc >= 2
    W = float(P[big].sum()); J = float((P * pc)[big].sum())
    sizes = np.array([bin(mm).count('1') for (mm, v) in terms])
    k = max(sum(1 for (mm, v) in terms if mm >> j & 1) for j in range(n))
    pi = 2.0 ** -sizes
    Lam = float(-np.log2(1 - pi).sum())
    # term reference Q1 on all sets
    unions = np.zeros(1 << m, dtype=np.int64)
    logq = np.full(1 << m, float(np.log(1 - pi).sum()))
    lr = np.log(pi) - np.log(1 - pi)
    for j in range(m):
        h = 1 << j
        unions[h:2 * h] = unions[:h] | terms[j][0]
        logq[h:2 * h] = logq[:h] + lr[j]
    Wt = np.zeros(N); np.add.at(Wt, unions, np.exp(logq - LN2 * pc[unions]))
    Q1 = superset_sum(Wt, n)
    sel = big & nz
    R1 = float((P[sel] * np.log2(1 / Q1[sel])).sum()) / J
    R2 = W * Lam / J
    # dense part: for each S with |S|>=2, sum of |V_t| over dense terms
    dense_sum = np.zeros(N)
    for (mm, v), wsz in zip(terms, sizes):
        dens = pc[xs & mm] >= wsz / BETA
        dense_sum += np.where(dens, wsz, 0)
    R5 = float((P[big] * dense_sum[big]).sum()) / J
    # per-coordinate: nu_i(empty) bound and sparse part
    R3 = 0.0; sparse_tot = 0.0
    for i in range(n):
        Ti = [t for t in range(m) if terms[t][0] >> i & 1]
        rest = xs[(xs >> i) & 1 == 0]; up = rest | (1 << i)
        d = fval[up].astype(float) - fval[rest].astype(float)
        if not np.any(d) or not Ti:
            continue
        D = np.zeros(N); D[rest] = d; D[up] = d
        c = wht(D) / N; inf_i = float(np.abs(d).mean())
        nu = c ** 2 / inf_i
        nu0 = float(nu[0])
        bnd = sum(2.0 ** -(sizes[t] - 1) for t in Ti)
        R3 = max(R3, nu0 / bnd)
        wi = min(sizes[t] for t in Ti)
        sp = np.ones(N, dtype=bool)
        for t in Ti:
            Vm = terms[t][0] & ~(1 << i)
            sp &= pc[xs & Vm] < sizes[t] / BETA - 1
        sp[0] = False                      # T nonempty
        sparse_tot += inf_i * wi * float(nu[sp].sum())
    R4 = sparse_tot / J
    return dict(k=k, R0=Hp / (I - Var), R1=R1, R2=R2, R3=R3, R4=R4, R5=R5,
                b2=4 * k, b4=max(math.log2(k) + 2, 2 * k * C3), b5=BETA * k)

if __name__ == '__main__':
    rng = np.random.default_rng(29)
    worst = {}
    configs = [(10, 1, [2, 3, 3, 4]), (10, 2, [2, 2, 3, 3, 3, 4]), (12, 2, [3] * 8), (12, 3, [2, 3, 3, 4, 4, 2, 3, 5, 2]),
               (14, 2, [4] * 7), (14, 3, [3, 3, 4, 4, 5, 5, 3, 4, 5, 6]), (14, 4, [2, 3, 3, 4, 4, 5, 2, 3, 4, 5, 6, 3]),
               (12, 5, [2, 2, 2, 3, 3, 3, 4, 4, 2, 3, 2, 5]), (13, 6, [1, 2, 3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 3, 4])]
    for n, kk, wl in configs:
        for r in range(8):
            for pneg in (0.0, 0.3, 0.5):
                terms = random_nonmono(n, kk, wl, rng, pneg=pneg)
                if not terms or len(terms) > 18:
                    terms = terms[:18]
                if not terms: continue
                a = audit(n, terms)
                key = a['k']
                w = worst.setdefault(key, {kk2: 0.0 for kk2 in ('R0', 'R1', 'R2', 'R3', 'R4', 'R5')})
                for kk2 in ('R0', 'R1', 'R2', 'R3', 'R4', 'R5'): w[kk2] = max(w[kk2], a[kk2])
                w['bounds'] = (a['b2'], round(a['b4'], 3), a['b5'])
    for key in sorted(worst):
        print(f"k={key}: " + " ".join(f"{kk2}={v:.3f}" if isinstance(v, float) else f"{kk2}={v}" for kk2, v in worst[key].items()), flush=True)
