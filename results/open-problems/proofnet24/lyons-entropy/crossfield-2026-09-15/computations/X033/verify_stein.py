"""Exact finite checks for X033; no random search is used by this certificate."""
from itertools import product
from pathlib import Path
import json
import sympy as sp

I, R = sp.I, sp.Rational
t = sp.symbols('t', real=True)
K = sp.Matrix([[45, -11-31*I, -1-28*I],
               [-11+31*I, 55, -8-21*I],
               [-1+28*I, -8+21*I, 69]]) / 100
A = sp.Matrix([[0, -3+3*I, 5+2*I],
               [-3-3*I, 0, -5+5*I],
               [5-2*I, -5-5*I, 0]]) / 10
bits = list(product((0, 1), repeat=3))
index = {x: i for i, x in enumerate(bits)}
checks = 0

def check(claim):
    global checks
    assert bool(claim)
    checks += 1

def eq(x, y=0):
    difference = sp.simplify(x-y)
    if isinstance(difference, sp.MatrixBase):
        check(difference == sp.zeros(*difference.shape))
    else:
        check(difference == 0)

def expectation(vals):
    return sp.factor(sum(px*vx for px, vx in zip(p, vals)))

def inner(xs, ys):
    return expectation([x*y for x, y in zip(xs, ys)])

polys = [sp.expand((-1)**(3-sum(x)) *
                  (K+t*A-sp.diag(*[1-y for y in x])).det()) for x in bits]
p = [sp.factor(f.subs(t, 0)) for f in polys]
v = [sp.factor(sp.diff(f, t).subs(t, 0)) for f in polys]
a = [sp.factor(sp.diff(f, t, 2).subs(t, 0)) for f in polys]
for px in p:
    check(px > 0)
eq(sum(p), 1); eq(sum(v)); eq(sum(a))
score = [vx/px for px, vx in zip(p, v)]
FI = inner(score, score)
d = sp.Matrix([K[i, i] for i in range(3)])
G = K.multiply_elementwise(sp.conjugate(K))
Sigma = sp.diag(*d) - G
for i in range(3):
    eq(sum(vx*x[i] for vx, x in zip(v, bits)))
    for j in range(3):
        eq(Sigma[i, j], expectation([(x[i]-d[i])*(x[j]-d[j]) for x in bits]))

# The endpoint indicator is projected off all conserved first moments.
endpoint = 7
e = sp.ones(3, 1)
b = p[endpoint]*(e-d)
beta = Sigma.inv()*b
h = [sp.factor(int(k == endpoint)-p[endpoint] -
               (beta.T*(sp.Matrix(x)-d))[0]) for k, x in enumerate(bits)]
kappa = sp.factor(1-p[endpoint]-p[endpoint]*((e-d).T*Sigma.inv()*(e-d))[0])
check(0 < kappa < 1)
eq(expectation(h)); eq(inner(h, h), p[endpoint]*kappa)
for i in range(3):
    eq(inner(h, [x[i]-d[i] for x in bits]))
eq(inner(score, h), v[endpoint])
rho = [sp.factor(s-v[endpoint]*z/(p[endpoint]*kappa)) for s, z in zip(score, h)]
eq(expectation(rho)); eq(inner(rho, h))
eq(FI, inner(rho, rho)+v[endpoint]**2/(p[endpoint]*kappa))

# The independent-copy pair is exchangeable, with this explicit Stein kernel.
for x in range(8):
    eq(sum(p[y]*(h[x]-h[y]) for y in range(8)), h[x])
    lhs = p[x]*h[x]
    rhs = sum(p[u]*p[w]*(h[u]-h[w])*(int(u == x)-int(w == x))
              for u in range(8) for w in range(8))/2
    eq(lhs, rhs)
eq(inner(rho, rho), sum(p[x]*p[y]*(rho[x]-rho[y])**2
                       for x in range(8) for y in range(8))/2)

# Matrix projection: no square roots are needed for exact verification.
nu = sp.factor(3-(d.T*G.inv()*d)[0])
gamma = sp.factor(1-1/nu)
trC = sp.simplify(sp.trace(K.inv()*A))
trC2 = sp.simplify(sp.trace(K.inv()*A*K.inv()*A))
matrix_residual = sp.factor(trC2-trC**2/nu)
check(matrix_residual >= 0)
eq(v[endpoint], p[endpoint]*trC)
eq(a[endpoint], gamma*v[endpoint]**2/p[endpoint] - p[endpoint]*matrix_residual)
check(1 < nu < R(25, 24)-R(1, 200))
check(0 < gamma < R(1, 25))

# Formal coefficients of log(p_x) verify the entire Hessian, including p''.
delta_coeff = sp.Matrix([(-1)**sum(x) for x in bits])
face_log = sp.zeros(8, 1)
face_drift = sp.zeros(8, 1)
pair_generator = sp.zeros(64, 64)
pair_law = sp.kronecker_product(sp.Matrix(p), sp.Matrix(p))
recombination_log = sp.zeros(8, 1)
r_values = []
for i, j in ((0, 1), (0, 2), (1, 2)):
    r = sp.simplify(-A.extract([i, j], [i, j]).det())
    r_values.append(r); check(r > 0)
    inds = []
    for bi, bj in ((0, 0), (1, 0), (0, 1), (1, 1)):
        x = [0, 0, 0]; x[i] = bi; x[j] = bj
        inds.append(index[tuple(x)])
    aa, bb, cc, dd = inds
    U, V = p[aa]*p[dd], p[bb]*p[cc]
    check(V > U)
    rate = sp.factor(2*r/(V-U))
    for u, w in ((8*aa+dd, 8*bb+cc), (8*dd+aa, 8*cc+bb)):
        pair_generator[u, w] += rate; pair_generator[w, u] += rate
        pair_generator[u, u] -= rate; pair_generator[w, w] -= rate
    for z, sign in zip(inds, (-1, 1, 1, -1)):
        face_log[z] += 2*r*sign
        recombination_log[z] += 4*r*sign
        face_drift[z] -= 2*r*sign

eq(pair_generator-pair_generator.T, sp.zeros(64))
eq(pair_generator*sp.ones(64, 1), sp.zeros(64, 1))
joint_drift = pair_generator*pair_law
marginal_drift = sp.Matrix([sum(joint_drift[8*x+y] for y in range(8)) for x in range(8)])
eq(marginal_drift, face_drift)
eq(sp.Matrix(a), -marginal_drift-a[endpoint]*delta_coeff)
eq(sp.Matrix(a), face_log +
   (-gamma*v[endpoint]**2/p[endpoint]+p[endpoint]*matrix_residual)*delta_coeff)
eq(recombination_log/2, face_log)

# Exact ingredients for the full six-real-dimensional convex neighborhood.
leading = {}
for name, J in [('K-I/200', K-sp.eye(3)/200),
                ('I-K-I/200', sp.eye(3)-K-sp.eye(3)/200),
                ('G-I/10', G-sp.eye(3)/10)]:
    leading[name] = [sp.factor(J[:j, :j].det()) for j in (1, 2, 3)]
    for minor in leading[name]:
        check(minor > 0)
odds_ratio = sp.factor(p[0]*p[3]*p[5]*p[6]/(p[7]*p[1]*p[2]*p[4]))
check(9 < odds_ratio < 14)
check(sum(R(14, 5)**j/sp.factorial(j) for j in range(7)) > 14)
eps = R(1, 10**6)
check(R(1, 200)-3*eps > R(1, 250))
tau_error = 8*3*250*3*eps
check(2-tau_error > 0)
check(R(14, 5)+tau_error < 3)
check((d.T*d)[0] < 1)
nu_error = 800*eps/(1-80*eps)
check(nu_error < R(1, 1000))
check(nu+nu_error < R(25, 24))
eq(sp.simplify(-sp.trace(K*A.adjugate())), -R(119, 10000))
eq(sum(r_values), R(97, 100))

# The sufficient scalar certificate is genuinely nonautomatic.
K_fail = sp.Matrix([[7417, -1309-1294*I, -687+1309*I],
                    [-1309+1294*I, 6734, 1457+891*I],
                    [-687-1309*I, 1457-891*I, 8469]])/10000
for J_check in (K_fail, sp.eye(3)-K_fail):
    for j in (1, 2, 3):
        check(sp.factor(J_check[:j, :j].det()) > 0)
p_fail = [sp.factor((-1)**(3-sum(x)) *
                   (K_fail-sp.diag(*[1-y for y in x])).det()) for x in bits]
d_fail = sp.Matrix([K_fail[i, i] for i in range(3)])
J_fail = sp.eye(3)-K_fail
dj_fail = sp.ones(3, 1)-d_fail
nu_fail = sp.factor(3-(dj_fail.T *
    J_fail.multiply_elementwise(sp.conjugate(J_fail)).inv()*dj_fail)[0])
sigma_fail = sp.diag(*d_fail)-K_fail.multiply_elementwise(sp.conjugate(K_fail))
kappa_fail = sp.factor(1-p_fail[0]-p_fail[0]*(d_fail.T*sigma_fail.inv()*d_fail)[0])
inverse_ratio_fail = sp.factor(p_fail[7]*p_fail[1]*p_fail[2]*p_fail[4] /
                              (p_fail[0]*p_fail[3]*p_fail[5]*p_fail[6]))
check(nu_fail > R(3, 2))
check(kappa_fail > R(99, 100))
check(inverse_ratio_fail > 81)  # e<3 implies lambda>4.

delta = sp.log(odds_ratio)
curvature = FI+sum(ax*sp.log(px) for ax, px in zip(a, p))
rhs = (inner(rho, rho)+(1/kappa-delta*gamma)*v[endpoint]**2/p[endpoint]
       +delta*p[endpoint]*matrix_residual
       +sum(face_log[x]*sp.log(p[x]) for x in range(8)))
eq(sp.expand_log(curvature-rhs, force=True))

result = {'status': 'PASS', 'exact_assertions': checks,
          'atoms': list(map(str, p)), 'nu': str(nu), 'kappa': str(kappa),
          'gamma': str(gamma), 'third_ratio': str(odds_ratio),
          'q': '-119/10000', 'R': '97/100',
          'leading_minors': {k: list(map(str, vv)) for k, vv in leading.items()},
          'box_radius_per_real_component': str(eps),
          'failure_example_exact_bounds': {'nu': '>3/2', 'kappa': '>99/100',
                                           'lambda': '>4',
                                           'lambda_kappa_gamma': '>33/25'},
          'illustrative_decimal_third_interaction': str(delta.evalf(16)),
          'illustrative_decimal_negative_entropy_hessian': str(curvature.evalf(16))}
Path(__file__).with_name('results.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
