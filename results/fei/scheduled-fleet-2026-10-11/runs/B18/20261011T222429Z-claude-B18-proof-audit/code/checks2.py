"""B18 lead second-lane checks (independent implementations, small exact/float domains, frozen here):
 (1) A021 exact entropy/influence formula: b in {dictator, Maj3, 3-bit balanced 'mux'}, t in {1,2}, k in {1,2,3}.
 (2) A087 own claim: lambda_s on the control-first tree equals u-u^2+u^2 log2((1-2u+2u^2)/u^2), u=2^-s.
 (3) A036: K>=T/4-8I and B<=T/4+8I on tensor products of point defects (m=2..5, up to 3 factors, <=12 bits),
     random translations; float64 (evidence; the claims are analytic).
 (4) A092 closed form E(p)=J-M for f=(-1)^{xy}, P(Y=1)=1/4: check E>=p(log2(1/p)/2-7) and E<=h2(p)-h2(1-sqrt(1-p))
     (A096 bound) at p=2^-k, k=1..60, mpmath 50 digits.
 (5) A096 universal singleton tax J-M<=h2(r)-h2(1-sqrt(1-r)): random falsification search, residual 1..3 bits,
     random Boolean children and random interior biases, 40000 trials + the stated extremal pair. Float64 evidence only.
Memory < 100 MB, runtime < 3 min.
"""
import numpy as np, math, itertools, json, sys, random
import mpmath as mp
res = {}
def walsh(vals, nb):
    # vals: truth table on nb uniform bits (index bit i = x_i in {0,1}); return fhat over subsets (uniform)
    N = 1 << nb
    h = np.array(vals, dtype=float).copy()
    step = 1
    while step < N:
        for s in range(0, N, 2 * step):
            a = h[s:s + step].copy(); b = h[s + step:s + 2 * step].copy()
            h[s:s + step] = a + b; h[s + step:s + 2 * step] = a - b
        step *= 2
    return h / N
def ent(P):
    P = np.asarray(P, dtype=float); P = P[P > 0]
    return float(-(P * np.log2(P)).sum())
def infl(P, nb):
    return float(sum(P[s] * bin(s).count('1') for s in range(1 << nb)))
# (1) A021
def bfun(name):
    if name == 'dict': return 1, lambda x: 1 - 2 * (x & 1)
    if name == 'maj3': return 3, lambda x: 1 if bin(x & 7).count('1') <= 1 else -1
    if name == 'mux': return 3, lambda x: (1 - 2 * ((x >> 1) & 1)) if (x & 1) else (1 - 2 * ((x >> 2) & 1))
out1 = []
for name in ('dict', 'maj3', 'mux'):
    m, b = bfun(name)
    Pb = walsh([b(x) for x in range(1 << m)], m) ** 2
    Hb, Ib = ent(Pb), infl(Pb, m)
    for t in (1, 2):
        for k in (1, 2, 3):
            nb = t * m + k
            if nb > 12: continue
            def F(x):
                ctrl = x >> (t * m)
                if ctrl != (1 << k) - 1: return 1
                v = 1
                for j in range(t): v *= b((x >> (j * m)) & ((1 << m) - 1))
                return v
            P = walsh([F(x) for x in range(1 << nb)], nb) ** 2
            q = 2.0 ** -k
            Hf = q * t * Hb + (4 * q - 2 * q * q) * k - 2 * (1 - q) ** 2 * math.log2(1 - q)
            If = q * (t * Ib + k)
            out1.append([name, t, k, ent(P) - Hf, infl(P, nb) - If])
res['A021_max_abs_dev_H'] = max(abs(r[3]) for r in out1); res['A021_max_abs_dev_I'] = max(abs(r[4]) for r in out1)
# (2) A087 lambda identity: node with s remaining controls, core g; query one control coordinate.
out2 = []
for name in ('dict', 'maj3', 'mux'):
    m, g = bfun(name)
    for s in (1, 2, 3, 4):
        nb = m + s
        def G(x):
            return g(x & ((1 << m) - 1)) if (x >> m) == (1 << s) - 1 else 1
        a = walsh([G(x) for x in range(1 << nb)], nb)
        bit = 1 << m  # first control
        lam = 0.0
        for T in range(1 << nb):
            if T & bit: continue
            at, bt = a[T], a[T | bit]
            if bt * bt > 0: lam += bt * bt * math.log2((at * at + bt * bt) / (bt * bt))
        u = 2.0 ** -s
        pred = u - u * u + u * u * math.log2((1 - 2 * u + 2 * u * u) / (u * u))
        out2.append([name, s, lam - pred])
res['A087_lambda_max_abs_dev'] = max(abs(r[2]) for r in out2)
# A_k and the bound q(k+A_k) <= 4kq
Ak = lambda k: sum(2.0 ** -s * (2 * s - 1 + math.log2(1 - 2.0 ** (1 - s) + 2.0 ** (1 - 2 * s))) for s in range(1, k + 1))
res['A087_weighted_sum_check'] = [[k, (2.0 ** -k) * (k + Ak(k)), 4 * k * 2.0 ** -k] for k in (1, 2, 5, 10)]
# (3) A036
def ptdef(m, x0):
    return [(-1 if x == x0 else 1) for x in range(1 << m)]
def tensor_coeffs(ms, x0s):
    a = np.array([1.0])
    for m, x0 in zip(ms, x0s):
        am = walsh(ptdef(m, x0), m)
        a = np.kron(am, a)  # new factor occupies higher bits
    return a
def wht(v):
    h = v.copy(); N = len(h); step = 1
    while step < N:
        for s in range(0, N, 2 * step):
            x = h[s:s + step].copy(); y = h[s + step:s + 2 * step].copy()
            h[s:s + step] = x + y; h[s + step:s + 2 * step] = x - y
        step *= 2
    return h
worst_K = 1e9; worst_B = 1e9; rows3 = []
rng = random.Random(20261011)
configs = [(2,), (3,), (4,), (5,), (2, 2), (2, 3), (3, 3), (2, 4), (3, 4), (4, 4), (2, 5), (2, 2, 2), (2, 2, 3), (2, 3, 3), (3, 3, 3), (2, 2, 4), (2, 3, 4), (4, 4, 4)]
for ms in configs:
    nb = sum(ms)
    for trial in range(3):
        x0s = [rng.randrange(1 << m) for m in ms] if trial else [0] * len(ms)
        a = tensor_coeffs(ms, x0s)
        P = a * a
        N = len(P)
        pi = np.array([P[[s for s in range(N) if s >> i & 1]].sum() for i in range(nb)])
        Bm = sum(-(x * math.log2(x) + (1 - x) * math.log2(1 - x)) for x in pi if 0 < x < 1)
        H = ent(P); I = float(pi.sum()); K = Bm - H
        Q = np.ones(N)
        for i in range(nb):
            sel = np.array([(s >> i) & 1 for s in range(N)])
            Q *= np.where(sel == 1, pi[i], 1 - pi[i])
        bvec = np.where(P > 0, np.sign(a) * np.sqrt(Q), 0.0)
        # autocorrelation over F2^n: (b*b)(U) = (1/N) WHT( WHT(b)^2 ) with unnormalized WHT
        wb = wht(bvec)
        conv = wht(wb * wb) / N
        v = conv ** 2
        Z = v.sum()
        T = ent(v / Z) - math.log2(Z)
        rows3.append([list(ms), trial, H, I, Bm, K, T, K - (T / 4 - 8 * I), T / 4 + 8 * I - Bm])
        worst_K = min(worst_K, K - (T / 4 - 8 * I)); worst_B = min(worst_B, T / 4 + 8 * I - Bm)
res['A036_min_slack_K_ge_T4_minus_8I'] = worst_K
res['A036_min_slack_B_le_T4_plus_8I'] = worst_B
res['A036_min_slack_H_le_4I'] = min(4 * r[3] - r[2] for r in rows3)
res['A036_sample_rows'] = [[r[0], r[1]] + [round(x, 5) for x in r[2:]] for r in rows3[:6]]
# (4) A092 / A096 consistency on the AND endpoint
mp.mp.dps = 50
def h2(x):
    x = mp.mpf(x)
    if x <= 0 or x >= 1: return mp.mpf(0)
    return -(x * mp.log(x, 2) + (1 - x) * mp.log(1 - x, 2))
def E_and(p):
    p = mp.mpf(p)
    J = h2(3 * p / 4) - p * h2(mp.mpf(1) / 4)
    M = (1 - 3 * p / 4) * h2(p * (1 - p) / (4 - 3 * p)) + (3 * p / 4) * h2(p)
    return J - M
lowfail = []; upfail = []; ratios = []
for k in range(1, 61):
    p = mp.mpf(2) ** -k
    E = E_and(p)
    lo = p * (mp.log(1 / p, 2) / 2 - 7)
    up = h2(p) - h2(1 - mp.sqrt(1 - p))
    if E < lo: lowfail.append(k)
    if E > up: upfail.append(k)
    if k in (5, 10, 20, 40, 60): ratios.append([k, float(E / (p * mp.log(1 / p, 2)))])
res['A092_lower_bound_failures_k'] = lowfail
res['A096_upper_bound_failures_on_AND_k'] = upfail
res['AND_E_over_plog'] = ratios
# (5) A096 random falsification (float64)
def phi(x, p):
    return (x - p) / math.sqrt(p * (1 - p))
def biased_coeffs(tab, nb, ps):
    # tab: values on {0,1}^nb (index bit i = x_i); ps[i] = P(x_i=1); return coefficients over subsets
    N = 1 << nb
    w = np.array([math.prod(ps[i] if (x >> i) & 1 else 1 - ps[i] for i in range(nb)) for x in range(N)])
    co = np.zeros(N)
    for S in range(N):
        bas = np.array([math.prod(phi((x >> i) & 1, ps[i]) for i in range(nb) if (S >> i) & 1) for x in range(N)])
        co[S] = float((w * tab * bas).sum())
    return co
def tax(Gt, Ht, nres, pres, p):
    # X is bit 0 (X=1 -> G, X=0 -> H); residual bits 1..nres
    nb = nres + 1; N = 1 << nb
    tab = np.array([Gt[x >> 1] if x & 1 else Ht[x >> 1] for x in range(N)], dtype=float)
    co = biased_coeffs(tab, nb, [p] + list(pres))
    P = co * co
    M = 0.0
    for T in range(0, N, 2):
        mm = P[T] + P[T | 1]
        if mm > 0 and P[T | 1] > 0 and P[T] > 0:
            x = P[T | 1] / mm; y = P[T] / mm
            if x > 0 and y > 0: M += mm * (-(x * math.log2(x) + y * math.log2(y)))
    Sres = np.array([P[T] + P[T | 1] for T in range(0, N, 2)])
    cG = biased_coeffs(np.array(Gt, dtype=float), nres, pres); cH = biased_coeffs(np.array(Ht, dtype=float), nres, pres)
    J = ent(Sres) - p * ent(cG * cG) - (1 - p) * ent(cH * cH)
    r = min(p, 1 - p); dl = 1 - math.sqrt(1 - r)
    hh = lambda y: 0.0 if y <= 0 or y >= 1 else -(y * math.log2(y) + (1 - y) * math.log2(1 - y))
    return J - M, hh(r) - hh(dl)
rng = random.Random(7)
worst5 = -1e9; worst5_case = None; ntr = 0
for trial in range(40000):
    nres = rng.choice([1, 2, 2, 3])
    Nr = 1 << nres
    Gt = [rng.choice([1, -1]) for _ in range(Nr)]; Ht = [rng.choice([1, -1]) for _ in range(Nr)]
    pres = [rng.choice([rng.uniform(0.01, 0.99), 0.5, 0.25, 0.75, rng.uniform(0.001, 0.05)]) for _ in range(nres)]
    p = rng.choice([rng.uniform(0.0005, 0.5), 2.0 ** -rng.randint(1, 14), rng.uniform(0.5, 0.9995)])
    e, ub = tax(Gt, Ht, nres, pres, p)
    ntr += 1
    if e - ub > worst5:
        worst5 = e - ub; worst5_case = [Gt, Ht, pres, p, e, ub]
# stated extremal pair: H=1, G=(-1)^{y1 y2} on two uniform residual bits
ext = []
for k in (2, 4, 8, 12, 16):
    p = 2.0 ** -k
    e, ub = tax([1, 1, 1, -1], [1, 1, 1, 1], 2, [0.5, 0.5], p)
    ext.append([k, e, ub, e / (p * math.log2(1 / p))])
res['A096_random_trials'] = ntr
res['A096_max_E_minus_bound'] = worst5
res['A096_worst_case'] = worst5_case
res['A096_extremal_pair'] = ext
json.dump(res, open(sys.argv[1], 'w'), indent=1, default=str)
print(json.dumps(res, indent=0, default=str)[:4000])
