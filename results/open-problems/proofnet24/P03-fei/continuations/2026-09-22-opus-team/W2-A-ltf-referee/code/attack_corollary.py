"""Corollary 2: f = F(f_1..f_k), f_l = sgn(w^(l).x - theta_l), co-monotone |w^(l)|.

Checks, with U_i = {j != i : |w^(l)_j| >= |w^(l)_i| for all l}:
  (i)   Lemma 3 analogue: sum_{S ni i} fhat^2 ln(N_i/(|S & U_i|+1)) <= (L1 + 2 ln k) Inf_i
  (ii)  tail: nu(k <= K) <= k B sqrt(K/N)
  (iii) Lemma 4 analogue: Sigma <= (L1 + 2 ln k) I
  (iv)  Theorem: H <= C_k I
  (v)   pointwise Lemma 2 analogue: max_x Pr[D_i f(y) != 0 | x] <= E min(1, k LO(m))  and <= k (2/sqrt pi) c^-1/2
usage: python attack_corollary.py n k trials seed [pointwise]
"""
import math, sys, time, itertools
import numpy as np
import ltf_ref as L

L.be_polite()
n, k, trials, seed = map(int, sys.argv[1:5])
do_pw = len(sys.argv) > 5 and sys.argv[5] == "pw"
rng = np.random.default_rng(seed)
Lk = L.L1_CONST + 2 * math.log(k)
Ck = L.C_THM1(k)
print(f"n={n} k={k} L1+2lnk={Lk:.6f} C_k={Ck:.6f}")


def gen_weights():
    """co-monotone weight vectors; integer valued so ties are exact."""
    style = rng.integers(4)
    if style == 0:      # common base values with ties, monotone integer transforms
        v = np.sort(rng.integers(1, 6, size=n))[::-1]
    elif style == 1:    # geometric-ish integers
        v = np.array([int(round(1.6 ** (n - j))) for j in range(n)])
    elif style == 2:    # all equal (symmetric)
        v = np.ones(n, dtype=int)
    else:
        v = np.sort(rng.integers(1, 3 * n, size=n))[::-1]
    Ws = []
    for l in range(k):
        a = int(rng.integers(1, 4)); b = int(rng.integers(0, 3))
        mode = rng.integers(3)
        if mode == 0:
            h = a * v + b
        elif mode == 1:
            h = v ** 2 if a == 1 else a * v
        else:  # flatten the tail: creates extra ties for this l only
            cut = int(rng.integers(1, n + 1))
            h = np.maximum(v, v[min(cut, n - 1)])
        signs = rng.choice([-1, 1], size=n) if rng.random() < 0.7 else np.ones(n, dtype=int)
        Ws.append([int(s * t) for s, t in zip(signs, h)])
    order = sorted(range(n), key=lambda j: (-v[j], j))
    return Ws, order


def build(Ws, thetas, Ftab):
    tabs = [L.ltf_table(w, t) for w, t in zip(Ws, thetas)]
    idx = np.zeros(1 << n, dtype=np.int64)
    for l, tb in enumerate(tabs):
        idx |= ((tb > 0).astype(np.int64) << l)
    return np.asarray(Ftab, dtype=np.int8)[idx]


worst = {}
def upd(key, val, info):
    if key not in worst or val > worst[key][0]:
        worst[key] = (val, info)

t0 = time.time()
Fs = list(itertools.product([-1, 1], repeat=1 << k))
for tr in range(trials):
    Ws, order = gen_weights()
    thetas = []
    for w in Ws:
        v = np.sort(L.linear_values(w))
        thetas.append(int(v[int(rng.integers(len(v)))]) - int(rng.integers(0, 2)))
    r = [0] * n
    for pos, j in enumerate(order):
        r[j] = pos + 1
    U, N = [], []
    for i in range(n):
        m = 0; cnt = 0
        for j in range(n):
            if j != i and all(abs(w[j]) >= abs(w[i]) for w in Ws):
                m |= 1 << j; cnt += 1
        U.append(m); N.append(cnt + 1)
    assert all(N[i] >= r[i] for i in range(n)), "co-monotone order violated"
    Fsel = Fs if k <= 2 else [Fs[int(q)] for q in rng.integers(len(Fs), size=24)]
    for Ft in Fsel:
        tab = build(Ws, thetas, Ft)
        sp = L.Spec(tab)
        if sp.I < 1e-12:
            continue
        inf = sp.influences()
        Sigma = 0.0
        for i in range(n):
            if inf[i] < 1e-15:
                continue
            hl = sp.hist_level_in(i)
            ls = np.arange(n + 1)
            lnp = np.where(ls > 0, np.maximum(np.log(r[i] / np.maximum(ls, 1)), 0.0), 0.0)
            Sigma += float((hl * lnp).sum())
            if N[i] == 1:
                continue
            hist = sp.hist_in(i, U[i])[:N[i]]
            Inf = hist.sum()
            kk = np.arange(N[i])
            A = float((hist * np.log(N[i] / (kk + 1.0))).sum())
            upd("L3cor", A / (Lk * Inf), (tr, i, N[i]))
            cum = np.cumsum(hist) / Inf
            for K in range(1, N[i]):
                upd("tailcor", cum[K] / (k * L.B_CONST * math.sqrt(K / N[i])), (tr, i, N[i], K))
            if do_pw:
                h = L.deriv_nonzero(tab, i)
                hh = L.fwht(h) / float(1 << n)
                kU = L.popcount(np.arange(1 << n, dtype=np.int64) & U[i])
                for c in sorted(set([x for x in [0.5, 1, 2, 4, N[i] / 2, N[i]] if 0 < x <= N[i]])):
                    rho = 1 - c / N[i]
                    mult = rho ** kU if rho > 0 else (kU == 0).astype(float)
                    P = L.fwht(hh * mult)
                    maxP = float(P.max())
                    pm = L.binom_pmf(N[i] - 1, c / N[i])
                    bc = sum(pm[m] * min(1.0, k * L.lo_exact(m)) for m in range(N[i]))
                    upd("pw_exactLO", maxP / bc, (tr, i, N[i], c))
                    upd("pw_lemma", maxP / (k * (2 / L.SQRT_PI) * c ** -0.5), (tr, i, N[i], c))
        upd("L4cor", Sigma / (Lk * sp.I), (tr,))
        upd("Thm_cor", sp.H / (Ck * sp.I), (tr, round(sp.H / sp.I, 4)))
        upd("HI", sp.H / sp.I, (tr, Ws, thetas, Ft))
print(f"time {time.time() - t0:.0f}s")
for key, (v, info) in worst.items():
    print(f"  worst {key:12s} = {v:.6f}  {str(info)[:160]}")
