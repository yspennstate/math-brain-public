"""Psi >= 0 for every vector with exactly one positive coordinate, every n >= 5: a finite coefficient check.

x = (a, -y_1, ..., -y_(n-1)),  y_1 >= y_2 >= ... >= y_(n-1) >= 0,  a = sum y.  Then m T = y_1 y_2 and
G = T^3 Psi = (n-4)(2Q - T^2) T - 2(n-3) P^2 + (n-1)((n^2-6n+6) T^2 + 2nQ) y_1 y_2  is a sextic form in the
increments w_i = y_i - y_(i+1) >= 0.  A monomial of degree 6 involves at most six of the w_i; putting the other
increments to zero leaves a vector with r <= 6 levels: values v_1 > ... > v_r > 0 taken c_1, ..., c_r times and
j zeros, v_s = z_s + ... + z_r.  So G has no negative coefficient in w, for every n, as soon as for r = 1, ..., 6
the form G_r(z; c, j) has no negative coefficient for all integers c_s >= 1, j >= 0 with n = 1 + sum c + j >= 5.
Two shapes: c_1 = 1 (then y_1 y_2 = v_1 v_2, or v_1 * 0 if r = 1) and c_1 >= 2 (then y_1 y_2 = v_1^2).

For each r and shape the coefficients are polynomials in g_s = c_s - 1 (or c_1 - 2) and j; the script reports every
coefficient that has a negative coefficient as a polynomial in (g, j).  Those need a case split and are printed.

Usage: one_positive_all.py rmax [rmin]      an agent, 11 Nov 2026."""
import sys
import time
from sympy import ZZ
from sympy.polys.rings import ring


def run(r, shape):
    names = [f"z{s}" for s in range(1, r + 1)] + [f"g{s}" for s in range(1, r + 1)] + ["j"]
    R, *gens = ring(",".join(names), ZZ)
    z, g, j = gens[:r], gens[r:2 * r], gens[2 * r]
    c = [g[s] + 1 for s in range(r)]
    if shape == "II":
        c[0] = g[0] + 2
    else:
        c[0] = R(1)  # g1 unused in shape I
    v = [sum(z[s:], R(0)) for s in range(r)]
    a = sum((c[s] * v[s] for s in range(r)), R(0))
    n = R(1) + sum(c, R(0)) + j
    T = a**2 + sum((c[s] * v[s] ** 2 for s in range(r)), R(0))
    P = a**3 - sum((c[s] * v[s] ** 3 for s in range(r)), R(0))
    Q = a**4 + sum((c[s] * v[s] ** 4 for s in range(r)), R(0))
    if shape == "II":
        mT = v[0] ** 2
    else:
        mT = v[0] * v[1] if r >= 2 else R(0)
    G = (n - 4) * (2 * Q - T**2) * T - 2 * (n - 3) * P**2 + (n - 1) * ((n**2 - 6 * n + 6) * T**2 + 2 * n * Q) * mT
    by_mon = {}
    for mon, co in G.terms():
        zk, gk = mon[:r], mon[r:]
        d = by_mon.setdefault(zk, {})
        d[gk] = d.get(gk, 0) + co
    negs = []
    for zk, d in by_mon.items():
        if any(val < 0 for val in d.values()):
            negs.append((zk, {k: val for k, val in d.items() if val < 0}, d))
    return len(by_mon), negs, names[r:]


def main():
    rmax = int(sys.argv[1])
    rmin = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    for r in range(rmin, rmax + 1):
        for shape in ("I", "II"):
            t0 = time.time()
            nm, negs, gn = run(r, shape)
            print(f"r={r} shape {shape}: z-monomials {nm}, with a negative coefficient in (g, j): {len(negs)}  [{time.time() - t0:.1f} s]", flush=True)
            for zk, neg, full in negs[:40]:
                const = full.get(tuple([0] * len(gn)), 0)
                print(f"   z^{zk}: {len(neg)} negative terms of {len(full)}, constant term {const}; negative: "
                      + "; ".join(f"{val}*" + "".join(f"{gn[i]}^{e}" for i, e in enumerate(k) if e) for k, val in list(neg.items())[:6]), flush=True)


if __name__ == "__main__":
    main()
