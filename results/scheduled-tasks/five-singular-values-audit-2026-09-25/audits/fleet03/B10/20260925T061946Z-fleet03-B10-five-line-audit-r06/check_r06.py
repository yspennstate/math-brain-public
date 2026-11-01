from fractions import Fraction as F
import math

for p in [F(3,2),F(2,1),F(7,3)]:
    a=F(5,7)
    assert 2*a+2*a/(p-1)==2*a*p/(p-1)

for q in [F(1,1),F(9,16),F(25,49)]:
    sq=F(math.isqrt(q.numerator), math.isqrt(q.denominator))
    assert sq*sq==q
    assert 4*sq+4*sq==8*sq

for n in range(1,1000):
    beta=n/1000
    assert beta*math.log(1/beta) <= 1-beta + 1e-14

p_at_2=0.0
assert p_at_2==0.0
try:
    math.log(p_at_2)
    raise AssertionError("log(0) unexpectedly returned")
except ValueError:
    pass

def kappa(z):
    return max(1-abs(z),0)
for j in range(-20,21):
    z=j/10
    assert abs(kappa(z)-kappa(-z))<1e-15
assert F(1,2)+F(1,2)==1

for k in range(1,7):
    assert F(2**k,2**k)==1

assert 15*F(100,9) < 167
assert F(122,10)*F(2055,1000) < 26
assert 12*77*77 < 267*267
print("ALL R06 EXACT/FINITE CHECKS PASS")
print("NEW_LITERAL_GAP: short.tex line 224 may evaluate ordinary log at p(y)=0")
print("NO_THEOREM_LEVEL_COUNTEREXAMPLE_FOUND_IN_LINES_80_379")
