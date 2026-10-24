#!/usr/bin/env python3
from fractions import Fraction

def compiler(kappa, eta):
    k=Fraction(kappa); e=Fraction(eta)
    q=1-k*e
    a=2-2*e
    assert q>0 and e>0
    return q,a

cases=[
    (Fraction(1),Fraction(1,4),Fraction(3,4),Fraction(3,2)),
    (Fraction(2),Fraction(1,4),Fraction(1,2),Fraction(3,2)),
    (Fraction(3),Fraction(1,4),Fraction(1,4),Fraction(3,2)),
    (Fraction(4),Fraction(1,5),Fraction(1,5),Fraction(8,5)),
    (Fraction(5),Fraction(1,6),Fraction(1,6),Fraction(5,3)),
]
for k,e,q0,a0 in cases:
    q,a=compiler(k,e)
    assert (q,a)==(q0,a0)
    print(f'kappa={k} eta={e} q={q} a={a}')

for m in range(2,101):
    e=Fraction(1,4)-Fraction(1,4*m)
    q,a=compiler(4,e)
    assert q==Fraction(1,m)
    assert a==Fraction(3,2)+Fraction(1,2*m)

print('PASS: R11-C001 exact exponent arithmetic; calculus implication checked in written audit.')
