import math

nu = 1/48
x = 1/130
c0 = 12/math.sqrt(47)
eta = 0.0037987340155334467
f = c0*eta
Rbd = (x + 2*f)/(1-nu)
Dbd = (x + (1+nu)*f)/(1-nu)
offbd = math.sqrt(2)*Rbd + f
gapbd = 2*Rbd

# Roots of [2(x+2 c0 d)/(1-nu)]^2 = 2 c0 d.
# Solve the quadratic directly.
a = 16*c0*c0
b = 16*x*c0 - 2*c0*(1-nu)**2
c = 4*x*x
disc = b*b - 4*a*c
dminus = (-b-math.sqrt(disc))/(2*a)
dplus = (-b+math.sqrt(disc))/(2*a)

def gap_upper(d):
    return 2*(x+2*c0*d)/(1-nu)

def g(d):
    return math.sqrt(2*c0*d)

assert 0 < dminus < eta < dplus
assert gap_upper(eta) < g(eta)
assert abs(gap_upper(dminus)-g(dminus)) < 1e-10
assert abs(gap_upper(dplus)-g(dplus)) < 1e-10

print('c0', c0)
print('eta', eta)
print('Frob_residual_over_L', f)
print('Rop_over_L', Rbd)
print('Dop_over_L', Dbd)
print('offdiag_E_Frob_over_L', offbd)
print('carrier_gap_over_L', gapbd)
print('dminus', dminus)
print('dplus', dplus)
print('g_eta', g(eta))
print('scalar_residual_eta', math.sqrt(c0*eta)+c0*eta)
print('Frob_residual_dminus', c0*dminus)
print('QFORM_B08_R40_CARRIER_CONTRACTION_CHECK_PASS')
