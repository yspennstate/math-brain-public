#!/usr/bin/env python3
"""
R11 exact-arithmetic certificate for the speed-rate compiler.

This checker does NOT prove an asymptotic SAW exponent. It certifies the
rational exponent arithmetic used in R11-GH-C001 and the finite algebraic
relations stated in the report.
"""
from fractions import Fraction

def compiler(kappa, eta):
    kappa=Fraction(kappa)
    eta=Fraction(eta)
    q=1-kappa*eta
    a=2-2*eta
    assert eta>0
    assert q>0
    return q,a

tests=[
    (Fraction(1), Fraction(1,4)),
    (Fraction(2), Fraction(1,4)),
    (Fraction(3), Fraction(1,4)),
    (Fraction(4), Fraction(1,5)),
    (Fraction(5), Fraction(1,6)),
]
for k,e in tests:
    q,a=compiler(k,e)
    print(f"kappa={k}, eta={e}: q={q}, a={a}")

# Direct Flory upper exponent a=3/2 via eta=1/4 requires kappa<4.
for k in [Fraction(1),Fraction(2),Fraction(3),Fraction(15,4),Fraction(399,100)]:
    q,a=compiler(k,Fraction(1,4))
    assert a == Fraction(3,2)
    assert q > 0

# Borderline kappa=4 cannot use eta=1/4 in the stated exponential-tail compiler,
# but any eta<1/4 gives any exponent a>3/2.
k=Fraction(4)
for m in [5,10,100,1000]:
    eta=Fraction(1,4)-Fraction(1,4*m)
    q,a=compiler(k,eta)
    assert q == Fraction(1,m)
    assert a == Fraction(3,2)+Fraction(1,2*m)

# Any finite kappa admits some eta>0, hence some a<2.
for k in range(1,101):
    eta=Fraction(1,2*k)
    q,a=compiler(k,eta)
    assert q == Fraction(1,2)
    assert a < 2

print("PASS: exact rational exponent arithmetic.")
