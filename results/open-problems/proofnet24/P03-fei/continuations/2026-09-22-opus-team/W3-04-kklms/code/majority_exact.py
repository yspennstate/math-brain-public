"""Exact Fourier data of Maj_n (n = 2m+1) and the shape test of KKLMS Corollary 6.7.

|Maj^(S)| = M_k = 4^-m C(2m,m) C(m,j)/C(2m,2j) for |S| = k = 2j+1 (F4 Prop 6.1, checked below
against the Walsh transform), W_k = C(n,k) M_k^2, I = n 4^-m C(2m,m).

Shape test.  Corollary 6.7 of KKLMS (0/1 convention, f = (1-F)/2) has the form
   <f,g> <= A ||f||^{3/4} ||g||^{3/4} max_{|S|~d} |fhat(S) ghat(S)|^{1/4} + B I[f,g] + C ||f|| ||g||.
For f = (1-Maj_n)/2 and g = f restricted to a band of levels, every quantity is explicit:
   <f,g> = ||g||^2 = W_band/4, ||f||^2 = 1/2, I[f,g] = sqrt(I(Maj) * I_band)/4,
   max |fhat ghat|^{1/4} = (M_{kmin}/2)^{1/2}.
Hence the inequality forces  A >= (W_band/4 - B I[f,g] - C ||f|| ||g||) / (2^{-3/8} (W_band/4)^{3/8} (M_kmin/2)^{1/2}).
"""
import sys
import mpmath as mp
from fei_core import limit_process, majority, spectrum

mp.mp.dps = 60


def lnC(a, b):
    return mp.loggamma(a + 1) - mp.loggamma(b + 1) - mp.loggamma(a - b + 1)


def lnM(n, k):
    m = (n - 1) // 2
    j = (k - 1) // 2
    return -2 * m * mp.log(2) + lnC(2 * m, m) + lnC(m, j) - lnC(2 * m, 2 * j)


def W(n, k):
    return mp.e ** (lnC(n, k) + 2 * lnM(n, k))


def I_maj(n):
    m = (n - 1) // 2
    return n * mp.e ** (-2 * m * mp.log(2) + lnC(2 * m, m))


def check_against_walsh():
    import numpy as np
    for n in (5, 9, 13, 17):
        nn, p, sz = spectrum(majority(n))
        for k in range(1, n + 1, 2):
            val = float(p[sz == k].max())
            ex = float(mp.e ** (2 * lnM(n, k)))
            wk = float(p[sz == k].sum())
            assert abs(val - ex) < 1e-12 and abs(wk - float(W(n, k))) < 1e-12, (n, k)
    print("majority closed form matches Walsh transform for n = 5, 9, 13, 17 (all odd levels)")


def forced_A(n, kmin, kmax, B, C):
    """lower bound on A forced by f = Maj_n, g = band [kmin,kmax] (odd levels)."""
    ks = [k for k in range(kmin, kmax + 1) if k % 2 == 1]
    Wb = mp.fsum(W(n, k) for k in ks)
    Ib = mp.fsum(k * W(n, k) for k in ks)
    If = I_maj(n)
    lhs = Wb / 4
    Bterm = B * mp.sqrt(If * Ib) / 4
    Cterm = C * mp.sqrt(mp.mpf(1) / 2) * mp.sqrt(Wb) / 2
    num = lhs - Bterm - Cterm
    Mk = mp.e ** lnM(n, ks[0])
    den = mp.mpf(2) ** (-mp.mpf(3) / 8) * (Wb / 4) ** (mp.mpf(3) / 8) * mp.sqrt(Mk / 2)
    return num, (num / den if num > 0 else None), Wb, Bterm, Cterm


if __name__ == "__main__":
    limit_process()
    check_against_walsh()
    print()
    print("Single level k (g = level-k part), n = k^C, B = k^-beta, C3 = 1/(8k).")
    print("log2(A_forced) / (k log2 k); 'vac' = the B- and C-terms already exceed <f,g>")
    for beta in (1.25, 1.5, 2.0, 3.0, 6000.0):
        row = []
        for k in (9, 33, 129, 513, 2049):
            best = None
            for C in (1.25, 1.5, 2.0, 3.0, 4.0, 6.0, 8.0):
                n = int(mp.floor(mp.mpf(k) ** C))
                if n % 2 == 0:
                    n += 1
                if n <= k:
                    continue
                num, A, Wb, Bt, Ct = forced_A(n, k, k, mp.mpf(k) ** (-beta), mp.mpf(1) / (8 * k))
                if A is not None:
                    v = float(mp.log(A, 2) / (k * mp.log(k, 2)))
                    if best is None or v > best[0]:
                        best = (v, C)
            row.append("vac" if best is None else f"{best[0]:.3f}(C={best[1]})")
        print(f"beta={beta:7.2f}: " + "  ".join(row))
    print()
    print("Band [d/2, d] (alpha = 1/2), n = d^C, B = d^-beta, C3 = 1/(8d).")
    for beta in (1.1, 1.25, 1.5, 2.0):
        row = []
        for d in (17, 65, 257, 1025):
            best = None
            for C in (1.1, 1.25, 1.5, 2.0, 3.0, 4.0, 6.0):
                n = int(mp.floor(mp.mpf(d) ** C))
                if n % 2 == 0:
                    n += 1
                if n <= d:
                    continue
                kmin = d // 2 + (1 - (d // 2) % 2)
                num, A, Wb, Bt, Ct = forced_A(n, kmin, d, mp.mpf(d) ** (-beta), mp.mpf(1) / (8 * d))
                if A is not None:
                    v = float(mp.log(A, 2) / (d * mp.log(d, 2)))
                    if best is None or v > best[0]:
                        best = (v, C)
            row.append("vac" if best is None else f"{best[0]:.3f}(C={best[1]})")
        print(f"beta={beta:5.2f}: " + "  ".join(row))
    sys.stdout.flush()
