"""Exact self-checks for X031. No random search or numerical optimization."""
from itertools import product
from pathlib import Path
import json
import sympy as s

Q = s.Rational
checks = 0


def equal(a, b=0):
    global checks
    if isinstance(a, s.MatrixBase) or isinstance(b, s.MatrixBase):
        a = s.Matrix(a)
        if b == 0:
            b = s.zeros(*a.shape)
        assert all(s.simplify(x) == 0 for x in a - b), (a, b)
    else:
        assert s.simplify(a - b) == 0, (a, b)
    checks += 1


def positive(x):
    global checks
    assert x > 0, x
    checks += 1


def atoms(K):
    n = K.rows
    out = []
    for bits in product((0, 1), repeat=n):
        absence = s.diag(*(1 - b for b in bits))
        W = K - absence
        mass = s.simplify((-1) ** (n - sum(bits)) * W.det())
        positive(mass)
        Y = W.inv()
        equal(Y, Y.conjugate().T)
        out.append((bits, mass, Y))
    equal(sum(p for _, p, _ in out), 1)
    equal(sum((p * Y for _, p, Y in out), s.zeros(n)))
    return out


def phi(data, U):
    return s.simplify(sum((p * Y * U * Y for _, p, Y in data), s.zeros(U.rows)))


def fisher(data, U, V=None):
    if V is None:
        V = U
    return s.simplify(sum(p * s.trace(Y * U) * s.trace(Y * V) for _, p, Y in data))


def basis(n):
    out = []
    for i in range(n):
        U = s.zeros(n)
        U[i, i] = 1
        out.append(U)
    for i in range(n):
        for j in range(i + 1, n):
            U = s.zeros(n)
            U[i, j] = U[j, i] = 1
            out.append(U)
            V = s.zeros(n)
            V[i, j], V[j, i] = s.I, -s.I
            out.append(V)
    return out


# Dense complex three-site base: exact atom normalization and full Hermitian
# polarization, including imaginary velocities. This verifies the CP identity
# used in the theorem; it does not test only the diagonal score subspace.
K = s.Matrix([[Q(3, 10), Q(1, 20), s.I / 30],
              [Q(1, 20), Q(1, 2), Q(1, 40)],
              [-s.I / 30, Q(1, 40), Q(7, 10)]])
for M in (K, s.eye(3) - K):
    for j in range(1, 4):
        positive(M[:j, :j].det())
data = atoms(K)
Bs = basis(3)
for U in Bs:
    for V in Bs:
        equal(fisher(data, U, V), s.trace(phi(data, U) * V))

A = s.Matrix([[1, s.I / 3, Q(1, 7)],
              [-s.I / 3, -2, Q(1, 5)],
              [Q(1, 7), Q(1, 5), 3]])
t = s.Symbol('t', real=True)
for bits, p, Y in data:
    Wt = K + t * A - s.diag(*(1 - b for b in bits))
    pt = (-1) ** (3 - sum(bits)) * Wt.det()
    equal(s.diff(pt, t).subs(t, 0), p * s.trace(Y * A))
    equal(s.diff(pt, t, 2).subs(t, 0),
          p * (s.trace(Y * A) ** 2 - s.trace(Y * A * Y * A)))

# Exact rational non-spectral optimum. Cubic self-consistency, primal
# feasibility, and the matching dual potential together establish optimality.
Kd = s.diag(Q(7, 16), Q(1, 64))
Ad = s.Matrix([[0, 1], [1, 0]])
D = s.diag(2, Q(1, 2))
dd = atoms(Kd)
V = phi(dd, D)
equal(V, s.diag(Q(512, 63), Q(2048, 63)))
equal(D * V * D, Ad * V * Ad)
for sign in (-1, 1):
    equal((D + sign * Ad).det())
    positive((D + sign * Ad).trace())
beta = fisher(dd, D)
equal(beta, Q(2048, 63))
equal(fisher(dd, s.eye(2)), Q(4352, 63))
fstar = [s.trace(Y * D) for _, p, Y in dd]
equal(sum(p * f for (_, p, _), f in zip(dd, fstar)))
Vf = sum((p * f * Y for (_, p, Y), f in zip(dd, fstar)), s.zeros(2))
equal(Vf, V)
variance = sum(p * f * f for (_, p, _), f in zip(dd, fstar))
equal(variance, beta)
# sqrt(V) A sqrt(V) has zero diagonal and off-diagonal 1024/63.
trace_absolute = 2 * Q(1024, 63)
equal(2 * trace_absolute - variance, beta)

# Generic probability/potential jets: retain arbitrary second potential
# derivatives and verify their cancellation at a touching point.
ps = [Q(1, 5), Q(3, 10), Q(1, 2)]
ds = [Q(1, 7), -Q(2, 7), Q(1, 7)]
dds = [Q(3, 11), -Q(4, 11), Q(1, 11)]
us = [Q(2, 3), -Q(1, 7), Q(3, 5)]
ws = [Q(7, 11), -Q(3, 13), Q(2, 17)]
logp = [s.log(p) for p in ps]
mean_u = sum(p * u for p, u in zip(ps, us))
variance_u = sum(p * u * u for p, u in zip(ps, us)) - mean_u ** 2
Gpp = (variance_u + sum(p * w for p, w in zip(ps, ws))
       - sum(b * l + 2 * a * u + p * w
             for p, a, b, l, u, w in zip(ps, ds, dds, logp, us, ws)))
Hpp = -sum(a * a / p + b * l for p, a, b, l in zip(ps, ds, dds, logp))
residual = [u - a / p for p, a, u in zip(ps, ds, us)]
mean_r = sum(p * r for p, r in zip(ps, residual))
variance_r = sum(p * r * r for p, r in zip(ps, residual)) - mean_r ** 2
equal(Gpp - Hpp, variance_r)

# Scalar global obstruction for the affine score potential. At the displayed
# q, the exponential surrogate is Bernoulli(1/2), so no log approximation is
# involved in the positive Hessian calculation.
k0 = Q(1, 10)
qstar = k0 + Q(9, 100) * s.log(9)
v0 = k0 * (1 - k0)
surrogate_odds = s.exp(s.log(k0 / (1 - k0)) + (qstar - k0) / v0)
equal(surrogate_odds, 1)
Gpp_scalar = Q(1, 4) / v0 ** 2 - 2 / v0
equal(Gpp_scalar, Q(700, 81))
positive(Gpp_scalar)

result = {
    'status': 'PASS',
    'exact_assertions': checks,
    'dense_complex_hermitian_polarizations': len(Bs) ** 2,
    'rational_optimum': str(beta),
    'spectral_majorant_cost': str(fisher(dd, s.eye(2))),
    'optimizer': str(D.tolist()),
    'cubic_equation': 'D Phi(D) D = A Phi(D) A',
    'affine_score_surrogate_positive_scalar_curvature': str(Gpp_scalar),
}
path = Path(__file__).with_name('certificate.json')
path.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
