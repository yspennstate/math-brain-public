"""Monte Carlo for Schramm's Problem 6.2: homology classes of the dual theta graph of a UST on the n x n torus.

For a spanning tree T of the torus, each non-tree edge e closes a fundamental cycle of class h(e) in Z^2. The
noncontractible classes are +-p, +-q, +-(p+q) for a basis (p, q); the dual theta's three cycles are the duals of
these. We record the superbase {p, q, -(p+q)} through its sorted squared norms (aspect ratio of the torus = 1, or a
rectangle n1 x n2 with metric scaling).

Usage: python ust_torus_theta.py n1 n2 samples seed out.tsv
"""
import sys
import numpy as np
from numba import njit


@njit(cache=True)
def wilson(n1, n2, rng_state):
    N = n1 * n2
    np.random.seed(rng_state)
    intree = np.zeros(N, np.bool_)
    nxt = -np.ones(N, np.int64)
    intree[0] = True
    for start in range(N):
        u = start
        while not intree[u]:
            x = u % n1
            y = u // n1
            r = np.random.randint(4)
            if r == 0:
                v = ((x + 1) % n1) + n1 * y
            elif r == 1:
                v = ((x - 1) % n1) + n1 * y
            elif r == 2:
                v = x + n1 * ((y + 1) % n2)
            else:
                v = x + n1 * ((y - 1) % n2)
            nxt[u] = v
            u = v
        u = start
        while not intree[u]:
            intree[u] = True
            u = nxt[u]
    return nxt


@njit(cache=True)
def disp(u, v, n1, n2):
    # displacement of the lattice step u -> v (neighbours on the torus)
    ux, uy = u % n1, u // n1
    vx, vy = v % n1, v // n1
    dx = vx - ux
    dy = vy - uy
    if dx > 1:
        dx -= n1
    if dx < -1:
        dx += n1
    if dy > 1:
        dy -= n2
    if dy < -1:
        dy += n2
    return dx, dy


@njit(cache=True)
def lifts(nxt, n1, n2):
    N = n1 * n2
    lx = np.zeros(N, np.int64)
    ly = np.zeros(N, np.int64)
    done = np.zeros(N, np.bool_)
    done[0] = True
    stack = np.empty(N, np.int64)
    for s in range(N):
        if done[s]:
            continue
        k = 0
        u = s
        while not done[u]:
            stack[k] = u
            k += 1
            u = nxt[u]
        # u is done; unwind
        for j in range(k - 1, -1, -1):
            w = stack[j]
            p = nxt[w]
            dx, dy = disp(w, p, n1, n2)
            lx[w] = lx[p] - dx
            ly[w] = ly[p] - dy
            done[w] = True
    return lx, ly


@njit(cache=True)
def classes(nxt, lx, ly, n1, n2):
    out = np.zeros((16, 2), np.int64)
    m = 0
    N = n1 * n2
    for u in range(N):
        x = u % n1
        y = u // n1
        for k in range(2):
            if k == 0:
                v = ((x + 1) % n1) + n1 * y
                dx, dy = 1, 0
            else:
                v = x + n1 * ((y + 1) % n2)
                dx, dy = 0, 1
            if nxt[u] == v or nxt[v] == u:
                continue
            a = lx[u] + dx - lx[v]
            b = ly[u] + dy - ly[v]
            if a == 0 and b == 0:
                continue
            a //= n1
            b //= n2
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
    n1, n2, S, seed, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
    with open(out, "w") as f:
        for s in range(S):
            nxt = wilson(n1, n2, seed * 1000003 + s)
            lx, ly = lifts(nxt, n1, n2)
            c = classes(nxt, lx, ly, n1, n2)
            f.write(f"{n1}\t{n2}\t{len(c)}\t" + ";".join(f"{a},{b}" for a, b in c) + "\n")


if __name__ == "__main__":
    main()
