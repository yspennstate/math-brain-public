# T354 rigorous remainder, iid sampling, any beta1, eps = 0 (agent B, 20 Oct 2026).
# Lemma. Frozen x, g uniform on {g_i(x)}, m = min g_i^2 > 0, V = E g^2, Z = g^2 - V, C = E g^3 - f'(x) V, d = 1 - beta2,
# stationary v_k = d sum_j beta2^j g_{k-j}^2. For momentum lag i write v_k = V t_i + d beta2^i Z_{k-i}, t_i - 1 =
# sum_{j != i} d beta2^j Z_{k-j}/V, so t_i is independent of g_{k-i}, E t_i = 1, Var t_i <= s2 = d Var(g^2)/((1+beta2)V^2),
# t_i >= rho = m/V. With phi(y) = y^(-1/2), h = d beta2^i Z/V and K = (1-b1)/(1-b1 b2):
#   sqrt(V) D(x) = f'(x) P0 - (d K C/(2V)) P1 + R,
#   P0 = sum_i (1-b1) b1^i E phi(t_i),   P1 = -2 sum_i w_i E phi'(t_i) (weights w_i = (1-b1)(b1 b2)^i / K),
#   |R| <= (1-b1)/(1-b1 b2^2) d^2 E[|g| Z^2]/(2 V^2) sup_i E phi''(t_i - d)   (t_i + h >= t_i - d).
# Taylor around 1 with the divided-difference remainders q(t) = int_0^1 (1-s) psi''(1 + s(t-1)) ds, monotone in t because
# psi'' is monotone for psi = phi, phi', t^(-5/2); q at t0 on {t >= t0}, q at rho on {t < t0}, and Bernstein's lower-tail bound
# P(t_i < t0) <= exp(-(1-t0)^2 V^2/(2(s2 V^2 + d (V - m)(1-t0) V/3))) (summands d beta2^j Z_j/V have -Z_j <= V - m).
# Then P0 in [1, 1 + q0 bound], P1 in [1, 1 + 2 |q1 bound|] (Jensen: phi convex, phi' concave).
# Every zero x* therefore satisfies f'(x*) P0 = d K C P1/(2V) - R. Argv: beta2 beta1.
# Model: n = 10, a_i = 1, b = (9, -1 x 9) (the NOTE's test model; f'(x) = x). Floats on closed forms (margins >> 1e-12).
import sys, math
b2 = float(sys.argv[1]); b1 = float(sys.argv[2]); d = 1 - b2
B = [9.0] + [-1.0] * 9
K = (1 - b1) / (1 - b1 * b2); Kr = (1 - b1) / (1 - b1 * b2 * b2)
def qdiv(f, f0, f1, t):  # (f(t) - f0 - f1 (t-1))/(t-1)^2
    return (f(t) - f0 - f1 * (t - 1)) / (t - 1) ** 2
phi = lambda t: t ** -0.5; dphi = lambda t: -0.5 * t ** -1.5; p52 = lambda t: t ** -2.5
def pieces(x):
    g = [x + b for b in B]; n = len(g)
    V = sum(t * t for t in g) / n; m = min(t * t for t in g)
    C = sum(t ** 3 for t in g) / n - x * V
    varg2 = sum((t * t - V) ** 2 for t in g) / n
    EgZ2 = sum(abs(t) * (t * t - V) ** 2 for t in g) / n
    return V, C, m / V, d * varg2 / ((1 + b2) * V * V), EgZ2, m
def slops(x):
    V, C, rho, s2, EgZ2, m = pieces(x); best = None
    for t0 in [0.2 + 0.01 * k for k in range(79)]:
        if t0 <= rho or t0 - d <= 0: continue
        P = math.exp(-(1 - t0) ** 2 / (2 * (s2 + d * (V - m) / V * (1 - t0) / 3)))
        q0 = qdiv(phi, 1, -0.5, t0) * s2 + (qdiv(phi, 1, -0.5, rho) - qdiv(phi, 1, -0.5, t0)) * (1 - rho) ** 2 * P
        q1 = qdiv(dphi, -0.5, 0.75, t0) * s2 + (qdiv(dphi, -0.5, 0.75, rho) - qdiv(dphi, -0.5, 0.75, t0)) * (1 - rho) ** 2 * P
        e52 = 1 + qdiv(p52, 1, -2.5, t0) * s2 + (qdiv(p52, 1, -2.5, rho) - qdiv(p52, 1, -2.5, t0)) * (1 - rho) ** 2 * P
        Ephi2 = 0.75 * ((1 - d / t0) ** -2.5 * e52 + (rho - d) ** -2.5 * P) if rho > d else float("inf")
        R = Kr * d * d * EgZ2 / (2 * V * V) * Ephi2
        cand = (q0, 2 * abs(q1), R, t0)
        if best is None or cand[1] + cand[2] < best[1] + best[2]: best = cand
    return V, C, best
def Fbounds(x):
    V, C, (q0, p1s, R, t0) = slops(x); lead = d * K * C / (2 * V)
    return x * 1.0 - lead * (1 + p1s) - R, x * (1 + q0) - lead + R   # x >= 0 here
x0 = d * K * 72 / 18
def bis(fn):
    a, c = 0.0, 3 * x0
    for _ in range(60):
        mid = (a + c) / 2
        a, c = (mid, c) if fn(mid) else (a, mid)
    return a
xl = bis(lambda x: Fbounds(x)[1] < 0); xh = bis(lambda x: Fbounds(x)[0] <= 0)
V, C, (q0, p1s, R, t0) = slops(x0)
print("beta2 %s beta1 %s K %.6f x0 %.6g | at x0: P0-1 <= %.3g, P1-1 <= %.3g, |R|/lead <= %.3g (t0 %.2f) | every zero in [0, 3x0] lies in x0*[%.4f, %.4f]; F changes sign there"
      % (sys.argv[1], sys.argv[2], K, x0, q0, p1s, R / (d * K * C / (2 * V)), t0, xl / x0, xh / x0))
# grid scan of the monotonicity the bisection assumes: F_hi < 0 on [0, xl), F_lo > 0 on (xh, 3 x0]
bad = [x for x in [3 * x0 * k / 4000 for k in range(1, 4001)] if (x < xl and Fbounds(x)[1] >= 0) or (x > xh and Fbounds(x)[0] <= 0)]
print("scan of 4000 points: %d violate the bracket" % len(bad))
