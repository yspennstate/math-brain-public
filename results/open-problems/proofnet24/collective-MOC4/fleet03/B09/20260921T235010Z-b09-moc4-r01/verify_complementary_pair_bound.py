from fractions import Fraction
from itertools import combinations, permutations

N = 4
SUBS = list(combinations(range(N), 2))
IDX = {s: i for i, s in enumerate(SUBS)}
PERMS4 = list(permutations(range(N)))
PAIR_CLASSES = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]
REPS = [x[0] for x in PAIR_CLASSES]


def comp(s):
    ss = set(s)
    return tuple(i for i in range(N) if i not in ss)


def prod(v, inds):
    out = Fraction(1)
    for i in inds:
        out *= v[i]
    return out


def det2(U, S, T):
    i, j = S
    k, l = T
    return U[i][k] * U[j][l] - U[i][l] * U[j][k]


def det4(M):
    ans = Fraction(0)
    for p in PERMS4:
        inv = sum(p[i] > p[j] for i in range(N) for j in range(i + 1, N))
        term = Fraction(-1 if inv % 2 else 1)
        for i in range(N):
            term *= M[i][p[i]]
        ans += term
    return ans


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))]
            for i in range(len(A))]


def tr(A):
    return [list(x) for x in zip(*A)]


def induced_pair_data(p):
    rho = [-1] * 3
    eps = [0] * 3
    for a, S in enumerate(REPS):
        image = tuple(sorted(p[i] for i in S))
        for b, (T, Tc) in enumerate(PAIR_CLASSES):
            if image == T:
                rho[a], eps[a] = b, 1
                break
            if image == Tc:
                rho[a], eps[a] = b, -1
                break
        assert rho[a] >= 0
    return tuple(rho), tuple(eps)


# Exact finite S4 fact used in the proof: for every quotient matching rho,
# exactly four lifts occur, and their three orientation signs have even parity.
lifts = {}
for p in PERMS4:
    rho, eps = induced_pair_data(p)
    assert eps[0] * eps[1] * eps[2] == 1
    lifts.setdefault(rho, set()).add(eps)
assert len(lifts) == 6
EVEN = {(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)}
for rho in permutations(range(3)):
    assert lifts[rho] == EVEN


# Rational orthogonal peer matrix from fleet04/B09.
U = [
    [Fraction(492, 625), Fraction(-31, 625), Fraction(-48, 125), Fraction(12, 25)],
    [Fraction(-9, 25), Fraction(12, 25), Fraction(-4, 5), Fraction(0)],
    [Fraction(-36, 125), Fraction(48, 125), Fraction(9, 25), Fraction(4, 5)],
    [Fraction(-256, 625), Fraction(-492, 625), Fraction(-36, 125), Fraction(9, 25)],
]
I = mm(U, tr(U))
assert I == [[Fraction(int(i == j)) for j in range(N)] for i in range(N)]

Q = [[det2(U, S, T) ** 2 for T in SUBS] for S in SUBS]
for S in SUBS:
    for T in SUBS:
        assert Q[IDX[S]][IDX[T]] == Q[IDX[comp(S)]][IDX[comp(T)]]
for row in Q:
    assert sum(row) == 1
for j in range(6):
    assert sum(Q[i][j] for i in range(6)) == 1

# Build R,D and verify the 3x3 transport claims.
R = [[Fraction(0) for _ in range(3)] for _ in range(3)]
D = [[Fraction(0) for _ in range(3)] for _ in range(3)]
for a, S in enumerate(REPS):
    for b, T in enumerate(REPS):
        q_plus = Q[IDX[S]][IDX[T]]
        q_minus = Q[IDX[S]][IDX[comp(T)]]
        R[a][b] = q_plus + q_minus
        D[a][b] = q_plus - q_minus
        assert abs(D[a][b]) <= R[a][b]
for row in R:
    assert sum(row) == 1
for j in range(3):
    assert sum(R[i][j] for i in range(3)) == 1

# Exact spectrum example from the report.
a = [Fraction(1), Fraction(2), Fraction(3), Fraction(7)]
b = [Fraction(5), Fraction(2), Fraction(2), Fraction(3)]

Aplus, Aminus, Bplus, Bminus = [], [], [], []
for S, Sc in PAIR_CLASSES:
    x, y = prod(a, Sc), prod(a, S)
    u, v = prod(b, S), prod(b, Sc)
    Aplus.append(x + y)
    Aminus.append(x - y)
    Bplus.append(u + v)
    Bminus.append(u - v)

# Direct L2 and block formula (eta=1, hence all support quantities are rational real).
L2_direct = Fraction(0)
for i, S in enumerate(SUBS):
    for j, T in enumerate(SUBS):
        L2_direct += prod(a, comp(S)) * prod(b, T) * Q[i][j]

L2_block = Fraction(0)
for aa in range(3):
    for bb in range(3):
        L2_block += Fraction(1, 2) * (
            R[aa][bb] * Aplus[aa] * Bplus[bb]
            + D[aa][bb] * Aminus[aa] * Bminus[bb]
        )
assert L2_direct == L2_block


def middle_perm(p):
    val = Fraction(0)
    for S in SUBS:
        T = tuple(sorted(p[i] for i in S))
        val += prod(a, comp(S)) * prod(b, T)
    return val

best_perm_middle = max(middle_perm(p) for p in PERMS4)

# Eq. (15): quotient-matching relaxed bound plus exact parity defect.
best_sharp_rhs = None
coarse_delta = Fraction(0)
for rho in permutations(range(3)):
    xs = [Aplus[i] * Bplus[rho[i]] for i in range(3)]
    ys = [Aminus[i] * Bminus[rho[i]] for i in range(3)]
    parity_product = ys[0] * ys[1] * ys[2]
    delta = Fraction(0) if parity_product >= 0 else min(abs(y) for y in ys)
    coarse_delta = max(coarse_delta, delta)
    even_best = max(sum(eps[i] * ys[i] for i in range(3)) for eps in EVEN)
    Hperm = Fraction(1, 2) * (sum(xs) + even_best)
    rhs = Hperm + delta
    best_sharp_rhs = rhs if best_sharp_rhs is None else max(best_sharp_rhs, rhs)

assert L2_direct <= best_sharp_rhs
assert L2_direct <= best_perm_middle + coarse_delta
assert L2_direct == Fraction(193455501, 390625)
assert best_perm_middle == 583
assert best_sharp_rhs == 587
assert coarse_delta == 11

# Check the 1+3 paired formula and full determinant layer reconstruction.
P = [[u * u for u in row] for row in U]
L13 = Fraction(0)
for i in range(4):
    for j in range(4):
        L13 += P[i][j] * (prod(a, comp((i,))) * b[j] + a[i] * prod(b, comp((j,))))

endpoint = prod(a, tuple(range(4))) + prod(b, tuple(range(4)))
Bdiag = [[b[i] if i == j else Fraction(0) for j in range(4)] for i in range(4)]
Brot = mm(mm(U, Bdiag), tr(U))
M = [[Brot[i][j] + (a[i] if i == j else Fraction(0)) for j in range(4)] for i in range(4)]
full_det = det4(M)
assert endpoint + L13 + L2_direct == full_det
assert full_det == Fraction(18646794, 15625)

print("PASS")
print("L2=", L2_direct)
print("best_S4_middle=", best_perm_middle)
print("sharp_complement_pair_bound=", best_sharp_rhs)
print("coarse_parity_defect=", coarse_delta)
print("full_det=", full_det)
