from fractions import Fraction as F
import math

# Pass-2 reconstruction of introductory counterexamples and scaling.
for z in (1/2, 1/4, 1/16, 1/256):
    p1 = 0.5*math.acosh(1/math.sqrt(z))
    p2 = 0.5*math.asinh(math.sqrt((1-z)/z))
    assert abs(p1-p2) < 1e-13
vals=[0.5*math.acosh(1/math.sqrt(z)) for z in (1/4,1/16,1/256,1/65536)]
assert all(vals[i+1] > vals[i] for i in range(len(vals)-1))

K=F(7,3); s=F(11,5)
assert (s/(K*K))*(K/s) == 1/K
assert (s/(K*K))*(K*K/s) == 1
assert 1/(s/(K*K)) == K*K/s

a=F(3,2); dz=F(0)
assert not (dz/a > 0)
assert abs(a)*abs(dz) == 0

print("PASS: introductory density formula equivalence and logarithmic growth")
print("PASS: K^2/s scaling algebra")
print("PASS: line-398 endpoint diagnostic (strict indicator false, denominator zero)")
print("sample p_Z values:", [float(x) for x in vals])
