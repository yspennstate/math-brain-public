"""High-precision biased FEI+ ratio for small functions (n <= 6), to decide whether float searches that report
values slightly above 2 + 4 log2 e are real. Usage: exact_ratio(F_pm_table, mu) with mpmath numbers."""
import mpmath as mp, numpy as np, math
mp.mp.dps = 50

def biased_coeffs_mp(F, mu):
    n = len(mu); N = 1 << n
    a = [mp.mpf(int(v)) for v in F]
    for i in range(n):
        m_ = mp.mpf(mu[i]); p = (1 + m_) / 2; s = mp.sqrt(1 - m_ ** 2)
        b = list(a)
        for x in range(N):
            if (x >> i) & 1: continue
            v0 = a[x]; v1 = a[x | (1 << i)]            # bit 0: x_i=+1, bit 1: x_i=-1
            b[x] = p * v0 + (1 - p) * v1
            b[x | (1 << i)] = p * v0 * (1 - m_) / s + (1 - p) * v1 * (-1 - m_) / s
        a = b
    return a

def exact_ratio(F, mu):
    n = len(mu); N = 1 << n
    c = biased_coeffs_mp(F, mu); P = [v * v for v in c]
    sig2 = [1 - mp.mpf(m_) ** 2 for m_ in mu]
    Hp = mp.mpf(0); inf = mp.mpf(0); var = mp.mpf(0)
    for x in range(1, N):
        k = bin(x).count('1'); inf += k * P[x]; var += P[x]
        if P[x] > 0:
            ls = mp.fsum([mp.log(sig2[i], 2) for i in range(n) if (x >> i) & 1])
            Hp += P[x] * (ls - mp.log(P[x], 2))
    return Hp / (inf - var)

def ltf_table(w, theta):
    n = len(w); N = 1 << n
    out = []
    for x in range(N):
        s = sum(w[i] * (-1 if (x >> i) & 1 else 1) for i in range(n))
        out.append(1 if s - theta > 0 else -1)
    return out

if __name__ == '__main__':
    BOUND = 2 + 4 / mp.log(2)
    rng = np.random.default_rng(17)
    from bfp_ltf import ratio_tt  # float version for the search
