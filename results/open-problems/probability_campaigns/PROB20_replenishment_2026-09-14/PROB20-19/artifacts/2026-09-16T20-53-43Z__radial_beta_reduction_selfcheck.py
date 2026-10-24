from fractions import Fraction
import random
import sympy as sp
import mpmath as mp

# Supporting self-check for the 2026-09-16T20-53-43Z report.
# The theorem is proved analytically in the report; this file is not an
# independent proof.

# Symbolic curvature check for J'(x) = (4/pi) int_0^theta sin^4.
x = sp.symbols('x', positive=True)
th = sp.atan(1/sp.sqrt(x))
A = 3*th/sp.Integer(8) - sp.sin(2*th)/4 + sp.sin(4*th)/32
Jp = 4*A/sp.pi
Jpp_target = -2/(sp.pi*sp.sqrt(x)*(1+x)**3)
resid = sp.trigsimp(sp.simplify(sp.diff(Jp, x) - Jpp_target))
print('SYMBOLIC_JPP_RESIDUAL=', resid)
assert resid == 0

# Beta mean used in the radial decomposition.
mean_q = sp.Rational(3,2)/(sp.Rational(3,2)+sp.Rational(1,2))
print('BETA_MEAN=', mean_q)
assert mean_q == sp.Rational(3,4)

# Exact deterministic bottom-two identity from Theorem 6.1.
rng = random.Random(20260916)
for _ in range(500):
    bs = sorted(Fraction(rng.randint(0,50), rng.randint(1,25)) for _ in range(3))
    q = Fraction(rng.randint(0,100), 100)
    lam = Fraction(rng.randint(1,50), rng.randint(1,25))
    vals = sorted([q*bs[0], q*bs[1], q*bs[2], lam*(1-q)])
    lhs = vals[0] + vals[1]
    rhs = q*bs[0] + min(q*bs[1], lam*(1-q))
    assert lhs == rhs
print('EXACT_BOTTOM_TWO_CASES=500 PASS')

# High-precision diagnostic: elementary J formula vs direct Beta integral.
mp.mp.dps = 70

def J_closed(z):
    z = mp.mpf(z)
    if z == 0:
        return mp.mpf('0')
    t = mp.atan(1/mp.sqrt(z))
    A = 3*t/8 - mp.sin(2*t)/4 + mp.sin(4*t)/32
    B = mp.pi/16 - t/8 + mp.sin(4*t)/32
    return 4/mp.pi*(z*A+B)

def J_direct(z):
    z = mp.mpf(z)
    f = lambda q: min(q*z, 1-q)*(2/mp.pi)*mp.sqrt(q/(1-q))
    q0 = 1/(1+z) if z > 0 else mp.mpf(1)
    if z == 0:
        return mp.mpf(0)
    return mp.quad(f, [0,q0,1])

for z in ['0.01','0.1','0.5','1','2','10','100']:
    a,b = J_closed(z), J_direct(z)
    err=abs(a-b)
    print(f'J_CHECK x={z} abs_err={mp.nstr(err,8)} value={mp.nstr(a,20)}')
    assert err < mp.mpf('1e-55')

# Mixture representation diagnostic via direct quadrature.
def rho(s):
    return 2/(mp.pi*mp.sqrt(s)*(1+s)**3)

def J_mix(z):
    z=mp.mpf(z)
    if z==0:
        return mp.mpf(0)
    return mp.quad(lambda s: min(z,s)*rho(s), [0,z, mp.inf])

for z in ['0.1','1','3','20']:
    a,b=J_closed(z),J_mix(z)
    err=abs(a-b)
    print(f'MIX_CHECK x={z} abs_err={mp.nstr(err,8)}')
    assert err < mp.mpf('1e-50')

print('SELF_CHECK_ONLY_ALL_PASS')
