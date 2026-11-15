#!/usr/bin/env python3
"""Exact small-model checks; Python standard library only.

Enumerates complete factor priors, never samples. Separately integrates the
Hermite correction as an ordinary polynomial using Gaussian monomial moments.
"""
import itertools as it
import json
import math
import os
from pathlib import Path
import resource
import time
from collections import defaultdict
from fractions import Fraction as F

resource.setrlimit(resource.RLIMIT_CPU, (90, 90))
# macOS can reject RLIMIT_AS below the interpreter's reserved address space.
# This small standard-library enumeration is checked against actual peak RSS.
assert os.environ.get("OMP_NUM_THREADS") == "1"
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
START = time.monotonic()

RAD = ((-1, 1), (1, 1))
SP2 = ((-2, 1), (0, 6), (2, 1))
SP3 = ((-3, 1), (0, 16), (3, 1))
PRIORS = {"rad": RAD, "sparse2": SP2, "sparse3": SP3}


def fourth(prior):
    den = sum(w for _, w in prior)
    assert F(sum(w * x * x for x, w in prior), den) == 1
    return F(sum(w * x**4 for x, w in prior), den)


def distribution(n, p, m, pu, pv):
    """Distribution of the integer vector S=UV^T, before division by sqrt(N)."""
    counts = defaultdict(int)
    supports = [pu] * (n * m) + [pv] * (p * m)
    for state in it.product(*supports):
        values = [v for v, _ in state]
        weight = math.prod(w for _, w in state)
        u, v = values[:n*m], values[n*m:]
        s = tuple(sum(u[i*m+k] * v[j*m+k] for k in range(m))
                  for i in range(n) for j in range(p))
        counts[s] += weight
    den = sum(w for _, w in pu)**(n*m) * sum(w for _, w in pv)**(p*m)
    assert sum(counts.values()) == den
    return counts, den


def poly_add(target, source, scale=F(1)):
    for powers, c in source.items():
        target[powers] += scale * c


def hermite_product(counts):
    # Probabilists' Hermite polynomials as ordinary monomial coefficients.
    h = [{0: 1}, {1: 1}, {2: 1, 0: -1},
         {3: 1, 1: -3}, {4: 1, 2: -6, 0: 3}]
    return {tuple(e for e, _ in terms): math.prod(c for _, c in terms)
            for terms in it.product(*(tuple(h[c].items()) for c in counts))}


def normal_moment(k):
    return 0 if k % 2 else math.prod(range(1, k, 2))


def polynomial_square_integral(poly):
    # Direct monomial expansion, with no Hermite orthogonality formula.
    ans = F(0)
    items = [(powers, c) for powers, c in poly.items() if c]
    for powers, c in items:
        for other, b in items:
            ans += c * b * math.prod(normal_moment(x+y)
                                     for x, y in zip(powers, other))
    return ans


def check(n, p, m, uname, vname):
    assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss < 1024**3
    pu, pv = PRIORS[uname], PRIORS[vname]
    dist, den = distribution(n, p, m, pu, pv)
    d, rho = n*p, F(m, n)
    # Check every covariance, including off-diagonal entries, from full factors.
    for i, j in it.product(range(d), repeat=2):
        cov = F(sum(w*s[i]*s[j] for s, w in dist.items()), den*n)
        assert cov == (rho if i == j else 0)
    norm = F(0)
    poly = defaultdict(F)
    patterns = defaultdict(int)
    for indices in it.combinations_with_replacement(range(d), 4):
        i, j, k, l = indices
        moment = F(sum(w * math.prod(s[q] for q in indices)
                       for s, w in dist.items()), den*n*n)
        pairings = ((i == j and k == l) + (i == k and j == l)
                    + (i == l and j == k))
        cumulant = moment - rho*rho*pairings
        multiplicities = tuple(indices.count(q) for q in range(d))
        factorials = math.prod(math.factorial(c) for c in multiplicities)
        norm += F(24, factorials) * cumulant*cumulant
        if cumulant:
            patterns[str(cumulant)] += 24 // factorials
            poly_add(poly, hermite_product(multiplicities), cumulant/factorials)
    a, b = fourth(pu), fourth(pv)
    bracket = ((a*b-3)**2 + 3*(p-1)*(a-1)**2
               + 3*(n-1)*(b-1)**2 + 6*(n-1)*(p-1))
    expected = F(d*m*m, n**4) * bracket
    assert norm == expected, (n, p, m, norm, expected)
    poly_norm = polynomial_square_integral(poly)
    assert poly_norm == norm / 24
    gradient_norm = F(0)
    for q in range(d):
        deriv = defaultdict(F)
        for powers, c in poly.items():
            if powers[q]:
                reduced = list(powers)
                reduced[q] -= 1
                deriv[tuple(reduced)] += c * powers[q]
        gradient_norm += polynomial_square_integral(deriv)
    assert gradient_norm == norm / 6
    result = dict(N=n, P=p, M=m, U=uname, V=vname,
                  distinct_products=len(dist), a=str(a), b=str(b),
                  tensor_norm_squared=str(norm),
                  direct_gaussian_A_squared=str(poly_norm),
                  direct_gaussian_gradient_squared=str(gradient_norm),
                  MI_deficit_coefficient=str(norm / (48*d)),
                  MMSE_improvement_coefficient=str(gradient_norm/d),
                  nonzero_ordered_cumulants=dict(patterns))
    print(f"PASS N={n} P={p} M={m} U={uname} V={vname} "
          f"C={result['MI_deficit_coefficient']} "
          f"8C={result['MMSE_improvement_coefficient']}")
    return result


CASES = [(1, 1, 1, "rad", "rad"), (1, 2, 2, "rad", "rad"),
         (2, 1, 2, "rad", "rad"), (2, 2, 1, "rad", "rad"),
         (2, 2, 2, "rad", "rad"), (2, 3, 2, "rad", "rad"),
         (2, 2, 1, "sparse2", "rad"),
         (2, 2, 1, "rad", "sparse3"),
         (2, 2, 1, "sparse2", "sparse3"),
         (1, 2, 2, "sparse2", "sparse3")]
results = [check(*case) for case in CASES]

# Independent scalar posterior calculation: tanh(z)^2 through degree six.
# For z=t+sqrt(t)G, E[z^k] has integer powers since odd Gaussian moments vanish.
posterior_square = defaultdict(F)
for degree, coefficient in ((2, F(1)), (4, F(-2, 3)), (6, F(17, 45))):
    for gaussian_degree in range(0, degree+1, 2):
        power = degree - gaussian_degree // 2
        if power <= 3:
            posterior_square[power] += (coefficient * math.comb(degree, gaussian_degree)
                                        * normal_moment(gaussian_degree))
assert dict(posterior_square) == {1: F(1), 2: F(-1), 3: F(5, 3)}
print("PASS scalar posterior MMSE = 1-t+t^2-(5/3)t^3+O(t^4)")

# Independent MI calculation from the exact scalar likelihood:
# I=t-E log cosh(t+sqrt(t)G), with no I-MMSE differentiation.
logcosh = defaultdict(F)
for degree, coefficient in ((2, F(1, 2)), (4, F(-1, 12)),
                            (6, F(1, 45)), (8, F(-17, 2520))):
    for gaussian_degree in range(0, degree+1, 2):
        power = degree - gaussian_degree // 2
        if power <= 4:
            logcosh[power] += (coefficient * math.comb(degree, gaussian_degree)
                               * normal_moment(gaussian_degree))
scalar_mi = {power: (F(1) if power == 1 else F(0))-value
             for power, value in logcosh.items()}
assert scalar_mi == {1: F(1, 2), 2: F(-1, 4), 3: F(1, 6), 4: F(-5, 24)}
assert F(-1, 8) - scalar_mi[4] == F(1, 12)
print("PASS scalar likelihood MI = t/2-t^2/4+t^3/6-(5/24)t^4+O(t^5)")

# A deliberately asymmetric nondegenerate proportional scaling checks alpha,beta.
sequence = []
for n in (10, 100, 1000, 10000):
    m, p = 2*n, 3*n
    c = F(m*m * (4+6*(n-1)*(p-1)), 48*n**4)
    sequence.append(dict(N=n, P=p, M=m, C=str(c), decimal=float(c)))
assert sequence[-1]["decimal"] < 1.5
print("Rademacher alpha=2 beta=3: C(N=10000)="
      f"{sequence[-1]['decimal']:.10f}; predicted limit=1.5")

payload = dict(cases=results, scalar_MMSE_coefficients=["1", "-1", "1", "-5/3"],
               scalar_MI_coefficients=["0", "1/2", "-1/4", "1/6", "-5/24"],
               proportional_sequence=sequence, predicted_limit="3/2",
               effective_nice=os.getpriority(os.PRIO_PROCESS, 0),
               elapsed_seconds=round(time.monotonic()-START, 6),
               peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
assert payload["peak_rss_bytes"] < 1024**3
Path("verification.json").write_text(json.dumps(payload, indent=2) + "\n")
print(f"ALL {len(results)} exact cases passed; data: verification.json")
print(f"elapsed_seconds={payload['elapsed_seconds']} "
      f"peak_rss_bytes={payload['peak_rss_bytes']} nice={payload['effective_nice']}")
