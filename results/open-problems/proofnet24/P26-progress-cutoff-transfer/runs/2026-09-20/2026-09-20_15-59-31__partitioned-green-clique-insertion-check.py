import math
import numpy as np
import sympy as sp

# Exact arithmetic for the degree-six clique-inserted class Y=L(Sd(G)).
d = 6
q = d - 1
theta = sp.symbols('theta', real=True)

qplus = sp.Rational(1, 3) + sp.sqrt(10 + theta) / 6
qminus = sp.Rational(1, 3) - sp.sqrt(10 + theta) / 6
theta_max = 2 * sp.sqrt(5)
qmax = sp.simplify(qplus.subs(theta, theta_max))
gap = sp.simplify(1 - qmax)

print('d =', d)
print('qplus(theta) =', qplus)
print('qminus(theta) =', qminus)
print('Ramanujan qmax =', qmax)
print('output gap lower bound =', gap, '=', float(gap.evalf()))
assert gap > 0

# Two radial shell types on L(Sd(T_6)).
T = sp.Matrix([[sp.Rational(2, 3), sp.Rational(1, 3)], [1, 0]])
piA, piB = sp.Rational(3, 4), sp.Rational(1, 4)
assert sp.Matrix([[piA, piB]]) * T == sp.Matrix([[piA, piB]])
print('type kernel =', T)
print('stationary type law =', (piA, piB))

# One-jump tilted matrix. For rate-one Poissonization the cumulant exponent
# is lambda(theta)-1, so lambda'(0) and lambda''(0) are the CT drift and
# variance rates.
th = sp.symbols('th')
M = sp.Matrix([
    [sp.Rational(d - 2, d), (sp.exp(-th) + sp.exp(th)) / d],
    [(sp.exp(-th) + (d - 1) * sp.exp(th)) / d, 0],
])
tr, det = M.trace(), M.det()
lam = sp.simplify((tr + sp.sqrt(tr**2 - 4 * det)) / 2)
assert sp.simplify(lam.subs(th, 0) - 1) == 0
v = sp.simplify(sp.diff(lam, th).subs(th, 0))
sigma2 = sp.simplify(sp.diff(lam, th, 2).subs(th, 0))
tau2_ell = sp.simplify(sigma2 / v**3)
tau2_log5 = sp.simplify(2 * sigma2 / v**3)
print('radial speed v =', v)
print('continuous-time variance rate sigma^2 =', sigma2)
print('tau^2 on sqrt(ell) scale =', tau2_ell)
print('tau^2 on sqrt(log_5 N) scale =', tau2_log5)
assert v == sp.Rational(1, 6)
assert sigma2 == sp.Rational(11, 24)
assert tau2_ell == 99
assert tau2_log5 == 198

# Tail-bipartition color chain: one reversal among d neighbors flips color.
color_decay = sp.Rational(2, d)
print('color CT decay exponent =', color_decay)
assert color_decay == sp.Rational(1, 3)

# Exact sphere sizes in the clique-inserted tree cover.
sizes = [1]
for r in range(1, 9):
    if r % 2 == 0:
        sizes.append(2 * q ** (r // 2))
    else:
        sizes.append(d * q ** ((r - 1) // 2))
print('sphere sizes r=0..8 =', sizes)
assert sizes == [1, 6, 10, 30, 50, 150, 250, 750, 1250]

# Finite K_{6,6} sanity check for the full line-of-subdivision spectral transform.
# The toy is not used to infer asymptotics.
n = 12
A = np.zeros((n, n))
for i in range(6):
    for j in range(6, 12):
        A[i, j] = A[j, i] = 1
base_eigs = np.linalg.eigvalsh(A)
edges = [(i, j) for i in range(6) for j in range(6, 12)]
arcs = []
for u, w in edges:
    arcs.extend([(u, w), (w, u)])
N = len(arcs)
idx = {a: i for i, a in enumerate(arcs)}
AY = np.zeros((N, N))
for i, (vtx, w) in enumerate(arcs):
    # Clique move: same tail, different head.
    for wp in range(n):
        if A[vtx, wp] and wp != w:
            AY[i, idx[(vtx, wp)]] = 1
    # Reversal move.
    AY[i, idx[(w, vtx)]] = 1
assert np.allclose(AY, AY.T)
assert np.allclose(AY.sum(axis=1), d)
eig = np.linalg.eigvalsh(AY / d)

# For a base adjacency eigenvalue theta, the paired normalized line eigenvalues are
# ((d-2) +/- sqrt((d-2)^2 + 4(d+theta))) / (2d).
pred = []
for bt in base_eigs:
    s2 = d + bt
    disc = (d - 2) ** 2 + 4 * s2
    pred += [((d - 2) + math.sqrt(max(0, disc))) / (2 * d),
             ((d - 2) - math.sqrt(max(0, disc))) / (2 * d)]
# The subdivision biadjacency is 12x36: add its extra right-kernel zero modes,
# then the flat -2/d line modes to reach the full arc dimension.
pred += [0.0] * 24
pred += [-2 / d] * (N - len(pred))
assert len(pred) == N
err = np.max(np.abs(np.sort(eig) - np.sort(np.array(pred))))
print('finite K6,6 clique-inserted spectrum check max error =', err)
assert err < 1e-12

print('P26_T08_PARTITIONED_GREEN_CLIQUE_INSERTION_EXACT_PASS')
