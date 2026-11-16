"""Second check of arXiv 2611.12795: the query procedure in the proof of Theorem 2, and Lemma 6.

Part E  For a random partial f: lambda from the classical-adversary programme, the completion G of Lemma 3, then
        the procedure of the proof of Theorem 2 (query a free coordinate of largest influence in G restricted to
        the current subcube C until m(C) = min(delta_0(C), delta_1(C)) is 0).  At every subcube reached:
          the restricted certificates 4 lambda^x cost at most 4 CAdv;
          the queried coordinate has influence at least delta_0 delta_1 / (gamma_0 gamma_1)      (Lemma 4 on C);
          identity (8): I(G|C) - (I(G|C_0) + I(G|C_1)) / 2 = I_i(G|C).
        Over the tree: e_t = E[m(C_t)] does not increase, sum_t E[m(C_t)^2] <= 16 CAdv^2 I(G), and
        s e_s^2 <= sum_{t < s} E[m(C_t)^2].
Part F  Lemma 6 (the form of the O'Donnell-Saks-Schramm-Servedio inequality used in the appendix): for a random
        decision tree computing h with values in [-1, 1] and a random real p,
        |Cov(p, h)| <= (1/2) sum_i q_i E|p(X) - p(X^i)| <= (D/2) max_i sqrt(I_i(p)).
"""
import random
from collections import defaultdict

from t042_check import cadv_lp, influences

TOL = 1e-7


def completion(f, n):
    A, lam, A1, A0 = cadv_lp(f, n)

    def d(a, z):
        return sum(lam[a][i] for i in range(n) if (a ^ z) >> i & 1)

    g = [min(1.0, min(d(a, z) for a in A1)) for z in range(1 << n)]
    cuts = sorted(set([0.25, 0.75] + [v for v in g if 0.25 < v < 0.75]))
    best = None
    for lo, hi in zip(cuts, cuts[1:]):
        tt = (lo + hi) / 2
        G = [1 if g[z] < tt else 0 for z in range(1 << n)]
        I = sum(influences(G, n))
        if best is None or I < best[0]:
            best = (I, G)
    return A, lam, best[1], best[0]


def part_e(f, n, stats):
    A, lam, G, IG = completion(f, n)
    assert all(G[x] == f[x] for x in f)
    em = defaultdict(float)
    em2 = defaultdict(float)
    drop = [0.0]
    maxdepth = [0]

    def cube(mask, base):
        free = [i for i in range(n) if not mask >> i & 1]
        pts = []
        for s in range(1 << len(free)):
            x = base
            for k, i in enumerate(free):
                if s >> k & 1:
                    x |= 1 << i
            pts.append(x)
        return free, pts

    def infl(free, pts):
        return {i: sum(1 for x in pts if G[x] != G[x ^ (1 << i)]) / len(pts) for i in free}

    def rec(mask, base, depth):
        free, pts = cube(mask, base)
        dom = [x for x in pts if x in f]
        d0 = sum(1 for x in dom if f[x] == 0) / len(pts)
        d1 = sum(1 for x in dom if f[x] == 1) / len(pts)
        m = min(d0, d1)
        if m == 0:
            return
        maxdepth[0] = max(maxdepth[0], depth + 1)
        w = 0.5 ** depth
        em[depth] += w * m
        em2[depth] += w * m * m
        I = infl(free, pts)
        i = max(free, key=lambda k: I[k])
        gam = [max(4 * sum(lam[x][k] for k in free) for x in dom if f[x] == b) for b in (0, 1)]
        assert 0 < gam[0] <= 4 * A + TOL and 0 < gam[1] <= 4 * A + TOL
        assert I[i] >= d0 * d1 / (gam[0] * gam[1]) - TOL, ("Lemma 4 fails on a subcube", f, mask, base)
        stats["e_minratio"] = min(stats["e_minratio"], I[i] * gam[0] * gam[1] / (d0 * d1))
        tot = sum(I.values())
        halves = 0.0
        for b in (0, 1):
            fr, ps = cube(mask | (1 << i), base | (b << i))
            halves += sum(infl(fr, ps).values()) / 2
        assert abs(tot - halves - I[i]) < 1e-9, "identity (8) fails"
        drop[0] += w * I[i]
        stats["e_nodes"] += 1
        for b in (0, 1):
            rec(mask | (1 << i), base | (b << i), depth + 1)

    rec(0, 0, 0)
    assert drop[0] <= IG + TOL
    S = 0.0
    prev = None
    for t in range(maxdepth[0] + 1):
        e = em.get(t, 0.0)
        if prev is not None:
            assert e <= prev + TOL, "e_t increases"
        assert t * e * e <= S + TOL, "s e_s^2 above the partial sum"
        S += em2.get(t, 0.0)
        prev = e
    assert S <= 16 * A * A * drop[0] + TOL and S <= 16 * A * A * IG + TOL
    stats["e_cases"] += 1
    stats["e_maxfrac"] = max(stats["e_maxfrac"], S / (16 * A * A * IG))
    stats["e_maxdepth"] = max(stats["e_maxdepth"], maxdepth[0])


def random_tree(rng, n, depth, used=()):
    if depth == 0 or len(used) == n or rng.random() < 0.15:
        return rng.uniform(-1, 1)
    i = rng.choice([k for k in range(n) if k not in used])
    return (i, random_tree(rng, n, depth - 1, used + (i,)), random_tree(rng, n, depth - 1, used + (i,)))


def part_f(rng, n, D, stats):
    tree = random_tree(rng, n, D)
    N = 1 << n
    h = [0.0] * N
    q = [0.0] * n
    for x in range(N):
        node = tree
        while isinstance(node, tuple):
            q[node[0]] += 1 / N
            node = node[1 + (x >> node[0] & 1)]
        h[x] = node
    kind = rng.randrange(3)
    if kind == 0:
        p = [rng.random() for _ in range(N)]
    elif kind == 1:
        p = [0.5 * (hx + 1) + 0.1 * rng.random() for hx in h]
    else:
        p = [float(bin(x & rng.randrange(1, N)).count("1") & 1) for x in range(N)]
    mp = sum(p) / N
    cov = sum((p[x] - mp) * h[x] for x in range(N)) / N
    l1 = [sum(abs(p[x] - p[x ^ (1 << i)]) for x in range(N)) / N for i in range(n)]
    l2 = [sum((p[x] - p[x ^ (1 << i)]) ** 2 for x in range(N)) / N for i in range(n)]
    mid = 0.5 * sum(q[i] * l1[i] for i in range(n))
    assert abs(cov) <= mid + 1e-9, ("OSSS form fails", abs(cov), mid)
    assert mid <= D / 2 * max(l2) ** 0.5 + 1e-9
    stats["f_cases"] += 1
    if mid > 0:
        stats["f_maxratio"] = max(stats["f_maxratio"], abs(cov) / mid)


def main():
    rng = random.Random(7)
    stats = dict(e_cases=0, e_nodes=0, e_minratio=1e9, e_maxfrac=0.0, e_maxdepth=0, f_cases=0, f_maxratio=0.0)
    for n, count in ((3, 60), (4, 60), (5, 40), (6, 25)):
        done = 0
        while done < count:
            q = rng.choice((0.3, 0.5, 0.8, 1.0))
            f = {x: rng.randint(0, 1) for x in range(1 << n) if rng.random() < q}
            if len(set(f.values())) < 2 or len(f) > 22:
                continue
            part_e(f, n, stats)
            done += 1
        print("part E: %d random partial functions on %d bits" % (count, n), flush=True)
    print("part E: %d functions, %d subcubes queried; Lemma 4 on every subcube (smallest I_i gamma_0 gamma_1 / (delta_0 delta_1) = %.3f), identity (8) exact, e_t never increases, sum_t E[m^2] at most %.4f of 16 CAdv^2 I(G); deepest tree %d" % (stats["e_cases"], stats["e_nodes"], stats["e_minratio"], stats["e_maxfrac"], stats["e_maxdepth"]), flush=True)
    for n in (3, 4, 5, 6, 7):
        for D in range(1, n + 1):
            for _ in range(300):
                part_f(rng, n, D, stats)
    print("part F: Lemma 6 on %d random (tree, p) pairs, 3 to 7 bits; largest |Cov| / ((1/2) sum q_i E|p - p^i|) = %.4f" % (stats["f_cases"], stats["f_maxratio"]), flush=True)
    print("all assertions passed")


if __name__ == "__main__":
    main()
