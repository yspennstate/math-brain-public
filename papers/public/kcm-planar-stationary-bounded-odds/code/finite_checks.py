"""Finite-volume checks for the paper (not part of any proof).

For FA-1f and FA-2f on small planar boxes (filled exterior, empty exterior, or periodic), the generator Q of the
finite chain is built with rational q. The script checks, exactly:

1. for every bootstrap fiber C (configurations with the same bootstrap limit), the product weight restricted to C,
   w(z) = q^(#zeros) p^(#ones), is stationary (w Q = 0 in exact rational arithmetic) and satisfies detailed balance;
2. the dimension of the left kernel of Q equals the number of fibers. The kernel contains the fiber vectors of
   item 1, which are linearly independent, so its rational dimension is at least the number of fibers; its dimension
   modulo a large prime is at least its rational dimension, and the script checks that the former equals the number
   of fibers.

Spin 0 is a vacancy (infected), 1 is filled; pi(eta_x = 0) = q. Pure Python 3, no dependencies.
Run from the repository root:  python code/finite_checks.py   (about two minutes; writes data/finite_checks.json).
"""
import itertools
import json
import os
from fractions import Fraction

PRIME = 2_147_483_647


def neighbours(w, h, periodic):
    nb = {}
    for x in range(w):
        for y in range(h):
            out = []
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                a, b = x + dx, y + dy
                if periodic:
                    a, b = a % w, b % h
                    if (a, b) != (x, y) and (a, b) not in out:
                        out.append((a, b))
                elif 0 <= a < w and 0 <= b < h:
                    out.append((a, b))
                else:
                    out.append(None)  # exterior site
            nb[(x, y)] = out
    return nb


def constraint(conf, site, nb, idx, ext, k):
    vac = 0
    for s in nb[site]:
        v = ext if s is None else conf[idx[s]]
        vac += (v == 0)
    return vac >= k


def bootstrap(conf, sites, nb, idx, ext, k):
    c = list(conf)
    changed = True
    while changed:
        changed = False
        for s in sites:
            i = idx[s]
            if c[i] == 1 and constraint(c, s, nb, idx, ext, k):
                c[i] = 0
                changed = True
    return tuple(c)


def rank_mod_p(rows, ncols):
    m = [r[:] for r in rows]
    rank = 0
    for col in range(ncols):
        piv = None
        for r in range(rank, len(m)):
            if m[r][col] % PRIME:
                piv = r
                break
        if piv is None:
            continue
        m[rank], m[piv] = m[piv], m[rank]
        inv = pow(m[rank][col], PRIME - 2, PRIME)
        m[rank] = [(v * inv) % PRIME for v in m[rank]]
        for r in range(len(m)):
            if r != rank and m[r][col] % PRIME:
                f = m[r][col]
                m[r] = [(a - f * b) % PRIME for a, b in zip(m[r], m[rank])]
        rank += 1
    return rank


def case(model_k, w, h, boundary, q):
    p = 1 - q
    periodic = boundary == "periodic"
    ext = {"filled": 1, "empty": 0, "periodic": None}[boundary]
    sites = [(x, y) for x in range(w) for y in range(h)]
    idx = {s: i for i, s in enumerate(sites)}
    nb = neighbours(w, h, periodic)
    states = list(itertools.product((0, 1), repeat=len(sites)))
    sidx = {s: i for i, s in enumerate(states)}
    n = len(states)
    # transitions: (i, j, rate)
    trans = []
    for i, c in enumerate(states):
        for s in sites:
            if constraint(c, s, nb, idx, ext, model_k):
                c2 = list(c)
                c2[idx[s]] = 1 - c[idx[s]]
                rate = q if c[idx[s]] == 1 else p
                trans.append((i, sidx[tuple(c2)], rate))
    fibers = {}
    for i, c in enumerate(states):
        fibers.setdefault(bootstrap(c, sites, nb, idx, ext, model_k), []).append(i)
    weight = [q ** c.count(0) * p ** c.count(1) for c in states]
    # item 1: exact stationarity and detailed balance of each fiber vector
    for members in fibers.values():
        mem = set(members)
        flow = [Fraction(0)] * n
        for i, j, r in trans:
            if i in mem:
                flow[j] += weight[i] * r
                flow[i] -= weight[i] * r
                assert j in mem, "a legal flip left its bootstrap fiber"
        assert all(v == 0 for v in flow), "fiber product weight is not stationary"
    rates = {(i, j): r for i, j, r in trans}
    for (i, j), r in rates.items():
        assert weight[i] * r == weight[j] * rates[(j, i)], "detailed balance fails"
    # item 2: rank of Q^T modulo a prime (Q^T has rows indexed by target state)
    den = q.denominator
    rows = [[0] * n for _ in range(n)]
    for i, j, r in trans:
        v = int(r * den)
        rows[j][i] = (rows[j][i] + v) % PRIME
        rows[i][i] = (rows[i][i] - v) % PRIME
    kernel_dim = n - rank_mod_p(rows, n)
    assert kernel_dim == len(fibers), (kernel_dim, len(fibers))
    active = fibers.get(tuple([0] * len(sites)), [])
    return {"model": "FA-%df" % model_k, "box": "%dx%d" % (w, h), "boundary": boundary, "q": str(q), "states": n,
            "fibers": len(fibers), "kernel_dim": kernel_dim, "largest_fiber": max(len(v) for v in fibers.values()),
            "fully_emptyable_states": len(active)}


def main():
    out = []
    for k in (1, 2):
        for (w, h) in ((2, 2), (3, 2), (2, 3), (4, 2)):
            for boundary in ("filled", "empty", "periodic"):
                if boundary == "periodic" and (w < 3 or h < 2):
                    continue
                if w * h > 8 and boundary != "filled":
                    continue
                for q in (Fraction(1, 3), Fraction(5, 7)):
                    r = case(k, w, h, boundary, q)
                    out.append(r)
                    print(r)
    os.makedirs("data", exist_ok=True)
    with open(os.path.join("data", "finite_checks.json"), "w", newline="\n") as fh:
        json.dump(out, fh, indent=1)
    print(len(out), "cases, all checks passed")


if __name__ == "__main__":
    main()
