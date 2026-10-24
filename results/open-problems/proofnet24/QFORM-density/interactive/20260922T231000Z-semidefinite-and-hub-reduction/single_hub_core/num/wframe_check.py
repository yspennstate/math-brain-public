# Check of the w-frame remark: X' = Y + L w, t = L + beta. Given Y the hub equation is a x^2 + 2 x t + N(t) = s with
# N quadratic in t and leading coefficient C = 2<q,w> + sum_j d_j w_j^2 (no lambda); Z_0 = t - t_m has coefficient
# vector w - (component orthogonal to w), so its norm is >= 1.
import numpy as np, sympy as sp
rng = np.random.default_rng(3)
n = 5
M = np.linalg.qr(rng.standard_normal((n, n)))[0]
w, v, e = M[:, 0], M[:, 1], M[:, 2:]
q, b, d = rng.standard_normal(n), rng.standard_normal(n), rng.standard_normal(n)
a, lam, beta, s = 0.7, 1.3, 0.4, 0.9
x, t = sp.symbols('x t'); ys = sp.symbols('y0:%d' % (n - 1))
basis = np.column_stack([v, e])                      # orthonormal basis of w-perp
Y = [sum(sp.Float(basis[j, k]) * ys[k] for k in range(n - 1)) for j in range(n)]
L = t - beta
X = [Y[j] + sp.Float(w[j]) * L for j in range(n)]
dot = lambda c, z: sum(sp.Float(c[j]) * z[j] for j in range(n))
V = dot(v, X)
Q = a * x**2 + 2 * x * (L + beta) + lam * V**2 + 2 * L * dot(q, X) + sum(sp.Float(d[j]) * X[j]**2 + sp.Float(b[j]) * X[j] for j in range(n))
N = sp.expand(Q - a * x**2 - 2 * x * t)
P = sp.Poly(N, t)
C_sym = P.coeff_monomial(t**2)
C_claim = 2 * q @ w + np.sum(d * w**2)
print("deg_t N =", P.degree(), " C from expansion = %.12f  claimed = %.12f" % (float(C_sym), C_claim))
B = sp.expand(P.coeff_monomial(t))
kappa = 1 - a * C_claim
grad = np.array([float(B.coeff(yk)) for yk in ys])   # B = <grad, y> + const in the basis of w-perp
cvec = basis @ grad * a / (2 * kappa)                # t_m = a B/(2 kappa) = <cvec, X'> + const, cvec orthogonal to w
print("kappa = %.4f   <cvec, w> = %.2e   |w - cvec| = %.4f (>= 1)" % (kappa, cvec @ w, np.linalg.norm(w - cvec)))
print("t-coefficient of V (should be <v,w> = %.1e): %.1e" % (v @ w, float(sp.Poly(sp.expand(V), t).coeff_monomial(t))))
