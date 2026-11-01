"""Rigorous (interval arithmetic, mpmath.iv) verification of the Lagrangian certificate for scenario B with
rho in {2,3} (and, as a cross-check, rho in {4,5}), both parities of e.

Statement verified (see NOTES.md Section 5): for the given rational mu,
   mu + M_0(mu) + 2 M_1(mu) + M_2(mu) < 0,
where M_t(mu) = max( max over odd rows of w (ebar_t - mu),  sup_{L in [Lmin,Lmax]} 2^{-L} (Eeven_t(L) - mu) ),
 odd rows (e odd only): r = rho, nu' odd, odd-odd pairs; N = nu'^2 prod n_i, w = N 2^{-rho-2} in [lo, 1-3lo];
   ebar_t = delta L + 2 kappa (1 - log2 nu') - sum G_i - c t, G_i = kappa (s_i - 2) + c m_i - h(m_i) (exact per pair,
   minimised over the pairs with a given n and over factorisations of N),
 even rows: Eeven_t(L) = delta L + max_{j>=1} [2 kappa (1-j) - Gmin((rmin + 2 - L - 2j)_+, 2j)] - c t,
   Gmin(X,E) = GA min(X, SA E) + GB (X - SA E)_+, GA = G(2,1)/SA, SA = log2 5 - 1,
   GB = (kappa (log2 10 - 2) - psi)/(log2 10 - 1), psi = log2(1 + 2^{-c}),
 lo = e_min 2^{-rho-2} (e_min = 1 for e odd, 2 for e even), Lmin = -log2(1-3lo), Lmax = -log2(lo),
 rmin = rho + 1 (e odd) or rho (e even).
The sup over L is bounded by splitting [Lmin, Lmax] into K pieces and evaluating the interval extension."""
import sys
from math import gcd
from mpmath import iv, mpf, mp
iv.dps = 40

def LO(x):
    """lower endpoint of an interval as a plain mpf"""
    return mp.make_mpf(x._mpi_[0])
def HI(x):
    return mp.make_mpf(x._mpi_[1])

LN2 = iv.log(2)
def log2(x):
    return iv.log(x) / LN2
def h(t):
    return -(t * log2(t) + (1 - t) * log2(1 - t))

C = iv.mpf(16) / 3 - iv.mpf(3) / 2 * log2(iv.mpf(3))
KAP = C / 2 - 1
DEL = 2 - C / 2
PSI = log2(1 + iv.mpf(2) ** (-C))
SA = log2(iv.mpf(5)) - 1
def Gpair(p, q):
    S = p * p + q * q
    s = log2(iv.mpf(S)); m = iv.mpf(q * q) / S
    return KAP * (s - 2) + C * m - h(m)
GA = Gpair(2, 1) / SA
L10 = log2(iv.mpf(10))
GB = (KAP * (L10 - 2) - PSI) / (L10 - 1)

def up(x):
    return x.b   # upper endpoint (mpf)

def Gmin(X, E):
    # X, E: intervals / numbers; piecewise linear, increasing in X
    cap = SA * E
    # X could straddle cap; evaluate both branches and take max upper (sound since Gmin is a min-form lower bound:
    # we need an UPPER bound of -Gmin, i.e. a LOWER bound of Gmin): Gmin(X) >= min(GA X, GA cap + GB (X - cap))
    a = GA * X
    b = GA * cap + GB * (X - cap)
    # Gmin(X) = GA X for X <= cap (and then b <= a since GB > GA), = GA cap + GB (X-cap) for X >= cap (then b >= a).
    # So Gmin = max(a, b) pointwise; an enclosure over the interval X is [max(lo a, lo b), max(hi a, hi b)].
    return iv.mpf([max(LO(a), LO(b)), max(HI(a), HI(b))])

def Eeven(Lint, t, rmin):
    best = None
    j = 1
    while True:
        Xraw = rmin + 2 - Lint - 2 * j
        X = iv.mpf([max(mpf(0), LO(Xraw)), max(mpf(0), HI(Xraw))])
        term = 2 * KAP * (1 - j) - Gmin(X, 2 * j)
        best = term if best is None else iv.mpf([max(LO(best), LO(term)), max(HI(best), HI(term))])
        if HI(Xraw) <= 0 or j > 60:
            break
        j += 1
    return DEL * Lint + best - C * t

def odd_pairs(NMAX):
    tab = {}
    p = 3
    while (p * p + 1) // 2 <= NMAX:
        for q in range(1, p, 2):
            if gcd(p, q) == 1:
                n = (p * p + q * q) // 2
                if n <= NMAX:
                    g = Gpair(p, q)
                    if n not in tab or g.a < tab[n].a:
                        tab[n] = g
        p += 2
    return tab

def odd_rows(rho, NMAX):
    tab = odd_pairs(NMAX)
    ns = sorted(tab)
    out = []
    def rec(start, prod, g, u):
        nu = 1
        while prod * nu * nu <= NMAX:
            out.append((prod * nu * nu, nu, g))
            nu += 2
        if u == rho:
            return
        for k in range(start, len(ns)):
            if prod * ns[k] > NMAX:
                break
            rec(k, prod * ns[k], g + tab[ns[k]], u + 1)
    rec(0, 1, iv.mpf(0), 0)
    return out

def certificate(rho, e_odd, mu, K=20000):
    emin = 1 if e_odd else 2
    lo = iv.mpf(emin) / 2 ** (rho + 2)
    hi = 1 - 3 * lo
    Lmin = -log2(hi); Lmax = -log2(lo)
    rmin = rho + 1 if e_odd else rho
    mu = iv.mpf(mu)
    M = {}
    for t in (0, 1, 2):
        best = mpf("-inf")
        # even rows: subdivide [lo Lmin, hi Lmax]
        a0 = LO(Lmin); b0 = HI(Lmax)
        for k in range(K):
            La = a0 + (b0 - a0) * k / K
            Lb = a0 + (b0 - a0) * (k + 1) / K
            if k == K - 1:
                Lb = b0
            Lint = iv.mpf([La, Lb])
            val = iv.mpf(2) ** (-Lint) * (Eeven(Lint, t, rmin) - mu)
            if HI(val) > best:
                best = HI(val)
        # odd rows
        if e_odd:
            NMAX = 2 ** (rho + 2) - 3 * emin   # exact: hi * 2^(rho+2)
            for N, nu, g in odd_rows(rho, NMAX):
                w = iv.mpf(N) / 2 ** (rho + 2)
                if N < emin or N > NMAX:
                    continue
                L = -log2(w)
                eb = DEL * L + 2 * KAP * (1 - log2(iv.mpf(nu))) - g - C * t
                val = w * (eb - mu)
                if HI(val) > best:
                    best = HI(val)
        M[t] = best
    total = iv.mpf(HI(mu)) + iv.mpf(M[0]) + 2 * iv.mpf(M[1]) + iv.mpf(M[2])   # outward rounded
    total_up = HI(total)                                                      # rigorous upper bound
    return total_up, M

if __name__ == "__main__":
    print("c* =", C, " kappa =", KAP, " delta =", DEL)
    print("GA =", GA, " GB =", GB, " SA =", SA, " psi =", PSI)
    cases = [(2, True, "-1.7668"), (2, False, "-1.7058"), (3, True, "-1.4779"), (3, False, "-1.4921"),
             (4, True, "-1.3517"), (4, False, "-1.2337"), (5, True, "-0.8501"), (5, False, "-1.4284")]
    K = int(sys.argv[1]) if len(sys.argv) > 1 else 4000
    for rho, e_odd, mu in cases:
        tot, M = certificate(rho, e_odd, mu, K)
        print(f"rho={rho} e {'odd ' if e_odd else 'even'} mu={mu}: certified upper bound of mu+M0+2M1+M2 = {float(tot):+.6f}",
              "PASS" if tot < 0 else "FAIL", flush=True)
