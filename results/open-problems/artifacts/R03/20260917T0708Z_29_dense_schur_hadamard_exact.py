from fractions import Fraction
from itertools import product
from math import comb


def det_q(M):
    A = [[Fraction(x) for x in row] for row in M]
    n = len(A)
    det = Fraction(1)
    for j in range(n):
        pivot = next((i for i in range(j, n) if A[i][j]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != j:
            A[j], A[pivot] = A[pivot], A[j]
            det = -det
        pv = A[j][j]
        det *= pv
        for k in range(j, n):
            A[j][k] /= pv
        for i in range(j + 1, n):
            f = A[i][j]
            if f:
                for k in range(j, n):
                    A[i][k] -= f * A[j][k]
    return det


def inv_q(M):
    n = len(M)
    A = [[Fraction(M[i][j]) for j in range(n)] + [Fraction(i == j) for j in range(n)] for i in range(n)]
    for j in range(n):
        pivot = next((i for i in range(j, n) if A[i][j]), None)
        if pivot is None:
            return None
        A[j], A[pivot] = A[pivot], A[j]
        pv = A[j][j]
        A[j] = [x / pv for x in A[j]]
        for i in range(n):
            if i == j:
                continue
            f = A[i][j]
            if f:
                A[i] = [A[i][k] - f * A[j][k] for k in range(2*n)]
    return [row[n:] for row in A]


def rank_q(M):
    if not M:
        return 0
    A = [[Fraction(x) for x in row] for row in M]
    m, n = len(A), len(A[0])
    r = 0
    for j in range(n):
        pivot = next((i for i in range(r, m) if A[i][j]), None)
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        pv = A[r][j]
        A[r] = [x / pv for x in A[r]]
        for i in range(m):
            if i != r and A[i][j]:
                f = A[i][j]
                A[i] = [A[i][k] - f * A[r][k] for k in range(n)]
        r += 1
        if r == m:
            break
    return r


def collision_free_binary(A):
    m = len(A)
    z = (0,) * m
    rows = [tuple(r) for r in A]
    cols = [tuple(A[i][j] for i in range(m)) for j in range(m)]
    return z not in rows and z not in cols and len(set(rows)) == m and len(set(cols)) == m


def cofactor_nonzero_count(M):
    n = len(M)
    out = 0
    for i in range(n):
        for j in range(n):
            minor = [[M[a][b] for b in range(n) if b != j] for a in range(n) if a != i]
            if det_q(minor):
                out += 1
    return out


def xi_sign(A):
    d = len(A)
    inv = inv_q(A)
    assert inv is not None
    sv = list(product((-1, 1), repeat=d))
    rows = [tuple(r) for r in A]
    cols = [tuple(A[i][j] for i in range(d)) for j in range(d)]
    forb_b = set(cols) | {tuple(-x for x in v) for v in cols}
    forb_c = set(rows) | {tuple(-x for x in v) for v in rows}
    total = 0
    by_b = {}
    for b in sv:
        if b in forb_b:
            continue
        y = [sum(inv[i][j] * b[j] for j in range(d)) for i in range(d)]
        cnt = 0
        for c in sv:
            if c in forb_c:
                continue
            t = sum(Fraction(c[i]) * y[i] for i in range(d))
            if t in (1, -1):
                cnt += 1
        if cnt:
            by_b[b] = cnt
            total += cnt
    return total, by_b


def sylvester(order_power):
    H = [[1]]
    for _ in range(order_power):
        H = [r + r for r in H] + [r + [-x for x in r] for r in H]
    return H


# A. Exact direct-sign Schur/cofactor identity check at sign order n=5.
n = 5
d = 4
sv = list(product((-1, 1), repeat=d))
sum_xi = 0
invertible_A = 0
for flat in product((-1, 1), repeat=d*d):
    A = [list(flat[i*d:(i+1)*d]) for i in range(d)]
    inv = inv_q(A)
    if inv is None:
        continue
    invertible_A += 1
    rows = [tuple(r) for r in A]
    cols = [tuple(A[i][j] for i in range(d)) for j in range(d)]
    forb_b = set(cols) | {tuple(-x for x in v) for v in cols}
    forb_c = set(rows) | {tuple(-x for x in v) for v in rows}
    for b in sv:
        if b in forb_b:
            continue
        y = [sum(inv[i][j] * b[j] for j in range(d)) for i in range(d)]
        for c in sv:
            if c in forb_c:
                continue
            t = sum(Fraction(c[i]) * y[i] for i in range(d))
            if t in (1, -1):
                sum_xi += 1

# Independently enumerate all dephased sign-equivalence classes via collision-free binary 4x4 matrices.
residual_classes = 0
weighted_classes = 0
min_cof = n*n
support_44 = 0
for flat in product((0, 1), repeat=d*d):
    A0 = [list(flat[i*d:(i+1)*d]) for i in range(d)]
    if not collision_free_binary(A0) or rank_q(A0) != d-1:
        continue
    residual_classes += 1
    C = [[1 - 2*A0[i][j] for j in range(d)] for i in range(d)]
    S = [[1] + [1]*d] + [[1] + C[i] for i in range(d)]
    cc = cofactor_nonzero_count(S)
    weighted_classes += cc
    min_cof = min(min_cof, cc)
    if cc == 16:
        support_44 += 1

switch_orbit = 2**(2*n - 1)
weighted_sign_total = weighted_classes * switch_orbit
assert invertible_A == 22272
assert sum_xi == 589824
assert residual_classes == 1800
assert weighted_classes == 28800
assert min_cof == 16
assert support_44 == 1800
assert n*n*sum_xi == weighted_sign_total

print('DIRECT_SIGN_SCHUR_N5')
print('invertible_sign_4x4_A =', invertible_A)
print('sum_Xi_pm_circ =', sum_xi)
print('dephased_collision_free_rank4_classes =', residual_classes)
print('weighted_cofactor_sum_dephased =', weighted_classes)
print('row_col_switch_orbit =', switch_orbit)
print('weighted_cofactor_sum_all_sign =', weighted_sign_total)
print('n^2 * sum_Xi =', n*n*sum_xi)
print('minimum_nonzero_cofactors =', min_cof)

# B. Hadamard-core obstruction at d=7 (Sylvester order 8).
H = sylvester(3)
A7 = [row[1:] for row in H[1:]]
d7 = 7
assert det_q(A7) == 512
assert [sum(r) for r in A7] == [-1]*d7
assert [sum(A7[i][j] for i in range(d7)) for j in range(d7)] == [-1]*d7
xi7, by_b7 = xi_sign(A7)
one = (1,)*d7
minus_one = (-1,)*d7
expected_per_constant_b = 2*comb(d7, (d7-1)//2) - 2*d7
assert expected_per_constant_b == 56
assert by_b7[one] == expected_per_constant_b
assert by_b7[minus_one] == expected_per_constant_b
assert xi7 == 5096

print('HADAMARD_CORE_D7')
print('det_core =', det_q(A7))
print('row_sums = -1 x', d7)
print('column_sums = -1 x', d7)
print('allowed_c_for_b=+1 =', by_b7[one])
print('allowed_c_for_b=-1 =', by_b7[minus_one])
print('Hadamard_lower_bound_from_two_b =', 2*expected_per_constant_b)
print('full_Xi_pm_circ_for_core =', xi7)
print('SELF-CHECK PASS')

# C. Bent-Walsh finite obstruction inside the JSS-unstructured sector at sign order n=16.
def walsh(k):
    vecs = list(product((0, 1), repeat=k))
    H = []
    for x in vecs:
        H.append([1 if sum(a*b for a, b in zip(x, z)) % 2 == 0 else -1 for z in vecs])
    return vecs, H


def is_cons_quarter_16(v):
    # Exact test for Cons(delta=1/4,rho=1/4) at n=16.
    # After normalization, 12 coordinates must fit in an interval of radius 1/16,
    # i.e. width 1/8. Before normalization: width^2 <= ||v||^2 / 64.
    assert len(v) == 16
    vals = sorted(Fraction(x) for x in v)
    norm2 = sum(x*x for x in vals)
    need = 12
    for i in range(16 - need + 1):
        width = vals[i + need - 1] - vals[i]
        if width*width <= norm2 / 64:
            return True
    return False

vecs, H16 = walsh(4)
A15 = [row[1:] for row in H16[1:]]
q = 16
d = 15
assert det_q(A15) == 268435456
assert [sum(r) for r in A15] == [-1]*d
assert [sum(A15[i][j] for i in range(d)) for j in range(d)] == [-1]*d
# Explicit quadratic bent sign b_x=(-1)^(x1 x2 + x3 x4), restricted to x != 0.
b15 = tuple(1 if (x[0]*x[1] + x[2]*x[3]) % 2 == 0 else -1 for x in vecs[1:])
cols15 = [tuple(A15[i][j] for i in range(d)) for j in range(d)]
rows15 = [tuple(r) for r in A15]
forb_b15 = set(cols15) | {tuple(-x for x in z) for z in cols15}
forb_c15 = set(rows15) | {tuple(-x for x in z) for z in rows15}
assert b15 not in forb_b15
sb = sum(b15)
Atb = [sum(A15[i][j]*b15[i] for i in range(d)) for j in range(d)]
y15 = [Fraction(Atb[j] - sb, q) for j in range(d)]  # A^{-1} b=(A^T-J)b/q
assert y15.count(Fraction(0)) == 9
assert y15.count(Fraction(-1, 2)) == 6
right_null = [-z for z in y15] + [Fraction(1)]
assert not is_cons_quarter_16(right_null)

raw_smallball = 0
allowed_smallball = 0
both_noncons = 0
for c in product((-1, 1), repeat=d):
    value = sum(Fraction(c[i]) * y15[i] for i in range(d))
    if value not in (1, -1):
        continue
    raw_smallball += 1
    if c in forb_c15:
        continue
    allowed_smallball += 1
    sc = sum(c)
    Ac = [sum(A15[i][j]*c[j] for j in range(d)) for i in range(d)]
    z = [Fraction(Ac[i] - sc, q) for i in range(d)]  # A^{-T} c=(A-J)c/q
    left_null = [-w for w in z] + [Fraction(1)]
    if not is_cons_quarter_16(left_null):
        both_noncons += 1

assert raw_smallball == 15360
assert allowed_smallball == 15330
assert both_noncons == 14622
print('BENT_WALSH_N16')
print('det_core_15 =', det_q(A15))
print('Ainv_b_values = 0 x 9, -1/2 x 6')
print('right_null_in_Cons(1/4,1/4) = False')
print('raw_c_with_cTAinvb=+-1 =', raw_smallball)
print('allowed_c_after_row_collision_deletion =', allowed_smallball)
print('allowed_c_with_both_null_directions_Noncons(1/4,1/4) =', both_noncons)
print('SELF-CHECK PASS BENT')
