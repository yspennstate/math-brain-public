"""Closed form of lim_{eta->0} lambda(eta)/eta for the K = M = 2 erf committee (T240 target 2).
At eta -> 0 the Saad-Solla ODE is the population gradient flow dw_i/dt = -eta grad_{w_i} eps (w normalized by sqrt N),
eps = (1/pi) [sum_ik asin(Q_ik/sqrt((1+Q_ii)(1+Q_kk))) + sum_nm asin(T_nm/...) - 2 sum_in asin(R_in/sqrt((1+Q_ii)(1+T_nn)))]
for g(z) = erf(z/sqrt 2). The symmetric fixed point has w_1 = w_2 = (v_1 + v_2)/sqrt 6, inside the teacher span, so
the gradient flow can be linearized in the 4 coordinates (w_i . v_n). lambda/eta is the top eigenvalue of -Hess eps there."""
import sympy as sp

a, b, c, d = sp.symbols('a b c d', real=True)       # w1 = a v1 + b v2, w2 = c v1 + d v2
W = [(a, b), (c, d)]
V = [(1, 0), (0, 1)]
dot = lambda x, y: x[0] * y[0] + x[1] * y[1]
G = lambda x, y: sp.asin(dot(x, y) / sp.sqrt((1 + dot(x, x)) * (1 + dot(y, y))))
eps = (sum(G(W[i], W[k]) for i in range(2) for k in range(2)) + sum(G(V[n], V[m]) for n in range(2) for m in range(2))
       - 2 * sum(G(W[i], V[n]) for i in range(2) for n in range(2))) / sp.pi
x = [a, b, c, d]
s6 = 1 / sp.sqrt(6)
pt = {a: s6, b: s6, c: s6, d: s6}
grad = [sp.simplify(sp.diff(eps, v).subs(pt)) for v in x]
print("gradient at the symmetric point:", grad)
H = sp.Matrix(4, 4, lambda i, j: sp.nsimplify(sp.simplify(sp.diff(eps, x[i], x[j]).subs(pt))))
H = sp.simplify(H)
print("Hessian:", H)
ev = H.eigenvals()
for e, mult in ev.items():
    print("eig", sp.simplify(e), "=", sp.N(e, 12), "mult", mult)
# antisymmetric direction: w1 - w2 along v1 - v2
u = sp.Matrix([1, -1, -1, 1]) / 2
lam = sp.simplify(-(u.T * H * u)[0])
print("lambda/eta along (v1-v2, -(v1-v2)):", lam, "=", sp.N(lam, 12))
