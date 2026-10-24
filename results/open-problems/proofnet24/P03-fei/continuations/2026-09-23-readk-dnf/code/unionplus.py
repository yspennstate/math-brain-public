"""Theorem 5.4(d) checks (read-k unions of threshold functions, the strengthened inequality):
 H+/J (true), W*Lambda/J (proof: <= 4k), and per coordinate the ratio
 E_nu_j[G_j 1[T != 0]] / nu_j(T != 0) (proof: <= 2k(a L1/ln2 + c2 K) = 19.70k), recording how often the proof's
 second case nu_j(0) > 1/2 occurs and the largest ratio there (proof: < (a/ln2) ln(4k^2) + c2 log2(4k)).
 Dictator-like threshold functions are mixed in so that the second case actually occurs."""
import math, numpy as np
import unionltf as U
from feicore import spectrum, total_influence, popcounts, polite, wht
polite()
LN2 = math.log(2); A = U.A_EXP; BETA = U.BETA; C1 = U.C1; C2 = U.C2; L1 = U.L1; K5 = 0.66241

def ltf_mixed(R, n, rng):
    xs = np.arange(1 << n)
    bits = ((xs[:, None] >> np.arange(n)[None, :]) & 1) * 2 - 1
    w = np.zeros(n); s = rng.choice([-1, 1], size=len(R)); mag = rng.exponential(size=len(R)) + 0.05
    if rng.random() < 0.4:                       # dictator-like: one dominant weight
        mag[0] += mag.sum() * rng.uniform(1.0, 3.0)
    w[R] = s * mag
    theta = float(rng.uniform(-1, 1) * mag.sum() * rng.choice([0.1, 0.3, 0.8]))
    return (bits @ w - theta) > 0, w

def run(n, k, rng):
    fam = U.build(n, k, rng)
    N = 1 << n; xs = np.arange(N); pc = popcounts(n)
    H_l, R_l, W_l = [], [], []
    for R in fam:
        h, w = ltf_mixed(R, n, rng)
        if h.all() or (~h).all(): continue
        rel = [j for j in R if np.any(h[xs[(xs >> j) & 1 == 0]] != h[xs[(xs >> j) & 1 == 0] | (1 << j)])]
        if not rel: continue
        H_l.append(h); R_l.append(rel); W_l.append(w)
    if not H_l: return None
    deg = np.zeros(n, dtype=int)
    for R in R_l:
        for j in R: deg[j] += 1
    kk = int(deg.max()); m = len(H_l)
    V = np.stack(H_l); out = V.any(axis=0)
    if out.all() or (~out).all(): return None
    g = np.where(out, -1.0, 1.0); P = spectrum(g)
    big = pc >= 2; W = float(P[big].sum()); J = float((P * pc)[big].sum())
    if J < 1e-12: return None
    nz = (xs > 0) & (P > 1e-300)
    Hplus = float(-(P[nz] * np.log2(P[nz])).sum())
    pis = V.mean(axis=1); pip = np.minimum(pis, 0.5)
    Lam = float(np.sum(np.log2(1 / (1 - pip))))
    rank = np.full((m, n), 10 ** 6, dtype=float); Umask = np.zeros((m, n), dtype=np.int64); Rmask = np.zeros(m, dtype=np.int64)
    for l in range(m):
        order = sorted(R_l[l], key=lambda j: (-abs(W_l[l][j]), j)); acc = 0
        for pos, j in enumerate(order):
            rank[l, j] = pos + 1; Umask[l, j] = acc; acc |= 1 << j
        Rmask[l] = acc
    kappa = np.stack([pc[xs & int(Rmask[l])] for l in range(m)])
    dense = kappa >= (np.log2(1 / pip) / BETA)[:, None]
    worst_ratio = 0.0; worst_case2 = 0.0; case2 = 0
    for j in range(n):
        inS = ((xs >> j) & 1) == 1
        rest = xs[(xs >> j) & 1 == 0]; up = rest | (1 << j)
        d = out[up].astype(float) - out[rest].astype(float)
        if not np.any(d): continue
        Dj = np.zeros(N); Dj[rest] = d; Dj[up] = d
        c = wht(Dj) / N; nu = c ** 2; nu /= nu.sum()                  # law of T over subsets (bit j always 0)
        best = np.full(N, np.inf)
        for l in range(m):
            if j not in R_l[l]: continue
            Fl = np.log(rank[l, j] / (pc[xs & int(Umask[l, j])] + 1.0))
            best = np.minimum(best, A * Fl / LN2 + C2 * math.log2(1 / pip[l]) * (~dense[l]))
        # G_j evaluated at A = T + j: shift the arrays indexed by A to T
        Gj_T = best[rest | (1 << j)]
        nuT = nu[rest]; nonempty = rest != 0
        num = float((nuT * Gj_T * nonempty).sum()); den = float((nuT * nonempty).sum())
        if den < 1e-15: continue
        r = num / den; worst_ratio = max(worst_ratio, r)
        if nuT[~nonempty].sum() > 0.5:
            case2 += 1; worst_case2 = max(worst_case2, r)
    return dict(FP=Hplus / J, vac=W * Lam / (kk * J), ratio=worst_ratio / kk, case2=case2, r2=worst_case2, k=kk)

rng = np.random.default_rng(404)
agg = dict(FP=0.0, vac=0.0, ratio=0.0, r2=0.0); cnt = 0; c2tot = 0; kmax = 0
for n in (10, 12, 14):
    for k in (1, 2, 3):
        for rep in range(6 if n < 14 else 3):
            a = run(n, k, rng)
            if a is None: continue
            cnt += 1; c2tot += a['case2']; kmax = max(kmax, a['k'])
            for f in agg: agg[f] = max(agg[f], a[f])
print(f"{cnt} formulas (k <= {kmax}): max H+/J {agg['FP']:.3f} (proof 11.9+33k); max W*Lambda/(kJ) {agg['vac']:.3f} "
      f"(proof <= 4); max per-coordinate E[G 1(T!=0)]/nu(T!=0) divided by k: {agg['ratio']:.3f} (proof <= 19.70); "
      f"coordinates in the second case nu(0) > 1/2: {c2tot}, largest ratio there {agg['r2']:.3f} "
      f"(proof < {A/LN2*math.log(4)+C2*2:.2f} at k=1)", flush=True)

# Targeted family for the proof's second case: h_1 dictator-like on {0,...}, the other h_l rarely true, so that
# coordinate 0 has Inf_0(f) > 1/2 and nu_0(empty) > 1/2.
def ltf_case2(R, n, rng, first):
    xs = np.arange(1 << n)
    bits = ((xs[:, None] >> np.arange(n)[None, :]) & 1) * 2 - 1
    w = np.zeros(n); s = rng.choice([-1, 1], size=len(R)); mag = rng.exponential(size=len(R)) * 0.2 + 0.05
    if first:
        mag[0] = 10.0; theta = float(rng.uniform(-0.3, 0.3))
    else:
        theta = float(mag.sum() * rng.uniform(0.7, 0.95))
    w[R] = s * mag
    return (bits @ w - theta) > 0, w

def build_case2(n, k, rng):
    fam = [[0] + sorted(rng.choice(np.arange(1, n), size=3, replace=False).tolist())]
    deg = np.zeros(n, dtype=int)
    for j in fam[0]: deg[j] += 1
    for _ in range(100):
        if len(fam) >= 6: break
        size = int(rng.integers(3, 7)); cand = [j for j in range(1, n) if deg[j] < k]
        if len(cand) < size: continue
        R = sorted(rng.choice(cand, size=size, replace=False).tolist())
        for j in R: deg[j] += 1
        fam.append(R)
    return fam

cnt = 0; c2 = 0; worst2 = 0.0; worstr = 0.0; worstFP = 0.0
for n in (10, 12):
    for k in (1, 2, 3):
        for rep in range(5):
            flag = {'first': True}
            def mk(R, n_, rng_, flag=flag):
                out = ltf_case2(R, n_, rng_, flag['first']); flag['first'] = False; return out
            ltf_mixed_saved = ltf_mixed
            globals()['ltf_mixed'] = mk
            U.build = build_case2
            a = run(n, k, rng)
            globals()['ltf_mixed'] = ltf_mixed_saved
            if a is None: continue
            cnt += 1; c2 += a['case2']; worst2 = max(worst2, a['r2']); worstr = max(worstr, a['ratio']); worstFP = max(worstFP, a['FP'])
print(f"case-2 family: {cnt} formulas, coordinates with nu(0) > 1/2: {c2}, largest ratio there {worst2:.3f} "
      f"(pointwise proof bound at k<=3 is at most {A/LN2*math.log(36)+C2*math.log2(12):.2f}); max ratio/k overall {worstr:.3f}; "
      f"max H+/J {worstFP:.3f}", flush=True)
