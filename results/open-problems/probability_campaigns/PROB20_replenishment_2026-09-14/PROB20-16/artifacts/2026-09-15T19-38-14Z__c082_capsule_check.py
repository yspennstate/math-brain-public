from __future__ import annotations

import math
import numpy as np
import sympy as sp

h, u = sp.symbols("h u", real=True)
I3 = sp.eye(3)

Lstar = sp.Matrix([
    [sp.Rational(8,5), sp.Rational(68,125), sp.Rational(51,125)*sp.sqrt(2)],
    [sp.Rational(68,125), sp.Rational(8,5), -sp.Rational(51,125)*sp.sqrt(2)],
    [sp.Rational(51,125)*sp.sqrt(2), -sp.Rational(51,125)*sp.sqrt(2), sp.Rational(9,5)],
])

# Exact Sylvester checks for 1/2 I < Lstar < 3 I.
low = Lstar - sp.Rational(1,2)*I3
high = 3*I3 - Lstar
low_minors = [sp.factor(low[:k,:k].det()) for k in range(1,4)]
high_minors = [sp.factor(high[:k,:k].det()) for k in range(1,4)]
assert low_minors == [
    sp.Rational(11,10),
    sp.Rational(57129,62500),
    sp.Rational(1462749,15625000),
]
assert high_minors == [
    sp.Rational(7,5),
    sp.Rational(26001,15625),
    sp.Rational(2786922,1953125),
]
assert all(x > 0 for x in low_minors + high_minors)

Kstar = sp.simplify(Lstar * (I3 + Lstar).inv())
Kexpected = sp.Matrix([
    [sp.Rational(8846539,15630789), sp.Rational(1812625,15630789), sp.Rational(6375,79546)*sp.sqrt(2)],
    [sp.Rational(1812625,15630789), sp.Rational(8846539,15630789), -sp.Rational(6375,79546)*sp.sqrt(2)],
    [sp.Rational(6375,79546)*sp.sqrt(2), -sp.Rational(6375,79546)*sp.sqrt(2), sp.Rational(47421,79546)],
])
assert sp.simplify(Kstar-Kexpected) == sp.zeros(3)

Kh = Kstar + h*I3
Lh = sp.simplify((I3-Kh).inv()-I3)

Q = 79546*h**2 - 75875*h + 15625
R = 31261578*h**3 - 8500547*h**2 - 10568625*h + 3125000
S = 79546*h**2 + 3671*h - 28125

expected_entries = {
    (0,0): -R/((393*h-125)*Q),
    (1,1): -R/((393*h-125)*Q),
    (2,2): -S/Q,
    (0,1): 4250*(853*h-250)/((393*h-125)*Q),
    (1,0): 4250*(853*h-250)/((393*h-125)*Q),
    (0,2): 6375*sp.sqrt(2)/Q,
    (2,0): 6375*sp.sqrt(2)/Q,
    (1,2): -6375*sp.sqrt(2)/Q,
    (2,1): -6375*sp.sqrt(2)/Q,
}
for ij, val in expected_entries.items():
    assert sp.factor(Lh[ij]-val) == 0

hlo = sp.Rational(-3,20)
hhi = sp.Rational(3,200)

ell1 = sp.factor(Lh[0,0])
ell3 = sp.factor(Lh[2,2])
assert ell1.subs(h,hlo) == sp.Rational(17654094467,21188122553)
assert ell1.subs(h,hhi) == sp.Rational(11858654039003,6910363881197)
assert ell3.subs(h,hlo) == sp.Rational(5377173,5759207)
assert ell3.subs(h,hhi) == sp.Rational(561040743,290095457)
assert sp.Rational(4,5) < ell1.subs(h,hlo)
assert ell1.subs(h,hhi) < sp.Rational(7,4)
assert sp.Rational(9,10) < ell3.subs(h,hlo)
assert ell3.subs(h,hhi) < sp.Rational(39,20)

# Bernstein conversion: if p(t)=sum q_k t^k has degree n, then
# b_i=sum_{k<=i} q_k*C(i,k)/C(n,k) are the degree-n Bernstein coefficients.
def bernstein_coeffs(poly: sp.Expr, a=hlo, b=hhi):
    transformed = sp.Poly(sp.expand(poly.subs(h, a+(b-a)*u)), u)
    n = transformed.degree()
    q = [transformed.nth(k) for k in range(n+1)]
    out = []
    for i in range(n+1):
        bi = sp.Rational(0)
        for k in range(i+1):
            bi += q[k] * sp.binomial(i,k) / sp.binomial(n,k)
        out.append(sp.factor(bi))
    return out

def assert_positive_bernstein(poly: sp.Expr, label: str):
    coeffs = bernstein_coeffs(sp.expand(poly))
    assert all(c > 0 for c in coeffs), (label, coeffs)
    return coeffs

# Denominator sign certificates over the whole interval.
bern_Q = assert_positive_bernstein(Q, "Q")
bern_R = assert_positive_bernstein(R, "R")
bern_minus_S = assert_positive_bernstein(-S, "-S")
bern_125_minus_393h = assert_positive_bernstein(125-393*h, "125-393h")

A12 = 18062500*(853*h-250)**2
C13 = sp.Integer(81281250)

# rho12^2 >= 1/9 and <= 9/64.
P12_lo = sp.expand(9*A12 - R**2)
P12_hi = sp.expand(9*R**2 - 64*A12)

# rho13^2 = C13*(393h-125)/(S*R), and S*R < 0.
# Multiplication by the negative denominator reverses inequalities.
P13_lo = sp.expand(S*R - 9*C13*(393*h-125))
P13_hi = sp.expand(64*C13*(393*h-125) - 9*S*R)

bern = {
    "rho12_lo": assert_positive_bernstein(P12_lo, "rho12_lo"),
    "rho12_hi": assert_positive_bernstein(P12_hi, "rho12_hi"),
    "rho13_lo": assert_positive_bernstein(P13_lo, "rho13_lo"),
    "rho13_hi": assert_positive_bernstein(P13_hi, "rho13_hi"),
}

# Exact capsule resolvent bound.
mI = sp.Rational(47,200)
delta = sp.Rational(1,1000)
resolvent_bound = sp.factor(delta/(mI*(mI-delta)))
assert resolvent_bound == sp.Rational(100,5499)
assert resolvent_bound < sp.Rational(1,50)

# Exact robust normalized-correlation bounds used in the proof.
rho_upper = sp.Rational(3,8)*sp.Rational(40,39) + sp.Rational(1,39)
rho_lower = sp.Rational(1,3)*sp.Rational(40,41) - sp.Rational(1,41)
assert rho_upper == sp.Rational(16,39)
assert rho_lower == sp.Rational(37,123)
assert rho_upper < sp.Rational(21,50)
assert rho_lower > sp.Rational(1,10)

# The upper scalar-shift endpoint is still outside the older weak-edge cone.
weak_old = sp.Rational(63250,109415523)
weak_upper = sp.factor(weak_old + sp.Rational(2,7)*sp.Rational(3,200))
assert weak_upper > 0

# Corroborative floating-point sampling of the full capsule.
Kstar_np = np.array(Kstar.evalf(30), dtype=np.complex128)
rng = np.random.default_rng(20260915)
mins = {
    "kernel": float("inf"),
    "complement": float("inf"),
    "ell": float("inf"),
    "rho": float("inf"),
}
maxs = {"ell": -float("inf"), "rho": -float("inf")}
for _ in range(1000):
    hv = rng.uniform(float(hlo), float(hhi))
    X = rng.normal(size=(3,3)) + 1j*rng.normal(size=(3,3))
    E = (X + X.conj().T)/2
    op = np.max(np.abs(np.linalg.eigvalsh(E)))
    if op == 0:
        continue
    E *= rng.uniform(0.0, 1.0/1000.0)/op
    K = Kstar_np + hv*np.eye(3) + E
    ev = np.linalg.eigvalsh(K)
    mins["kernel"] = min(mins["kernel"], float(ev.min()))
    mins["complement"] = min(mins["complement"], float((1-ev).min()))
    L = np.linalg.inv(np.eye(3)-K) - np.eye(3)
    ell = np.real(np.diag(L))
    rhos = [
        abs(L[1,2])/math.sqrt(ell[1]*ell[2]),
        abs(L[0,2])/math.sqrt(ell[0]*ell[2]),
        abs(L[0,1])/math.sqrt(ell[0]*ell[1]),
    ]
    mins["ell"] = min(mins["ell"], float(np.min(ell)))
    maxs["ell"] = max(maxs["ell"], float(np.max(ell)))
    mins["rho"] = min(mins["rho"], float(np.min(rhos)))
    maxs["rho"] = max(maxs["rho"], float(np.max(rhos)))
    assert ev.min() > 0 and ev.max() < 1
    assert ell.min() > 0.5 and ell.max() < 2
    assert min(rhos) > 0.1 and max(rhos) < 0.42

print("PROB20-16 C082 CAPSULE CHECK PASSED")
print("low Sylvester minors =", [str(x) for x in low_minors])
print("high Sylvester minors =", [str(x) for x in high_minors])
print("scalar interval =", str(hlo), str(hhi))
print("resolvent odds perturbation bound =", str(resolvent_bound), float(resolvent_bound))
print("robust rho interval =", str(rho_lower), str(rho_upper))
print("weak-edge violation at upper central endpoint =", str(weak_upper), float(weak_upper))
for key, coeffs in bern.items():
    print(key, "Bernstein count =", len(coeffs), "minimum =", min(float(sp.N(c,30)) for c in coeffs))
print("sample minimum kernel eigenvalue =", mins["kernel"])
print("sample minimum complement eigenvalue =", mins["complement"])
print("sample odds diagonal range =", mins["ell"], maxs["ell"])
print("sample normalized-correlation range =", mins["rho"], maxs["rho"])
