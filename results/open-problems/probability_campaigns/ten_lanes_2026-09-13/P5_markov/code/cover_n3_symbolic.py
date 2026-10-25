"""Symbolic proof attempt: E_pi C >= 3 for every reversible 3-state chain.

Reversible chain <-> symmetric nonnegative weights w_ij (i<=j), P_ij = w_ij/w_i,
pi_i = w_i / sum_k w_k, where w_i = sum_j w_ij (self-loop counted once).
"""
import itertools, sympy as sp

a, b, c, s1, s2, s3 = sp.symbols('a b c s1 s2 s3', nonnegative=True)
# a = w23, b = w13, c = w12, si = self-loop weight at i
W = sp.Matrix([[s1, c, b],
               [c, s2, a],
               [b, a, s3]])
n = 3
wrow = [sum(W[i, j] for j in range(n)) for i in range(n)]
P = sp.Matrix(n, n, lambda i, j: W[i, j] / wrow[i])
pi = [wrow[i] / sum(wrow) for i in range(n)]

# subset DP
full = (1 << n) - 1
h = {(full, i): sp.Integer(0) for i in range(n)}
for size in range(n - 1, 0, -1):
    for comb in itertools.combinations(range(n), size):
        S = 0
        for x in comb: S |= 1 << x
        idx = {v: t for t, v in enumerate(comb)}
        m = len(comb)
        M = sp.zeros(m, m); rhs = sp.zeros(m, 1)
        for t, i in enumerate(comb):
            M[t, t] += 1; rhs[t] += 1
            for j in range(n):
                if (S >> j) & 1:
                    M[t, idx[j]] -= P[i, j]
                else:
                    rhs[t] += P[i, j] * h[(S | (1 << j), j)]
        sol = M.solve(rhs)
        for t, i in enumerate(comb):
            h[(S, i)] = sp.simplify(sol[t])

EpiC = sp.simplify(sum(pi[i] * h[(1 << i, i)] for i in range(n)))
print("E_pi C =")
print(sp.simplify(EpiC))
diff = sp.together(sp.simplify(EpiC - 3))
num, den = sp.fraction(diff)
num = sp.expand(sp.simplify(num)); den = sp.expand(sp.simplify(den))
print("\nnumerator of (E_pi C - 3):")
print(sp.factor(num))
print("\ndenominator:")
print(sp.factor(den))
pn = sp.Poly(num, a, b, c, s1, s2, s3)
pd = sp.Poly(den, a, b, c, s1, s2, s3)
neg_n = [(m, co) for m, co in zip(pn.monoms(), pn.coeffs()) if co < 0]
neg_d = [(m, co) for m, co in zip(pd.monoms(), pd.coeffs()) if co < 0]
print("\nnumerator: #monomials =", len(pn.coeffs()), " negative coefficients:", neg_n)
print("denominator: #monomials =", len(pd.coeffs()), " negative coefficients:", neg_d)
