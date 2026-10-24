#!/usr/bin/env python3
"""Exact C066 certificate: adaptive reversible transport of four-site DPPs.

Only the final displayed entropy values use floating point. Atom identities,
operator identities, interval-wide positivity, and all rational constants
are certified by SymPy exact arithmetic.
"""
from itertools import product
from pathlib import Path
import json

import mpmath as mp
import sympy as sp

OUT = Path(__file__).resolve().parent
Q = sp.Rational
eta, theta = sp.symbols("eta theta", real=True)
b, a = Q(1, 20), Q(1, 40)
alpha, gamma = 4*b*b, 4*a*a
zeta, chi = 32*b*b*a*a, gamma*gamma
theta_eta = sp.cancel(zeta / (zeta + chi*eta**2))
assert sp.cancel(-eta*sp.diff(theta_eta, eta)
                 -2*theta_eta*(1-theta_eta)) == 0

K = sp.Matrix([
    [Q(1, 2), b, a*eta, 0],
    [b, Q(1, 2), 0, -a*eta],
    [a*eta, 0, Q(1, 2), b],
    [0, -a*eta, b, Q(1, 2)],
])
A = K.diff(eta)
I4 = sp.eye(4)
assert sp.simplify((K-I4/2)**2-(b*b+a*a*eta**2)*I4) == sp.zeros(4)
assert A.rank() == 4 and A[:2, 2:].rank() == 2
assert (b+a) < Q(1, 2)

spins = list(product((-1, 1), repeat=4))
mu, h, v, atoms = [], [], [], []
for y in spins:
    z, w, s = y[0]*y[1], y[2]*y[3], y[0]*y[2]
    q = (1-alpha*z)*(1-alpha*w)
    mui, hi, vi = q/16, -s*gamma*(1+z*w)/q, z*w/q
    fi = 1+eta**2*hi+(zeta*eta**2+chi*eta**4)*vi
    absent = [int(yi == 1) for yi in y]
    atom = sp.expand((-1)**sum(absent)*(K-sp.diag(*absent)).det())
    assert sp.expand(atom-mui*fi) == 0
    mu.append(mui)
    h.append(hi)
    v.append(vi)
    atoms.append(atom)

mu, h, v = map(sp.Matrix, (mu, h, v))
W = sp.diag(*mu)
one = sp.ones(16, 1)
def inner(x, y):
    return (x.T*W*y)[0]

assert inner(one, one) == 1
assert inner(one, h) == inner(one, v) == inner(h, v) == 0
H, V = inner(h, h), inner(v, v)
assert H == 2*gamma**2*(1+alpha**2)/(1-alpha**2)**2
assert V == 1/(1-alpha**2)**2

# Each mode has zero marginal on both coherent measured blocks. This proves
# its zero pairing with log(mu), without evaluating or simplifying logarithms.
for block in ((0, 1), (2, 3)):
    for state in product((-1, 1), repeat=2):
        ids = [i for i, y in enumerate(spins)
               if tuple(y[j] for j in block) == state]
        assert sum(mu[i]*h[i] for i in ids) == 0
        assert sum(mu[i]*v[i] for i in ids) == 0

R = one*mu.T
Ph = h*(h.T*W)/H
Pv = v*(v.T*W)/V
I = sp.eye(16)
for P in (R, Ph, Pv):
    assert P*P == P
    assert W*P == P.T*W
assert R*Ph == Ph*R == R*Pv == Pv*R == Ph*Pv == Pv*Ph == sp.zeros(16)

L = 4*(R-I)+2*Ph+2*theta*Pv
M = 12*(R-I)+10*Ph+10*theta*Pv
dotL = 4*theta*(1-theta)*Pv
compensation = dotL + L*L + L + M
assert compensation.applyfunc(sp.expand) == sp.zeros(16)
assert L*one == M*one == sp.zeros(16, 1)
assert (mu.T*L).applyfunc(sp.expand) == sp.zeros(1, 16)
assert (mu.T*M).applyfunc(sp.expand) == sp.zeros(1, 16)

f = one+eta**2*h+(zeta*eta**2+chi*eta**4)*v
Leta, Meta = L.subs(theta, theta_eta), M.subs(theta, theta_eta)
assert (Leta*f+eta*f.diff(eta)).applyfunc(sp.cancel) == sp.zeros(16, 1)
assert (Meta*f+eta**2*f.diff(eta, 2)).applyfunc(sp.cancel) == sp.zeros(16, 1)

# The affine kernel clock is u -> K_(eta0-u), and G=L_eta/eta. The identity
# -(dG/du + G^2)=M_eta/eta^2 follows from the checked operator polynomial;
# verify it again directly as a rational matrix identity in eta.
G = Leta/eta
affine_identity = -G.diff(eta)+G*G+Meta/eta**2
assert affine_identity.applyfunc(sp.cancel) == sp.zeros(16)

rho = (1+alpha)/(1-alpha)
theta_min = Q(8, 9)
assert theta_eta.subs(eta, 1) == theta_min
kappa = max(rho**2*(2/(1+alpha**2)-theta_min), rho)
assert kappa == Q(1020018392, 882178209) < Q(6, 5)
reset_weight = 12-10*kappa
assert reset_weight == Q(385954588, 882178209) > 0

endpoint_checks = []
for t in (theta_min, sp.Integer(1)):
    lt, mt = L.subs(theta, t), M.subs(theta, t)
    kernel_min = min(h[i]*h[j]/H+t*v[i]*v[j]/V
                     for i in range(16) for j in range(16) if i != j)
    predicted = -max(rho**2*(2/(1+alpha**2)-t), t*rho)
    assert kernel_min == predicted
    minL = min(lt[i, j] for i in range(16) for j in range(16) if i != j)
    minM = min(mt[i, j] for i in range(16) for j in range(16) if i != j)
    min_cL = min(mu[i]*lt[i, j] for i in range(16) for j in range(16) if i != j)
    min_cM = min(mu[i]*mt[i, j] for i in range(16) for j in range(16) if i != j)
    assert minL > 0 and minM > 0 and min_cL > 0 and min_cM > 0
    residual = mt-reset_weight*(R-I)
    assert all(residual[i, j] >= 0
               for i in range(16) for j in range(16) if i != j)
    endpoint_checks.append({
        "theta": str(t), "min_projection_kernel": str(kernel_min),
        "min_L_offdiag": str(minL), "min_M_offdiag": str(minM),
        "min_L_conductance": str(min_cL), "min_M_conductance": str(min_cM),
    })

# Rates and conductances are affine in theta, so checking the two endpoints
# certifies every eta in [0,1], rather than a numerical sampling grid.
density_lower_bound = 1-max(map(abs, h))-(zeta+chi)*max(map(abs, v))
assert density_lower_bound > 0

# The previously known fixed-reversibility obstruction is present here:
# distinct decay eigenmodes are nonorthogonal in L2(mu).
fixed_obstruction = inner(h+zeta*v, chi*v)
assert fixed_obstruction == Q(1, 3199360032) > 0
oblique_kappa = rho**2*(2+zeta/gamma)/(1+alpha**2)
assert oblique_kappa == Q(206060200, 98019801) > 2
assert min((h[i]+zeta*v[i])*h[j]/H
           for i in range(16) for j in range(16) if i != j) == -oblique_kappa

certificate = {
    "status": "ALL EXACT ASSERTIONS PASSED",
    "atom_polynomials_checked": 16,
    "continuum_certificate": "every rate is affine in theta in [8/9,1]",
    "b": str(b), "a": str(a), "alpha": str(alpha), "gamma": str(gamma),
    "zeta": str(zeta), "chi": str(chi), "theta_eta": str(theta_eta),
    "h_norm_squared": str(H), "v_norm_squared": str(V),
    "kappa": str(kappa), "six_fifths_gap": str(Q(6, 5)-kappa),
    "reset_weight": str(reset_weight),
    "density_lower_bound": str(density_lower_bound),
    "fixed_reversibility_obstruction": str(fixed_obstruction),
    "C029_canonical_oblique_kappa": str(oblique_kappa),
    "endpoint_checks": endpoint_checks,
    "states": [dict(spins=y, mu=str(mu[i]), h=str(h[i]), v=str(v[i]),
                    atom=str(atoms[i])) for i, y in enumerate(spins)],
}
(OUT / "exact_certificate.json").write_text(json.dumps(certificate, indent=2)+"\n")

mp.mp.dps = 70
def num(x):
    return mp.mpf(str(sp.N(x, 75)))

mu_n = [num(x) for x in mu]
numeric = []
for e in (Q(1, 4), Q(1, 2), sp.Integer(1)):
    f_n = [num(x.subs(eta, e)) for x in f]
    dp = [num(sp.diff(p, eta).subs(eta, e)) for p in atoms]
    ddp = [num(sp.diff(p, eta, 2).subs(eta, e)) for p in atoms]
    p_n = [mu_n[i]*f_n[i] for i in range(16)]
    fisher = mp.fsum(dp[i]**2/p_n[i] for i in range(16))
    direct = -fisher-mp.fsum(ddp[i]*mp.log(p_n[i]) for i in range(16))
    m_n = [[num(Meta[i,j].subs(eta,e)) for j in range(16)] for i in range(16)]
    dirichlet = mp.fsum(
        mu_n[i]*m_n[i][j]*(f_n[i]-f_n[j])*(mp.log(f_n[i])-mp.log(f_n[j]))/2
        for i in range(16) for j in range(16) if i != j)
    jeffreys = mp.fsum(mu_n[i]*(f_n[i]-1)*mp.log(f_n[i]) for i in range(16))
    residual = num(e)**2*(-direct-fisher)-dirichlet
    assert abs(residual) < mp.mpf("1e-65")
    remainder = dirichlet-num(reset_weight)*jeffreys
    assert remainder > 0
    numeric.append({
        "eta": str(e), "H_second_derivative": mp.nstr(direct, 35),
        "affine_fisher": mp.nstr(fisher, 35),
        "M_dirichlet": mp.nstr(dirichlet, 35),
        "jeffreys_to_decoupled_law": mp.nstr(jeffreys, 35),
        "reset_remainder_dirichlet": mp.nstr(remainder, 35),
        "identity_residual": mp.nstr(residual, 5),
    })
(OUT / "results.json").write_text(json.dumps(numeric, indent=2)+"\n")
print(json.dumps({k: certificate[k] for k in (
    "status", "atom_polynomials_checked", "kappa", "six_fifths_gap",
    "reset_weight", "density_lower_bound", "endpoint_checks")}, indent=2))
print(json.dumps(numeric, indent=2))
