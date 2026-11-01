"""T417 (agent A, 18 Oct 2026): exact check of the last inequality in the heavy-ball lower bound.
mu0 = 1 - delta/4, beta = (1 - delta/2)^2, eps = delta x / 4 (worst diagonal noise at c = 1/4).
p(mu) = (mu - beta)((mu + beta)^2 - k^2 mu) - eps mu (mu + beta), k = 1 + beta - x.
Need R = mu0 (mu0 + beta) x delta / p(mu0) < 4, i.e. F(delta, x) = (mu0 - beta) D(x) - (1/2) mu0 (mu0 + beta) delta x > 0,
D(x) = (mu0 + beta)^2 - (1 + beta - x)^2 mu0. F is concave in x, so it suffices to check x = delta^2/4 and x = 1."""
import sympy as sp
d, x = sp.symbols('delta x', positive=True)
mu = 1 - d / 4; be = (1 - d / 2) ** 2; k = 1 + be - x
eps = d * x / 4
p = (mu - be) * ((mu + be) ** 2 - k ** 2 * mu) - eps * mu * (mu + be)
assert sp.simplify(sp.diff(p - mu * (mu + be) * x * d / 4, x, 2) - (-(mu - be) * 2 * mu)) == 0  # concave in x
F = sp.expand(p - mu * (mu + be) * x * d / 4)       # 4p - mu(mu+be) x d > 0  <=>  R < 4
for name, xv in [('x = delta^2/4', d ** 2 / 4), ('x = 1', sp.Integer(1))]:
    g = sp.factor(sp.expand(F.subs(x, xv)))
    print(name, ':', g)
    P = sp.Poly(sp.expand(g), d)
    rts = [r for r in sp.real_roots(P) if 0 < r <= 2]
    print('   exact real roots in (0, 2]:', [float(r) for r in rts], ' sign at delta=1/2:', sp.sign(g.subs(d, sp.Rational(1, 2))),
          ' at delta=1:', sp.sign(g.subs(d, 1)))
# also check the leading small-delta behaviour of R at both ends and the max over x numerically on a fine grid
import numpy as np
f = sp.lambdify((d, x), 4 * mu * (mu + be) * x * d / 4 / p, 'numpy')
for dv in [1.0, 0.5, 0.1, 1e-3]:
    xs = np.linspace(dv ** 2 / 4, 1, 200001); print(f'delta {dv}: max R over x = {np.max(f(dv, xs)):.4f}')
