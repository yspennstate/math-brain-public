#!/usr/bin/env python3
"""R01 independent exact arithmetic audit for R02-KLS-C004/X004.
This checks the finite algebraic/probability-exponent core only.
The posterior continuity and filtering equivalence are audited in the R01 report.
"""
from fractions import Fraction as Q

a = Q(1,3)
b = Q(2,5)
c = Q(1,10)  # t_n = c / log n

# t=0 posterior: shifted exponential of rate 1-y.
vmin = 1 / (1-a)**2
vmax = 1 / (1-b)**2
assert vmin == Q(9,4)
assert vmax == Q(25,9)
assert vmin > 2

# Witness interval and endpoint implication.
width0 = b-a
assert width0 == Q(1,15)
# For t <= 1/30, [a+t,b] has length >=1/30.
tcap = Q(1,30)
assert width0 - tcap == Q(1,30)

# If X in [-1,0] and B in [a+t,b], then t X + B in [a,b].
# Exact endpoint inequalities are a+t-t=a and b+0=b.
assert a+tcap-tcap == a

# Gaussian exponent at upper endpoint b:
# exp(-b^2/(2 t_n)) = n^{-b^2/(2c)}.
power = b*b/(2*c)
assert power == Q(4,5)
assert 1-power == Q(1,5) > 0

# Thus n * p_n has polynomial factor n^(1/5) (times sqrt(log n)).
print("R01 independent audit of R02-C004 finite core")
print("posterior variance interval at t=0:", vmin, vmax)
print("witness width:", width0, "width at t=1/30:", width0-tcap)
print("Gaussian n exponent:", power, "remaining n exponent:", 1-power)
print("R01-AUDIT-R02-KLS-C004-X004-03=PASS_AT_STATED_SCOPE")
print("ALL_EXACT_CHECKS_PASS")
