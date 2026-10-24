from fractions import Fraction


def rank_q(M):
    A = [[Fraction(x) for x in row] for row in M]
    m = len(A); n = len(A[0]) if m else 0
    r = 0
    for c in range(n):
        p = next((i for i in range(r, m) if A[i][c] != 0), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        q = A[r][c]
        A[r] = [x / q for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] != 0:
                q = A[i][c]
                A[i] = [A[i][j] - q * A[r][j] for j in range(n)]
        r += 1
        if r == m:
            break
    return r


def det_q(M):
    A = [[Fraction(x) for x in row] for row in M]
    n = len(A); d = Fraction(1); sign = 1
    for c in range(n):
        p = next((i for i in range(c, n) if A[i][c] != 0), None)
        if p is None:
            return Fraction(0)
        if p != c:
            A[c], A[p] = A[p], A[c]; sign *= -1
        q = A[c][c]; d *= q
        for i in range(c + 1, n):
            if A[i][c] != 0:
                z = A[i][c] / q
                for j in range(c + 1, n):
                    A[i][j] -= z * A[c][j]
    return sign * d


# Exact arithmetic in the baseline 17-direction proof.
slack17 = Fraction(371,400) - 4*Fraction(23,112)
assert slack17 == Fraction(297,2800) and slack17 > 0

# Exact terminal r=4 slack if only sixteen directions are assumed.
slack16 = Fraction(371,400) - 3*Fraction(23,112)
assert slack16 == Fraction(109,350) and slack16 > 0

# Rigorous rational chain used in the B10 constant sharpening.
# Gamma(3/8) < 707/264; 2^(5/8)<25/16; pi^(-1/4)<61/80;
# e^(3/8)<3/2, hence the quarter-power coefficient C0 is below:
C0_upper = Fraction(25,16)*Fraction(61,80)*Fraction(3,2)*Fraction(707,264)
assert C0_upper == Fraction(215635,45056)
assert C0_upper < Fraction(24,5)
# e^(8/5) > its degree-4 Taylor lower sum = 9067/1875 > 24/5.
exp_8_5_lower = sum(Fraction(8,5)**k / Fraction([1,1,2,6,24][k],1) for k in range(5))
assert exp_8_5_lower == Fraction(9067,1875)
assert exp_8_5_lower - Fraction(24,5) == Fraction(67,1875)

# Singular-seed diagnostic: a singular order-1 seed can have a nonsingular
# disjoint order-2 extension, so the sampling proof genuinely uses <=.
A = [[0]*4 for _ in range(4)]
A[0][3] = A[3][0] = 1
A[1][2] = A[2][1] = 1
assert det_q([[A[0][1]]]) == 0
assert det_q([[A[0][1], A[0][3]], [A[2][1], A[2][3]]]) == -1

# Sharpness diagnostic for the manuscript completion rank bounds.
C = [[0,1,1],[1,0,1],[1,1,1]]
assert det_q(C) == 1
for r in range(1,5):
    n = 3*r
    M = [[0]*n for _ in range(n)]
    for b in range(r):
        for i in range(3):
            for j in range(3):
                M[3*b+i][3*b+j] = C[i][j]
    assert rank_q(M) == 3*r

print('PASS')
