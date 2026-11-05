"""T067 review: independent replay of the three-state certificates (agent H, 3 Nov 2026).

Built only from the definitions printed in paper/sections/certificate_appendix.tex (Sec. A.2),
not from the package's C++ programs:
 1. expand P_A (bidegree 10,10) and P_B (22,22) in the six barycentric variables a..f with exact
    integers (own sparse polynomial arithmetic), count positive / zero / negative coefficients;
 2. check the clearing identity P = c S^4 T^4 D R at random exact rational points, with R_A, R_B
    computed directly from the posterior-level definitions (x, y, H, F, G, z_pi, r_pi);
 3. compare the expanded coefficients with the package's tables q3_independent_coefficients_{A,B}.tsv
    up to one positive scalar per certificate (their column may be a Bernstein-normalized form, so
    the comparison also tries division by the multinomial weights).
Usage: python t067_q3_replay.py <dir holding the two tsv files>
Output: t067_q3_replay.json beside this file.
"""
import itertools
import json
import os
import random
import sys
import time
from fractions import Fraction as Fr
from math import factorial

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "t067_q3_replay.json")

# ---- sparse polynomials in 6 variables: dict exponent-tuple -> int ----
def padd(*ps):
    r = {}
    for p in ps:
        for k, v in p.items():
            r[k] = r.get(k, 0) + v
    return {k: v for k, v in r.items() if v}


def pscale(p, c):
    return {k: v * c for k, v in p.items()} if c else {}


def pmul(p, q):
    r = {}
    for k1, v1 in p.items():
        for k2, v2 in q.items():
            k = (k1[0] + k2[0], k1[1] + k2[1], k1[2] + k2[2], k1[3] + k2[3], k1[4] + k2[4], k1[5] + k2[5])
            r[k] = r.get(k, 0) + v1 * v2
    return {k: v for k, v in r.items() if v}


def ppow(p, n):
    r = {(0,) * 6: 1}
    for _ in range(n):
        r = pmul(r, p)
    return r


def var(i):
    e = [0] * 6
    e[i] = 1
    return {tuple(e): 1}


def const(c):
    return {(0,) * 6: c} if c else {}


a, b, c, d, e, f = (var(i) for i in range(6))


def lin(*terms):  # terms: (coef, poly)
    return padd(*[pscale(p, k) for k, p in terms])


def side(u, v, w):
    S = padd(u, v, w)
    X = lin((4, pmul(u, u)), (2, pmul(u, v)), (1, pmul(v, v)))
    Y = lin((8, ppow(u, 3)), (6, pmul(pmul(u, u), v)), (-3, pmul(u, pmul(v, v))), (-1, ppow(v, 3)))
    Hh = padd(pscale(pmul(Y, S), 4), pscale(pmul(X, X), -1))
    Fh = padd(pscale(pmul(X, S), 3), pscale(Y, -1))
    Gh = padd(pscale(pmul(S, S), 4), pscale(X, -1))
    P = [lin((6, u), (3, v), (2, w)), lin((3, v), (2, w)), lin((2, w),)]
    return S, X, Y, Hh, Fh, Gh, P


def build():
    S, X, Y, Hh, Fh, Gh, P = side(a, b, c)
    T, Xp, Yp, Hhp, Fhp, Ghp, Q = side(d, e, f)
    Zs, Vs, Js = [], [], []
    for pi in itertools.permutations(range(3)):
        U = [pmul(P[i], Q[pi[i]]) for i in range(3)]
        Z = padd(*U)
        W = [padd(pscale(U[i], 3), pscale(Z, -1)) for i in range(3)]
        V = padd(*[pmul(w, w) for w in W])
        J = padd(pscale(pmul(Z, pmul(W[0], pmul(W[1], W[2]))), 36), pscale(pmul(V, V), -1))
        Zs.append(Z); Vs.append(V); Js.append(J)
    S2, T2 = pmul(S, S), pmul(T, T)
    S4, T4 = pmul(S2, S2), pmul(T2, T2)
    KA = padd(pscale(padd(pmul(X, pmul(S2, T4)), pmul(Xp, pmul(S4, T2))), 8000),
              pscale(padd(pmul(Hh, pmul(Fhp, T)), pmul(Fh, pmul(Hhp, S))), -125),
              pscale(pmul(pmul(X, Xp), pmul(S2, T2)), -2))
    KB = padd(pscale(padd(pmul(Hh, pmul(Ghp, T2)), pmul(Gh, pmul(Hhp, S2))), -125),
              pscale(pmul(pmul(X, Xp), pmul(S2, T2)), -1))
    S3T3 = pmul(pmul(S2, S), pmul(T2, T))
    DA = const(1)
    for z in Zs:
        DA = pmul(DA, z)
    sumA = {}
    for j in range(6):
        rest = const(1)
        for l in range(6):
            if l != j:
                rest = pmul(rest, Zs[l])
        sumA = padd(sumA, pmul(Vs[j], rest))
    PA = padd(pscale(pmul(KA, DA), 27), pscale(pmul(S3T3, sumA), -2000))
    Z3 = [ppow(z, 3) for z in Zs]
    DB = const(1)
    for z in Z3:
        DB = pmul(DB, z)
    sumB = {}
    for j in range(6):
        rest = const(1)
        for l in range(6):
            if l != j:
                rest = pmul(rest, Z3[l])
        sumB = padd(sumB, pmul(Js[j], rest))
    PB = padd(pscale(pmul(KB, DB), 81), pscale(pmul(S3T3, sumB), 250))
    return PA, PB, DA, DB


def peval(p, pt):
    tot = Fr(0)
    for k, v in p.items():
        t = Fr(v)
        for i in range(6):
            if k[i]:
                t *= pt[i] ** k[i]
        tot += t
    return tot


# ---- residuals straight from the posterior definitions ----
def xs(p):
    return sum((3 * pi - 1) ** 2 for pi in p) / 6


def ys(p):
    return sum((3 * pi - 1) ** 3 for pi in p) / 6


def HFG(p):
    x, y = xs(p), ys(p)
    return y - x * x / 2, Fr(3, 2) * x - y, 1 - x


def residuals(p, q):
    eps = Fr(1, 1000)
    Hp, Fp, Gp = HFG(p)
    Hq, Fq, Gq = HFG(q)
    fx, fH = Fr(0), Fr(0)
    for pi in itertools.permutations(range(3)):
        z = 3 * sum(p[i] * q[pi[i]] for i in range(3))
        r = [3 * p[i] * q[pi[i]] / z for i in range(3)]
        fx += z * xs(r)
        fH += z * HFG(r)[0]
    RA = xs(p) + xs(q) - fx / 6 - Hp * Fq - Fp * Hq - eps * xs(p) * xs(q)
    RB = fH / 6 - Hp * Gq - Gp * Hq - eps * xs(p) * xs(q)
    return RA, RB


def signs(p):
    pos = sum(1 for v in p.values() if v > 0)
    neg = sum(1 for v in p.values() if v < 0)
    return pos, neg


def read_tsv(path):
    m = {}
    with open(path) as fh:
        next(fh)
        for line in fh:
            t = line.split()
            m[tuple(int(x) for x in t[:6])] = int(t[6])
    return m


def multi(k):
    return (factorial(k[0] + k[1] + k[2]) // (factorial(k[0]) * factorial(k[1]) * factorial(k[2]))) * \
           (factorial(k[3] + k[4] + k[5]) // (factorial(k[3]) * factorial(k[4]) * factorial(k[5])))


def compare(mine, theirs):
    out = {"their_positions": len(theirs),
           "their_pos": sum(1 for v in theirs.values() if v > 0),
           "their_zero": sum(1 for v in theirs.values() if v == 0),
           "their_neg": sum(1 for v in theirs.values() if v < 0)}
    for label, g in (("raw", lambda k, v: Fr(v)), ("div_multinomial", lambda k, v: Fr(v, multi(k)))):
        ratio, ok = None, True
        for k, tv in theirs.items():
            mv = g(k, mine.get(k, 0))
            if tv == 0 or mv == 0:
                if (tv == 0) != (mv == 0):
                    ok = False
                    break
                continue
            rr = mv / tv
            if ratio is None:
                ratio = rr
            elif rr != ratio:
                ok = False
                break
        extra = [k for k in mine if k not in theirs]
        out[label] = {"proportional": ok and not extra, "ratio": str(ratio), "my_keys_not_in_table": len(extra)}
    return out


def main():
    tdir = sys.argv[1]
    t0 = time.time()
    PA, PB, DA, DB = build()
    res = {"build_seconds": time.time() - t0}
    for name, P, deg in (("A", PA, 10), ("B", PB, 22)):
        degs = {(sum(k[:3]), sum(k[3:])) for k in P}
        pos, neg = signs(P)
        npos = (deg + 2) * (deg + 1) // 2
        res[name] = {"bidegrees": sorted(degs), "nonzero": len(P), "positive": pos, "negative": neg,
                     "positions": npos * npos, "zero": npos * npos - len(P)}
    # identity check at random exact rational points (interior)
    rnd = random.Random(20261103)
    worst = []
    for _ in range(12):
        pt = [Fr(rnd.randint(1, 50), rnd.randint(1, 50)) for _ in range(6)]
        S = sum(pt[:3]); T = sum(pt[3:])
        p = [(6 * pt[0] + 3 * pt[1] + 2 * pt[2]) / (6 * S), (3 * pt[1] + 2 * pt[2]) / (6 * S), 2 * pt[2] / (6 * S)]
        q = [(6 * pt[3] + 3 * pt[4] + 2 * pt[5]) / (6 * T), (3 * pt[4] + 2 * pt[5]) / (6 * T), 2 * pt[5] / (6 * T)]
        RA, RB = residuals(p, q)
        lhsA, lhsB = peval(PA, pt), peval(PB, pt)
        rhsA = 864000 * S ** 4 * T ** 4 * peval(DA, pt) * RA
        rhsB = 1296000 * S ** 4 * T ** 4 * peval(DB, pt) * RB
        worst.append({"A_identity": lhsA == rhsA, "B_identity": lhsB == rhsB,
                      "RA": float(RA), "RB": float(RB)})
    res["identity_points"] = worst
    res["identity_all_exact"] = all(w["A_identity"] and w["B_identity"] for w in worst)
    res["compare_A"] = compare(PA, read_tsv(os.path.join(tdir, "q3_independent_coefficients_A.tsv")))
    res["compare_B"] = compare(PB, read_tsv(os.path.join(tdir, "q3_independent_coefficients_B.tsv")))
    res["total_seconds"] = time.time() - t0
    json.dump(res, open(OUT, "w"), indent=1)
    print(json.dumps({k: v for k, v in res.items() if k != "identity_points"}, indent=1))


if __name__ == "__main__":
    main()
