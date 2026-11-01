#!/usr/bin/env python3
"""Independent finite-core audit for R19-I0084-C002.

This does NOT replace the analytic audit of Huang--Wang Proposition 3.2,
Theorem 3.6/Remark 3.7, and Theorem 3.9. It independently verifies the
finite constants and elementary algebra used by the R19 sparse-gap proof.
All certified comparisons use exact integer/Fraction arithmetic.
"""
from fractions import Fraction

# Weight upper bound:
# w_1 = 1/8.  For n>=2, A_n>=16 and
# w_n=2^{-n} A_n^{-n} <= 2^{-5n}=32^{-n}.
tail = Fraction(1,32**2) / (1-Fraction(1,32))
W_upper = Fraction(1,8)+tail
print("tail_upper =", tail)
print("W_upper =", W_upper)
assert tail == Fraction(1,992)
assert W_upper < Fraction(1,4)
w0_lower = 1-W_upper
assert w0_lower > Fraction(3,4)
print("w0_lower =", w0_lower)

# Gap geometry: A_n=2^(2^n), so A_{n-1}=sqrt(A_n).
# For n>=2, A_n>=16 => sqrt(A_n)<=A_n/4.
for n in range(2,10):
    A=2**(2**n)
    prev=2**(2**(n-1))
    assert prev*prev==A
    assert 4*prev<=A
print("gap_geometry_exact: PASS n=2..9; general step is exponent identity")

# Cauchy-transform bounds at c=-A/2.
# G(c) <= -2 w0/A + 2 W/A.
# With w0>3/4 and W<1/4 this is < -1/A.
coeff_G = -2*Fraction(3,4)+2*Fraction(1,4)
assert coeff_G == -1
print("G_coefficient_boundary =", coeff_G, "strict inequalities give G<-1/A")

# I2 terms:
# atom 0 < 4/A^2
# k<n < 16 W/A^2 < 4/A^2
# k>=n < 4 W/A^2 < 1/A^2
I2_coeff_boundary = Fraction(4,1)+16*Fraction(1,4)+4*Fraction(1,4)
assert I2_coeff_boundary == 9
print("I2_coefficient_boundary =", I2_coeff_boundary,
      "strict inequalities give I2<9/A^2")

# Derivative:
# a=-G>1/A and I2<9/A^2 imply
# t I2/(2 a^(3/2)) < 9t/(2 sqrt(A)).
# sqrt(A)>9t then RHS < 1/2, hence H_t'(c)>1/2.
ratio_boundary = Fraction(9,2)/9
assert ratio_boundary == Fraction(1,2)
print("derivative_loss_boundary =", ratio_boundary,
      "strict sqrt(A)>9t gives loss<1/2")

# Positive-half-stable transform coefficient:
# -exp(i*pi*alpha*rho) z^(1-alpha), alpha=1/2,rho=1
# has coefficient -i. Record the exact symbolic specialization.
print("free_stable_transform: -exp(i*pi/2)*sqrt(z) = -i*sqrt(z)")

# Every atom weight is <1: w0<1 because W>0; w_n<=w1=1/8 for n>=1.
assert Fraction(1,8)<1
print("atom_weights_lt_one: PASS")

print("R18_INDEPENDENT_R19_C002_FINITE_CORE_PASS")
