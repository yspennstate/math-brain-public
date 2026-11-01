#!/usr/bin/env python3
"""Exact self-check for P03's independent audit of P04-I0101-S3-STANDARD-HEXAGON-44.

Uses SymPy exact algebra in Q(sqrt(3)).  This checks only the finite S3/hexagon core
of Claim 44; it does not certify I0101's asymptotic Paley conjecture.
"""
from fractions import Fraction
import itertools
import sympy as sp

rt3 = sp.sqrt(3)
I = sp.eye(2)
R = sp.Matrix([[-sp.Rational(1, 2), -rt3/2],
               [ rt3/2,              -sp.Rational(1, 2)]])
R2 = sp.simplify(R*R)
S = sp.Matrix([[1, 0], [0, -1]])
even = [I, R, R2]
odd = [S, sp.simplify(S*R), sp.simplify(S*R2)]

# Character/Gram facts for the two parity triangles.
assert sp.simplify(sum(even, sp.zeros(2))) == sp.zeros(2)
assert sp.simplify(sum(odd, sp.zeros(2))) == sp.zeros(2)
for tri in (even, odd):
    for i in range(3):
        for j in range(3):
            ip = sp.trace(tri[i].T * tri[j])
            assert sp.simplify(ip - (2 if i == j else -1)) == 0
for a in even:
    for b in odd:
        assert sp.simplify(sp.trace(a.T*b)) == 0

def singular_squares(M):
    vals = []
    for v, mult in (M.T*M).eigenvals().items():
        vals += [sp.simplify(v)] * mult
    return tuple(sorted(vals, key=lambda z: float(z), reverse=True))

counts = {}
for eps in itertools.product((-1, 1), repeat=6):
    Fp = sum((eps[i]*even[i] for i in range(3)), sp.zeros(2))
    Fm = sum((eps[i+3]*odd[i] for i in range(3)), sp.zeros(2))
    F = sp.simplify(Fp + Fm)
    cp = len(set(eps[:3])) == 1
    cm = len(set(eps[3:])) == 1
    case = 'both_constant' if cp and cm else ('one_nonconstant' if cp ^ cm else 'both_nonconstant')
    sq = singular_squares(F)
    expected = {
        'both_constant': (0, 0),
        'one_nonconstant': (4, 4),
        'both_nonconstant': (16, 0),
    }[case]
    assert sq == expected
    counts[(case, sq)] = counts.get((case, sq), 0) + 1

# Exact weighted-support Pareto values.  In one parity triangle, the Gram matrix is
# diagonal 2 and off-diagonal -1, so ||sum w_i rho_i||_F^2 = 3 sum w_i^2 - m^2.
for k, expected_coeff in [(1, sp.Rational(2)), (2, sp.Rational(1,2)), (3, sp.Rational(0))]:
    m = sp.symbols('m', nonnegative=True)
    equal_weights = [m/sp.Integer(k)]*k
    norm_sq = sp.simplify(3*sum(w*w for w in equal_weights) - m*m)
    assert sp.simplify(norm_sq - expected_coeff*m*m) == 0

# Uniform 64-mask equality rule: put weight 8 on all three channels of any fully
# complementary parity triple.  Then each full triple has scalar mass 24.
Ts, Ss = [], []
for eps in itertools.product((-1, 1), repeat=6):
    rp = 24 if eps[:3] == (-1, -1, -1) else 0
    rm = 24 if eps[3:] == (-1, -1, -1) else 0
    Ts.append(rp + rm)
    Ss.append(rp - rm)
meanT = Fraction(sum(Ts), 64)
meanT2 = Fraction(sum(t*t for t in Ts), 64)
meanS2 = Fraction(sum(s*s for s in Ss), 64)
varT = meanT2 - meanT*meanT
assert meanT == 6
assert varT == 126
assert meanS2 == 126
assert meanT2 + meanS2 == 8*meanT*meanT

print('S3_MASK_CLASS_COUNTS', counts)
print('SUPPORT_PARETO_COEFFS', {'k=1': '2', 'k=2': '1/2', 'k=3': '0'})
print('UNIFORM_RULE_MEAN_T', meanT)
print('UNIFORM_RULE_VAR_T', varT)
print('UNIFORM_RULE_E_S2', meanS2)
print('ENERGY_EQUALITY', meanT2 + meanS2, '=', 8*meanT*meanT)
print('ALL_EXACT_CHECKS_PASS', True)
