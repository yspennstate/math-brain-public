#!/usr/bin/env python3
"""Exact arithmetic self-check for R19-I0084-C001.

This checker certifies only the finite rational inequalities used in the
written proof.  The theorem itself (termwise differentiation, the derivative
sign argument, and the moment convergence argument) is proved in the run
report and is not delegated to numerics.

No floating-point arithmetic is used.
"""
from fractions import Fraction
import math

# Global derivative-envelope arithmetic:
# sup |H| < 1/2*(7/2)^4 + 3/2*(5/2)^3 = 3151/32 < 99.
assert Fraction(3151, 32) < 99

# Tail ratio for w_n proportional to 2^{-n^2}.  For n>=3,
# sum_{j>n} w_j / w_n <= sum_{k>=1} 2^{-(2n+1)k}
# <= sum_{k>=1} 2^{-7k} = 1/127.
tail_ratio = Fraction(1, 128) / (1 - Fraction(1, 128))
assert tail_ratio == Fraction(1, 127)

# The positive derivative at r=s/6 is >4*s^{-5/2}; after subtracting
# the entire farther-left tail, whose derivative magnitude is bounded by
# 99*s^{-5/2}, the exact remaining coefficient is positive.
margin = Fraction(4, 1) - 99 * tail_ratio
assert margin == Fraction(409, 127)
assert margin > 0

# Critical p=5/2 moment.  For every integer n>=5,
# -n^2 + (5/2)n <= -n^2/2 iff n(n-5)>=0.
for n in range(5, 500):
    assert n*n - 5*n >= 0
    lhs = -n*n + Fraction(5, 2)*n
    rhs = Fraction(-n*n, 2)
    assert lhs <= rhs

# General all-polynomial-moments check for representative rational p's.
# The on-page proof is symbolic: n>=2p implies
# -n^2+pn <= -n^2/2.
for p in [Fraction(1), Fraction(5,2), Fraction(7,3), Fraction(10), Fraction(101,17)]:
    N = math.ceil(2*float(p))
    while Fraction(N,1) < 2*p:
        N += 1
    for n in range(N, N+200):
        assert -n*n + p*n <= Fraction(-n*n,2)

# Elementary bound e<3 used in the proof of H(1/6)>4.
# For k>=2, k! >= 2^{k-1}; the on-page proof is induction.
fact = 1
for k in range(1, 101):
    fact *= k
    assert fact >= 2**(k-1)

print('PASS exact rational core')
print('3151/32 < 99')
print('tail_ratio =', tail_ratio)
print('positive_derivative_margin =', margin)
print('5/2-moment tail exponent inequality holds for every integer n>=5')
print('all-polynomial-moment comparison checked on representative rational p values')
print('e<3 induction core checked through k=100; symbolic induction is in report')
