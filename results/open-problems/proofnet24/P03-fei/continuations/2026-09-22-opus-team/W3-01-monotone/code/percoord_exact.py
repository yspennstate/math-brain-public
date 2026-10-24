"""Exact version of percoord.py for large m, through Krawtchouk polynomials.

f = z AND T(x), T(x) = [|x| >= t] on m bits.  With characters chi_i = (-1)^{x_i}:
  That_0 = mu = Pr[T = 1],   That_k = -2^{-m} C(m-1,t-1) K_{k-1}(t-1; m-1) / C(m-1,k-1)   (k >= 1),
  Fhat(S) = [S = 0] - That_|S|  (z not in S),   Fhat(S + z) = That_|S|  (up to sign).
L_z = E[log2(1/Fhat^2)/|S|  |  z in S] and H/I are computed exactly (big integers, then logs).
Usage: python percoord_exact.py
"""
import math
from monolib import setup_process


def kraw_row(N, x):
    """K_k(x; N) for k = 0..N as Python ints (three-term recurrence in k)."""
    K = [1, N - 2 * x]
    for k in range(1, N):
        K.append(((N - 2 * x) * K[k] - (N - k + 1) * K[k - 1]) // (k + 1))
    return K[:N + 1]


def log2_abs(v):
    """log2 |v| for a nonzero Python int or Fraction-like int."""
    v = abs(v)
    b = v.bit_length()
    if b <= 1000:
        return math.log2(v)
    sh = b - 900
    return math.log2(v >> sh) + sh


def run(m, t):
    # mu = Pr[|x| >= t]
    tot = sum(math.comb(m, j) for j in range(t, m + 1))
    lg_mu = log2_abs(tot) - m
    mu = 2.0 ** lg_mu
    K = kraw_row(m - 1, t - 1)                   # K_{k-1}(t-1; m-1), k = 1..m -> K[k-1]
    # quantities in log2 domain: That_k^2 = K^2 4^{-m}
    H = 0.0
    I = 0.0
    Lz_num = 0.0
    Infz = 0.0
    # k = 0 terms: Fhat(empty) = 1 - mu, Fhat({z}) = mu
    p0 = (1.0 - mu) ** 2
    H += -p0 * math.log2(p0) if p0 > 0 else 0.0
    pz = mu * mu
    H += -pz * math.log2(pz)
    I += 1 * pz
    Infz += pz
    Lz_num += pz * (-math.log2(pz)) / 1.0
    for k in range(1, m + 1):
        Kv = K[k - 1]
        if Kv == 0:
            continue
        lg_p = 2 * (log2_abs(Kv) + log2_abs(math.comb(m - 1, t - 1)) - log2_abs(math.comb(m - 1, k - 1))) - 2 * m
        lg_c = log2_abs(math.comb(m, k))
        w = 2.0 ** (lg_c + lg_p)                 # C(m,k) That_k^2  (mass of the level, both halves equal)
        # z not in S: Fhat = -That_k (k >= 1); z in S: Fhat = That_k with |S| = k + 1
        H += 2 * w * (-lg_p)
        I += w * k + w * (k + 1)
        Infz += w
        Lz_num += w * (-lg_p) / (k + 1)
    return mu, H / I, Lz_num / Infz, Infz


def main():
    setup_process()
    for m in (8, 11, 14, 16, 64, 256, 1024, 4096, 8192):
        # t with mu closest to 1/8
        best = None
        c = int(m / 2 + 0.575 * math.sqrt(m))
        for t in range(max(1, c - 6), min(m, c + 6) + 1):
            tot = sum(math.comb(m, j) for j in range(t, m + 1))
            mu = 2.0 ** (log2_abs(tot) - m)
            if best is None or abs(mu - 0.125) < abs(best[1] - 0.125):
                best = (t, mu)
        t = best[0]
        mu, HI, Lz, Infz = run(m, t)
        print(f"m={m:5d} t={t:5d} mu={mu:.4f}  H/I={HI:.4f}  Inf_z={Infz:.4f}  L_z={Lz:.4f}  "
              f"log2(m)={math.log2(m):.2f}", flush=True)


if __name__ == "__main__":
    main()
