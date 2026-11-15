"""Exact min over ALL orders of the nested witness on small DNFs with no private term (FLOW 12(q)).

Family: points of Z_p^2 (p prime), terms = the lines of D parallel classes. Every variable lies in D terms of
width p, two terms share at most one variable, translations act transitively on the points.
Prints the same row as filt_big.py: minE = E_i/Inf_i, F = min over orders of the nested witness / Inf_i.

Usage: python leafless.py P D [D ...]        (P = 3 or 5; n = P^2 <= 25)
"""
import sys
import itertools
from filt_big import dnf, run


def plane_lines(p, D):
    pts = list(itertools.product(range(p), repeat=2))
    dirs = [(1, 0), (0, 1)] + [(1, s) for s in range(1, p)]
    lines = []
    for a, b in dirs[:D]:
        for c in range(p):
            lines.append([k for k, (x, y) in enumerate(pts) if (a * x + b * y) % p == c])
    return lines


def main():
    p = int(sys.argv[1])
    n = p * p
    for D in [int(t) for t in sys.argv[2:]]:
        lines = plane_lines(p, D)
        assert all(len(L) == p for L in lines)
        run("AG2_%d_D%d" % (p, D), n, (lambda L: lambda: dnf(n, L))(lines), True)


if __name__ == "__main__":
    main()
