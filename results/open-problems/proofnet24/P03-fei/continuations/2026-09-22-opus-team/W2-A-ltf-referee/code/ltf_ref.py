"""Independent referee code for the FEI-for-LTF claim (F5 report).

Written from scratch; does not import the authors' scripts.

Conventions
-----------
Index b in [0, 2^n): bit j of b equal to 1 means x_j = -1, bit 0 means x_j = +1.
chi_S(x) = (-1)^{popcount(b & S)}, so the Walsh-Hadamard transform F of the
truth table satisfies fhat(S) = F(S) / 2^n.
sgn(t) = +1 for t > 0 and -1 for t <= 0 (the report's convention).
Logs: H in bits; ln natural.
"""
import math
import numpy as np

SQRT_PI = math.sqrt(math.pi)
B_CONST = 3.0 * math.sqrt(3.0 / math.pi)
L1_CONST = 2.0 * math.log(B_CONST) + 2.0


def be_polite():
    """BelowNormal priority and the four permitted cores."""
    try:
        import psutil
        p = psutil.Process()
        p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
        p.cpu_affinity([2, 3, 14, 15])
    except Exception as e:  # pragma: no cover
        print("[polite] could not set priority/affinity:", e)


def fwht(a):
    """Unnormalised Walsh-Hadamard transform (returns a new float64 array)."""
    a = np.asarray(a, dtype=np.float64).copy()
    N = a.size
    h = 1
    while h < N:
        a = a.reshape(-1, 2, h)
        s = a[:, 0, :] + a[:, 1, :]
        d = a[:, 0, :] - a[:, 1, :]
        a = np.stack([s, d], axis=1).reshape(N)
        h *= 2
    return a


def linear_values(w):
    """Array of w.x over all x, in the index convention above (exact for ints)."""
    w = list(w)
    if all(isinstance(t, (int, np.integer)) for t in w):
        val = np.zeros(1, dtype=np.int64)
        for wj in w:
            val = np.concatenate([val + int(wj), val - int(wj)])
    else:
        val = np.zeros(1, dtype=np.float64)
        for wj in w:
            val = np.concatenate([val + float(wj), val - float(wj)])
    return val


def ltf_table(w, theta):
    """Truth table of sgn(w.x - theta) with sgn(0) = -1, as int8 array of +-1."""
    v = linear_values(w)
    return np.where(v - theta > 0, 1, -1).astype(np.int8)


def spectrum(tab):
    """Returns p(S) = fhat(S)^2 as float64 array (sums to 1)."""
    n = int(round(math.log2(tab.size)))
    F = fwht(tab.astype(np.float64))
    return (F / float(1 << n)) ** 2


def popcount(arr):
    return np.bitwise_count(arr).astype(np.int64)


class Spec:
    """Spectral quantities of a Boolean function given its truth table."""

    def __init__(self, tab):
        self.tab = tab
        self.n = int(round(math.log2(tab.size)))
        self.p = spectrum(tab)
        self.idx = np.arange(tab.size, dtype=np.int64)
        self.lev = popcount(self.idx)
        self._inf = None

    @property
    def H(self):
        p = self.p[self.p > 0]
        return float(-(p * np.log2(p)).sum())

    @property
    def I(self):
        return float((self.p * self.lev).sum())

    def level_weights(self):
        return np.bincount(self.lev, weights=self.p, minlength=self.n + 1)

    def H_level(self):
        W = self.level_weights()
        W = W[W > 0]
        return float(-(W * np.log2(W)).sum())

    def influences(self):
        if self._inf is None:
            self._inf = np.array([self.p[(self.idx >> i) & 1 == 1].sum()
                                  for i in range(self.n)])
        return self._inf

    def hist_in(self, i, mask):
        """hist[k] = sum over S containing i with |S & mask| = k of p(S)."""
        sel = ((self.idx >> i) & 1) == 1
        k = popcount(self.idx[sel] & mask)
        return np.bincount(k, weights=self.p[sel], minlength=bin(mask).count("1") + 1)

    def hist_level_in(self, i):
        """hl[l] = sum over S containing i with |S| = l of p(S)."""
        sel = ((self.idx >> i) & 1) == 1
        return np.bincount(self.lev[sel], weights=self.p[sel], minlength=self.n + 1)


def ranks_and_U(absw, tie_order=None):
    """Rank r(i) (1-based) by decreasing |w|, ties broken by tie_order (a
    permutation used as secondary key) or by index; U_i masks and N_i.
    U_i = {j != i : |w_j| >= |w_i|}."""
    n = len(absw)
    if tie_order is None:
        tie_order = list(range(n))
    order = sorted(range(n), key=lambda j: (-absw[j], tie_order[j]))
    r = [0] * n
    for pos, j in enumerate(order):
        r[j] = pos + 1
    U = []
    N = []
    for i in range(n):
        m = 0
        cnt = 0
        for j in range(n):
            if j != i and absw[j] >= absw[i]:
                m |= (1 << j)
                cnt += 1
        U.append(m)
        N.append(cnt + 1)
    return r, U, N


def binom_pmf(M, p):
    """pmf of Binomial(M, p) as array of length M+1 (stable via logs)."""
    if p <= 0:
        out = np.zeros(M + 1); out[0] = 1.0; return out
    if p >= 1:
        out = np.zeros(M + 1); out[M] = 1.0; return out
    k = np.arange(M + 1)
    lg = (np.array([math.lgamma(M + 1) - math.lgamma(t + 1) - math.lgamma(M - t + 1) for t in k])
          + k * math.log(p) + (M - k) * math.log1p(-p))
    return np.exp(lg)


def lo_exact(m):
    """C(m, floor(m/2)) / 2^m (the Erdos-Littlewood-Offord bound)."""
    return math.comb(m, m // 2) / float(2 ** m)


def lemma_checks(spec, absw, tie_order=None, cgrid=None):
    """Checks Lemmas 2 (average form), 3 (and its tail), 4, 5, 6 and Thm 1.
    Returns dict of worst ratios (value / bound) and detail."""
    n = spec.n
    r, U, N = ranks_and_U(absw, tie_order)
    inf = spec.influences()
    out = {"L2avg": 0.0, "L2avg_arg": None, "L3": 0.0, "L3_arg": None,
           "L3tail": 0.0, "L3tail_arg": None, "L3tail_mid": 0.0}
    Sigma = 0.0
    for i in range(n):
        if inf[i] <= 1e-15:
            continue
        hl = spec.hist_level_in(i)
        ls = np.arange(n + 1)
        with np.errstate(divide="ignore"):
            lnp = np.where(ls > 0, np.maximum(np.log(np.maximum(r[i], 1) / np.maximum(ls, 1)), 0.0), 0.0)
        Sigma += float((hl * lnp).sum())
        if N[i] == 1:
            continue
        hist = spec.hist_in(i, U[i])[:N[i]]
        Inf = hist.sum()
        k = np.arange(N[i])
        # Lemma 3
        A = float((hist * np.log(N[i] / (k + 1.0))).sum())
        rat = A / (L1_CONST * Inf)
        if rat > out["L3"]:
            out["L3"], out["L3_arg"] = rat, (i, N[i], A / Inf)
        # Lemma 2 average form, over c in (0, N]
        cs = cgrid if cgrid is not None else np.concatenate([
            np.linspace(0.05, 1.0, 20) * N[i], [N[i]]])
        for c in cs:
            if c <= 0 or c > N[i]:
                continue
            rho = 1.0 - c / N[i]
            stab = float((hist * rho ** k).sum()) if rho > 0 else float(hist[0])
            bound = (2.0 / SQRT_PI) * c ** -0.5 * Inf
            if stab / bound > out["L2avg"]:
                out["L2avg"], out["L2avg_arg"] = stab / bound, (i, N[i], c)
        # Lemma 3 tail: nu(k <= K) <= B sqrt(K/N), integer K in [1, N]
        cum = np.cumsum(hist) / Inf
        for K in range(1, N[i] + 1):
            val = cum[min(K, N[i] - 1)]
            b1 = B_CONST * math.sqrt(K / N[i])
            b_mid = (1 - 1 / (3 * K)) ** (-K) * (2 / SQRT_PI) * math.sqrt(3 * K / N[i])
            if val / b1 > out["L3tail"]:
                out["L3tail"], out["L3tail_arg"] = val / b1, (i, N[i], K)
            out["L3tail_mid"] = max(out["L3tail_mid"], val / b_mid)
    I = spec.I
    H = spec.H
    Hl = spec.H_level()
    a = (1 + math.sqrt(1 + 4 / L1_CONST)) / 2
    if I > 1e-15:
        out["L4"] = Sigma / (L1_CONST * I)
        out["L5"] = Hl / (3 * I)
        bound6 = (math.log(math.e * a / (a - 1)) * I + a * Sigma) / math.log(2)
        out["L6"] = (H - Hl) / bound6 if bound6 > 0 else (0.0 if H - Hl < 1e-12 else float("inf"))
        out["HI"] = H / I
        out["T1"] = H / (C_THM1() * I)
    else:
        out.update({"L4": 0, "L5": 0, "L6": 0, "HI": 0, "T1": 0})
    out["H"], out["I"], out["Sigma"] = H, I, Sigma
    return out


def C_THM1(k=1):
    L = L1_CONST + 2 * math.log(k)
    a = (1 + math.sqrt(1 + 4 / L)) / 2
    return 3 + (1 + math.log(a / (a - 1)) + a * L) / math.log(2)


def deriv_nonzero(tab, i):
    """1[D_i f(x) != 0] as float array over all x (independent of x_i)."""
    n = int(round(math.log2(tab.size)))
    t = tab.reshape(-1, 2, 1 << i)
    d = (t[:, 0, :] != t[:, 1, :])
    h = np.stack([d, d], axis=1).reshape(tab.size)
    return h.astype(np.float64)


def lemma2_pointwise(tab, absw, i, U_mask, N, cs, k_multi=1):
    """max over x of Pr[D_i f(y) != 0 | x] against three bounds, for each c.
    Bounds: (a) the lemma's (2/sqrt pi) c^{-1/2} * k_multi,
            (b) E_m min(1, k_multi * sqrt(2/(pi m))),
            (c) E_m min(1, k_multi * C(m, m//2)/2^m)  (tightest: exact LO).
    Returns list of (c, maxP, ratio_a, ratio_b, ratio_c)."""
    n = int(round(math.log2(tab.size)))
    h = deriv_nonzero(tab, i)
    if h.sum() == 0:
        return []
    hh = fwht(h) / float(tab.size)
    idx = np.arange(tab.size, dtype=np.int64)
    kU = popcount(idx & U_mask)
    res = []
    for c in cs:
        rho = 1.0 - c / N
        mult = rho ** kU if rho > 0 else (kU == 0).astype(np.float64)
        P = fwht(hh * mult)  # inverse transform (unnormalised forward = inverse * 2^n / 2^n)
        maxP = float(P.max())
        pm = binom_pmf(N - 1, c / N)
        ms = np.arange(N)
        bb = np.array([min(1.0, k_multi * math.sqrt(2 / (math.pi * m))) if m > 0 else 1.0 for m in ms])
        bc = np.array([min(1.0, k_multi * lo_exact(m)) for m in ms])
        ba = k_multi * (2 / SQRT_PI) * c ** -0.5
        res.append((c, maxP, maxP / ba, maxP / float((pm * bb).sum()), maxP / float((pm * bc).sum())))
    return res
