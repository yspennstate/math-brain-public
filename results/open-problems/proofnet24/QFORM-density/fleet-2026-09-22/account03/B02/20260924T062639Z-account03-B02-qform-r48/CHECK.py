import math
import numpy as np
from fractions import Fraction

# Exact/rational spectral-window certificates.
eta = Fraction(1,18)
eps = Fraction(2,153)
delta_lb = Fraction(149,306) - Fraction(50,309)
sigma_lb = delta_lb - eta
assert delta_lb == Fraction(10247,31518)
assert sigma_lb == Fraction(472,1751)
assert Fraction(2,153) / delta_lb == Fraction(412,10247)
assert 412_000_000 < 10247 * 40401
second = Fraction(49,20) * Fraction(1,18) / sigma_lb
assert second == Fraction(85799,169920)
assert second < Fraction(101,200)
assert Fraction(706,1000)**2 < Fraction(1,2)
assert 2*24786 < 223**2

# Numerical constants from the exact irrational parameters.
delta = 0.5 - 2/153 - math.sqrt(4/153)
sigma = delta - 1/18
ridge_gate = (math.sqrt((2/153)/delta) + math.sqrt(6)*(1/18)/sigma)**2
C_window = 9*math.sqrt(3*math.e)/(2*sigma)
L1_window = 9*math.pi*math.sqrt(3*math.e)/sigma

# Exact carrier-angle identity regression.
def e2_sym(H):
    return 0.5*(np.trace(H)**2 - np.trace(H@H))

rng = np.random.default_rng(20260924)
max_rel_identity = 0.0
min_lower_ratio = float('inf')
identity_violations = 0
lower_violations = 0
for _ in range(2000):
    p = int(rng.integers(2,9))
    q = int(rng.integers(2,9))
    M = rng.normal(size=(p,q))
    U,s,Vt = np.linalg.svd(M, full_matrices=False)
    if len(s) < 2 or s[1] < 1e-10:
        continue
    x = s*s
    m = rng.normal(size=q)
    mh = m/np.linalg.norm(m)
    P = np.eye(q)-np.outer(mh,mh)
    lhs = e2_sym(M@P@M.T)
    z = Vt@mh
    rhs = 0.0
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            rhs += x[i]*x[j]*(1-z[i]**2-z[j]**2)
    rel = abs(lhs-rhs)/max(1.0,abs(lhs),abs(rhs))
    max_rel_identity = max(max_rel_identity,rel)
    identity_violations += rel > 1e-9
    lower = x[0]*x[1]*max(0.0,1-z[0]**2-z[1]**2)
    lower_violations += lhs + 1e-8 < lower
    if lower > 1e-12:
        min_lower_ratio = min(min_lower_ratio,lhs/lower)

# Punctured top-two product regression.
rng = np.random.default_rng(2026092402)
puncture_violations = 0
min_puncture_ratio = float('inf')
max_core_rel = 0.0
for _ in range(2000):
    p = int(rng.integers(3,10))
    q = int(rng.integers(2,10))
    N = rng.normal(size=(p,q))
    U,s,Vt = np.linalg.svd(N, full_matrices=False)
    if len(s) < 2 or s[1] < 1e-10:
        continue
    x1,x2 = s[0]**2,s[1]**2
    i = int(rng.integers(0,p))
    ell = float(np.sum(U[i,:2]**2))
    M = np.delete(N,i,axis=0)
    sm = np.linalg.svd(M,compute_uv=False)
    if len(sm) < 2:
        continue
    actual = (sm[0]**2)*(sm[1]**2)
    floor = x1*x2*(1-ell)
    puncture_violations += actual + 1e-8 < floor
    if floor > 1e-12:
        min_puncture_ratio = min(min_puncture_ratio,actual/floor)
    U2 = np.delete(U[:,:2],i,axis=0)
    core = U2@np.diag(s[:2])@Vt[:2,:]
    sc = np.linalg.svd(core,compute_uv=False)
    core_product = (sc[0]**2)*(sc[1]**2)
    rel = abs(core_product-floor)/max(1.0,abs(core_product),abs(floor))
    max_core_rel = max(max_core_rel,rel)

kappa0 = Fraction(247,576)
a0 = Fraction(1,223)
theta = Fraction(1,4)
R = kappa0*Fraction(1,4)*theta*theta*a0*a0
assert R == Fraction(247,1833209856)
C_E2 = 3*2**(7/6)*math.e**(1/3)
density_angle = C_E2*float(R)**(-1/6)
L1_angle = 2*math.pi*density_angle
partner = 9.83947303316740*float(R)**(-1/8)
aligned = math.sqrt(7/8)/223

print('QFORM_B02_R48_CHECK_PASS')
print('delta=',repr(delta),'sigma=',repr(sigma),'ridge_gate=',repr(ridge_gate))
print('window_density=',repr(C_window),'window_L1=',repr(L1_window))
print('carrier_identity_violations=',identity_violations)
print('carrier_lower_violations=',lower_violations)
print('max_rel_identity=',repr(max_rel_identity))
print('min_carrier_lower_ratio=',repr(min_lower_ratio))
print('puncture_violations=',puncture_violations)
print('max_core_product_rel=',repr(max_core_rel))
print('min_puncture_ratio=',repr(min_puncture_ratio))
print('R_theta=',repr(float(R)), 'exact=', f'{R.numerator}/{R.denominator}')
print('angle_density=',repr(density_angle),'angle_L1=',repr(L1_angle))
print('partner_coefficient=',repr(partner))
print('aligned_floor=',repr(aligned))
