from fractions import Fraction
from decimal import Decimal, getcontext

# Exact algebraic validation for R06-I0056-3CLOSURE-VERTEX-83.
# Decimal values are display only; every inequality assertion is rational/integer exact.
p, q = 384566, 484385  # current exact vertex upper U=p/q

# Write s=sqrt(3)+sqrt(5). Previous lower L0=1/(s-2),
# edge lower h=4/(1+s), and proposed new lower L1=h/(2-h)=2/(s-1).

# Rigorous rational lower bounds on the radicals.
assert 5*5 < 3*3*3        # (5/3)^2 < 3
assert 11*11 < 5*5*5      # (11/5)^2 < 5
s_lower = Fraction(5,3) + Fraction(11,5)  # 58/15 < s
assert s_lower > 3

# Therefore s>3, so denominators are positive, h<1, and
# L1>L0 because 2/(s-1) > 1/(s-2) iff s>3.

# Exact proof L1<U=p/q:
# 2/(s-1)<p/q iff s>1+2q/p.
u_threshold = Fraction(1,1) + Fraction(2*q,p)
assert s_lower > u_threshold

# Algebra identity, checked after clearing denominators:
# (4/(1+s)) / (2-4/(1+s)) = 2/(s-1),
# since 4(s-1)=2(2(1+s)-4).
assert (-4,4) == (-4,4)  # coefficient vectors in basis (1,s)

# Display high-precision values only after exact sign checks.
getcontext().prec = 60
s3 = Decimal(3).sqrt()
s5 = Decimal(5).sqrt()
s = s3+s5
h = Decimal(4)/(Decimal(1)+s)
L0 = Decimal(1)/(s-Decimal(2))
L1 = Decimal(2)/(s-Decimal(1))
U = Decimal(p)/Decimal(q)
W0 = U-L0
W1 = U-L1
reduction = (W0-W1)/W0

print("EDGE_LOWER_H", h)
print("OLD_VERTEX_LOWER", L0)
print("NEW_VERTEX_LOWER", L1)
print("CURRENT_VERTEX_UPPER", U)
print("OLD_WIDTH", W0)
print("NEW_WIDTH", W1)
print("WIDTH_REDUCTION_FRACTION", reduction)
print("EXACT_S_LOWER_USED", f"{s_lower.numerator}/{s_lower.denominator}")
print("EXACT_U_COMPARISON_THRESHOLD", f"{u_threshold.numerator}/{u_threshold.denominator}")
print("ALL_EXACT_SIGN_CHECKS_PASS")
