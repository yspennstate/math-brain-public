"""Exact checks for the finite part of the argument (Section 4 of the paper).

Everything is computed with Python fractions. E is the middle-thirds Cantor set, F its distribution function,
nu = dF the Cantor measure, I(n,k) = [k/2^n, (k+1)/2^n]. The base cell is D0 = I(7,4); its children are
I(8,8) (left) and I(8,9) (right).
"""
from fractions import Fraction as Fr
import math, sys

ONE_THIRD, TWO_THIRDS = Fr(1, 3), Fr(2, 3)

def in_E(x):
    """x in E, for rational x in [0,1]; the orbit of x under the two inverse branches is finite."""
    seen = set()
    while x not in seen:
        if ONE_THIRD < x < TWO_THIRDS:
            return False
        seen.add(x)
        x = 3 * x if x <= ONE_THIRD else 3 * x - 2
    return True

def F(x):
    """Cantor function at a rational x in [0,1], exactly: F(x) = acc + w F(T x) along the orbit."""
    if x <= 0: return Fr(0)
    if x >= 1: return Fr(1)
    acc, w, seen = Fr(0), Fr(1), {}
    while True:
        if ONE_THIRD <= x <= TWO_THIRDS:
            return acc + w / 2
        if x in seen:                       # periodic orbit: acc1 + w1 F(x) = acc + w F(x)
            acc1, w1 = seen[x]
            Fx = (acc - acc1) / (w1 - w)
            return acc1 + w1 * Fx
        seen[x] = (acc, w)
        if x < ONE_THIRD:
            x, w = 3 * x, w / 2
        else:
            x, acc, w = 3 * x - 2, acc + w / 2, w / 2

def nu(a, b): return F(b) - F(a)

def meets(a, b):
    """[a,b] meets E: an endpoint lies in E, or the open interval carries Cantor mass."""
    return in_E(a) or in_E(b) or nu(a, b) > 0

def I(n, k): return Fr(k, 2 ** n), Fr(k + 1, 2 ** n)

def children(n, k):
    return [(n + 1, c) for c in (2 * k, 2 * k + 1) if meets(*I(n + 1, c))]

def wired(n, k, R):
    """effective conductance from (n,k) to its descendants at distance R, wired together (unit conductances)"""
    if R == 0: return None                  # None = infinite conductance
    tot = Fr(0)
    for c in children(n, k):
        C = wired(*c, R - 1)
        tot += 1 if C is None else C / (1 + C)
    return tot

ok = True
def check(name, cond):
    global ok
    ok &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name)

# sanity of F and in_E
check("F(1/4) = 1/3, F(3/4) = 2/3, F(1/3) = 1/2", F(Fr(1, 4)) == Fr(1, 3) and F(Fr(3, 4)) == Fr(2, 3) and F(ONE_THIRD) == Fr(1, 2))
check("1/4, 3/4, 1/3, 2/9 in E; 1/2, 5/9 not in E", all(in_E(Fr(*t)) for t in [(1, 4), (3, 4), (1, 3), (2, 9)]) and not in_E(Fr(1, 2)) and not in_E(Fr(5, 9)))

# 1. the base scenery
a0, b0 = I(7, 4)
C0 = (Fr(8, 243), Fr(9, 243))
check("C0 = [8/243, 9/243] is the level-5 cylinder with digits 0,0,0,2,2", Fr(2, 81) + Fr(2, 243) == C0[0])
check("C0 lies in the interior of D0", a0 < C0[0] and C0[1] < b0)
check("previous level-5 cylinder [6/243,7/243] and next one [18/243,19/243] lie outside D0", Fr(7, 243) < a0 and Fr(18, 243) > b0)
u0, r0 = (C0[0] - a0) * 128, (C0[1] - C0[0]) * 128
check("u0 = 52/243, r0 = 128/243", (u0, r0) == (Fr(52, 243), Fr(128, 243)))
check("u0/r0 = 13/32 < 1", u0 / r0 == Fr(13, 32))
check("(1-u0-r0)/r0 = 63/128 < 9", (1 - u0 - r0) / r0 == Fr(63, 128))
check("(1/2-u0)/r0 = 139/256 in (1/3,2/3)", (Fr(1, 2) - u0) / r0 == Fr(139, 256) and ONE_THIRD < Fr(139, 256) < TWO_THIRDS)
check("nu(D0) = 1/32, nu(I(8,8)) = nu(I(8,9)) = 1/64", nu(a0, b0) == Fr(1, 32) and nu(*I(8, 8)) == Fr(1, 64) == nu(*I(8, 9)))

# 2. no dyadic point of relative level <= 7 in D0 (absolute denominator 2^14) lies in E
pts = [Fr(4 * 2 ** 7 + i, 2 ** 14) for i in range(2 ** 7 + 1)]
check(f"none of the {len(pts)} points j/2^14 in D0 lies in E", not any(in_E(x) for x in pts))
dy = [Fr(i, 2 ** 16) for i in range(2 ** 16 + 1) if in_E(Fr(i, 2 ** 16))]
check("the points i/2^16 of [0,1] in E are 0, 1/4, 3/4, 1", dy == [0, Fr(1, 4), Fr(3, 4), 1])

# 3. left branch: Cantor flow, energy of the first eight descendant levels, tail
m = nu(*I(8, 8))
E8 = sum((nu(*I(8 + r, c)) / m) ** 2 for r in range(1, 9) for c in range(8 * 2 ** r, 9 * 2 ** r))
check("energy of the first eight levels = 955961/524288", E8 == Fr(955961, 524288))
d = math.log(2) / math.log(3)
check("2^(-log_3 2) < 2/3  (float, margin %.4f)" % (2 / 3 - 2 ** -d), 2 ** -d < 2 / 3 - 0.02)
tail = 384 * Fr(2, 3) ** 17
check("384 (2/3)^17 = 16777216/43046721", tail == Fr(16777216, 43046721))
Estar = E8 + tail
check("E_* = 49947079476089/22568879259648", Estar == Fr(49947079476089, 22568879259648))
GL = 1 / (1 + Estar)
check("G_L >= 22568879259648/72515958735737", GL == Fr(22568879259648, 72515958735737))

# 4. right branch: wired at radius six below I(8,9)
C6 = wired(8, 9, 6)
check("radius-six wired conductance below I(8,9) = 13703/31620", C6 == Fr(13703, 31620))
GR = C6 / (1 + C6)
check("G_R <= 13703/45323", GR == Fr(13703, 45323))
p = GL / (GL + GR)
check("p >= 1022889314685026304/2016575497240830415 > 1/2", p == Fr(1022889314685026304, 2016575497240830415) and p > Fr(1, 2))
print("   p >= %.6f, eta at the base point >= %.6f" % (float(p), float(p - Fr(1, 2))))
# for orientation: radius-six wired value on the left and the dependence on the radius on the right
print("   left radius-six wired conductance (upper bound, not used):", float(wired(8, 8, 6)))
print("   right wired conductance at radii 6..9:", [round(float(wired(8, 9, R)), 6) for R in range(6, 10)])
print("ALL PASS" if ok else "SOME CHECK FAILED")
sys.exit(0 if ok else 1)
