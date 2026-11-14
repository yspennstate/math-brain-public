"""Sheared-torus version of ust_torus_theta.py. Torus Z^2 / <(n1, 0), (s, n2)>, modulus tau = (s + i n2) / n1.

Output per sample: n1 n2 s m classes, each class (a, b) meaning a*(n1,0) + b*(s,n2), sign-normalised.
Usage: python ust_torus_shear.py n1 n2 s samples seed out.tsv
"""
import sys
import numpy as np
from numba import njit


@njit(cache=True)
def nb(u, r, n1, n2, s):
    # neighbour of u in direction r and the lifted step (dx, dy); crossing y = n2 - 1 -> 0 shifts x by -s
    x = u % n1
    y = u // n1
    if r == 0:
        return ((x + 1) % n1) + n1 * y, 1, 0
    if r == 1:
        return ((x - 1) % n1) + n1 * y, -1, 0
    if r == 2:
        if y == n2 - 1:
            return ((x - s) % n1), 0, 1
        return x + n1 * (y + 1), 0, 1
    if y == 0:
        return ((x + s) % n1) + n1 * (n2 - 1), 0, -1
    return x + n1 * (y - 1), 0, -1


@njit(cache=True)
def run(n1, n2, s, seed):
    N = n1 * n2
    np.random.seed(seed)
    intree = np.zeros(N, np.bool_)
    nxt = -np.ones(N, np.int64)
    sdx = np.zeros(N, np.int64)
    sdy = np.zeros(N, np.int64)
    intree[0] = True
    for start in range(N):
        u = start
        while not intree[u]:
            r = np.random.randint(4)
            v, dx, dy = nb(u, r, n1, n2, s)
            nxt[u] = v
            sdx[u] = dx
            sdy[u] = dy
            u = v
        u = start
        while not intree[u]:
            intree[u] = True
            u = nxt[u]
    # lifts: position of each vertex in the plane, following the tree to the root
    lx = np.zeros(N, np.int64)
    ly = np.zeros(N, np.int64)
    done = np.zeros(N, np.bool_)
    done[0] = True
    stack = np.empty(N, np.int64)
    for st in range(N):
        if done[st]:
            continue
        k = 0
        u = st
        while not done[u]:
            stack[k] = u
            k += 1
            u = nxt[u]
        for j in range(k - 1, -1, -1):
            w = stack[j]
            p = nxt[w]
            lx[w] = lx[p] - sdx[w]
            ly[w] = ly[p] - sdy[w]
            done[w] = True
    out = np.zeros((16, 2), np.int64)
    m = 0
    for u in range(N):
        for r in (0, 2):
            v, dx, dy = nb(u, r, n1, n2, s)
            if nxt[u] == v or nxt[v] == u:
                continue
            DX = lx[u] + dx - lx[v]
            DY = ly[u] + dy - ly[v]
            if DX == 0 and DY == 0:
                continue
            b = DY // n2
            a = (DX - b * s) // n1
            if a < 0 or (a == 0 and b < 0):
                a, b = -a, -b
            seen = False
            for i in range(m):
                if out[i, 0] == a and out[i, 1] == b:
                    seen = True
            if not seen and m < 16:
                out[m, 0] = a
                out[m, 1] = b
                m += 1
    return out[:m]


def main():
    n1, n2, s, S, seed, out = (int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]),
                               int(sys.argv[5]), sys.argv[6])
    with open(out, "w", encoding="utf-8") as f:
        for k in range(S):
            c = run(n1, n2, s, seed * 1000003 + k)
            f.write(f"{n1}\t{n2}\t{s}\t{len(c)}\t" + ";".join(f"{a},{b}" for a, b in c) + "\n")


if __name__ == "__main__":
    main()
