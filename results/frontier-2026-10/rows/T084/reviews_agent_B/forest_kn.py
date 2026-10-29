"""Forest measure t^|F| on K_n, adjacent pair e = ab, f = bc, exactly: a tree on s labelled vertices containing a fixed spanning
forest with component sizes a_i is counted by s^(k-2) prod a_i, so C_s = s^(s-2) t^(s-1), F_s = 2 s^(s-3) t^(s-1),
D_s = 3 s^(s-4) t^(s-1); Z_m = sum_k C(m-1,k-1) C_k Z_{m-k}. Returns 1 - Z Z_ef / Z_e^2."""
from mpmath import mp, mpf, nstr, binomial as Bn
mp.dps = 120


def margin(n, t):
    t = mpf(t)
    C = [mpf(0)] + [mpf(s) ** (s - 2) * t ** (s - 1) for s in range(1, n + 1)]
    F = [mpf(0), mpf(0)] + [2 * mpf(s) ** (s - 3) * t ** (s - 1) for s in range(2, n + 1)]
    D = [mpf(0)] * 3 + [3 * mpf(s) ** (s - 4) * t ** (s - 1) for s in range(3, n + 1)]
    Z = [mpf(1)] + [mpf(0)] * n
    for m in range(1, n + 1):
        Z[m] = sum(Bn(m - 1, k - 1) * C[k] * Z[m - k] for k in range(1, m + 1))
    Zef = sum(Bn(n - 3, s - 3) * D[s] * Z[n - s] for s in range(3, n + 1))
    Ze = sum(Bn(n - 2, s - 2) * F[s] * Z[n - s] for s in range(2, n + 1))
    return 1 - Z[n] * Zef / Ze ** 2
