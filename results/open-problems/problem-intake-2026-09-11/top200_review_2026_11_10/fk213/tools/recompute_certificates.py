"""Recompute the two coefficient arrays T_A and T_B of the three-state pair inequalities from their definitions,
with python-flint polynomials over Q, and count the signs of the coefficients.

Ordered posteriors are p = a e + b v + c u and q = d e + f v + g u with e = (1,0,0), v = (1/2,1/2,0),
u = (1/3,1/3,1/3). Everything is homogenised with s = a+b+c and t = d+f+g, which equal 1 on the domain.

    T_A = 6 D_A K_A - sum_sigma X_sigma prod_{tau != sigma} Z_tau,          bidegree (10,10)
    T_B = 6 D_B K_B + sum_sigma N_sigma prod_{tau != sigma} Z_tau^3,        bidegree (22,22)

A polynomial whose monomial coefficients in (a,b,c,d,f,g) are all nonnegative is nonnegative on the domain."""
import itertools, sys, time
from fractions import Fraction
from flint import fmpq_mpoly_ctx, fmpq, Ordering

ctx = fmpq_mpoly_ctx.get(["a", "b", "c", "d", "f", "g"], Ordering.lex)
a, b, c, d, f, g = ctx.gens()
Q = lambda n, m=1: fmpq(n, m)

s = a + b + c
t = d + f + g
p = [a + b * Q(1, 2) + c * Q(1, 3), b * Q(1, 2) + c * Q(1, 3), c * Q(1, 3)]
q = [d + f * Q(1, 2) + g * Q(1, 3), f * Q(1, 2) + g * Q(1, 3), g * Q(1, 3)]

def scalars(v, w):
    """x (degree 2), y (degree 3), H (degree 4), F (degree 3), G (degree 2) of a point v with coordinate sum w."""
    cen = [3 * vi - w for vi in v]
    x = sum(ci ** 2 for ci in cen) * Q(1, 6)
    y = sum(ci ** 3 for ci in cen) * Q(1, 6)
    return x, y, y * w - x ** 2 * Q(1, 2), x * w * Q(3, 2) - y, w ** 2 - x

xp, yp, Hp, Fp, Gp = scalars(p, s)
xq, yq, Hq, Fq, Gq = scalars(q, t)

perms = list(itertools.permutations(range(3)))
Z, X, N = [], [], []
for pi in perms:
    U = [3 * p[i] * q[pi[i]] for i in range(3)]
    z = U[0] + U[1] + U[2]
    V = [3 * u - z for u in U]
    x = sum(v ** 2 for v in V) * Q(1, 6)
    y = sum(v ** 3 for v in V) * Q(1, 6)
    Z.append(z); X.append(x); N.append(y * z - x ** 2 * Q(1, 2))

def prod(lst):
    r = lst[0]
    for term in lst[1:]:
        r = r * term
    return r

def count(T, deg):
    pos = zero = neg = 0
    seen = 0
    for mon, coef in T.to_dict().items():
        assert sum(mon[:3]) == deg and sum(mon[3:]) == deg, mon
        seen += 1
        if coef > 0: pos += 1
        elif coef < 0: neg += 1
    nmon = ((deg + 2) * (deg + 1) // 2) ** 2
    zero = nmon - seen
    return nmon, pos, zero, neg

def spot(T, which, trials=12):
    """Compare T with the direct Bayes-fusion expression at exact rational points."""
    import random
    rng = random.Random(7)
    for _ in range(trials):
        w = [rng.randrange(1, 50) for _ in range(6)]
        A = [Fraction(w[0], sum(w[:3])), Fraction(w[1], sum(w[:3])), Fraction(w[2], sum(w[:3]))]
        B = [Fraction(w[3], sum(w[3:])), Fraction(w[4], sum(w[3:])), Fraction(w[5], sum(w[3:]))]
        P = [A[0] + A[1] / 2 + A[2] / 3, A[1] / 2 + A[2] / 3, A[2] / 3]
        R = [B[0] + B[1] / 2 + B[2] / 3, B[1] / 2 + B[2] / 3, B[2] / 3]
        def xy(v):
            cen = [3 * vi - 1 for vi in v]
            return sum(ci ** 2 for ci in cen) / 6, sum(ci ** 3 for ci in cen) / 6
        x1, y1 = xy(P); x2, y2 = xy(R)
        H1, F1, G1 = y1 - x1 ** 2 / 2, Fraction(3, 2) * x1 - y1, 1 - x1
        H2, F2, G2 = y2 - x2 ** 2 / 2, Fraction(3, 2) * x2 - y2, 1 - x2
        bx = bh = Fraction(0); D = Fraction(1)
        for pi in perms:
            U = [3 * P[i] * R[pi[i]] for i in range(3)]
            z = sum(U); post = [u / z for u in U]
            xx, yy = xy(post)
            bx += z * xx; bh += z * (yy - xx ** 2 / 2); D *= z
        if which == "A":
            direct = 6 * D * (x1 + x2 - H1 * F2 - F1 * H2 - x1 * x2 * EPSF - bx / 6)
        else:
            direct = 6 * D ** 3 * (bh / 6 - H1 * G2 - G1 * H2 - x1 * x2 * EPSF)
        val = T(*[fmpq(v.numerator, v.denominator) for v in A + B])
        assert Fraction(int(val.p), int(val.q)) == direct, (which, A, B)
    return trials

t0 = time.time()
import os
_e = os.environ.get("EPS", "1/1000").split("/")   # negative control: EPS=1/2 must produce negative coefficients
eps = Q(int(_e[0]), int(_e[1])); EPSF = Fraction(int(_e[0]), int(_e[1]))
# K_A homogenised to bidegree (4,4)
KA = xp * s ** 2 * t ** 4 + xq * s ** 4 * t ** 2 - Hp * Fq * t - Fp * s * Hq - eps * xp * xq * s ** 2 * t ** 2
DA = prod(Z)
TA = 6 * DA * KA - (s * t) ** 3 * sum(X[i] * prod([Z[j] for j in range(6) if j != i]) for i in range(6))
print("T_A (monomials, positive, zero, negative):", count(TA, 10), "spot checks equal:", spot(TA, "A"),
      "%.1fs" % (time.time() - t0), flush=True)

if len(sys.argv) > 1 and sys.argv[1] == "A":
    sys.exit(0)
t0 = time.time()
Z3 = [z ** 3 for z in Z]
KB = -Hp * Gq * t ** 2 - Gp * s ** 2 * Hq - eps * xp * xq * s ** 2 * t ** 2
DB = prod(Z3)
TB = 6 * DB * KB + (s * t) ** 3 * sum(N[i] * prod([Z3[j] for j in range(6) if j != i]) for i in range(6))
print("T_B (monomials, positive, zero, negative):", count(TB, 22), "spot checks equal:", spot(TB, "B"),
      "%.1fs" % (time.time() - t0), flush=True)
