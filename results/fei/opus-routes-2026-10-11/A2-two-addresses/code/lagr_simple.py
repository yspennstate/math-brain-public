"""Simplified Lagrangian bound for scenario B (E_* nonempty), parameter rho, e odd or even, at c = c*.

Row values w (e_t - mu), e_t = (c-2)(1 - log2 nu') + delta L - sum G - c t, L = log2(1/w).
 odd rows (only when e odd): r = rho, nu' odd, all pairs odd; w = 2^{-rho-2} nu'^2 prod n_i, n_i = (p^2+q^2)/2,
   G summed exactly with alpha = m (its minimum), minimised over the pairs (p,q) giving each n.
 even rows: dropped data: value <= w (delta log2(1/w) - c t - mu) for any w in the admissible weight range.
Weight range for every row: [lo, 1 - 3 lo], lo = e 2^{-rho-2} (e >= 1 odd case, e >= 2 even case).
Prints min_mu B(mu) = mu + M_0 + 2 M_1 + M_2 for each rho."""
import math, sys
from math import gcd
C = 16 / 3 - 1.5 * math.log2(3)
DEL = 2 - C / 2

def h(t):
    return 0.0 if t <= 0 or t >= 1 else -t * math.log2(t) - (1 - t) * math.log2(1 - t)

def Gmin_table(NMAX):
    """minimal G over odd coprime pairs (p>q>=1) with (p^2+q^2)/2 = n, for n <= NMAX"""
    tab = {}
    p = 3
    while (p * p + 1) // 2 <= NMAX:
        for q in range(1, p, 2):
            if gcd(p, q) != 1:
                continue
            n = (p * p + q * q) // 2
            if n > NMAX:
                continue
            s = math.log2(2 * n); m = q * q / (2 * n)
            G = (C / 2 - 1) * (s - 2) + C * m - h(m)
            tab[n] = min(tab.get(n, 1e9), G)
        p += 2
    return tab

def odd_rows(rho, NMAX, Gt):
    """list of (w, base) with base = (c-2)(1-log2 nu') - sum G for odd rows of radius rho, N <= NMAX"""
    ns = sorted(Gt)
    out = []
    # products of up to rho unfair n's (with multiplicity), times odd nu'^2
    def rec(start, prod, g, u):
        for nu in range(1, 10 ** 6, 2):
            N = prod * nu * nu
            if N > NMAX:
                break
            out.append((N, (C - 2) * (1 - math.log2(nu)) - g))
        if u == rho:
            return
        for k in range(start, len(ns)):
            n = ns[k]
            if prod * n > NMAX:
                break
            rec(k, prod * n, g + Gt[n], u + 1)
    rec(0, 1, 0.0, 0)
    return out

def bound(rho, e_odd):
    lo = (1 if e_odd else 2) * 2.0 ** (-rho - 2)
    hi = 1 - 3 * lo
    NMAX = int(math.floor(hi * 2 ** (rho + 2) + 1e-9))
    Gt = Gmin_table(NMAX) if e_odd else {}
    od = []
    if e_odd:
        for N, base in odd_rows(rho, NMAX, Gt):
            w = N * 2.0 ** (-rho - 2)
            if lo - 1e-15 <= w <= hi + 1e-15:
                od.append((w, base))
    def even_sup(t, mu):
        # sup over w in [lo,hi] of w (DEL log2(1/w) - C t - mu): concave in w
        f = lambda w: w * (DEL * math.log2(1 / w) - C * t - mu)
        wstar = 2.0 ** (-(C * t + mu) / DEL - 1 / math.log(2))
        cands = [lo, hi] + ([wstar] if lo < wstar < hi else [])
        return max(f(w) for w in cands)
    def M(t, mu):
        best = even_sup(t, mu) if hi >= lo else -1e18
        for w, base in od:
            v = w * (base + DEL * math.log2(1 / w) - C * t - mu)
            if v > best:
                best = v
        return best
    def B(mu):
        return mu + M(0, mu) + 2 * M(1, mu) + M(2, mu)
    a, b = -20.0, 20.0
    for _ in range(300):
        m1 = a + (b - a) / 3; m2 = b - (b - a) / 3
        if B(m1) <= B(m2): b = m2
        else: a = m1
    mu = (a + b) / 2
    return mu, B(mu), len(od)

if __name__ == "__main__":
    RHO = int(sys.argv[1]) if len(sys.argv) > 1 else 24
    for rho in range(1, RHO + 1):
        for e_odd in (True, False):
            mu, val, nod = bound(rho, e_odd)
            print(f"rho={rho:2d} e {'odd ' if e_odd else 'even'}  odd-row options {nod:6d}  best mu {mu:+.4f}  B = {val:+.6f}", flush=True)
