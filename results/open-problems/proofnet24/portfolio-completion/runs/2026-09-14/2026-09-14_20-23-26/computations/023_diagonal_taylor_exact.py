"""Exact finite checks for the all-n proof in agents/023.md.

Uses only Python's standard library. Atom polynomials are direct mixed-column
determinants over the Gaussian rationals, followed by exact formal entropy
series. These finite checks do not replace the all-dimensional proof.
Run: python computations/023_diagonal_taylor_exact.py
"""

from dataclasses import dataclass
from fractions import Fraction as Q
import itertools
import json
from pathlib import Path


N = 7


@dataclass(frozen=True)
class G:
    r: Q = Q(0)
    i: Q = Q(0)

    def __post_init__(self):
        object.__setattr__(self, "r", Q(self.r))
        object.__setattr__(self, "i", Q(self.i))

    def __add__(self, other):
        other = other if isinstance(other, G) else G(other)
        return G(self.r + other.r, self.i + other.i)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.r, -self.i)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        other = other if isinstance(other, G) else G(other)
        return G(self.r*other.r-self.i*other.i, self.r*other.i+self.i*other.r)

    __rmul__ = __mul__

    def __truediv__(self, other):
        return G(self.r / other, self.i / other)

    def conj(self):
        return G(self.r, -self.i)

    def abs2(self):
        return self.r**2 + self.i**2

    def __str__(self):
        return str(self.r) if self.i == 0 else f"{self.r}+({self.i})i"


def conv(a, b):
    return [sum((a[j]*b[k-j] for j in range(k+1)), Q(0)) for k in range(N+1)]


def atom_polynomial(p, A, bits):
    n = len(p)
    result = [G() for _ in range(N+1)]
    for perm in itertools.permutations(range(n)):
        inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i+1,n))
        term = [G((-1)**inversions)] + [G() for _ in range(N)]
        for row, col in enumerate(perm):
            constant = G(p[col] if bits[col] else 1-p[col]) if row == col else G()
            linear = A[row][col] * (1 if bits[col] else -1)
            factor = [constant, linear] + [G() for _ in range(N-1)]
            term = conv(term, factor)
        result = [x+y for x,y in zip(result,term)]
    assert all(x.i == 0 for x in result)
    return [x.r for x in result]


def direct_entropy_coefficients(p, A):
    n = len(p)
    atoms = []
    coeff = [Q(0)] * (N+1)
    for bits in itertools.product((0,1), repeat=n):
        a = atom_polynomial(p,A,bits)
        expected0 = Q(1)
        for j in range(n):
            expected0 *= p[j] if bits[j] else 1-p[j]
        assert a[0] == expected0
        atoms.append((bits,a))
        u = [Q(0)] + [x/a[0] for x in a[1:]]
        power = u
        for m in range(2,N+1):
            power = conv(power,u)
            factor = -Q((-1)**m,m*(m-1))*a[0]
            coeff = [x+factor*y for x,y in zip(coeff,power)]
    # Normalization and affine marginals show all cross-entropy coefficients
    # of order >= 2 are zero, avoiding any symbolic-log simplification.
    for k in range(N+1):
        assert sum(a[k] for _,a in atoms) == (1 if k == 0 else 0)
        for i in range(n):
            expected = p[i] if k == 0 else A[i][i].r if k == 1 else 0
            assert sum(a[k] for bits,a in atoms if bits[i]) == expected
    return coeff


def predicted(p,A):
    n = len(p)
    v = [x*(1-x) for x in p]
    mu3 = [(1-2*x)/w**2 for x,w in zip(p,v)]
    c = {(i,j): A[i][j].abs2() for i in range(n) for j in range(i+1,n)}
    a = [A[i][i].r for i in range(n)]
    result = {
        2: -sum(a[i]**2/v[i] for i in range(n))/2,
        3: sum(a[i]**3*mu3[i] for i in range(n))/6,
        4: -sum(a[i]**4*(p[i]**-3+(1-p[i])**-3) for i in range(n))/12
           -sum(z**2/(v[i]*v[j]) for (i,j),z in c.items())/2,
        5: sum(a[i]**5*(p[i]**-4-(1-p[i])**-4) for i in range(n))/20
           +sum(z**2*(a[i]*mu3[i]/v[j]+a[j]*mu3[j]/v[i]) for (i,j),z in c.items())/2,
    }
    if all(x == 0 for x in a):
        sixth = -sum(z**3*mu3[i]*mu3[j] for (i,j),z in c.items())/6
        seventh = Q(0)
        for i,j,k in itertools.combinations(range(n),3):
            cycle = A[i][j]*A[j][k]*A[k][i]
            r = 2*cycle.r
            sixth -= (r**2/2+c[i,j]*c[i,k]*c[j,k])/(v[i]*v[j]*v[k])
            seventh += r*(c[i,j]*c[i,k]*mu3[i]/(v[j]*v[k])
                          +c[i,j]*c[j,k]*mu3[j]/(v[i]*v[k])
                          +c[i,k]*c[j,k]*mu3[k]/(v[i]*v[j]))
        result[6] = sixth
        result[7] = seventh
    return result


def run_case(name,p,A):
    n = len(p)
    assert all(A[i][j] == A[j][i].conj() for i in range(n) for j in range(n))
    actual = direct_entropy_coefficients(p,A)
    expected = predicted(p,A)
    for k,value in expected.items():
        assert actual[k] == value, (name,k,actual[k],value)
    return {
        "name": name,
        "n": n,
        "p": [str(x) for x in p],
        "A": [[str(x) for x in row] for row in A],
        "exact_entropy_coefficients_2_through_7": {str(k): str(actual[k]) for k in range(2,N+1)},
        "checked_orders": sorted(expected),
        "all_checks_passed": True,
    }


cases = [
    ("complex_pair_opposite_marginals", [Q(1,3),Q(2,3)],
     [[G(),G(1,1)/10],[G(1,-1)/10,G()]]),
    ("real_triangle_nonzero_seventh_coefficient", [Q(1,3),Q(1,2),Q(1,2)],
     [[G(0 if i == j else Q(1,10)) for j in range(3)] for i in range(3)]),
    ("general_complex_hermitian_four_sites", [Q(1,3),Q(2,5),Q(3,7),Q(4,9)],
     [[G(1)/10,G(1,1)/10,G(1)/10,G(0,1)/10],
      [G(1,-1)/10,G(-2)/10,G(1,-2)/10,G(-1)/10],
      [G(1)/10,G(1,2)/10,G(3)/10,G(2,1)/10],
      [G(0,-1)/10,G(-1)/10,G(2,-1)/10,G(-1)/10]]),
]

output = {
    "method": "Exact Gaussian-rational mixed-column atom determinants and formal entropy series; standard library only.",
    "scope": "Finite checks only; the all-n proof is in agents/023.md.",
    "cases": [run_case(*case) for case in cases],
}
destination = Path(__file__).with_name("023_diagonal_taylor_exact_output.json")
destination.write_text(json.dumps(output,indent=2)+"\n")
print(json.dumps({"all_checks_passed": True,
                  "cases": [x["name"] for x in output["cases"]],
                  "output": str(destination)},indent=2))
