"""Exact-rational sampling check of the pair inequalities (3.3) and (3.4) of the 24 Oct three-state cone.
Not a proof; an independent look at the targets as stated, with no rounding."""
import itertools, random, sys
from fractions import Fraction as Fr

def xy(p):
    v = [3 * t - 1 for t in p]
    return sum(t * t for t in v) / 6, sum(t ** 3 for t in v) / 6

def HFG(p):
    x, y = xy(p)
    return y - x * x / 2, Fr(3, 2) * x - y, 1 - x, x

PERMS = list(itertools.permutations(range(3)))

def brackets(p, r):
    sx = sh = Fr(0)
    for pi in PERMS:
        u = [3 * p[i] * r[pi[i]] for i in range(3)]
        z = sum(u)
        if z == 0:
            continue
        P = [t / z for t in u]
        x, y = xy(P)
        sx += z * x
        sh += z * (y - x * x / 2)
    return sx / 6, sh / 6

def simplex(rng, mode):
    D = 10 ** 9
    if mode == 0:
        a, b = sorted([rng.randrange(D + 1), rng.randrange(D + 1)])
        return [Fr(a, D), Fr(b - a, D), Fr(D - b, D)]
    if mode == 1:  # near uniform, at scale 10^-k
        k = rng.randrange(1, 7)
        e = [rng.randrange(-1000, 1001) for _ in range(2)]
        e.append(-e[0] - e[1])
        s = Fr(1, 4000 * 10 ** k)
        return [Fr(1, 3) + s * t for t in e]
    if mode == 2:  # near a vertex
        k = rng.randrange(1, 9); s = Fr(1, 10 ** k); a = Fr(rng.randrange(1001), 1000)
        p = [1 - s, s * a, s * (1 - a)]
    else:          # near an edge
        k = rng.randrange(1, 9); s = Fr(1, 10 ** k); a = Fr(rng.randrange(1001), 1000)
        p = [a * (1 - s), (1 - a) * (1 - s), s]
    rng.shuffle(p)
    return p

def main(n):
    rng = random.Random(20261110)
    worstA = worstB = None
    bad = 0
    for k in range(n):
        p = simplex(rng, rng.randrange(4)); r = simplex(rng, rng.randrange(4))
        assert sum(p) == 1 and sum(r) == 1 and min(p) >= 0 and min(r) >= 0
        Hp, Fp, Gp, xp = HFG(p); Hr, Fq, Gr, xr = HFG(r)
        bx, bh = brackets(p, r)
        slackA = (xp + xr - Hp * Fq - Fp * Hr - xp * xr / 1000) - bx
        slackB = bh - (Hp * Gr + Gp * Hr + xp * xr / 1000)
        if slackA < 0 or slackB < 0:
            bad += 1
            print("VIOLATION", [str(t) for t in p], [str(t) for t in r], float(slackA), float(slackB))
        sc = xp * xr
        if sc > 0:
            a, b = slackA / sc, slackB / sc
            if worstA is None or a < worstA[0]: worstA = (a, p, r)
            if worstB is None or b < worstB[0]: worstB = (b, p, r)
    print("samples", n, "violations", bad)
    for name, w in (("(3.3)", worstA), ("(3.4)", worstB)):
        print("min slack%s/(x x') = %.6g at p=%s r=%s" % (name, float(w[0]), [float(t) for t in w[1]], [float(t) for t in w[2]]))

if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 40000)
