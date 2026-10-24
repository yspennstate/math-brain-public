from fractions import Fraction as F

# HARD7-06 exact self-check for the boundary-semigroup route.
# This checks finite polynomial identities exactly and a current-degree
# quantitative anchor. The analytic support/concavity theorems are proved
# in the run report; this file is a self-check, not an independent audit.

# ---------- tiny exact polynomial algebra ----------
def poly_const(nvars, c):
    return {(0,) * nvars: F(c)}

def poly_var(nvars, i):
    e = [0] * nvars
    e[i] = 1
    return {tuple(e): F(1)}

def poly_add(*ps):
    out = {}
    for p in ps:
        for e, c in p.items():
            out[e] = out.get(e, F(0)) + c
            if out[e] == 0:
                del out[e]
    return out

def poly_scale(c, p):
    c = F(c)
    return {e: c * v for e, v in p.items() if c * v}

def poly_sub(p, q):
    return poly_add(p, poly_scale(-1, q))

def poly_mul(p, q):
    out = {}
    for e, c in p.items():
        for f, d in q.items():
            g = tuple(e[i] + f[i] for i in range(len(e)))
            out[g] = out.get(g, F(0)) + c * d
            if out[g] == 0:
                del out[g]
    return out

# ---------- exactly two messages: R({s,t}) = 2 s t ----------
nv = 2
one = poly_const(nv, 1)
s, t = poly_var(nv, 0), poly_var(nv, 1)
A = poly_mul(poly_sub(one, s), poly_sub(one, t))
B = poly_mul(poly_sub(one, poly_scale(2, s)),
             poly_sub(one, poly_scale(2, t)))
C = poly_mul(poly_sub(one, poly_scale(3, s)),
             poly_sub(one, poly_scale(3, t)))
N = poly_add(A, poly_scale(-2, B), C)
D = poly_add(poly_scale(3, A), poly_scale(-3, B), C)
assert N == poly_scale(2, poly_mul(s, t))
assert D == one

# ---------- insertion cross-difference ----------
# Generic background products A,B,C and inserted message u.
nv = 4
one = poly_const(nv, 1)
A, B, C, u = [poly_var(nv, i) for i in range(4)]
N = poly_add(A, poly_scale(-2, B), C)
D = poly_add(poly_scale(3, A), poly_scale(-3, B), C)
Ap = poly_mul(poly_sub(one, u), A)
Bp = poly_mul(poly_sub(one, poly_scale(2, u)), B)
Cp = poly_mul(poly_sub(one, poly_scale(3, u)), C)
Np = poly_add(Ap, poly_scale(-2, Bp), Cp)
Dp = poly_add(poly_scale(3, Ap), poly_scale(-3, Bp), Cp)
cross = poly_sub(poly_mul(Np, D), poly_mul(N, Dp))
target = poly_mul(
    u,
    poly_add(poly_scale(3, poly_mul(A, B)),
             poly_scale(-4, poly_mul(A, C)),
             poly_mul(B, C))
)
assert cross == target

# Strict upper endpoint identity D - 3N = 3B - 2C.
assert poly_sub(D, poly_scale(3, N)) == poly_add(poly_scale(3, B), poly_scale(-2, C))

# ---------- current-degree quantitative anchor ----------
d = F(46865076260769, 10**13)
tau = F(1, 1) / (3 * d * d)

def r_n(n, x):
    a = (1 - x) ** n
    b = (1 - 2 * x) ** n
    c = (1 - 3 * x) ** n
    return (a - 2 * b + c) / (3 * a - 3 * b + c)

r200 = r_n(200, tau)
r400 = r_n(400, tau)
r800 = r_n(800, tau)

assert r200 > F(159, 500)     # > 0.318
assert r400 > F(33, 100)      # > 0.33
assert r800 > F(333, 1000)    # > 0.333
assert r200 < r400 < r800 < F(1, 3)

print("TWO_INPUT_NUMERATOR_EQUALS_2ST = True")
print("TWO_INPUT_DENOMINATOR_EQUALS_1 = True")
print("INSERTION_CROSS_FACTOR_IDENTITY = True")
print("STRICT_ENDPOINT_IDENTITY_D_MINUS_3N = 3B_MINUS_2C")
print("d_cert = %.13f" % float(d))
print("tau = %.18e" % float(tau))
print("r_200(tau) = %.18f" % float(r200))
print("r_400(tau) = %.18f" % float(r400))
print("r_800(tau) = %.18f" % float(r800))
print("r_200 > 0.318 =", r200 > F(159, 500))
print("r_400 > 0.33 =", r400 > F(33, 100))
print("r_800 > 0.333 =", r800 > F(333, 1000))
print("ALL_EXACT_CHECKS_PASS = True")
