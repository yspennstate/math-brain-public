"""
PROB20-16 checker: explicit C082 core ball beyond the weak-edge cone.

This is corroborative only. The analytic proof is in the paired report.
Checks:
  * exact K_* inversion and exact weak-edge violation;
  * exact resolvent-radius identity;
  * random operator-ball points map into the C082 odds chart;
  * a concrete coherent-satellite chord satisfies the direct entropy inequality
    and the quantitative lower bound from the report.
"""
import math
import numpy as np
import sympy as sp

rng = np.random.default_rng(202609151837)

sqrt2 = sp.sqrt(2)
Lx = sp.Matrix([
    [sp.Rational(8,5), sp.Rational(68,125), sp.Rational(51,125)*sqrt2],
    [sp.Rational(68,125), sp.Rational(8,5), -sp.Rational(51,125)*sqrt2],
    [sp.Rational(51,125)*sqrt2, -sp.Rational(51,125)*sqrt2, sp.Rational(9,5)],
])
Kx = sp.simplify(Lx * (sp.eye(3) + Lx).inv())
K_expected = sp.Matrix([
    [sp.Rational(8846539,15630789), sp.Rational(1812625,15630789), sp.Rational(6375,79546)*sqrt2],
    [sp.Rational(1812625,15630789), sp.Rational(8846539,15630789), -sp.Rational(6375,79546)*sqrt2],
    [sp.Rational(6375,79546)*sqrt2, -sp.Rational(6375,79546)*sqrt2, sp.Rational(47421,79546)],
])
assert sp.simplify(Kx-K_expected) == sp.zeros(3)

weak_violation = sp.simplify(
    Kx[0,1] - sp.Rational(2,7)*(1-Kx[2,2])
)
assert weak_violation == sp.Rational(63250,109415523)
assert weak_violation > 0

delta = sp.Rational(25,6201)
h0 = sp.Rational(25,117)
resolvent_ratio = sp.simplify(delta/(h0*(h0-delta)))
assert resolvent_ratio == sp.Rational(9,100)
assert sp.Rational(317,755) < sp.Rational(21,50)

Kstar = np.array(Kx.evalf(40)).astype(np.complex128)
delta_f = float(delta)
gamma = 2.0/(99.0*468.0**3)

min_l = float("inf")
max_l = -float("inf")
min_rho = float("inf")
max_rho = -float("inf")
min_spec_margin = float("inf")

for _ in range(1000):
    Z = rng.normal(size=(3,3)) + 1j*rng.normal(size=(3,3))
    E = (Z + Z.conj().T)/2
    op = np.linalg.norm(E,2)
    if op == 0:
        continue
    radius = delta_f * rng.uniform(0.0, 1.0)
    E *= radius/op
    K = Kstar + E
    ev = np.linalg.eigvalsh(K)
    min_spec_margin = min(min_spec_margin, ev[0], 1-ev[-1])
    assert ev[0] > 0 and ev[-1] < 1
    L = K @ np.linalg.inv(np.eye(3)-K)
    ell = np.real(np.diag(L))
    rhos = [
        abs(L[1,2])/math.sqrt(ell[1]*ell[2]),
        abs(L[0,2])/math.sqrt(ell[0]*ell[2]),
        abs(L[0,1])/math.sqrt(ell[0]*ell[1]),
    ]
    min_l = min(min_l, *ell)
    max_l = max(max_l, *ell)
    min_rho = min(min_rho, *rhos)
    max_rho = max(max_rho, *rhos)
    assert min(ell) >= 0.5
    assert max(ell) <= 2.0
    assert min(rhos) >= 0.1
    assert max(rhos) <= 0.42

def atom_probs(K):
    K = np.asarray(K, dtype=complex)
    n = K.shape[0]
    out = np.empty(1 << n, dtype=float)
    for mask in range(1 << n):
        M = K.copy()
        outside = [i for i in range(n) if not ((mask >> i) & 1)]
        for i in outside:
            M[i,i] -= 1
        val = ((-1)**len(outside))*np.linalg.det(M)
        assert abs(val.imag) < 2e-10
        out[mask] = val.real
    out[np.abs(out) < 1e-14] = 0.0
    assert out.min() > -2e-10
    assert abs(out.sum()-1) < 2e-10
    return out

def entropy(K):
    p = atom_probs(K)
    p = p[p > 1e-15]
    return float(-(p*np.log(p)).sum())

c = 0.55
v = 0.15
b = np.array([0.45, 0.30j, 0.25], dtype=complex)
bn2 = float(np.vdot(b,b).real)
Delta = max(v*v/c, v*v/(1-c))

E0 = np.array([
    [0.00020, 0.00010j, 0],
    [-0.00010j, -0.00015, 0.00005],
    [0, 0.00005, -0.00005],
], dtype=complex)
E1 = np.array([
    [-0.00010, 0.00008, 0.00003j],
    [0.00008, 0.00012, -0.00004],
    [-0.00003j, -0.00004, -0.00002],
], dtype=complex)
z0 = 0.22 + 0.03j
z1 = -0.18 + 0.11j
A0 = Kstar + E0
A1 = Kstar + E1

for A,E,z in [(A0,E0,z0),(A1,E1,z1)]:
    s = abs(z)**2
    budget = np.linalg.norm(E,2) + s*Delta*bn2
    assert budget < delta_f
    B = (z*b*v).reshape(3,1)
    Kfull = np.block([[A, B], [B.conj().T, np.array([[c]])]])
    ev = np.linalg.eigvalsh(Kfull)
    assert ev[0] > 0 and ev[-1] < 1

def full(A,z):
    B = (z*b*v).reshape(3,1)
    return np.block([[A, B], [B.conj().T, np.array([[c]])]])

K0 = full(A0,z0)
K1 = full(A1,z1)
H0 = entropy(K0)
H1 = entropy(K1)

min_gap = float("inf")
for t in np.linspace(0.01,0.99,99):
    Kt = (1-t)*K0 + t*K1
    gap = entropy(Kt) - ((1-t)*H0 + t*H1)
    min_gap = min(min_gap, gap)
    assert gap > 0

t = 0.5
actual_gap = entropy((K0+K1)/2) - (H0+H1)/2
s0 = abs(z0)**2
s1 = abs(z1)**2
bars = (s0+s1)/2
ds = s1-s0
nu = v**4/(c*(1-c))
dA = A1-A0
lb_core = (
    gamma/2*t*(1-t) *
    (np.linalg.norm(dA,'fro')**2 + ds**2*nu*bn2**2)
)
lb_phase = (
    8*t*(1-t)*abs(z1-z0)**2*bars *
    np.max(np.abs(b))**4 * abs(v)**4
)
lower_bound = lb_core + lb_phase
assert actual_gap + 1e-14 >= lower_bound

print("PROB20-16 C082 CORE-BALL CHECK PASSED")
print("exact weak-edge violation =", weak_violation)
print("delta_star =", delta, "=", delta_f)
print("exact resolvent odds radius =", resolvent_ratio)
print("sampled min spectral margin =", min_spec_margin)
print("sampled odds diagonal range =", (min_l, max_l))
print("sampled normalized-rho range =", (min_rho, max_rho))
print("satellite minimum sampled chord gap =", min_gap)
print("satellite midpoint actual gap =", actual_gap)
print("satellite midpoint analytic lower bound =", lower_bound)
