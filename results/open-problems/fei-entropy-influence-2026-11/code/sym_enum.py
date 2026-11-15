"""Exhaustive search over ALL Boolean functions invariant under a transitive permutation group, for the largest
self-tower value of G = E_1/Inf_1 (FLOW 12(y) item 4; same recursion as tower_hill.py, vectorised over a batch).

A function invariant under a transitive group has all E_i equal and all Inf_i equal, so G_r = sum_i E_i / I for
every level r of its self-tower, and max_r G_r is a lower bound for G* and A*.

Usage: python sym_enum.py group outdir [lane nlanes] [batch] [maxdepth] [patterns]
  group: k33 | k24 | k4 | q3v | agl7 | agl11 | f21 | ag23 | petv | s3ws3 | s2ws5 | s2ws6 | info
  "info" prints the orbit count of every group and exits.
  patterns: comma list from pp, mm, mp, pm (default pp): the output signs of the gates from the bottom up,
  period two. pp = self-tower of f; mm = self-tower of -f; mp = -f, f, -f, ...; pm = f, -f, f, ....
  With several patterns the reported depth is depth + 100 * (index of the winning pattern).
The functions are coded by an integer: bit j-1 of the code is the sign of orbit j (orbit 0, the empty set, is
fixed to +1; f and -f have the same G). Lane l of L handles the codes congruent to l mod L.
Writes <outdir>/enum_<group>_l<lane>of<L>.txt (progress) and .top.txt (the 40 best by tower value and the 40 best by
depth-one value: value, depth, code, mean). Stops early if <outdir>/STOP exists.
"""
import heapq
import itertools
import os
import sys
import time
import numpy as np


def wht_b(F):
    a = np.array(F, dtype=np.float64)
    B, N = a.shape
    h = 1
    while h < N:
        a = a.reshape(B, -1, 2, h)
        a = np.stack((a[:, :, 0, :] + a[:, :, 1, :], a[:, :, 0, :] - a[:, :, 1, :]), axis=2).reshape(B, N)
        h *= 2
    return a / N


def xlog(x, s):
    """x log2(x/s), 0 where x = 0."""
    ok = x > 0
    return np.where(ok, x * (np.log2(np.where(ok, x, 1.0)) - np.log2(np.where(s > 0, s, 1.0))), 0.0)


def phi(p, q):
    s = p + q
    return -(xlog(p, s) + xlog(q, s))


def group_gens(name):
    """(k, list of generators as permutations of range(k))."""
    if name == "k33":      # edges of K_{3,3} = cells of the 3 x 3 grid, Aut of order 72
        c = lambda u, v: 3 * u + v
        g = []
        g.append([c((u + 1) % 3, v) for u in range(3) for v in range(3)])
        g.append([c(u, (v + 1) % 3) for u in range(3) for v in range(3)])
        sw = [1, 0, 2]
        g.append([c(sw[u], v) for u in range(3) for v in range(3)])
        g.append([c(u, sw[v]) for u in range(3) for v in range(3)])
        g.append([c(v, u) for u in range(3) for v in range(3)])
        return 9, g
    if name == "k24":      # edges of K_{2,4}
        c = lambda u, v: 4 * u + v
        g = [[c(1 - u, v) for u in range(2) for v in range(4)],
             [c(u, (v + 1) % 4) for u in range(2) for v in range(4)]]
        sw = [1, 0, 2, 3]
        g.append([c(u, sw[v]) for u in range(2) for v in range(4)])
        return 8, g
    if name == "k4":       # edges of K_4 under S_4
        edges = list(itertools.combinations(range(4), 2))
        pos = {e: i for i, e in enumerate(edges)}
        g = []
        for perm in ([1, 0, 2, 3], [1, 2, 3, 0]):
            g.append([pos[tuple(sorted((perm[a], perm[b])))] for a, b in edges])
        return 6, g
    if name == "q3v":      # vertices of the cube, group of order 48
        g = [[x ^ 1 for x in range(8)],
             [((x & 1) << 1) | ((x >> 1) & 1) | (x & 4) for x in range(8)],
             [((x << 1) & 7) | (x >> 2) for x in range(8)]]
        return 8, g
    if name == "agl7":
        return 7, [[(x + 1) % 7 for x in range(7)], [(3 * x) % 7 for x in range(7)]]
    if name == "f21":
        return 7, [[(x + 1) % 7 for x in range(7)], [(2 * x) % 7 for x in range(7)]]
    if name == "agl11":
        return 11, [[(x + 1) % 11 for x in range(11)], [(2 * x) % 11 for x in range(11)]]
    if name == "ag23":     # points of the affine plane over F_3 under AGL(2,3)
        c = lambda x, y: 3 * (x % 3) + (y % 3)
        pts = [(x, y) for x in range(3) for y in range(3)]
        g = [[c(x + 1, y) for x, y in pts], [c(y, x) for x, y in pts], [c(x + y, y) for x, y in pts],
             [c(2 * x, y) for x, y in pts]]
        return 9, g
    if name == "petv":     # vertices of the Petersen graph = 2-subsets of 5 points under S_5
        prs = list(itertools.combinations(range(5), 2))
        pos = {e: i for i, e in enumerate(prs)}
        g = []
        for perm in ([1, 0, 2, 3, 4], [1, 2, 3, 4, 0]):
            g.append([pos[tuple(sorted((perm[a], perm[b])))] for a, b in prs])
        return 10, g
    if name in ("s3ws3", "s2ws5", "s2ws6"):   # S_m wr S_b on b blocks of m points
        m, b = {"s3ws3": (3, 3), "s2ws5": (2, 5), "s2ws6": (2, 6)}[name]
        k = m * b
        g = []
        p = list(range(k)); p[0], p[1] = 1, 0; g.append(p)                    # swap inside block 0
        p = list(range(k)); p[0:m] = [(j + 1) % m for j in range(m)]; g.append(p)  # cycle inside block 0
        g.append([((u + 1) % b) * m + j for u in range(b) for j in range(m)])  # cycle the blocks
        p = list(range(k))
        for j in range(m):
            p[j], p[m + j] = m + j, j
        g.append(p)                                                           # swap blocks 0 and 1
        return k, g
    raise SystemExit("unknown group " + name)


def orbits(k, gens):
    N = 1 << k
    idx = np.arange(N, dtype=np.int64)
    maps = []
    for g in gens:
        y = np.zeros_like(idx)
        for src in range(k):
            y |= ((idx >> src) & 1) << g[src]
        maps.append(y)
    rep = idx.copy()
    while True:
        new = rep.copy()
        for y in maps:
            new = np.minimum(new, rep[y])
            tmp = new.copy()
            np.minimum.at(tmp, y, rep)
            new = tmp
        if np.array_equal(new, rep):
            break
        rep = new
    reps, inv = np.unique(rep, return_inverse=True)
    # transitivity on points
    single = {int(rep[1 << j]) for j in range(k)}
    return reps.size, inv, len(single) == 1


class BatchTower:
    def __init__(self, k, maxdepth):
        self.k, self.maxdepth = k, maxdepth
        idx = np.arange(1 << k)
        pc = np.zeros(idx.size, dtype=np.int64)
        for j in range(k):
            pc += (idx >> j) & 1
        self.lo = idx[(idx & 1) == 0]
        self.pc_lo = pc[self.lo].astype(np.float64)

    def values(self, F, pat="pp", Fh=None):
        """F: (B, N) of +-1. Returns (best value, depth of best, depth-one value), each of shape (B,).

        pat gives the output signs of the gates from the bottom up, repeated with period two: "pp" is the
        self-tower of f, "mm" of -f, "mp" is -f, f, -f, ... and "pm" is f, -f, f, ....  Replacing the gate F by -F
        changes K_A to -K_A, so only the mean c of the level changes sign; a, R and Inf are unchanged.
        """
        B, N = F.shape
        lo = self.lo
        if Fh is None:
            Fh = wht_b(F)
        sgn = [1.0 if ch == "p" else -1.0 for ch in pat]
        mu = Fh ** 2
        p, q = mu[:, lo], mu[:, lo | 1]
        d = q.sum(axis=1)
        live = d > 1e-12
        dd = np.where(live, d, 1.0)
        c, a = sgn[0] * Fh[:, 0], mu[:, 1].copy()
        R = phi(p[:, 1:], q[:, 1:]).sum(axis=1)
        g = np.where(live, (R + phi(c * c, a)) / dd, 0.0)
        g1 = g.copy()
        best, bdep = g.copy(), np.ones(B, dtype=np.int64)
        for r in range(2, self.maxdepth + 1):
            K = Fh.copy()
            h = 1
            while h < N:
                K = K.reshape(B, -1, 2, h)
                K[:, :, 0, :] += c[:, None, None] * K[:, :, 1, :]
                K = K.reshape(B, N)
                h *= 2
            t = 1.0 - c * c
            live &= t > 1e-300
            ts = np.where(live, t, 1.0)
            w = ts[:, None] ** self.pc_lo[None, :]
            k0, k1 = K[:, lo] ** 2, K[:, lo | 1] ** 2
            infF = (w * k1).sum(axis=1)
            R = (w[:, 1:] * phi(k0[:, 1:], k1[:, 1:] * a[:, None])).sum(axis=1) + infF * R
            c, a, d = sgn[(r - 1) % 2] * K[:, 0], K[:, 1] ** 2 * a, infF * d
            live &= (d > 1e-200) & (a > 1e-250)
            dd = np.where(live, d, 1.0)
            g = np.where(live, (R + phi(c * c, a)) / dd, -1.0)
            up = g > best
            best = np.where(up, g, best)
            bdep = np.where(up, r, bdep)
            if not live.any():
                break
        return best, bdep, g1


def main():
    name = sys.argv[1]
    if name == "info":
        for nm in ("k4", "agl7", "f21", "q3v", "k24", "k33", "ag23", "s3ws3", "petv", "s2ws5", "agl11", "s2ws6"):
            k, gens = group_gens(nm)
            m, inv, tr = orbits(k, gens)
            print("%-6s k=%2d orbits=%3d functions=2^%d transitive=%s" % (nm, k, m, m - 1, tr))
        return
    outdir = sys.argv[2]
    lane = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    nl = int(sys.argv[4]) if len(sys.argv) > 4 else 1
    batch = int(sys.argv[5]) if len(sys.argv) > 5 else 2048
    maxdepth = int(sys.argv[6]) if len(sys.argv) > 6 else 14
    pats = sys.argv[7].split(",") if len(sys.argv) > 7 else ["pp"]
    for nm in name.split(","):          # several groups, one after the other
        if os.path.exists(os.path.join(outdir, "STOP")):
            break
        run(nm, outdir, lane, nl, batch, maxdepth, pats)


def run(name, outdir, lane, nl, batch, maxdepth, pats):
    k, gens = group_gens(name)
    m, inv, tr = orbits(k, gens)
    if not tr:
        raise SystemExit("group not transitive on the points")
    os.makedirs(outdir, exist_ok=True)
    ptag = "" if pats == ["pp"] else "_" + "".join(pats)
    tag = os.path.join(outdir, "enum_%s%s_l%dof%d" % (name, ptag, lane, nl))
    total = 1 << (m - 1)
    bt = BatchTower(k, maxdepth)
    shifts = np.arange(m - 1, dtype=np.int64)
    top, top1 = [], []     # heaps of (value, code, depth + 100 * pattern number, mean)
    keep = 40
    t0 = time.time()
    done = 0
    log = open(tag + ".txt", "a", encoding="utf-8")
    log.write("start group=%s k=%d orbits=%d total=%d lane=%d/%d batch=%d maxdepth=%d\n" % (
        name, k, m, total, lane, nl, batch, maxdepth))
    log.flush()

    def dump():
        with open(tag + ".top.txt", "w", encoding="utf-8") as fh:
            fh.write("group %s k %d orbits %d codes_done %d of %d (lane %d of %d) sec %.0f\n" % (
                name, k, m, done, (total - lane + nl - 1) // nl, lane, nl, time.time() - t0))
            fh.write("TOP by tower value: value depth code mean\n")
            for v, code, dep, mean in sorted(top, reverse=True):
                fh.write("%.12f %d %d %.10f\n" % (v, dep, code, mean))
            fh.write("TOP by depth-one value: value depth code mean\n")
            for v, code, dep, mean in sorted(top1, reverse=True):
                fh.write("%.12f %d %d %.10f\n" % (v, dep, code, mean))

    start = lane
    nb = 0
    while start < total:
        codes = np.arange(start, min(total, start + batch * nl), nl, dtype=np.int64)
        start += batch * nl
        sg = np.ones((codes.size, m))
        sg[:, 1:] = 1.0 - 2.0 * ((codes[:, None] >> shifts[None, :]) & 1)
        F = sg[:, inv]
        Fh = wht_b(F)
        best, bdep, g1 = bt.values(F, pats[0], Fh)
        for pi in range(1, len(pats)):          # depth is reported as depth + 100 * (index of the pattern)
            b2, d2, _ = bt.values(F, pats[pi], Fh)
            up = b2 > best
            best = np.where(up, b2, best)
            bdep = np.where(up, d2 + 100 * pi, bdep)
        means = F.mean(axis=1)
        for arr, heap in ((best, top), (g1, top1)):
            thr = heap[0][0] if len(heap) >= keep else -1.0
            for j in np.nonzero(arr > thr)[0]:
                item = (float(arr[j]), int(codes[j]), int(bdep[j]) if heap is top else 1, float(means[j]))
                if len(heap) < keep:
                    heapq.heappush(heap, item)
                elif item > heap[0]:
                    heapq.heapreplace(heap, item)
        done += codes.size
        nb += 1
        if nb % 50 == 0:
            log.write("done %d sec %.0f best %.12f\n" % (done, time.time() - t0, max(top)[0]))
            log.flush()
            dump()
            if os.path.exists(os.path.join(outdir, "STOP")):
                log.write("STOP file seen\n")
                break
    dump()
    log.write("end done=%d best=%.12f sec=%.0f\n" % (done, max(top)[0], time.time() - t0))
    log.close()


if __name__ == "__main__":
    main()
