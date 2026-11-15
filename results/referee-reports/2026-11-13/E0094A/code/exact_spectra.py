"""Rational inertia and polynomial certificates, n <= 10 in the graph census."""
from fractions import Fraction
import math
import sympy as sp


def negative_inertia(a, p, q):
    """Inertia of q L - p D by fraction-free congruence.

    Nonzero leading minors suffice here. For a symmetric matrix with leading
    minors Delta_0=1,...,Delta_n, the LDL pivots have signs Delta_i/Delta_(i-1).
    Bareiss elimination returns these minors without rational divisions.
    """
    n = len(a)
    deg = [int(sum(row)) for row in a]
    m = [[(q-p)*deg[i] if i == j else -q*int(a[i][j])
          for j in range(n)] for i in range(n)]
    prev, count = 1, 0
    for k in range(n):
        pivot = m[k][k]
        if pivot == 0:
            raise ArithmeticError('zero leading minor; choose another endpoint')
        count += int((pivot > 0) != (prev > 0))
        if k < n-1:
            for i in range(k+1, n):
                for j in range(i, n):
                    num = pivot*m[i][j]-m[i][k]*m[k][j]
                    assert num % prev == 0
                    m[i][j] = m[j][i] = num // prev
        prev = pivot
    return count


def certify_bracket(a, approximate):
    q = 10**8
    lo = math.floor(approximate*q)-1
    hi = lo+3
    while True:
        try:
            nlo = negative_inertia(a, lo, q)
            break
        except ArithmeticError:
            lo -= 1
    while True:
        try:
            nhi = negative_inertia(a, hi, q)
            break
        except ArithmeticError:
            hi += 1
    assert nlo == 1 and nhi >= 2, (approximate,lo,hi,nlo,nhi)
    return lo, hi, q


def polynomial(a):
    n = len(a)
    a = sp.Matrix([[int(z) for z in row] for row in a])
    d = sp.diag(*[sum(a[i,:]) for i in range(n)])
    x = sp.Symbol('x')
    return sp.Poly((d.inv()*(d-a)).charpoly(x).as_expr(), x).clear_denoms()[1].primitive()[1]


def certify_optimizer(candidates, best_index):
    """Return all exact optimizers; candidates=(edge set, matrix, float gap)."""
    brackets = [certify_bracket(a,z) for _,a,z in candidates]
    bestlo,besthi,q = brackets[best_index]
    bp = None
    optimal = []
    for i, ((_,a,_),(lo,hi,qi)) in enumerate(zip(candidates,brackets)):
        assert qi == q
        if hi <= bestlo:
            continue
        if i != best_index:
            if bp is None:
                bp = polynomial(candidates[best_index][1]).sqf_part()
            cp = polynomial(a).sqf_part()
            left,right = sp.Rational(min(lo,bestlo),q),sp.Rational(max(hi,besthi),q)
            common = sp.gcd(bp,cp)
            assert bp.count_roots(left,right)==1
            assert cp.count_roots(left,right)==1
            assert common.count_roots(left,right)==1, 'unresolved close distinct roots'
        optimal.append(i)
    return brackets, optimal
