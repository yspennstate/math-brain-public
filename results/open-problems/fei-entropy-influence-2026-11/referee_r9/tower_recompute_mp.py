"""Same recursion as tower_recompute.py in 40-digit mpmath, to settle the record's last digits."""
import sys

import mpmath as mp
import numpy as np

from tower_recompute import PM, T, dual, PMK4, table

mp.mp.dps = 40


def H2(p):
    if p <= 0 or p >= 1:
        return mp.mpf(0)
    return -p * mp.log(p, 2) - (1 - p) * mp.log(1 - p, 2)


def biased_c2(t, m, mu):
    p_true = (1 - mu) / 2
    s = mp.sqrt(1 - mu * mu)
    phi_t, phi_f = (-1 - mu) / s, (1 - mu) / s
    c = np.array([mp.mpf(int(v)) for v in t], dtype=object)
    for k in range(m):
        c = c.reshape(-1, 2, 1 << k)
        v0, v1 = c[:, 0, :].copy(), c[:, 1, :].copy()
        c[:, 0, :] = (1 - p_true) * v0 + p_true * v1
        c[:, 1, :] = (1 - p_true) * v0 * phi_f + p_true * v1 * phi_t
        c = c.reshape(-1)
    return c


def compose(state, t, m):
    mean, z, a, e, inf = state
    c = biased_c2(t, m, mean)
    c2 = c * c
    r = 1 / (1 - z)
    Pj = sum(c2[1::2])
    Ei = Pj * e * r
    for S in range(0, 1 << m, 2):
        w0, w1 = c2[S], c2[S + 1] * a * r
        if w0 + w1 > 0:
            Ei += (w0 + w1) * H2(w1 / (w0 + w1))
    newmean = c[0]
    z2, a2, inf2 = newmean ** 2, c2[1] * a * r, Pj * inf * r
    e2 = Ei - (z2 + a2) * H2(a2 / (z2 + a2))
    return (newmean, z2, a2, e2, inf2), Ei / inf2, abs(sum(c2) - 1)


def main():
    M, P, D = PM(3), PM(4), dual(PM(3))
    words = {"small": [M, D, D, D, D, dual(T(2, 5))],
             "record": [M, D, D, D, D, M, P, P, P, dual(T(2, 2)), dual(PMK4()), dual(T(4, 3)), T(2, 6), T(3, 5)]}
    tabs = {}
    for name, gs in words.items():
        st = (mp.mpf(0), mp.mpf(0), mp.mpf(1), mp.mpf(0), mp.mpf(1))
        for lvl, g in enumerate(gs):
            if id(g) not in tabs:
                tabs[id(g)] = (table(*g), g[1])
            t, m = tabs[id(g)]
            st, ratio, err = compose(st, t, m)
            print(f"  {name} level {lvl+1} m={m} ratio {mp.nstr(ratio, 20)} |sum c2 - 1| {mp.nstr(err, 3)}", flush=True)
        print(f"{name}: {mp.nstr(ratio, 25)}", flush=True)


if __name__ == "__main__":
    sys.exit(main())
