# T417 lower bound by hand (agent B, 18 Oct). Choice: delta = min(1, 2/sqrt(kappa), B h_min/tr H), beta = (1-delta/2)^2,
# eta = delta^2/(4 h_min). Claim: rho_HB <= 1 - delta/4, hence speedup >= (1/16) min(max(1, B h_max/tr H), sqrt(kappa)).
# (A) symbolic: block identities and the two endpoint inequalities of the concave quadratic h(x).
import sympy as sp, numpy as np
d, x, mu = sp.symbols('delta x mu', positive=True)
beta = (1 - d / 2) ** 2; a = 1 + beta; u = 1 - d / 4
k = 1 + beta - x
M0 = sp.Matrix([[k * k, -2 * beta * k, beta ** 2], [k, -beta, 0], [1, 0, 0]])
p0 = sp.expand((mu * sp.eye(3) - M0).det())
print("p0 == (mu-beta)((mu+beta)^2 - mu k^2):", sp.simplify(p0 - (mu - beta) * ((mu + beta) ** 2 - mu * k ** 2)) == 0)
cof = sp.simplify(((mu * sp.eye(3) - M0).adjugate())[0, 0]); print("(1,1) cofactor:", sp.factor(cof))
mu0 = 1 - d / 4
F0 = sp.expand((mu0 + beta) ** 2 - mu0 * k ** 2)
print("F(mu0) == u(2ax - x^2 - a d^2/4) + d^2/16:", sp.simplify(F0 - (u * (2 * a * x - x ** 2 - a * d ** 2 / 4) + d ** 2 / 16)) == 0)
print("mu0 - beta == d(3-d)/4:", sp.simplify(mu0 - beta - d * (3 - d) / 4) == 0)
# condition Q(mu0) > delta x/2  <=>  (3-d) F0 > 2 x u (a - d/4)  (all factors positive); divide by u:
h = sp.expand((3 - d) * (2 * a * x - x ** 2 - a * d ** 2 / 4) + (3 - d) * d ** 2 / (16 * u) - 2 * x * (a - d / 4))
print("coefficient of x^2:", sp.factor(sp.Poly(sp.numer(sp.together(h)), x).all_coeffs()[0] / 1))
for xv, name in [(d ** 2 / 4, "x = d^2/4"), (sp.Integer(1), "x = 1")]:
    P = sp.factor(sp.numer(sp.together(h.subs(x, xv) * 16 * u)))
    rr = [r for r in sp.Poly(P, d).real_roots() if 0 <= r <= 1]
    print(name, " numerator:", P, " roots in [0,1]:", rr, " value at d=1/2:", float(P.subs(d, sp.Rational(1, 2))))
# monotonicity of Q in mu on mu >= beta needs k^2 <= 4 beta, i.e. x in [(1-sqrt b)^2, (1+sqrt b)^2] = [d^2/4, (2-d/2)^2] contains [d^2/4, 1].
# (B) numeric: the full map at random points.
rng = np.random.default_rng(7)
def msmap(h, eta, b, B):
    n = len(h); M = np.zeros((3 * n, 3 * n)); kk = 1 + b - eta * h
    for j in range(n):
        A, X, C = 3 * j, 3 * j + 1, 3 * j + 2
        M[A, A] += kk[j] ** 2 + eta ** 2 / B * h[j] ** 2; M[A, X] = -2 * b * kk[j]; M[A, C] = b ** 2
        for l in range(n): M[A, 3 * l] += eta ** 2 / B * h[j] * h[l]
        M[X, A] = kk[j]; M[X, X] = -b; M[C, A] = 1.0
    return M
worst = 1e9; worst_sp = 1e9
for t in range(3000):
    n = int(rng.integers(1, 25)); h = np.sort(10.0 ** (-4 * rng.random(n)))[::-1]
    if rng.random() < 0.3: h = h * 0 + h[0] * np.r_[1, 10.0 ** (-4 * rng.random(n - 1))] if n > 1 else h
    h = np.sort(h)[::-1]; B = float(10 ** (4 * rng.random())); kap = h[0] / h[-1]; tr = h.sum()
    dl = min(1.0, 2 / np.sqrt(kap), B * h[-1] / tr); b = (1 - dl / 2) ** 2; eta = dl ** 2 / (4 * h[-1])
    rho = np.abs(np.linalg.eigvals(msmap(h, eta, b, B))).max()
    worst = min(worst, (1 - rho) / dl)
    ceil = 4 * h[-1] * min(B / tr, 1 / h[0]); target = min(max(1, B * h[0] / tr), np.sqrt(kap))
    worst_sp = min(worst_sp, (1 - rho) / ceil / target)
print("min (1 - rho_HB)/delta over 3000 points: %.4f (claim >= 0.25)" % worst)
print("min speedup-over-SGD-ceiling / min(max(1,B h_max/trH), sqrt kappa): %.4f (claim >= 1/16 = 0.0625)" % worst_sp)
