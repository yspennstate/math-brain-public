"""Exact small algebra checks, standard library only; no TW simulation.

Run with one thread and nice -n 15 as recorded in LOG.md. Refuse to do
computational work if the effective nice value is below 15.
"""

import os
import sys

if os.getpriority(os.PRIO_PROCESS, 0) < 15:
    print("NOT RUN: process nice value is below 15; priority adjustment unavailable.")
    sys.exit(77)

import itertools
import math
import time
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache

started = time.monotonic()


def check_time():
    if time.monotonic() - started > 60:
        raise RuntimeError("60-second scalar-check budget exceeded")


def falling(n, k):
    return math.prod(range(n-k+1, n+1)) if n >= k else 0


def spherical_even(d, s):
    return Q(math.prod(range(1, 2*s, 2)),
             math.prod(d+2*j for j in range(s)))


def fourth_centered(d):
    return sum(math.comb(4, j)*(-Q(1, d))**(4-j)*spherical_even(d, j)
               for j in range(5))


@lru_cache(None)
def monomial_sphere(d, exponents):
    if any(e % 2 for e in exponents):
        return Q(0)
    half_degree = sum(exponents)//2
    numerator = math.prod(math.prod(range(1, e, 2)) for e in exponents)
    denominator = math.prod(d+2*j for j in range(half_degree))
    return Q(numerator, denominator)


def integrate_graph(d, edges):
    """Expand each (u_i dot u_j)^2-1/d in coordinates and integrate.

    This uses neither the traceless-tensor identity nor fourth-trace formula.
    Only scalar spherical monomial moments and independence of vertices enter.
    """
    vertices = 1 + max(max(edge) for edge in edges)
    zero = (0,)*(vertices*d)
    polynomial = {zero: Q(1)}
    for i, j in edges:
        factor = [(zero, -Q(1, d))]
        for a in range(d):
            for b in range(a, d):
                exponent = [0]*(vertices*d)
                for vertex in (i, j):
                    exponent[vertex*d+a] += 1
                    exponent[vertex*d+b] += 1
                factor.append((tuple(exponent), Q(1 if a == b else 2)))
        result = {}
        for old, coefficient in polynomial.items():
            for increment, scalar in factor:
                key = tuple(x+y for x, y in zip(old, increment))
                result[key] = result.get(key, Q(0)) + coefficient*scalar
        polynomial = {key: value for key, value in result.items() if value}
        check_time()
    answer = Q(0)
    for powers, coefficient in polynomial.items():
        moment = Q(1)
        for vertex in range(vertices):
            moment *= monomial_sphere(d, powers[vertex*d:(vertex+1)*d])
        answer += coefficient*moment
    return answer


# Independent audit of the predecessor: exact rational kernel cancellation.
for v, t, u in ((Q(2), Q(5, 2), Q(-1, 5)),
                (Q(3, 2), Q(4, 3), Q(-1, 4)),
                (Q(1), Q(1, 2), Q(-1, 3))):
    delta = t-v
    lhs = t/(1+t*u)-v/(1+v*u)-delta/(1+v*u)**2
    rhs = -u*delta**2/((1+v*u)**2*(1+t*u))
    assert lhs == rhs
print("Predecessor rational cancellation identity: 3 exact checks passed")

for d in (2, 3, 10, 100):
    assert spherical_even(d, 3) == Q(15, d*(d+2)*(d+4))
    simplified = Q(12*(d-1)*(5*d*d-13*d+12),
                   d**4*(d+2)*(d+4)*(d+6))
    assert fourth_centered(d) == simplified
    assert simplified <= Q(60, d**4)
print("Spherical sixth and centered eighth moments: exact checks passed")

graphs = (
    ((0, 1),)*4,
    ((0, 1), (0, 1), (0, 2), (0, 2)),
    ((0, 1), (1, 2), (2, 3), (3, 0)),
)
for d in (2, 3):
    c, tau = 1-Q(1, d), Q(2, d*(d+2))
    expected = (fourth_centered(d), (c*tau)**2, c*tau**3)
    computed = tuple(integrate_graph(d, edges) for edges in graphs)
    assert computed == expected
    print(f"d={d}: coordinate integrations pair/star/cycle = "
          + ", ".join(str(value) for value in computed))

# Count all walks directly, independently of the falling-factorial count.
for n in range(2, 8):
    counts = Counter()
    for walk in itertools.product(range(n), repeat=4):
        if all(walk[i] != walk[(i+1) % 4] for i in range(4)):
            counts[len(set(walk))] += 1
    assert counts[2] == falling(n, 2)
    assert counts[3] == 2*falling(n, 3)
    assert counts[4] == falling(n, 4)
print("Fourth-trace walk multiplicities: exhaustive n=2,...,7 passed")


def finite_edge(n, r, spike, method):
    # Exactly trace-preserving rank-one population, a subcase of the new lemma.
    top, bulk = 1+spike, 1-spike/(n-1)
    def f(u):
        return -1/u+r*(top/(1+top*u)+(n-1)*bulk/(1+bulk*u))/n
    lo, hi = -1/top+1e-12, -1e-12
    if method == "derivative":
        for _ in range(130):
            u = (lo+hi)/2
            derivative = 1/u**2-r*(top**2/(1+top*u)**2
                +(n-1)*bulk**2/(1+bulk*u)**2)/n
            if derivative < 0:
                lo = u
            else:
                hi = u
        return f((lo+hi)/2)
    ratio = (math.sqrt(5)-1)/2
    left, right = hi-ratio*(hi-lo), lo+ratio*(hi-lo)
    for _ in range(130):
        if f(left) < f(right):
            hi, right = right, left
            left = hi-ratio*(hi-lo)
        else:
            lo, left = left, right
            right = lo+ratio*(hi-lo)
    return min(f(left), f(right))


maximum_disagreement = 0.0
for r in (0.25, 0.5, 2.0, 4.0):
    spike = 0.5*math.sqrt(r)
    e0 = (1+math.sqrt(r))**2
    shifts = []
    for n in (1000, 10000, 100000):
        edge = finite_edge(n, r, spike, "derivative")
        other = finite_edge(n, r, spike, "minimization")
        maximum_disagreement = max(maximum_disagreement, abs(edge-other))
        assert abs(edge-other) < 1e-10
        assert edge >= e0-1e-12
        shifts.append(n*(edge-e0))
    # Formula (15) gives the first-order 1/n coefficient at the scalar edge.
    u0 = -1/(1+math.sqrt(r))
    coefficient = r*(-u0)*spike**2/((1+u0)**2*(1+(1+spike)*u0))
    assert abs(shifts[-1]/coefficient-1) < 0.005
    print(f"r={r:g}: n*(edge-e0)={shifts[-1]:.9f}; "
          f"independent first-order coefficient={coefficient:.9f}")
print(f"Edge solver maximum disagreement: {maximum_disagreement:.3e}")

for r in (0.25, 0.5, 2.0, 4.0):
    u0 = -1/(1+math.sqrt(r))
    for fraction in (0.5, 1.0, 1.5):
        spike = fraction*math.sqrt(r)
        separation = 1+(1+spike)*u0
        expected = (1-fraction)*math.sqrt(r)/(1+math.sqrt(r))
        assert abs(separation-expected) < 1e-14
print("Subcritical / critical / supercritical pole signs: passed")

for m, n in ((200, 500), (500, 200), (317, 991), (991, 317)):
    r, b = n/m, m/n
    left = r**(1/6)/(1+math.sqrt(r))**(4/3)*r*m**(2/3)
    right = b**(1/6)/(1+math.sqrt(b))**(4/3)*n**(2/3)
    assert abs(left/right-1) < 1e-14
print("Transposition normalization: both rectangular orientations passed")
print(f"PASS: exact algebra and scalar edges only; elapsed {time.monotonic()-started:.3f}s")
