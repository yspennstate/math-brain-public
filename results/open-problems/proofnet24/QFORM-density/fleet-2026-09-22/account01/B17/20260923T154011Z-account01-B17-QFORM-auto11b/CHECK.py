import math

# Deterministic arithmetic/check companion for REPORT.md.
# The analytic proof of monotonicity of g is in the report; here we verify
# the endpoint constants and sample the radial representation numerically.

SQ2 = math.sqrt(2.0)
Cminus = math.sqrt(6.0*math.pi)*math.erf(math.sqrt(1.5))
Kexact = 0.5*(Cminus + 3.0*SQ2)
Kelem = 97.0/48.0 + 1.5*SQ2
TARGET = 3.0*SQ2

assert Cminus < 97.0/24.0
assert Kexact < Kelem < TARGET
# Exact rational-square certificate used by the endpoint source:
assert 9409 < 18*576

def g_midpoint(z, n=40000):
    if z == 0.0:
        return math.sqrt(math.pi)/(2.0*math.sqrt(6.0))
    if z == 1.0:
        return 0.5
    L = 1.0/(2.0*math.sqrt(z))
    h = L/n
    total = 0.0
    for i in range(n):
        r = (i+0.5)*h
        total += math.exp(-6.0*(1.0-z)*r*r)
    return total*h

# Diagnostics consistent with the proved g-monotonicity.
grid = [0.0, 0.1, 0.25, 0.5, 0.75, 0.9, 1.0]
vals = [g_midpoint(z) for z in grid]
assert all(vals[i] <= vals[i+1] + 1e-10 for i in range(len(vals)-1))
assert abs(6.0*SQ2*vals[3] - Cminus) < 1e-8

print('Cminus =', repr(Cminus))
print('Kexact =', repr(Kexact))
print('Kelem =', repr(Kelem))
print('3sqrt2 =', repr(TARGET))
print('gap_exact =', repr(TARGET-Kexact))
print('PASS QFORM_B17_N3_UNIFORM_CONE_GAP')
