from fractions import Fraction
from itertools import permutations

S4 = list(permutations(range(4)))
S3 = list(permutations(range(3)))
PAIR_REPS = [(0, 1), (0, 2), (0, 3)]
PAIR_CLASSES = [
    {frozenset((0, 1)), frozenset((2, 3))},
    {frozenset((0, 2)), frozenset((1, 3))},
    {frozenset((0, 3)), frozenset((1, 2))},
]


def pair_class(S):
    F = frozenset(S)
    for k, Cc in enumerate(PAIR_CLASSES):
        if F in Cc:
            return k
    raise AssertionError(F)


def rho(sig):
    return tuple(pair_class((sig[i], sig[j])) for i, j in PAIR_REPS)


# a=(-4-3i,i,-4+4i,-1+i), b=(-1+4i,-4+4i,i,3+i), eta=1.
C0 = Fraction(40)
C = [
    [Fraction(-87, 4), Fraction(84), Fraction(-1169, 4), Fraction(-47)],
    [Fraction(-423, 4), Fraction(-132), Fraction(639, 4), Fraction(-87)],
    [Fraction(92), Fraction(455, 4), Fraction(595, 2), Fraction(-349, 4)],
    [Fraction(-203, 2), Fraction(-679, 4), Fraction(128), Fraction(-91, 4)],
]
X = [
    [Fraction(-243), Fraction(24), Fraction(51)],
    [Fraction(-436), Fraction(-505), Fraction(-262)],
    [Fraction(-124), Fraction(-25), Fraction(2)],
]

c = {s: sum(C[i][s[i]] for i in range(4)) for s in S4}
x = {p: sum(X[i][p[i]] for i in range(3)) for p in S3}
endpoint = {s: c[s] + Fraction(1, 2) * x[rho(s)] for s in S4}

cs = sorted(c.items(), key=lambda kv: kv[1], reverse=True)
xs = sorted(x.items(), key=lambda kv: kv[1], reverse=True)
sigma0, cmax = cs[0]
beta = cs[0][1] - cs[1][1]
rho_c = rho(sigma0)
xmax = xs[0][1]
gamma = xs[0][1] - xs[1][1]
delta = xmax - x[rho_c]
M = max(endpoint.values())
kappa = cmax + Fraction(1, 2) * xmax - M

assert sigma0 == (1, 2, 0, 3)
assert rho_c == (2, 0, 1)
assert cmax == 313 and beta == 60
assert xmax == -362 and gamma == 48
assert x[rho_c] == -410 and delta == 48
assert M == 108 and kappa == 24
assert beta >= 2 * kappa
assert gamma < 6 * kappa

# Direct Gaussian-integer reconstruction of all 24 OM endpoint real parts.
a = [(-4, -3), (0, 1), (-4, 4), (-1, 1)]
b = [(-1, 4), (-4, 4), (0, 1), (3, 1)]


def gadd(z, w):
    return (z[0] + w[0], z[1] + w[1])


def gmul(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def gprod(zs):
    z = (1, 0)
    for w in zs:
        z = gmul(z, w)
    return z


for s in S4:
    direct_real = gprod([gadd(a[i], b[s[i]]) for i in range(4)])[0]
    assert C0 + endpoint[s] == direct_real

print("ONE_POINT_GAP_EXACT_CHECK=PASS")
print("sigma0=", sigma0, "rho_sigma0=", rho_c)
print("cmax=", cmax, "beta=", beta)
print("xmax=", xmax, "x_rho_sigma0=", x[rho_c], "delta=", delta)
print("gamma=", gamma, "M=", M, "kappa=", kappa)
print("beta_minus_2kappa=", beta - 2 * kappa)
print("gamma_minus_6kappa=", gamma - 6 * kappa)
print("full_support_endpoint_max=", C0 + M)
print("independent_assignment_upper=", C0 + cmax + Fraction(1, 2) * xmax)
