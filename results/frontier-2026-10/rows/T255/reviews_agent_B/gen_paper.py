"""Independent generator for T255, built from the PAPER's Theorem 4.2 (arXiv 2306.17759 v-Dec-2023 source, main.tex
lines 640-690 and line 455 for Sigma_lin), not from the author's noise representation.

Coordinates: the upper-triangle entries V_ab (a <= b). For a function F(V):
  drift(F) = grad F . b + (1/2) sum_pq Hess F_pq Sigma_pq,   QV rate(F) = grad F^T Sigma grad F.
Everything is evaluated in mpmath at 60 digits so limits can be read off a sequence.
"""
import itertools, sympy as sp, mpmath as mp

mp.mp.dps = 60


class Model:
    def __init__(self, m):
        self.m = m
        self.pairs = [(a, b) for a in range(m) for b in range(a, m)]
        self.sym = {p: sp.Symbol(f"v{p[0]}{p[1]}") for p in self.pairs}
        self.Vs = sp.Matrix(m, m, lambda i, j: self.sym[(min(i, j), max(i, j))])

    # ---- the paper's coefficients, numerically (V an mpmath matrix) ----
    def coeffs(self, V, g2, tau0):
        m = self.m
        xb = [sum(V[a, n] for n in range(m)) / m for a in range(m)]       # V^{a xbar}
        xx = sum(xb) / m                                                    # V^{xbar xbar}
        Vbar = sum(V[n, n] for n in range(m)) / m
        S1 = lambda a, d, b, w: V[a, b] * (V[d, w] - xb[d] - xb[w] + xx)
        S2 = lambda a, d: V[a, a] * (V[d, d] - 2 * xb[d] + 2 * xx - Vbar)
        t2 = mp.mpf(tau0) ** 2
        b = []
        for (a, be) in self.pairs:
            s = sum(V[n, k] * S1(a, n, be, k) for n in range(m) for k in range(m)) / m ** 2
            s += sum(V[be, n] * S2(a, n) + V[a, n] * S2(be, n) for n in range(m)) / (2 * m)
            b.append(g2 / t2 * s)
        c = g2 * (2 - g2)
        P = len(self.pairs)
        Sig = mp.matrix(P, P)
        for i, (a, be) in enumerate(self.pairs):
            for j, (d, w) in enumerate(self.pairs):
                A = sum(V[a, k] * V[d, n] * S1(be, k, w, n) + V[a, k] * V[w, n] * S1(be, k, d, n)
                        + V[be, n] * V[d, k] * S1(a, n, w, k) + V[be, n] * V[w, k] * S1(a, n, d, k)
                        for n in range(m) for k in range(m)) / m ** 2
                Sig[i, j] = c * (V[a, d] * V[be, w] + V[a, w] * V[be, d]) + g2 ** 2 / t2 * A
        return b, Sig

    def compile(self, Fexpr):
        x = [self.sym[p] for p in self.pairs]
        g = [sp.diff(Fexpr, v) for v in x]
        H = [[sp.diff(gi, v) for v in x] for gi in g]
        f = sp.lambdify(x, [Fexpr, g, H], modules="mpmath")
        return lambda V: f(*[V[p[0], p[1]] for p in self.pairs])

    def gen(self, Fc, V, g2, tau0):
        b, Sig = self.coeffs(V, g2, tau0)
        F, g, H = Fc(V)
        P = len(self.pairs)
        drift = sum(g[i] * b[i] for i in range(P)) + sum(H[i][j] * Sig[i, j] for i in range(P) for j in range(P)) / 2
        qv = sum(g[i] * Sig[i, j] * g[j] for i in range(P) for j in range(P))
        return F, drift, qv

    def W2(self, V):
        m = self.m
        Pm = mp.eye(m) - mp.ones(m, m) / m
        W = Pm * V * Pm
        return sum(W[i, j] ** 2 for i in range(m) for j in range(m))
