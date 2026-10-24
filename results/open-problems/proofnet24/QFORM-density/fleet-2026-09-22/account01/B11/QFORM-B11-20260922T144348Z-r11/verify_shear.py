import math
import random
import numpy as np

rng = random.Random(26092211)

# Algebraic regression for the left shear u' = u + B^{-T}s x.
for _ in range(2000):
    B = np.array([[rng.uniform(-2,2), rng.uniform(-2,2)],
                  [rng.uniform(-2,2), rng.uniform(-2,2)]], dtype=float)
    if abs(np.linalg.det(B)) < 0.2:
        continue
    C0 = np.array([[rng.uniform(-2,2), rng.uniform(-2,2)],
                   [0.0, rng.uniform(-2,2)]], dtype=float)
    C = C0 + C0.T - np.diag(np.diag(C0))
    D0 = np.array([[rng.uniform(-2,2), rng.uniform(-2,2)],
                   [0.0, rng.uniform(-2,2)]], dtype=float)
    D = D0 + D0.T - np.diag(np.diag(D0))
    r = np.array([rng.uniform(-2,2), rng.uniform(-2,2)])
    s = np.array([rng.uniform(-2,2), rng.uniform(-2,2)])
    gamma = np.array([rng.uniform(-2,2), rng.uniform(-2,2)])
    delta = np.array([rng.uniform(-2,2), rng.uniform(-2,2)])
    a = rng.uniform(-2,2)
    beta = rng.uniform(-2,2)
    c0 = rng.uniform(-2,2)
    x = rng.uniform(-2,2)
    up = np.array([rng.uniform(-2,2), rng.uniform(-2,2)])
    v = np.array([rng.uniform(-2,2), rng.uniform(-2,2)])

    kappa = np.linalg.solve(B.T, s)
    u = up - kappa*x
    q0 = (a*x*x + 2*x*(beta + r@u + s@v) + u@C@u + 2*gamma@u
          + 2*u@B@v + v@D@v + 2*delta@v + c0)

    aL = a - 2*r@kappa + kappa@C@kappa
    rL = r - C@kappa
    betaL = beta - gamma@kappa
    q1 = (aL*x*x + 2*x*(betaL + rL@up) + up@C@up + 2*gamma@up
          + 2*up@B@v + v@D@v + 2*delta@v + c0)
    assert abs(q0-q1) < 1e-9

# Exact double-null target example.
M = np.array([[2.,1.,0.,1.,0.],
              [1.,0.,0.,1.,0.],
              [0.,0.,0.,0.,1.],
              [1.,1.,0.,0.,0.],
              [0.,0.,1.,0.,0.]])
eigs = np.linalg.eigvalsh(M)
assert np.allclose(eigs, [-1.,-1.,0.,1.,3.], atol=1e-10)

Cstar = 5 * 3**(3/5) * 2**(-2/5)
partner_quarter = 4*math.sqrt(math.pi*math.e)
print('left_shear_random_checks=PASS')
print('double_null_spectrum=', ','.join(f'{x:.12g}' for x in eigs))
print('Cstar=', f'{Cstar:.12f}')
print('partner_delta_quarter=', f'{partner_quarter:.12f}')
print('QFORM_TWOSIDED_SHEAR_CHECK_PASS')
