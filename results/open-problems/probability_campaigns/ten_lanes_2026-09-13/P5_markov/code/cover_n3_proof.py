import itertools, sympy as sp
a, b, c, s1, s2, s3 = sp.symbols('a b c s1 s2 s3', nonnegative=True)
W = sp.Matrix([[s1, c, b], [c, s2, a], [b, a, s3]])
n = 3
wrow = [sum(W[i, j] for j in range(n)) for i in range(n)]
P = sp.Matrix(n, n, lambda i, j: W[i, j] / wrow[i])
pi = [wrow[i] / sum(wrow) for i in range(n)]
full = (1 << n) - 1
h = {(full, i): sp.Integer(0) for i in range(n)}
for size in range(n - 1, 0, -1):
    for comb in itertools.combinations(range(n), size):
        S = 0
        for x in comb: S |= 1 << x
        idx = {v: t for t, v in enumerate(comb)}; m = len(comb)
        M = sp.zeros(m, m); rhs = sp.zeros(m, 1)
        for t, i in enumerate(comb):
            M[t, t] += 1; rhs[t] += 1
            for j in range(n):
                if (S >> j) & 1: M[t, idx[j]] -= P[i, j]
                else: rhs[t] += P[i, j] * h[(S | (1 << j), j)]
        sol = M.solve(rhs)
        for t, i in enumerate(comb): h[(S, i)] = sp.simplify(sol[t])
EpiC = sp.simplify(sum(pi[i] * h[(1 << i, i)] for i in range(n)))
num, den = sp.fraction(sp.together(sp.simplify(EpiC - 3)))
num = sp.expand(num); den = sp.expand(den)
# strip the positive square factor
R = sp.simplify(sp.cancel(num / (a*b + a*c + b*c)**2))
R = sp.expand(R)
print("den factored:", sp.factor(den))
pR = sp.Poly(R, a, b, c, s1, s2, s3)
neg = [(m, co) for m, co in zip(pR.monoms(), pR.coeffs()) if co < 0]
print("R: negative-coefficient monomials all have s-degree 0? ",
      all(m[3] == m[4] == m[5] == 0 for m, _ in neg), " count:", len(neg))
R0 = sp.expand(R.subs({s1: 0, s2: 0, s3: 0}))
print("\nR0 = R|_{s=0} =", sp.factor(R0))
print("R0(1,1,1) =", R0.subs({a: 1, b: 1, c: 1}))
print("R0 symmetric under a<->b:", sp.simplify(R0 - R0.subs({a: b, b: a}, simultaneous=True)) == 0)
print("R0 symmetric under b<->c:", sp.simplify(R0 - R0.subs({b: c, c: b}, simultaneous=True)) == 0)
# Try to certify R0 >= 0 on the nonnegative orthant
print("\n-- attempting certificate --")
# substitute a=1 (homogeneous degree 6, symmetric); minimise on b,c>=0
import numpy as np
f = sp.lambdify((b, c), R0.subs(a, 1), 'numpy')
bb = np.linspace(0.0, 6.0, 1201); cc = np.linspace(0.0, 6.0, 1201)
B, C = np.meshgrid(bb, cc)
V = f(B, C)
print("min on grid a=1, b,c in [0,6]:", V.min(), " at ", (B.flat[V.argmin()], C.flat[V.argmin()]))
# Schur-like attempt: R0 in terms of p=a+b+c, q=ab+bc+ca, r=abc
p, q, r = sp.symbols('p q r', nonnegative=True)
try:
    expr = sp.simplify(sp.symmetrize(R0)) if hasattr(sp, 'symmetrize') else None
except Exception:
    expr = None
from sympy.polys.polyfuncs import symmetrize
sym, rem, _ = symmetrize(R0, [a, b, c], formal=True)
print("\nsymmetrize remainder zero?", sp.simplify(rem) == 0)
print("R0 in elementary symmetric polys:", sp.factor(sym))
