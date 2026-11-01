"""Envelope Lagrangian for scenario B (E_* nonempty), rho >= 2, at c = c*.

Per-row upper bound ebar_t <= E_t(L) depending only on the row's L = log2(1/w):
 odd rows (e odd; r = rho; nu' odd; odd-odd pairs; ebar = delta L + 2 kappa (1 - log2 nu') - sum G - c t,
   sum(s_i - 1) = rho + 2 - L - 2 log2 nu'):  exact for the finitely many odd rows (N = nu'^2 prod n_i).
 even rows (nu' even, 2 v2(nu') >= e_c, r >= rmin; rmin = rho+1 (e odd) or rho (e even)):
   ebar <= delta L + max_{j>=1} [2 kappa (1 - j) - Gmin((rmin + 2 - L - 2j)_+, 2j)] - c t,
   Gmin(X, E) = gA min(X, 1.3219 E) + gB (X - 1.3219 E)_+,  gA = 0.017484 ((2,1) rate), gB = 0.19678 (all others)
   (nu' = 2^j * odd: an odd factor only increases log2 nu'; it costs 2 kappa per unit and saves at most
    2 gB < 2 kappa per unit, so nu' = 2^j is the worst case.)
Weights: every row w in [lo, 1 - 3 lo], lo = e 2^{-rho-2} (e >= 1 odd case, e >= 2 even case).
Phi <= mu + M_0(mu) + 2 M_1(mu) + M_2(mu),  M_t(mu) = sup_rows w (ebar_t - mu)."""
import math, sys
from math import gcd
C = 16 / 3 - 1.5 * math.log2(3)
KAP = C / 2 - 1
DEL = 2 - C / 2
GA = 0.017484822147904956
GB = 0.1967827332258318
SA = math.log2(5) - 1   # s - 1 for (2,1)

def h(t):
    return 0.0 if t <= 0 or t >= 1 else -t * math.log2(t) - (1 - t) * math.log2(1 - t)

def Gmin(X, E):
    if X <= 0:
        return 0.0
    a = min(X, SA * E)
    return GA * a + GB * (X - a)

def even_env(L, t, rmin):
    best = -1e18
    for j in range(1, 64):
        X = max(0.0, rmin + 2 - L - 2 * j)
        v = 2 * KAP * (1 - j) - Gmin(X, 2 * j)
        best = max(best, v)
        if X == 0:
            break
    return DEL * L + best - C * t

def odd_rows(rho, NMAX):
    # odd coprime pairs with n = (p^2+q^2)/2 <= NMAX, exact G at alpha = m
    Gt = {}
    p = 3
    while (p * p + 1) // 2 <= NMAX:
        for q in range(1, p, 2):
            if gcd(p, q) == 1:
                n = (p * p + q * q) // 2
                if n <= NMAX:
                    s = math.log2(2 * n); m = q * q / (2 * n)
                    Gt[n] = min(Gt.get(n, 1e9), KAP * (s - 2) + C * m - h(m))
        p += 2
    ns = sorted(Gt)
    out = []
    def rec(start, prod, g, u):
        nu = 1
        while prod * nu * nu <= NMAX:
            out.append((prod * nu * nu, 2 * KAP * (1 - math.log2(nu)) - g))
            nu += 2
        if u == rho:
            return
        for k in range(start, len(ns)):
            if prod * ns[k] > NMAX:
                break
            rec(k, prod * ns[k], g + Gt[ns[k]], u + 1)
    rec(0, 1, 0.0, 0)
    return out

def bound(rho, e_odd, grid=4000):
    lo = (1 if e_odd else 2) * 2.0 ** (-rho - 2)
    hi = 1 - 3 * lo
    Lmin, Lmax = -math.log2(hi), -math.log2(lo)
    rmin = rho + 1 if e_odd else rho
    od = []
    if e_odd:
        NMAX = int(math.floor(hi * 2 ** (rho + 2) + 1e-9))
        for N, base in odd_rows(rho, NMAX):
            w = N * 2.0 ** (-rho - 2)
            if lo - 1e-15 <= w <= hi + 1e-15:
                od.append((w, -math.log2(w), base))
    Ls = [Lmin + (Lmax - Lmin) * k / grid for k in range(grid + 1)]
    env = {t: [(2.0 ** (-L), even_env(L, t, rmin)) for L in Ls] for t in (0, 1, 2)}
    def M(t, mu):
        best = max(w * (e - mu) for w, e in env[t])
        for w, L, base in od:
            best = max(best, w * (DEL * L + base - C * t - mu))
        return best
    def B(mu):
        return mu + M(0, mu) + 2 * M(1, mu) + M(2, mu)
    a, b = -15.0, 15.0
    for _ in range(120):
        m1 = a + (b - a) / 3; m2 = b - (b - a) / 3
        if B(m1) <= B(m2): b = m2
        else: a = m1
    mu = (a + b) / 2
    return mu, B(mu), len(od)

if __name__ == "__main__":
    R = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    for rho in range(2, R + 1):
        for e_odd in (True, False):
            mu, val, nod = bound(rho, e_odd)
            print(f"rho={rho:2d} e {'odd ' if e_odd else 'even'} odd-rows {nod:5d}  mu {mu:+.4f}  B = {val:+.5f}", flush=True)
