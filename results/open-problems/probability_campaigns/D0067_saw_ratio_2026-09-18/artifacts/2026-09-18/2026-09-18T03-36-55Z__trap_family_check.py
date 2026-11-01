#!/usr/bin/env python3
"""Exact finite sanity checks for the D0067 trapping-pattern family.

The theorem for all k and all sufficiently large M is proved algebraically
in the run report.  This executable checks representative integer cases:
* T_k is a self-avoiding nearest-neighbor path of length 2k+5;
* T_k visits all four neighbors of its root;
* its D4 orbit has size 8;
* oriented patterns for distinct (k,g) are prefix-incompatible;
* the explicit two-end construction is a SAW of length M+4k+12.
"""

D4 = [
    lambda x, y: ( x,  y),
    lambda x, y: ( y, -x),
    lambda x, y: (-x, -y),
    lambda x, y: (-y,  x),
    lambda x, y: (-x,  y),
    lambda x, y: ( x, -y),
    lambda x, y: ( y,  x),
    lambda x, y: (-y, -x),
]

NN = {(1, 0), (-1, 0), (0, 1), (0, -1)}

def T(k):
    assert k >= 1
    p = [(0, 0)]
    p += [(x, 0) for x in range(1, k + 1)]
    p += [(k, 1)]
    p += [(x, 1) for x in range(k - 1, -1, -1)]
    p += [(-1, 1), (-1, 0), (-1, -1), (0, -1)]
    return p

def transform(path, f):
    return [f(x, y) for x, y in path]

def is_nn_path(path):
    return all(abs(x2-x1) + abs(y2-y1) == 1
               for (x1,y1),(x2,y2) in zip(path, path[1:]))

def pair_walk(k, M):
    """Base-orientation T_k at both ends; terminal copy is read backwards."""
    pre = T(k)
    z = (M, 0)
    translated = [(z[0] + x, z[1] + y) for x, y in T(k)]
    suffix = list(reversed(translated))  # starts at (M,-1), ends at z
    connector = [pre[-1], (0, -2)]
    connector += [(x, -2) for x in range(1, M + 1)]
    connector += [(M, -1)]
    return pre + connector[1:] + suffix[1:]

def main():
    K = 25

    for k in range(1, K + 1):
        p = T(k)
        assert len(p) - 1 == 2*k + 5
        assert len(set(p)) == len(p)
        assert is_nn_path(p)
        assert NN.issubset(set(p))
        orbit = {tuple(transform(p, f)) for f in D4}
        assert len(orbit) == 8

    oriented = []
    for k in range(1, K + 1):
        for gi, f in enumerate(D4):
            oriented.append((k, gi, tuple(transform(T(k), f))))

    # Distinct exact start patterns are incompatible: neither can be a prefix
    # of the other. Hence the corresponding start events are disjoint.
    for i, (k, g, s) in enumerate(oriented):
        for ell, h, t in oriented[i+1:]:
            m = min(len(s), len(t))
            assert s[:m] != t[:m], (k, g, ell, h)

    for k in range(1, K + 1):
        for M in range(k + 2, k + 13):
            w = pair_walk(k, M)
            assert is_nn_path(w)
            assert len(set(w)) == len(w), (k, M)
            assert len(w) - 1 == M + 4*k + 12
            # first end is T_k
            assert w[:len(T(k))] == T(k)
            # backwards from terminal endpoint, recentered, is T_k
            z = w[-1]
            back = [(x-z[0], y-z[1]) for x,y in reversed(w[-len(T(k)):])]
            assert back == T(k)

    print("PASS")
    print(f"checked k=1..{K}")
    print("all T_k are exact SAWs of length 2k+5 and trap the root")
    print("all D4 orbits have size 8")
    print("all tested oriented (k,g) start patterns are prefix-incompatible")
    print("all tested paired constructions M=k+2..k+12 are exact SAWs")
    print("paired construction length identity: M+4k+12")

if __name__ == "__main__":
    main()
