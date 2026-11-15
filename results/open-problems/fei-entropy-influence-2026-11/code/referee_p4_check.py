"""Independent numerical check of P4 (fei-equivalent-forms) Theorem 1 (a)-(d), Prop 2, Remark (centring),
and the step the remark leaves out: Inf_i - fhat(i)^2 >= Inf_i (1 - Inf_i), so I - W1 >= sum_i min(Inf_i, 1-Inf_i)/2.
Written by an agent without reading the paper's code."""
import numpy as np
from numpy.polynomial.legendre import leggauss

L2 = np.log(2)


def wht(f):
    a = f.astype(float).copy(); h = 1
    while h < len(a):
        a = a.reshape(-1, 2 * h); x = a[:, :h].copy(); y = a[:, h:].copy()
        a[:, :h] = x + y; a[:, h:] = x - y; a = a.reshape(-1); h *= 2
    return a / len(a)


def check(f, n):
    N = 1 << n; c = wht(f); mu = c * c
    pc = np.array([bin(S).count("1") for S in range(N)])
    supp = mu > 1e-30
    H = -(mu[supp] * np.log2(mu[supp])).sum(); I = (pc * mu).sum(); Var = 1 - mu[0]
    sup = np.zeros((N, N), bool)  # sup[T, U] = U contains T
    for T in range(N):
        sup[T] = (np.arange(N) & T) == T
    K = pc[None, :] - pc[:, None]  # |U \ T| where U contains T

    def gam(t):
        return (sup * mu[None, :] * np.where(sup, t ** np.clip(K, 0, None), 0)).sum(1)

    def m(t):
        g = gam(t); num = (sup * mu[None, :] * K * np.where(sup, t ** np.clip(K, 0, None), 0)).sum(1)
        return num / g
    g1 = gam(1.0)
    A = (mu[supp] * np.log2(1 / g1[supp])).sum(); B = (mu[supp] * np.log2(g1[supp] / mu[supp])).sum()
    out = {"H-A-B": abs(H - A - B)}
    # lemma: mu(T) <= 4^{|T|-1} gamma(T)^2
    nz = supp & (pc > 0)
    out["lemma_max_ratio"] = (mu[nz] / (4.0 ** (pc[nz] - 1) * g1[nz] ** 2)).max()
    out["a_slack"] = 2 * B + 2 * I - 2 * Var - H
    bs = []
    for t in (0.25, 0.5, 0.75, 0.9):
        At = (mu[supp] * np.log2(1 / gam(t)[supp])).sum()
        bs.append(min(H - At, At + I * np.log2(1 / (1 - t)) - H))
    out["b_slack"] = min(bs)
    x, w = leggauss(80)
    s0 = (x + 1) / 2; w0 = w / 2  # [0,1]
    Ms = np.array([(mu[supp] * m(s)[supp]).sum() for s in s0])
    out["B_integral_err"] = abs((w0 * Ms / s0).sum() / L2 - B)
    s1 = 0.75 + x / 4; w1 = w / 4  # [1/2,1]
    Ms1 = np.array([(mu[supp] * m(s)[supp]).sum() for s in s1])
    M1 = (mu[supp] * m(1.0)[supp]).sum()
    mid = 4 * I - 2 * Var + 2 / L2 * (w1 * Ms1 / s1).sum()
    out["c_slack1"] = mid - H; out["c_slack2"] = 4 * I - 2 * Var + 2 * M1 - mid
    out["m_monotone_min_step"] = min(np.diff(Ms)) if len(Ms) > 1 else 0
    # (d)
    E = 0.0; IL = 0.0
    for i in range(n):
        for T in range(N):
            if T >> i & 1:
                continue
            p, q = mu[T], mu[T | 1 << i]
            if p + q < 1e-30:
                continue
            if p > 0: E += p * np.log2((p + q) / p)
            if q > 0: E += q * np.log2((p + q) / q); IL += q * np.log2((p + q) / q)
    out["d_lo"] = E - IL; out["d_hi"] = IL + I / L2 - E
    # constant predictor: L <= log2(n/I)
    out["const_pred_slack"] = np.log2(n / I) - IL / I
    # centring step
    inf = np.array([mu[(np.arange(N) >> i & 1) == 1].sum() for i in range(n)])
    w1v = np.array([mu[1 << i] for i in range(n)])
    out["inf_minus_w_minus_inf(1-inf)"] = (inf - w1v - inf * (1 - inf)).min()
    out["H/I"] = H / I
    return out


rng = np.random.default_rng(51)
worst = {}
fs = []
for n in range(3, 8):
    for bias in (0.5, 0.15, 0.03):
        for _ in range(4):
            fs.append((n, np.where(rng.random(1 << n) < bias, -1, 1)))
n = 7; maj = np.array([1 if bin(x).count("1") <= 3 else -1 for x in range(1 << n)]); fs.append((n, maj))
for n, f in fs:
    if abs(f.mean()) == 1:
        continue
    o = check(f, n)
    for k, v in o.items():
        worst.setdefault(k, []).append(v)
for k, v in worst.items():
    print(f"{k:32s} min {min(v): .3e}  max {max(v): .3e}")
o = check(maj, 7); print("Maj7 H/I", round(o["H/I"], 4), "sumE-IL", o["d_lo"])
