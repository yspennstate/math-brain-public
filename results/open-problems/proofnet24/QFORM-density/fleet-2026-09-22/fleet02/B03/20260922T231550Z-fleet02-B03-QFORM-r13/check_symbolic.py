import itertools
import sympy as sp


def e3_cross(B):
    nr, nc = B.shape
    total = sp.Integer(0)
    for I in itertools.combinations(range(nr), 3):
        for J in itertools.combinations(range(nc), 3):
            total += B.extract(I, J).det() ** 2
    return sp.factor(sp.cancel(total))


# Exact D' witness: a five-row Parseval frame with leverage 3/5.
U = sp.Matrix([
    [
        1 / sp.sqrt(5),
        sp.sqrt(sp.Rational(2, 5)) * sp.cos(2 * sp.pi * k / 5),
        sp.sqrt(sp.Rational(2, 5)) * sp.sin(2 * sp.pi * k / 5),
    ]
    for k in range(5)
])
UTU = sp.simplify(sp.trigsimp(U.T * U))
lev = [sp.simplify(sp.trigsimp((U.row(k) * U.row(k).T)[0])) for k in range(5)]
A0 = sp.zeros(8)
A0[:5, 5:] = U
A0[5:, :5] = U.T
z = sp.symbols("z")
charpoly = sp.factor(A0.charpoly(z).as_expr())
C_Dprime = 10 * sp.sqrt(5 * sp.E / 6)

# Exact Walsh near-rank-three boundary family.
def sylvester8():
    H = sp.Matrix([[1]])
    while H.rows < 8:
        old = H
        H = old.row_join(old).col_join(old.row_join(-old))
    return H


H = sylvester8()
R = H[:, :3] / sp.sqrt(8)
P = sp.simplify(R * R.T)
t = sp.symbols("t", positive=True)
At = t * sp.eye(8) + (1 - t) * P
d = sp.factor(At[0, 0])
rest = list(range(1, 8))
Sch = sp.simplify(
    At.extract(rest, rest)
    - At.extract(rest, [0]) * At.extract([0], rest) / d
)

# Enumerate every ordered residual binary cut L|R with |L|,|R| >= 3.
F = sp.factor(t**2 * (1 - t) ** 6 * (5 * t + 3) ** 4 / 2**20)
ratios = set()
best = None
for assignment in itertools.product(range(3), repeat=7):
    # 0 = unused, 1 = L, 2 = R.
    L = [i for i, a in enumerate(assignment) if a == 1]
    RR = [i for i, a in enumerate(assignment) if a == 2]
    if len(L) < 3 or len(RR) < 3:
        continue
    E3 = e3_cross(Sch.extract(L, RR))
    cert = sp.factor(sp.cancel(d**6 * E3))
    ratio = sp.Integer(0) if E3 == 0 else sp.factor(sp.cancel(cert / F))
    ratios.add(ratio)
    if best is None or float(ratio) > float(best[-1]):
        best = (L, RR, E3, cert, ratio)

# Original-matrix overlap-one four-by-four minor bank at pivot 0.
M = sp.Integer(0)
for I in itertools.combinations(rest, 3):
    remainder = [x for x in rest if x not in I]
    for J in itertools.combinations(remainder, 3):
        M += At.extract((0,) + I, (0,) + J).det() ** 2
M = sp.factor(sp.cancel(M))
M_expected = sp.Rational(7, 128) * t**2 * (1 - t) ** 6

C3 = sp.sqrt(sp.E) / 6 * sp.beta(sp.Rational(1, 12), sp.Rational(1, 24))
partner_asym = sp.N(C3 * (sp.Rational(81, 2**20)) ** (-sp.Rational(1, 12)), 18)
transducer_asym = sp.N(
    sp.sqrt(2)
    * C3
    * (sp.Rational(3, 8)) ** (-sp.Rational(1, 3))
    * (sp.Rational(7, 128)) ** (-sp.Rational(1, 12)),
    18,
)

assert UTU == sp.eye(3)
assert lev == [sp.Rational(3, 5)] * 5
assert sp.expand(charpoly - z**2 * (z - 1) ** 3 * (z + 1) ** 3) == 0
assert sp.simplify(P * P - P) == sp.zeros(8)
assert [P[i, i] for i in range(8)] == [sp.Rational(3, 8)] * 8
assert ratios == {sp.Integer(0), sp.Rational(1, 4), sp.Rational(1, 2), sp.Integer(1)}
assert sp.simplify(M - M_expected) == 0

print("DPRIME_UTU=" + str(UTU))
print("DPRIME_ROW_LEVERAGES=" + str(lev))
print("DPRIME_CHARPOLY=" + str(charpoly))
print("DPRIME_CONSTANT=" + str(sp.N(C_Dprime, 18)))
print("WALSH_P_DIAG=" + str([P[i, i] for i in range(8)]))
print("WALSH_IDEMPOTENT=True")
print("WALSH_PIVOT_d=" + str(d))
print("WALSH_CERT_RATIOS=" + str(sorted(ratios, key=lambda x: float(x))))
print("WALSH_MAX_LOCAL_SETS=" + str(best[0]) + "|" + str(best[1]))
print(
    "WALSH_MAX_ORIGINAL_SETS="
    + str([rest[i] for i in best[0]])
    + "|"
    + str([rest[i] for i in best[1]])
)
print("WALSH_BEST_E3=" + str(sp.factor(best[2])))
print("WALSH_F=" + str(F))
print("WALSH_M_i=" + str(M))
print("C3=" + str(sp.N(C3, 18)))
print("PARTNER_BEST_ASYM_COEFF=" + str(partner_asym))
print("RANDOMCUT_TRANSDUCER_ASYM_COEFF=" + str(transducer_asym))
print("STATUS=PASS")
