import math
import numpy as np
import sympy as sp

# Exact target-class family.
tau = sp.symbols('tau', real=True)
A0 = sp.diag(1, -1, 1, -1)
v = sp.Matrix([1/sp.sqrt(2), 0, 0, 1/sp.sqrt(2)])
A = A0 + tau * (v * v.T)
assert sp.factor(A.charpoly().as_expr()) == (sp.Symbol('lambda')-1)*(sp.Symbol('lambda')+1)*(sp.Symbol('lambda')**2-sp.Symbol('lambda')*tau-1)
assert sp.factor(A.extract([0,1],[0,1]).det()) == -(1+tau/2)
assert sp.factor(A.extract([2,3],[2,3]).det()) == tau/2-1

# Deterministic finite stress check of the general rank-one identities and lower bound.
rng = np.random.default_rng(20260922)
trials = 0
min_ratio = float('inf')
for _ in range(2000):
    th = rng.uniform(0, 2*np.pi)
    Q = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])
    a = float(np.exp(rng.uniform(-1,1)))
    b = float(np.exp(rng.uniform(-1,1)))
    B = Q @ np.diag([a,-b]) @ Q.T
    w = rng.normal(size=2)
    q = float(w @ np.linalg.solve(B,w))
    if abs(q) < 1e-3:
        continue
    t = float(10**rng.uniform(-4,4)) * np.sign(q)
    Bt = B + t*np.outer(w,w)
    assert np.isclose(np.linalg.det(Bt), np.linalg.det(B)*(1+t*q), rtol=1e-8, atol=1e-8)
    Binv = np.linalg.inv(B)
    formula = Binv - (t/(1+t*q))*np.outer(Binv@w, Binv@w)
    assert np.allclose(np.linalg.inv(Bt), formula, rtol=1e-8, atol=1e-8)
    M = np.linalg.norm(Binv,2)
    L = np.linalg.norm(w)
    beta = 1/(M + M*M*L*L/abs(q))
    kappa = np.linalg.svd(Bt,compute_uv=False)[-1]
    assert kappa + 1e-9 >= beta
    ev = np.linalg.eigvalsh(Bt)
    assert ev[0] < 0 < ev[1]
    min_ratio = min(min_ratio, kappa/beta)
    trials += 1

print('PASS')
print('charpoly=(lambda-1)(lambda+1)(lambda^2-tau*lambda-1)')
print('trials=', trials)
print('min_kappa_over_beta=', min_ratio)
print('partner_constant=', 6*400**(1/3))
