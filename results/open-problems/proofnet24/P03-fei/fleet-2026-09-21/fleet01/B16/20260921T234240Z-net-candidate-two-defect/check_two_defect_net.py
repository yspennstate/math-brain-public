#!/usr/bin/env python3
"""Self-check for B16 two-defect NET calculation. Standard library only."""
from fractions import Fraction
from decimal import Decimal, getcontext
import math

getcontext().prec = 80

# Exact spectrum normalization and influence bookkeeping.
for n in range(2, 31):
    M = 1 << n
    x = Fraction(4, M)
    p0 = (1-x)**2
    K = M//2 - 1
    assert p0 + K*x*x == 1
    J = Fraction(4*n, M)
    assert J > 0

# Stable high-precision entropy tests and asymptotic expansion.
ln2 = Decimal(2).ln()
for n in range(3, 121):
    M = Decimal(2) ** n
    x = Decimal(4) / M
    H = -Decimal(2)*(Decimal(1)-x)**2*(Decimal(1)-x).ln() \
        -Decimal(2)*x*(Decimal(2)-x)*x.ln()
    J = Decimal(4*n) / M
    assert H < Decimal(4)*ln2*J
    approx = Decimal(4)*ln2 + (Decimal(2)-Decimal(8)*ln2)/Decimal(n)
    # Error is exponentially small after the 1/n term.
    assert abs(H/J-approx) < Decimal(20)*x

kappa = Decimal(2)/Decimal(3) + Decimal(3).ln()/Decimal(2)
limit_net = Decimal(4)*ln2-kappa
fallback = limit_net + Decimal('1.5')
assert abs(limit_net-Decimal('1.5566159112390596')) < Decimal('1e-15')
assert abs(fallback-Decimal('3.0566159112390596')) < Decimal('1e-15')

# Pointwise self-phase obstruction: M*Xi(c sqrt(M)) -> 4 c^2.
for c in (Decimal('0.5'), Decimal('1'), Decimal('2')):
    vals=[]
    for n in (20, 24, 28, 32):
        M = Decimal(2) ** n
        # Decimal has no trig; float is safe here because arguments to the
        # small-angle term are tiny and we only check convergence diagnostics.
        Mf=float(M)
        sf=float(c)*math.sqrt(Mf)
        xf=4.0/Mf
        Kf=Mf/2.0-1.0
        X=math.cos(sf)-math.cos((1.0-xf)*sf)+Kf*(1.0-math.cos(xf*sf))
        vals.append(X)
    target=4.0*float(c*c)
    assert abs(vals[-1]-target) < 0.02*max(1.0,target)

print('PASS')
print('limit_net_over_J =', limit_net)
print('archive_family_bound_constant =', fallback)
print('checked exact spectrum n=2..30 and entropy n=3..120')
