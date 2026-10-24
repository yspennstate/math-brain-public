"""Is the coefficient of the logarithm in Theorem 1.3 sharp?

Base functions g(y, z) = M(y) OR (z AND [y = y*]) with M(y) = [|y| >= k] a symmetric threshold on n
variables and y* a maximal zero of M (|y*| = k - 1). Then F_0 = 1 - 2M, F_1 = F_0 - 2 delta_{y*}, and for
T in [n]:  2^n Ghat(T) = N_t - chi_T(y*),  2^n Ghat(T + z) = chi_T(y*),  N_t = 2^n (1 - 2M)^(T), t = |T|,
with chi_T(y*) = (-1)^{|T cap supp y*|}. Group T by j = |T cap supp y*|, l = |T - supp y*|.
Delta_z = sum_T [phi(P(T)) + phi(P(T+z)) - (phi(P0(T)) + phi(P1(T)))/2], computed per T in mpmath
(no cancellation between large entropies). Inf_z = 2^-n. Theorem 1.3 bounds Delta_z / Inf_z by
4.6355 + Psi(4m/Inf_z - 2) ~ log2(4 e m 2^n); Remark 6.1 (majority, k = (n+1)/2) gives about n/2.
"""
import math
import sys
import functools
import mpmath as mp

print = functools.partial(print, flush=True)


def threshold_coeffs(n, k):
    """N_t = sum_y (1 - 2[|y| >= k]) chi_T(y) for |T| = t, t = 0..n, exact integers.
    N_t = 2 S_t - 2^n [t = 0], S_t = sum_{w < k} [u^w] (1-u)^t (1+u)^(n-t)."""
    # c = coefficients of (1+u)^n
    c = [math.comb(n, w) for w in range(n + 1)]
    out = []
    for t in range(n + 1):
        S = sum(c[:k])
        out.append(2 * S - (2 ** n if t == 0 else 0))
        if t == n:
            break
        # c <- c * (1 - u) / (1 + u): first divide by (1+u), then multiply by (1-u)
        d = [0] * (n + 1)
        rem = 0
        # division of polynomial c (degree n) by (1+u): d_w = c_w - d_{w-1}
        prev = 0
        for w in range(n + 1):
            d[w] = c[w] - prev
            prev = d[w]
        assert d[n] == 0, "not divisible"
        e = [0] * (n + 1)
        for w in range(n + 1):
            e[w] = d[w] - (d[w - 1] if w >= 1 else 0)
        c = e
    return out


def phi(p):
    return mp.mpf(0) if p == 0 else -p * mp.log(p, 2)


def delta_ratio(n, k):
    mp.mp.prec = 2 * n + 128
    N = threshold_coeffs(n, k)
    four = mp.mpf(4) ** n
    Pz = 1 / four
    ks = k - 1                      # |supp y*|
    tot = mp.mpf(0)
    B = mp.mpf(0)
    for j in range(ks + 1):
        e = -1 if j % 2 else 1
        for l in range(n - ks + 1):
            t = j + l
            X = N[t]
            mult = math.comb(ks, j) * math.comb(n - ks, l)
            P = mp.mpf((X - e) ** 2) / four
            P0 = mp.mpf(X ** 2) / four
            P1 = mp.mpf((X - 2 * e) ** 2) / four
            term = phi(P) + phi(Pz) - (phi(P0) + phi(P1)) / 2
            tot += mult * term
            B += mult * (phi(P) + phi(Pz) - phi(P + Pz))
    infz = mp.mpf(2) ** (-n)
    qM0 = mp.mpf(sum(math.comb(n, w) for w in range(k))) / mp.mpf(2) ** n     # Pr[M = 0]
    q = qM0 - infz / 2
    m = min(q, 1 - q)
    r = 4 * m / infz - 2
    Psi = mp.log(mp.e * (r + 2 * mp.sqrt(r) + 2), 2)
    bound = mp.mpf('4.6355') + Psi
    return float(tot / infz), float(B / infz), float(bound), float(mp.log(4 * m / infz, 2))


def main():
    ns = [int(a) for a in sys.argv[1:]] or [9, 15, 21, 31, 41, 61, 81, 101, 141, 201]
    for n in ns:
        best = None
        for k in range(1, n + 1):
            d, b, bd, lg = delta_ratio(n, k)
            if best is None or d > best[1]:
                best = (k, d, b, bd, lg)
            if k in ((n + 1) // 2,):
                print(f"  n={n:4d} k={k:4d} (majority threshold): Delta_z/Inf_z = {d:9.4f}, B_z/Inf_z = {b:9.4f}, "
                      f"log2(4m/Inf_z) = {lg:9.4f}, ratio/log = {d / lg:.4f}")
        k, d, b, bd, lg = best
        print(f"n={n:4d} best k={k:4d}: Delta_z/Inf_z = {d:9.4f} (B_z part {b:9.4f}); Theorem 1.3 bound {bd:9.4f}; "
              f"log2(4m/Inf_z) = {lg:9.4f}; Delta/log = {d / lg:.4f}; Delta/bound = {d / bd:.4f}")


if __name__ == "__main__":
    main()
