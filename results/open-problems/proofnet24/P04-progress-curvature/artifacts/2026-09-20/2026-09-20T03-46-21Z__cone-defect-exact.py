from fractions import Fraction
from functools import lru_cache

# Exact checker for the P04 T10 cone-defect theorem.
# Model: undirected nearest-neighbor Z^2 FPP with iid Exp(1) edge weights.


def exp_upper(x: Fraction, N: int) -> Fraction:
    """Rigorous upper bound for exp(x), x>=0.

    Sum through N exactly; bound the positive tail geometrically using
    term_{k+1}/term_k = x/(k+1) <= x/(N+2) for k>=N+1.
    """
    term = Fraction(1)
    partial = term
    for k in range(1, N + 1):
        term = term * x / k
        partial += term
    next_term = term * x / (N + 1)
    ratio = x / (N + 2)
    assert 0 <= ratio < 1
    return partial + next_term / (1 - ratio)


def rectangle_expectation(L=6, h=1):
    """Exact E distance in [0,L] x [-h,h] from (0,0) to (L,0).

    Richardson/FPP infection recursion.  For an infected set S not yet
    containing the target, b(S) is the number of boundary physical edges,
    and r_S(v) is the number leading to outside vertex v.  Exponential
    memorylessness gives

       E(S)=1/b(S)+sum_v r_S(v)/b(S) E(S union {v}).

    Every operation is Fraction arithmetic.
    """
    vertices = [(x, y) for x in range(L + 1) for y in range(-h, h + 1)]
    index = {v: i for i, v in enumerate(vertices)}
    N = len(vertices)
    adj = [[] for _ in range(N)]
    for i, (x, y) in enumerate(vertices):
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            w = (x + dx, y + dy)
            if w in index:
                adj[i].append(index[w])

    start = index[(0, 0)]
    target = index[(L, 0)]
    calls = 0

    @lru_cache(None)
    def E(mask):
        nonlocal calls
        calls += 1
        if (mask >> target) & 1:
            return Fraction(0)
        rates = {}
        b = 0
        for i in range(N):
            if (mask >> i) & 1:
                for j in adj[i]:
                    if not ((mask >> j) & 1):
                        rates[j] = rates.get(j, 0) + 1
                        b += 1
        assert b > 0
        ans = Fraction(1, b)
        for j, rate in rates.items():
            ans += Fraction(rate, b) * E(mask | (1 << j))
        return ans

    value = E(1 << start)
    return value, calls, len(vertices)


# 1. Exact six-column, height-one ladder block.
EM, states, nverts = rectangle_expectation(6, 1)
axis_upper = EM / 6
# If mu(1,2)>=2/3 and mu(e1)<=axis_upper, then the symmetric-pair
# triangle defect is at least 4/3 - 2*axis_upper.
defect = Fraction(4, 3) - 2 * axis_upper
assert defect > Fraction(1, 24)

# 2. Rational non-backtracking transfer certificate.
# Direction weights correspond to h=(log(9/5), log 3): E,W,N,S.
A = Fraction(9, 5)
B = Fraction(3, 1)
weights = [A, 1 / A, B, 1 / B]
opp = [1, 0, 3, 2]
M = [[Fraction(0) for _ in range(4)] for _ in range(4)]
for i in range(4):
    for j in range(4):
        if j != opp[i]:
            M[i][j] = weights[j]

# Positive Collatz vector.  Componentwise M z <= r z proves rho(M)<=r.
z_raw = [2164, 1571, 2269, 1000]
z = [Fraction(t, 1000) for t in z_raw]
r = Fraction(511, 100)
ratios = []
for i in range(4):
    lhs = sum(M[i][j] * z[j] for j in range(4))
    ratios.append(lhs / z[i])
    assert lhs <= r * z[i]

# Chernoff parameter s and resulting geometric ratio q.
s = Fraction(21, 5)
q = r / (1 + s)
assert q == Fraction(511, 520)
assert q < 1

# For the boundary slope b=2a and candidate lower speed (2/3)a,
# beta = exp(14/5) * (5/81) * q^3.
# Bound exp(14/5) rigorously using 20 Taylor terms plus a geometric tail.
eu = exp_upper(Fraction(14, 5), 20)
beta_upper = eu * Fraction(5, 81) * q**3
assert beta_upper < 1

# Explicit prefactor in the union bound over all path lengths.
# Weighted number of length-m non-backtracking walks is at most
# (weights dot z) r^(m-1).  Since min(z)=1, this controls the all-ones vector.
b_dot_z = sum(weights[i] * z[i] for i in range(4))
K = b_dot_z / r
prob_prefactor = K / (1 - q)

print("RECTANGLE_VERTICES =", nverts)
print("RECTANGLE_STATES =", states)
print("E_M_6_1 =", EM)
print("AXIS_UPPER =", axis_upper)
print("AXIS_UPPER_FLOAT =", float(axis_upper))
print("DEFECT_EXACT =", defect)
print("DEFECT_FLOAT =", float(defect))
print("DEFECT_GT_1_OVER_24 =", defect > Fraction(1, 24))
print("COLLATZ_RATIOS =", ", ".join(str(x) for x in ratios))
print("COLLATZ_R =", r)
print("Q =", q)
print("EXP_14_5_UPPER =", eu)
print("BETA_UPPER =", beta_upper)
print("BETA_UPPER_FLOAT =", float(beta_upper))
print("PROB_PREFACTOR =", prob_prefactor)
print("PROB_PREFACTOR_FLOAT =", float(prob_prefactor))
print("ALL_EXACT_CHECKS_PASS")
