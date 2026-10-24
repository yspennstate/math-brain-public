#!/usr/bin/env python3
"""
Exact finite core for HARD7-05 run 3.

Claim certified here:
For x in (0,1), the polynomial/radical inequality obtained from
R_{H=1/4}(t) >= cosh(4t/3)/cosh(5t/3), x=e^{-t/12},
has the sign pattern used in the written proof.

This is a self-check, not an independent audit.
"""
import sympy as sp

x = sp.symbols("x")
QQ = sp.QQ

# After multiplying the covariance inequality by the positive factor
# 3*x^15*(1+x^40), the desired inequality is
# (1+x^40)*(1-x^12)^(5/2) + P(x) >= 0.
P = sp.Poly(
    sp.expand(
        (sp.Rational(5,2)*(x**12 + x**18) - 1 - x**30)*(1+x**40)
        - 3*x**19*(1+x**32)
    ),
    x, domain=QQ
)

# Exact polynomial C defined by P=-(1-x)^2(x^2+x+1)C/2.
denC = (x-1)**2*(x**2+x+1)
C_expr = sp.cancel(-2*P.as_expr()/denC)
assert sp.denom(C_expr) == 1
C = sp.Poly(sp.expand(C_expr), x, domain=QQ)
assert sp.expand(P.as_expr() + denC*C.as_expr()/2) == 0

# Squared comparison core:
# D=(1+x^40)^2(1-x^12)^5-P^2
#   = -x^18(1-x)^4(x^2+x+1)^2 Q/4.
D = sp.Poly(
    sp.expand((1+x**40)**2*(1-x**12)**5 - P.as_expr()**2),
    x, domain=QQ
)
denQ = x**18*(x-1)**4*(x**2+x+1)**2
Q_expr = sp.cancel(-4*D.as_expr()/denQ)
assert sp.denom(Q_expr) == 1
Q = sp.Poly(sp.expand(Q_expr), x, domain=QQ)
assert sp.expand(D.as_expr() + denQ*Q.as_expr()/4) == 0

# Exact real-root isolation. SymPy intervals() uses exact rational arithmetic.
eps = sp.Rational(1,10**6)
C_intervals = sp.intervals(C, eps=eps)
Q_intervals = sp.intervals(Q, eps=eps)

def unit_intervals(intervals):
    ans = []
    for (a,b), mult in intervals:
        if b <= 0 or a >= 1:
            continue
        assert 0 < a < b < 1
        ans.append(((a,b), mult))
    return ans

C_unit = unit_intervals(C_intervals)
Q_unit = unit_intervals(Q_intervals)

assert len(C_unit) == 1 and C_unit[0][1] == 1
assert len(Q_unit) == 1 and Q_unit[0][1] == 1

(ca, cb), _ = C_unit[0]
(qa, qb), _ = Q_unit[0]

# The unique C-root lies strictly before the unique Q-root.
assert cb < qa

# Endpoint signs orient the two sign changes.
assert C.eval(0) > 0 and C.eval(1) < 0
assert Q.eval(0) < 0 and Q.eval(1) > 0

# Therefore C(x)>0 => Q(x)<0 on (0,1), exactly the implication
# needed when P(x)<0.
# Arithmetic of the comparison process's persistence exponent:
reference_exponent = sp.Rational(10,3) * sp.Rational(3,8) * sp.Rational(1,10)
assert reference_exponent == sp.Rational(1,8)

print("P_degree =", P.degree())
print("C_degree =", C.degree())
print("Q_degree =", Q.degree())
print("C(0), C(1) =", C.eval(0), C.eval(1))
print("Q(0), Q(1) =", Q.eval(0), Q.eval(1))
print("C_real_root_intervals =", C_intervals)
print("Q_real_root_intervals =", Q_intervals)
print("C_unit_root =", C_unit[0])
print("Q_unit_root =", Q_unit[0])
print("C_root_before_Q_root =", cb < qa)
print("reference_exponent =", reference_exponent)
print("ALL_EXACT_CHECKS_PASS")
