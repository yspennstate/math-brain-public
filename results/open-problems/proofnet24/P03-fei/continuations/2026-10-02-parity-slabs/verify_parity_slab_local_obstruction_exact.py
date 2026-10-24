"""Exact slab realization and Fraction-majority checks for the local obstruction.

The analytic asymptotic theorem is in parity_slab_local_minimum_obstruction.md.
Decimal logarithms are numerical verification, explicitly separate from the
exact integer/Fraction assertions. No local helper imports.
"""
import json
import math
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path

import numpy as np


def walsh(f):
    a = np.array(f, dtype=np.int64).copy()
    for j in range(len(a).bit_length()-1):
        v = a.reshape(-1, 2 << j)
        l, r = v[:, :1 << j].copy(), v[:, 1 << j:].copy()
        v[:, :1 << j], v[:, 1 << j:] = l+r, l-r
    return a


def majority_coeff(N, k):
    if k % 2 == 0:
        return Fraction(0)
    d, ell = (N-1)//2, (k-1)//2
    return (-1)**ell * Fraction(math.comb(2*d,d), 1 << (2*d)) * Fraction(
        math.comb(d,ell), math.comb(2*d,2*ell))


def dec(x):
    return Decimal(x.numerator)/Decimal(x.denominator)


def ent(x):
    if not x:
        return Decimal(0)
    z = dec(x)
    return -z*z.ln()/Decimal(2).ln()


report = {"status": "passed", "scope": "exact realization/coefficient certificates; logarithms Decimal",
          "truth_realizations": [], "fraction_coefficient_cases": 0,
          "coefficient_bounds": [], "decimal_entropy_cases": []}


for N in range(3, 16, 2):
    size = 1 << N
    scores = np.array([2*s.bit_count()-N for s in range(size)], dtype=np.int64)
    M = np.where(scores > 0, 1, -1)
    D = np.zeros(size, dtype=np.int64)
    D[0] = 1
    minus = np.where((-N+2*scores > -N+.5) & (-N+2*scores < N+.5), -1, 1)
    plus = np.where((N+2*scores > -N+.5) & (N+2*scores < N+.5), -1, 1)
    assert np.array_equal(minus, -M)
    assert np.array_equal(plus, M+2*D)
    assert int(np.sum(minus != plus)) == size-1
    g = np.concatenate([minus, plus])
    old_f = np.concatenate([M, M+2*D])
    z = np.concatenate([-np.ones(size, dtype=np.int64), np.ones(size, dtype=np.int64)])
    assert np.array_equal(g, z*old_f)
    idx = np.arange(2*size)
    # The integer FWHT uses (-1)^bit; physical z=2*bit-1 is its negative.
    assert np.array_equal(walsh(g), -walsh(old_f)[idx ^ size])
    Mh = walsh(M)
    for s in range(size):
        physical_coeff = Fraction((-1)**s.bit_count()*int(Mh[s]), size)
        assert physical_coeff == majority_coeff(N, s.bit_count())
    report["truth_realizations"].append({"N": N, "pivot_weight": N,
        "remaining_weights": 2, "strictly_unique_largest": N>2,
        "interval": [str(Fraction(-2*N+1,2)),str(Fraction(2*N+1,2))],
        "pivot_influence":str(Fraction(size-1,size))})


for N in range(15, 514, 2):
    d = (N-1)//2
    epsilon = Fraction(1, 1 << N)
    lower = Fraction(1, (1 << d)*N*(d+1))
    vals = [abs(majority_coeff(N,k)) for k in range(1,N+1,2)]
    assert min(vals) >= lower >= 2*epsilon
    assert Fraction(1 << (d+1), (2*d+1)*(d+1)) >= 2
    # Exact positivity of the ratio step r(d+1)/r(d)-1.
    assert 2*(2*d+1)*(d+1) > (2*d+3)*(d+2)
    report["fraction_coefficient_cases"] += len(vals)
    report["coefficient_bounds"].append({"N":N,
        "uniform_lower_over_epsilon":str(lower/epsilon),
        "actual_minimum_over_epsilon":str(min(vals)/epsilon)})


with localcontext() as ctx:
    ctx.prec = 100
    log2 = Decimal(2).ln()
    for N in range(3, 102, 2):
        epsilon = Fraction(1,1 << N)
        delta = Decimal(0)
        mass = Fraction(0)
        for k in range(N+1):
            a = (-1)**k * epsilon
            b = majority_coeff(N,k) + a
            P = a*a+b*b
            mass += math.comb(N,k)*P
            # Exact pair masses; entropy difference uses high precision.
            pair = ent(a*a)+ent(b*b)-(ent((a+b)**2)+ent((a-b)**2))/2
            if k%2 == 0:
                assert a == b and P == 2*epsilon**2
                assert abs(pair-dec(4*epsilon**2)) < Decimal('1e-90')
            delta += math.comb(N,k)*pair
        assert mass == 1
        ratio = delta/dec(epsilon)
        lower = Decimal(N+3)/2-Decimal(N*(N+1)//2).ln()/log2
        if N >= 15:
            assert ratio + Decimal('1e-50') >= lower
        report["decimal_entropy_cases"].append({"N":N,
            "delta_over_min_influence":str(ratio),
            "analytic_lower_bound":str(lower)})


out = Path(__file__).with_name("parity_slab_local_obstruction_exact_checks.json")
out.write_text(json.dumps(report,indent=2)+"\n")
print(json.dumps({"status":report["status"],
    "truth_realizations":len(report["truth_realizations"]),
    "fraction_coefficient_cases":report["fraction_coefficient_cases"],
    "uniform_bound_dimensions":len(report["coefficient_bounds"]),
    "decimal_entropy_cases":len(report["decimal_entropy_cases"]),
    "result_file":str(out)},indent=2))
