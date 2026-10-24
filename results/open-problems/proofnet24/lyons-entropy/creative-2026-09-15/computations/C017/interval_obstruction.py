"""A rational certificate that the occupation-only Fisher test can fail.

No floating-point arithmetic is used in the certificate. Logarithms use a
positive atanh series with an explicit rational tail bound; subsequent
operations round outwards to a fixed dyadic grid.
"""
from fractions import Fraction as F
from pathlib import Path
import json

BITS = 256
GRID = 1 << BITS
TERMS = 100


def floor_grid(q):
    q = F(q)
    return F((q.numerator*GRID)//q.denominator, GRID)


def ceil_grid(q):
    q = F(q)
    return F(-((-q.numerator*GRID)//q.denominator), GRID)


class Interval:
    def __init__(self, lo, hi=None):
        self.lo = floor_grid(lo)
        self.hi = ceil_grid(lo if hi is None else hi)
        assert self.lo <= self.hi

    @staticmethod
    def lift(x):
        return x if isinstance(x, Interval) else Interval(x)

    def __add__(self, other):
        other = self.lift(other)
        return Interval(self.lo+other.lo, self.hi+other.hi)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + -self.lift(other)

    def __rsub__(self, other):
        return self.lift(other) + -self

    def __mul__(self, other):
        other = self.lift(other)
        values = [a*b for a in (self.lo, self.hi) for b in (other.lo, other.hi)]
        return Interval(min(values), max(values))

    __rmul__ = __mul__

    def reciprocal(self):
        assert not self.lo <= 0 <= self.hi
        return Interval(1/self.hi, 1/self.lo)

    def __truediv__(self, other):
        return self * self.lift(other).reciprocal()

    def __rtruediv__(self, other):
        return self.lift(other)*self.reciprocal()


def unit_log_bounds(q):
    """Exact log bounds for rational 1<=q<=2."""
    assert 1 <= q <= 2
    z = (q-1)/(q+1)
    power = z
    partial = F(0)
    for j in range(TERMS):
        partial += 2*power/F(2*j+1)
        power *= z*z
    # Every omitted denominator is >=2*TERMS+1.
    tail = 2*power/(F(2*TERMS+1)*(1-z*z))
    return Interval(partial, partial+tail)


LOG_TWO = unit_log_bounds(F(2))


def log_interval(q):
    q = F(q)
    assert q > 0
    exponent = q.numerator.bit_length()-q.denominator.bit_length()
    scale = F(2)**exponent
    reduced = q/scale
    if reduced < 1:
        exponent -= 1
        reduced *= 2
    elif reduced >= 2:
        exponent += 1
        reduced /= 2
    assert 1 <= reduced < 2
    return unit_log_bounds(reduced) + exponent*LOG_TWO


def det3(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
            - A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
            + A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))


def inv3(A):
    det = det3(A)
    out = []
    for i in range(3):
        row = []
        for j in range(3):
            rows = [k for k in range(3) if k != j]
            cols = [k for k in range(3) if k != i]
            minor = A[rows[0]][cols[0]]*A[rows[1]][cols[1]] - A[rows[0]][cols[1]]*A[rows[1]][cols[0]]
            row.append((-1)**(i+j)*minor/det)
        out.append(row)
    return out


def matmul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def main():
    d = [F(18,25), F(12934613807,30843413807), F(1,1600)]
    u = [F(9,20), F(2,5), F(7,200)]
    assert all(0 < z < 1 for z in d)
    defect = 1-sum(u[i]*u[i]/(1-d[i]) for i in range(3))
    assert defect == F(1,10**7)
    K = [[(d[i] if i == j else F(0))+u[i]*u[j] for j in range(3)] for i in range(3)]
    IminusK = [[F(i == j)-K[i][j] for j in range(3)] for i in range(3)]
    L = matmul(K, inv3(IminusK))
    assert L == [list(row) for row in zip(*L)]
    detL = det3(L)
    assert detL > 0
    pairs = [(0,1), (0,2), (1,2)]
    minors = {(i,j):L[i][i]*L[j][j]-L[i][j]*L[j][i] for i,j in pairs}
    assert all(v > 0 for v in minors.values())
    coeff = {(i,j):log_interval(L[i][i]*L[j][j]/minors[(i,j)]) for i,j in pairs}
    tau = log_interval(minors[(0,1)]*minors[(0,2)]*minors[(1,2)]/
                       (detL*L[0][0]*L[1][1]*L[2][2]))
    comp = [coeff[(1,2)], coeff[(0,2)], coeff[(0,1)]]
    M = [[tau*K[i][j]+(comp[i] if i == j else 0) for j in range(3)] for i in range(3)]
    delta = det3(M)
    assert delta.lo > 0
    sigma = [[K[i][i]*(1-K[i][i]) if i == j else -K[i][j]*K[j][i]
              for j in range(3)] for i in range(3)]
    C = [[M[i][j]*M[i][j]+delta*sigma[i][j] for j in range(3)] for i in range(3)]
    Cinv = inv3(C)
    scalar = sum(M[i][i]*Cinv[i][j]*M[j][j] for i in range(3) for j in range(3))
    assert F(1947,1000) < scalar.lo <= scalar.hi < F(1948,1000)
    assert scalar.hi-scalar.lo < F(1,10**35)
    output = {
        "status": "PASS",
        "arithmetic": "rational only; dyadic interval operations round outwards",
        "bits": BITS,
        "atanh_series_terms": TERMS,
        "D": [str(v) for v in d],
        "u": [str(v) for v in u],
        "strict_contraction_defect": str(defect),
        "certified_coarse_interval": ["1947/1000", "1948/1000"],
        "exact_enclosure": [str(scalar.lo), str(scalar.hi)],
        "enclosure_width": str(scalar.hi-scalar.lo),
        "interpretation": "The occupation-indicator sufficient certificate is below 2. This is not an entropy counterexample.",
    }
    target = Path(__file__).with_name("interval_obstruction_results.json")
    target.write_text(json.dumps(output, indent=2)+"\n")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
