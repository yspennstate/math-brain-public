"""The bound of the width paper (Corollary 5 there) for the k-clique property below its threshold.

For a monotone f all of whose influences are equal (every monotone graph property), Corollary 5 of the width paper,
  H <= sum_v Inf_v (4.6355 + Psi(4m/Inf_v - 2)),   Psi(r) = log2(e(r + 2 sqrt r + 2)),  m = min(q, 1 - q),
together with Inf_v = I/N and the edge-isoperimetric inequality I >= 2 m log2(1/m), gives
  H/I <= 4.6355 + Psi(2N/log2(1/m) - 2).
For the clique property m <= q and Janson's inequality (both forms) gives ln(1/q) >= lambda/(2 max(1, eta)), so
  H/I <= D(n,k) := 4.6355 + Psi(2 ln2 * 2N max(1,eta)/lambda - 2)      (valid whenever this lower bound is used).
Printed per (n, k): lambda, eta, Gamma = N max(1, eta)/lambda, D(n,k), the width-theorem constant C(k,2) + 8.1, and
7.55 + 4 log2 k (the value of D when t_2 dominates eta).
"""
import functools
import mpmath as mp

print = functools.partial(print, flush=True)
mp.mp.dps = 50


def C(a, b):
    if b < 0 or a < 0 or b > a:
        return mp.mpf(0)
    return mp.binomial(a, b)


def Psi(r):
    r = max(mp.mpf(0), r)
    return mp.log(mp.e * (r + 2 * mp.sqrt(r) + 2), 2)


def main():
    for e in (12, 16, 20, 24, 32, 40):
        n = 2 ** e
        N = C(n, 2)
        print(f"--- n = 2^{e}")
        for k in range(3, 200):
            m = k * (k - 1) // 2
            lam = C(n, k) * mp.mpf(2) ** (-m)
            if lam < mp.mpf(2) ** -6:
                break
            eta = mp.mpf(0)
            t2 = C(k, 2) * C(n - k, k - 2) * mp.mpf(2) ** (-(m - 1))
            for j in range(2, k):
                eta += C(k, j) * C(n - k, k - j) * mp.mpf(2) ** (-(m - j * (j - 1) // 2))
            L = lam / (2 * mp.log(2) * max(mp.mpf(1), eta))          # lower bound for log2(1/q)
            Gamma = N * max(mp.mpf(1), eta) / lam
            D = mp.mpf('4.6355') + Psi(2 * N / L - 2)
            width = m + 8.1
            print(f"k={k:3d} lambda={mp.nstr(lam, 4):>10} eta={mp.nstr(eta, 4):>10} (t2 share {mp.nstr(t2 / eta, 3) if eta > 0 else '-':>5}) "
                  f"Gamma={mp.nstr(Gamma, 4):>10}  D={mp.nstr(D, 4):>7}  width {width:7.1f}  7.55+4log2k {float(7.55 + 4 * mp.log(k, 2)):6.2f}")


if __name__ == "__main__":
    main()
