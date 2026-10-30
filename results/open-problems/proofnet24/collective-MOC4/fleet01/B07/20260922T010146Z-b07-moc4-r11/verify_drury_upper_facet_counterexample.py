from fractions import Fraction as F
from itertools import permutations


def c(re=0, im=0):
    return (F(re), F(im))


def add(z, w):
    return (z[0] + w[0], z[1] + w[1])


def mul(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def scale(q, z):
    return (q * z[0], q * z[1])


def prod(vals):
    z = c(1, 0)
    for x in vals:
        z = mul(z, x)
    return z


def re_eta(eta, z):
    return eta[0] * z[0] - eta[1] * z[1]


def compose(p, q):
    # p o q
    return tuple(p[q[i]] for i in range(4))


def inverse(p):
    r = [0] * 4
    for i, j in enumerate(p):
        r[j] = i
    return tuple(r)


S4 = list(permutations(range(4)))
id4 = (0, 1, 2, 3)

# Simple nonzero Gaussian-integer spectra; all 16 pair sums are nonzero.
a = [c(2, -2), c(-1, 2), c(0, -3), c(1, -1)]
b = [c(2, 0), c(-1, 2), c(2, -3), c(-1, -3)]
assert len(set(a)) == 4 and len(set(b)) == 4
assert all(add(a[i], b[j]) != c(0, 0) for i in range(4) for j in range(4))


def vertex(sigma):
    return prod([add(a[i], b[sigma[i]]) for i in range(4)])


v = {sigma: vertex(sigma) for sigma in S4}
assert len(set(v.values())) == 24

# Drury lead's base exceptional functional:
# 3u(f)=f(2134)+f(3214)+f(1432)+f(4321)-f(1234).
base = [
    ((1, 0, 2, 3), F(1)),
    ((2, 1, 0, 3), F(1)),
    ((0, 3, 2, 1), F(1)),
    ((3, 2, 1, 0), F(1)),
    (id4, F(-1)),
]

# Use the valid left-right orbit representative rho1=rho2=(12).
t = (1, 0, 2, 3)
tinv = inverse(t)
terms = []
for sigma, coeff in base:
    image = compose(compose(t, sigma), tinv)
    terms.append((image, coeff))

# Exact orbit is +1324,+2134,+3412,+4231,-1234, all divided by 3.
expected = {
    (0, 2, 1, 3): F(1),
    (1, 0, 2, 3): F(1),
    (2, 3, 0, 1): F(1),
    (3, 1, 2, 0): F(1),
    id4: F(-1),
}
assert dict(terms) == expected

u_num = c(0, 0)
for sigma, coeff in terms:
    u_num = add(u_num, scale(coeff, v[sigma]))
u_point = scale(F(1, 3), u_num)
assert u_point == c(F(77, 3), F(88, 3))

# Support normal x -> 28 Re x + 71 Im x is eta=28-71 i in Re(eta z) convention.
eta = c(28, -71)
Fvals = {sigma: re_eta(eta, z) for sigma, z in v.items()}
M = max(Fvals.values())
maximizers = sorted([sigma for sigma, val in Fvals.items() if val == M])
assert M == F(2720)
assert maximizers == [(0, 2, 1, 3), (2, 0, 3, 1)]

uF = re_eta(eta, u_point)
assert uF == F(8404, 3)
assert uF - M == F(244, 3) > 0

# Directly verify the exceptional upper-facet inequality fails.
# Since u has real coefficients, u(F_{t,t}) = Re(eta * u_point).
assert uF > M

print("PASS")
print("a =", a)
print("b =", b)
print("orbit_terms =", terms)
print("u_point =", u_point)
print("eta =", eta)
print("M =", M)
print("maximizers =", maximizers)
print("u(F_tt) =", uF)
print("upper_facet_gap =", uF - M)
print("status = exact counterexample to MOC4-DRURY-UPPER-FACET-v1; not a counterexample to MOC4")
