import sympy as sp
import mpmath as mp

# Analytic constants used by QFORM-TWO-ORTHOGONAL-SAMESIGN-HEAVY-NOESCAPE-v1.
x = sp.symbols('x', positive=True)
beta_half = sp.integrate(x**(-sp.Rational(1, 2)) * (1-x)**(-sp.Rational(1, 2)), (x, 0, 1))
assert sp.simplify(beta_half - sp.pi) == 0

baseline_R = 1 / (2 * sp.sqrt(2))
baseline_Q = sp.simplify(12 * baseline_R)
assert sp.simplify(baseline_Q - 3 * sp.sqrt(2)) == 0

# The erf majorant proof uses d/dy [y/sqrt(1+2y^2/3)].
y = sp.symbols('y', positive=True)
rhs_core = y * (1 + sp.Rational(2, 3) * y**2)**(-sp.Rational(1, 2))
assert sp.simplify(sp.diff(rhs_core, y) - (1 + sp.Rational(2, 3) * y**2)**(-sp.Rational(3, 2))) == 0

# Exact Parseval/frame identities for the two heavy rows plus their diffuse banks.
ell1, ell2 = sp.symbols('ell1 ell2', nonnegative=True)
assert sp.simplify(ell1 + (1-ell1) - 1) == 0
assert sp.simplify(ell2 + (1-ell2) - 1) == 0

# Numerical sanity checks for the exact one-dimensional zero-peak integral
# in the centered-interval limiting model. These are NOT used as proof.
mp.mp.dps = 40

def interval_gaussian_integral(c):
    if abs(c) < mp.mpf('1e-40'):
        return mp.mpf(1)
    return mp.sqrt(mp.pi/c) * mp.erf(mp.sqrt(c)/2)

def L(t, ell):
    d = 1 + 2*t*(1-ell)
    c = 12*ell*t/d
    return d**(-mp.mpf('0.5')) * interval_gaussian_integral(c)

def pQ0(ell_a, ell_b):
    # Substitute u=z^2 to remove the u^{-1/2} endpoint singularity.
    f = lambda z: 2 * L(z*z + mp.mpf('0.5'), ell_a) * L(z*z + mp.mpf('0.5'), ell_b)
    pR0 = mp.quad(f, [0, 1, mp.inf]) / (mp.pi * mp.sqrt(2))
    return 12 * pR0

samples = [
    (mp.mpf(0), mp.mpf(0)),
    (mp.mpf('0.25'), mp.mpf('0.5')),
    (mp.mpf(1), mp.mpf(1)),
]
values = [pQ0(a, b) for a, b in samples]
assert abs(values[0] - 3*mp.sqrt(2)) < mp.mpf('1e-30')
assert values[1] < 3*mp.sqrt(2)
assert values[2] < 3*mp.sqrt(2)

print('PASS')
print('beta_half =', beta_half)
print('baseline_Q =', sp.N(baseline_Q, 30))
for pair, value in zip(samples, values):
    print('sample', pair, 'pQ0 =', mp.nstr(value, 25))
