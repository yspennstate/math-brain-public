from fractions import Fraction

# P26 independent exact checks for the L=6 analytic-family inequalities
# in P20-I0081-LOGUNIFORM-FAMILY-02.

# 22/7 upper bound implies pi^2 < 484/49 < 10.
assert Fraction(484,49) < 10

# e^6 > (sum_{k=0}^5 1/k!)^6 = (163/60)^6 > 400, hence a=e^-6 < 1/400.
assert Fraction(163,60) ** 6 > 400

# derivative lower bound A >= L*(1-a)/(1+a)-1 with L=6, a<1/400.
A_lower = 6*Fraction(399,401) - 1
assert A_lower == Fraction(1993,401) and A_lower > 0

# P20's rational upper envelope for C_6 after pi^2<10 and a<1/400.
C6_upper = Fraction(1,400) * Fraction(46**2,6) * Fraction(400,399)**4
assert C6_upper == Fraction(67712000000,76034875203)
assert C6_upper < 1

# logarithmic derivative upper bound used to make F(L) decreasing for L>=6.
logder_upper = -1 + Fraction(3,6)
assert logder_upper == Fraction(-1,2) and logder_upper < 0

print('P26-I0081-AUDIT-EXACT-CHECK: PASS')
print('A_lower =', A_lower)
print('C6_upper =', C6_upper)
print('1-C6_upper =', 1-C6_upper)
print('logder_upper =', logder_upper)
