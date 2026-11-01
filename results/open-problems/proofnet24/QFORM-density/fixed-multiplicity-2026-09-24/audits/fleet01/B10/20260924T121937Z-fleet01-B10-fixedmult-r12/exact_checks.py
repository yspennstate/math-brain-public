from fractions import Fraction as F
import json


def rank_q(M):
    A = [[F(x) for x in row] for row in M]
    m = len(A)
    n = len(A[0]) if m else 0
    r = 0
    for c in range(n):
        piv = next((i for i in range(r, m) if A[i][c] != 0), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        p = A[r][c]
        A[r] = [x / p for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] != 0:
                a = A[i][c]
                A[i] = [A[i][j] - a * A[r][j] for j in range(n)]
        r += 1
        if r == m:
            break
    return r


def det_q(M):
    A = [[F(x) for x in row] for row in M]
    n = len(A)
    d = F(1)
    for c in range(n):
        piv = next((i for i in range(c, n) if A[i][c] != 0), None)
        if piv is None:
            return F(0)
        if piv != c:
            A[c], A[piv] = A[piv], A[c]
            d = -d
        p = A[c][c]
        d *= p
        for i in range(c + 1, n):
            if A[i][c] != 0:
                a = A[i][c] / p
                for j in range(c + 1, n):
                    A[i][j] -= a * A[c][j]
                A[i][c] = F(0)
    return d


A0 = [
    [-3, 1, -3, -3],
    [1, -3, -3, -3],
    [-3, -3, 10, 9],
    [-3, -3, 9, 9],
]
D = [[0] * 4 for _ in range(4)]
D[2][2] = 1
R = [[F(A0[i][j]) - F(D[i][j]) for j in range(4)] for i in range(4)]
RLL = [[R[i][j] for j in [2, 3]] for i in [2, 3]]

C = [[0, 1], [1, 0]]
deleted = []
for i in range(2):
    for j in range(2):
        deleted.append(C[1 - i][1 - j])

q = F(6933, 10000)
term = F(1)
exp5 = F(1)
for k in range(1, 6):
    term = term * q / F(k)
    exp5 += term
constant_upper = F(2010) + F(4800) * q

result = {
    "rank_example": {
        "det_A0": str(det_q(A0)),
        "rank_A0": rank_q(A0),
        "rank_R": rank_q(R),
        "rank_R_LL": rank_q(RLL),
    },
    "singular_seed_extension": {
        "det_C": str(det_q(C)),
        "one_by_one_deleted_values": deleted,
        "nonsingular_deleted_count": sum(x != 0 for x in deleted),
    },
    "rational_slack": {
        "eta2_plus_eta_lt_1_over_49": F(101, 10000) < F(1, 49),
        "eps_max": str(F(1, 16)),
        "diag_lower": str(F(371, 400)),
        "off_single": str(F(23, 112)),
        "row_sum_r4": str(F(23, 28)),
        "dominance_slack": str(F(297, 2800)),
    },
    "constant_sharpening": {
        "q": str(q),
        "taylor_exp_q_through_5": str(exp5),
        "taylor_gt_2": exp5 > 2,
        "therefore_log2_lt_q": True,
        "upper_bound_2010_plus_1200_log16": str(constant_upper),
        "upper_bound_decimal": float(constant_upper),
        "strictly_below_5338": constant_upper < F(5338),
    },
}

print(json.dumps(result, indent=2))
