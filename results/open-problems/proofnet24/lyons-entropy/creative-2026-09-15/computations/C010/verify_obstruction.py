"""Exact rational interval certificate: every three-feature support fails.

The base L has diagonal 100 and off-diagonal -499/10.  All seven Fisher
features of the reveal order (1,2,3) are constructed from its exact rational
kernel.  Every principal minor of size at most 3 of (199/100) C - b b^T
is proved positive.  A rational seven-feature trial is proved > 223/100.

Only two logarithms enter.  Their enclosures use the positive atanh series
with an explicit geometric remainder, followed by outward rounding.
"""
from fractions import Fraction as F
from itertools import combinations, permutations, product
from pathlib import Path
import json


class IV:
    def __init__(self, lo, hi=None):
        self.lo = F(lo)
        self.hi = F(lo if hi is None else hi)
        assert self.lo <= self.hi

    @staticmethod
    def lift(x):
        return x if isinstance(x, IV) else IV(x)

    def __add__(self, other):
        other = self.lift(other)
        return IV(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return IV(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-self.lift(other))

    def __rsub__(self, other):
        return self.lift(other) - self

    def __mul__(self, other):
        other = self.lift(other)
        values = [a*b for a in (self.lo, self.hi) for b in (other.lo, other.hi)]
        return IV(min(values), max(values))

    __rmul__ = __mul__

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        ans = IV(1)
        for _ in range(n):
            ans = ans * self
        return ans

    def strings(self):
        return [str(self.lo), str(self.hi)]


def quantize(v, denominator=10**12):
    lo = (v.lo * denominator).__floor__()
    hi = (v.hi * denominator).__ceil__()
    return IV(F(lo, denominator), F(hi, denominator))


def log_iv(x, n=32):
    x = F(x)
    assert x >= 1
    z = (x - 1) / (x + 1)
    subtotal = 2*sum((z**(2*k+1) / (2*k+1) for k in range(n)), F(0))
    remainder = 2*z**(2*n+1) / ((2*n+1)*(1-z*z))
    return IV(subtotal, subtotal + remainder)


def exact_det(matrix):
    n = len(matrix)
    ans = F(0)
    for perm in permutations(range(n)):
        inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i+1,n))
        term = F((-1)**inversions)
        for i in range(n):
            term *= matrix[i][perm[i]]
        ans += term
    return ans


def iv_det(matrix):
    n = len(matrix)
    ans = IV(0)
    for perm in permutations(range(n)):
        inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i+1,n))
        term = IV((-1)**inversions)
        for i in range(n):
            term = term * matrix[i][perm[i]]
        ans = ans + term
    return ans


def solve_small(matrix, rhs):
    n = len(matrix)
    if n == 0:
        return []
    if n == 1:
        return [rhs[0] / matrix[0][0]]
    assert n == 2
    a,b = matrix[0]
    c,d = matrix[1]
    determinant = a*d-b*c
    return [(d*rhs[0]-b*rhs[1])/determinant,
            (-c*rhs[0]+a*rhs[1])/determinant]


def main():
    # Eigenvalues are 1/6 in the all-ones direction and 1499/1509 twice.
    K = [[F(6499, 9054) if i == j else F(-2495, 9054)
          for j in range(3)] for i in range(3)]
    assert exact_det(K) > 0
    d_unrounded = log_iv(F(1000000, 750999))
    # det(R)=2247001/500000000.  Splitting off 2^7 gives short series.
    tau_unrounded = 7*log_iv(F(2)) + log_iv(F(3906250,2247001)) - 3*d_unrounded
    d, tau = quantize(d_unrounded), quantize(tau_unrounded)
    assert d.lo > 0 and tau.lo > 0
    delta = (d + tau*F(1,6)) * (d + tau*F(1499,1509))**2

    features, eta, labels = [], [], []
    for i in range(3):
        for history in product((0,1), repeat=i):
            Q = [[K[j][k] - (F(1-history[j]) if j == k else 0)
                  for k in range(i)] for j in range(i)]
            prob = (-1)**(i-sum(history)) * exact_det(Q)
            wi = solve_small(Q, [-K[j][i] for j in range(i)]) + [F(1)] + [F(0)]*(2-i)
            q = K[i][i] + sum((K[i][j]*wi[j] for j in range(i)), F(0))
            assert prob > 0 and 0 < q < 1
            features.append(wi)
            eta.append(q*(1-q)/prob)
            labels.append("empty" if not history else "".join(map(str,history)))
    gram0 = [[sum((u[k]*v[k] for k in range(3)), F(0))
              for v in features] for u in features]
    gramK = [[sum((u[j]*K[j][k]*v[k] for j in range(3) for k in range(3)), F(0))
              for v in features] for u in features]
    H = [[d*gram0[i][j] + tau*gramK[i][j] for j in range(7)] for i in range(7)]
    b = [H[i][i] for i in range(7)]
    C = [[H[i][j]**2 + (delta*eta[i] if i == j else 0)
          for j in range(7)] for i in range(7)]
    Q = [[F(199,100)*C[i][j] - b[i]*b[j] for j in range(7)] for i in range(7)]

    records = {}
    minimum_lower = {}
    thresholds = {1: F(20), 2: F(400), 3: F(9000)}
    for size in (1,2,3):
        minima = []
        for support in combinations(range(7),size):
            minor = iv_det([[Q[i][j] for j in support] for i in support])
            assert minor.lo > thresholds[size]
            minima.append(minor.lo)
            records[",".join(str(i+1) for i in support)] = {
                "lower_floor": minor.lo.__floor__(),
                "upper_ceil": minor.hi.__ceil__(),
            }
        minimum_lower[size] = min(minima).__floor__()

    r = [F(v,1000) for v in (58,57,65,1,56,56,103)]
    trial = 2*sum((b[i]*r[i] for i in range(7)), IV(0)) - sum(
        (C[i][j]*r[i]*r[j] for i in range(7) for j in range(7)), IV(0))
    assert trial.lo > F(223,100)
    output = {
        "all_assertions_passed": True,
        "K": [[str(x) for x in row] for row in K],
        "d_interval": d.strings(),
        "tau_interval": tau.strings(),
        "feature_labels": labels,
        "features": [[str(x) for x in row] for row in features],
        "inverse_weights_eta": [str(x) for x in eta],
        "minor_floor_minima": minimum_lower,
        "minor_enclosures_outward_integer": records,
        "all_supports_size_at_most_three_value_less_than": "199/100",
        "seven_feature_trial": [str(x) for x in r],
        "trial_interval_outward_1e12": quantize(trial).strings(),
        "seven_feature_trial_greater_than": "223/100",
    }
    destination = Path(__file__).with_name("obstruction_results.json")
    destination.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps({k:v for k,v in output.items() if k not in {
        "minor_enclosures_outward_integer", "K", "features", "inverse_weights_eta"
    }}, indent=2))


if __name__ == "__main__":
    main()
