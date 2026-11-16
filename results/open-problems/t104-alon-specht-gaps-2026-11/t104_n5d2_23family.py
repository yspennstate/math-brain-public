"""T104 n=5 D=2 on the 2+3 family: triple {0,1,2}, pair {3,4}; G = g1 uu' + g2 ww', u=(0,0,0,1,-1)/sqrt2,
w=(2,2,2,-3,-3)/sqrt30, lambda=(2+g1+g2)/4; top space = contrasts inside the triple. Exact T and its infimum ratio."""
import sympy as sp
import numpy as np
g1, g2 = sp.symbols('g1 g2', positive=True)
lam = (2 + g1 + g2) / 4
u = sp.Matrix([0, 0, 0, 1, -1]) / sp.sqrt(2); w = sp.Matrix([2, 2, 2, -3, -3]) / sp.sqrt(30)
H = sp.eye(5) - sp.ones(5, 5) / 5
G = g1 * u * u.T + g2 * w * w.T
L = lam * H - G
W = -L + sp.diag(*[L[i, i] for i in range(5)])
Pi = H - u * u.T - w * w.T
n, D = 5, 2; c = sp.Rational(10, 3); beta = (1 - lam) / 3
X1 = D * (lam * G.trace() - (G * G).trace())
X2 = c * (G * Pi.multiply_elementwise(G)).trace()
X3 = beta * (D * G.trace() - c * sum(Pi[i, i] * G[i, i] for i in range(5)))
S5 = sum(W[i, j] * (Pi[i, i] + Pi[j, j] - 2 * Pi[i, j]) * (G[i, i] + G[j, j] - 2 * G[i, j]) for i in range(5) for j in range(i + 1, 5))
T = sp.factor(sp.simplify(X1 + X2 + X3 - 2 * S5))
print("T =", T)
print("weights: triple", sp.simplify(W[0, 1]), " cross", sp.simplify(W[0, 3]), " pair", sp.simplify(W[3, 4]))
f = sp.lambdify((g1, g2), [T, X1 + X2 + X3, W[0, 1], W[0, 3], W[3, 4], lam - g1, lam - g2])
best = (np.inf, None)
for a in np.linspace(1e-4, 1.2, 1201):
    for b in np.linspace(1e-4, 1.2, 1201):
        t, den, *cons = f(a, b)
        if min(cons) < -1e-12:
            continue
        r = t / den
        if r < best[0]:
            best = (r, (a, b, t, den))
print("min ratio on 2+3 family (grid 1201^2):", best)
