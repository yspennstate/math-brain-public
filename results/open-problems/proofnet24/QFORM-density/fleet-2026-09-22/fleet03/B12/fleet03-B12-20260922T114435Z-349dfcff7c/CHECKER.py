from fractions import Fraction
import math

r0 = Fraction(193, 200)
pair_det = (1-r0)/2
triple_kappa = (3*r0-1)/4

assert pair_det == Fraction(7, 400)
assert triple_kappa == Fraction(379, 800)

# Exact principal-block spectral formulas for B_r=-I+(1+r)J/4.
def c2_eigs(r):
    return (-1.0, (r-1.0)/2.0)

def c3_eigs(r):
    return (-1.0, -1.0, (3.0*r-1.0)/4.0)

# Critical complementary degeneracies.
assert abs(c3_eigs(1/3)[2]) < 1e-15
assert abs(((1-(1/3))/2) - 1/3) < 1e-15
assert abs(c2_eigs(1.0)[1]) < 1e-15
assert abs(c3_eigs(1.0)[2] - 0.5) < 1e-15

C3 = 2*math.pi + 3*math.sqrt(3)
pair_constant = 20*math.pi/math.sqrt(7)
triple_constant = 800*C3/379
critical_triple = math.pi*math.sqrt(3)
critical_pair = 2*C3

assert pair_constant < 23.749
assert triple_constant < 24.231
assert critical_triple < 5.442
assert critical_pair < 22.959

# Check the switch covers the whole real line with the appropriate positive resource.
for j in range(-10000, 20001):
    r = j/1000
    if r <= float(r0):
        assert (1-r)/2 >= float(pair_det) - 1e-12
    else:
        kappa = min(1.0, abs(3*r-1)/4)
        assert kappa >= float(triple_kappa) - 1e-12

print('PASS')
print('r0=', float(r0))
print('pair_det_at_switch=', float(pair_det))
print('triple_kappa_at_switch=', float(triple_kappa))
print('pair_constant=', repr(pair_constant))
print('triple_constant=', repr(triple_constant))
print('Cstar=', repr(max(pair_constant, triple_constant)))
print('r=1/3 pair_bound=', repr(critical_triple))
print('r=1 triple_bound=', repr(critical_pair))
