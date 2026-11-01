"""Exact checks of the X071 conditional secant and nonlinear-flow identities."""
from pathlib import Path
import json
import sympy as s

OUT = Path(__file__).resolve().parent
I = s.I
checks = 0

def check(x):
    global checks
    if isinstance(x, s.MatrixBase):
        assert all(s.expand(z) == 0 for z in x), x
    else:
        assert bool(x), x
    checks += 1

def logq(x):
    x = s.Rational(x)
    assert x > 0
    return sum(e * s.log(p) for p, e in s.factorint(x.p).items()) - sum(
        e * s.log(p) for p, e in s.factorint(x.q).items())

def atom_data(J):
    n = J.rows
    out = []
    for m in range(2 ** n):
        M = J - s.diag(*[int(not (m >> j) & 1) for j in range(n)])
        sign = (-1) ** (n - m.bit_count())
        p = s.expand(sign * M.det())
        assert p > 0
        out.append((p, M.inv(), sign * M.adjugate()))
    return out

def gradient(J):
    return -sum((logq(p) * grad for p, Y, grad in atom_data(J)), s.zeros(J.rows))

def curvature(J, A):
    fi = s.S(0)
    acceleration = s.S(0)
    for p, Y, grad in atom_data(J):
        score = s.trace(Y * A)
        fi += p * score ** 2
        acceleration += p * (score ** 2 - s.trace(Y * A * Y * A)) * logq(p)
    return s.expand(fi + acceleration)

def integrated_log(x, y):
    if x == y:
        return logq(x)
    return (y * logq(y) - x * logq(x)) / (y - x) - 1

def secant(J1, J0):
    D = J0 - J1
    check(D.det() == 0)
    P = s.zeros(2)
    ilog = []
    for (p, Y, _), (p0, _, _) in zip(atom_data(J1), atom_data(J0)):
        coef = p if p == p0 else p ** 2 * (logq(p0) - logq(p)) / (p0 - p)
        P += coef * Y * D * Y
        ilog.append(integrated_log(p, p0))
    L = s.expand(ilog[1] + ilog[2] - ilog[0] - ilog[3])
    G = gradient(J1) - gradient(J0)
    check(G - P + L * D.adjugate())
    return D, s.expand(P), L, G

def conditional(K, A, k):
    rr = [j for j in range(3) if j != k]
    a, d = K[k, k], A[k, k]
    b, q = 1 - a, a * (1 - a)
    v, w = K.extract(rr, [k]), A.extract(rr, [k])
    R, C = K.extract(rr, rr), A.extract(rr, rr)
    J1, J0 = R - v * v.H / a, R + v * v.H / b
    E1 = C - (w * v.H + v * w.H) / a + d * v * v.H / a ** 2
    E0 = C + (w * v.H + v * w.H) / b + d * v * v.H / b ** 2
    D, P, L, G = secant(J1, J0)
    T = d * C - w * w.H
    rhs = d ** 2 / q + a * curvature(J1, E1) + b * curvature(J0, E0) - 2 * s.trace(G * T)
    check(s.expand(rhs - curvature(K, A)) == 0)
    rhs_new = d ** 2 / q + a * curvature(J1, E1) + b * curvature(J0, E0)
    rhs_new += 2 * (w.H * P * w)[0] - 2 * d * s.trace(P * C)
    rhs_new += 2 * L * s.trace(D.adjugate() * T)
    check(s.expand(rhs_new - curvature(K, A)) == 0)
    wedge = (v.H * v)[0] * (w.H * w)[0] - abs((v.H * w)[0]) ** 2
    check(s.expand(s.trace(D.adjugate() * w * w.H) - wedge / q) == 0)
    return rhs_new

K = s.Matrix([[s.Rational(1,5), s.Rational(1,10), s.Rational(1,20)],
              [s.Rational(1,10), s.Rational(3,5), s.Rational(1,10)],
              [s.Rational(1,20), s.Rational(1,10), s.Rational(4,5)]])
A = s.Matrix([[0, (1-I)/20, (1-I)/40],
              [(1+I)/20, s.Rational(1,4), I/20],
              [(1+I)/40, -I/20, s.Rational(1,5)]])
Ar = s.Matrix([[s.Rational(1,7), s.Rational(1,10), s.Rational(3,20)],
               [s.Rational(1,10), -s.Rational(1,8), s.Rational(1,5)],
               [s.Rational(3,20), s.Rational(1,5), s.Rational(1,9)]])
Az = Ar - s.diag(*Ar.diagonal())

for B in (A, Ar, Az):
    terms = [conditional(K, B, k) for k in range(3)]
    check(s.expand(sum(terms) - 3 * curvature(K, B)) == 0)

Kcomplex = K.copy()
Kcomplex[0,2], Kcomplex[2,0] = I/20, -I/20
terms = [conditional(Kcomplex, A, k) for k in range(3)]
check(s.expand(sum(terms) - 3 * curvature(Kcomplex, A)) == 0)

for endpoint in (K - A/10, K + A/10):
    for J in (endpoint, s.eye(3)-endpoint):
        for n in (1, 2, 3):
            check(s.expand(J[:n, :n].det()) > 0)

check(A.det() == -s.Rational(21,16000))
check(A[1:,1:].det() == s.Rational(19,400))
check(A[1:,0] == (1+I) * K[1:,0] / 2)

# The normal compression kills arbitrary pivot and incident accelerations.
t, a, d, e = s.symbols('t a d e', real=True)
v1, v2, w1, w2, z1, z2 = s.symbols('v1 v2 w1 w2 z1 z2', real=True)
vt = s.Matrix([v1+t*w1+t*t*z1/2, v2+t*w2+t*t*z2/2])
at = a+t*d+t*t*e/2
Djet = vt * vt.T / (at * (1-at))
normal = s.Matrix([-v2, v1])
normal_acc = (normal.T * Djet.diff(t, 2).subs(t, 0) * normal)[0]
check(s.factor(normal_acc - 2*(-v2*w1+v1*w2)**2/(a*(1-a))) == 0)

# Generic Hermitian Gram completion used in the sharp transverse cost.
p11,p22,pr,pi,r1,i1,r2,i2=s.symbols('p11 p22 pr pi r1 i1 r2 i2',real=True)
Pgeneric=s.Matrix([[p11,pr+I*pi],[pr-I*pi,p22]])
ugeneric=s.Matrix([r1+I*i1,r2+I*i2])
Dgeneric=ugeneric*ugeneric.H
check(Pgeneric*Dgeneric*Pgeneric+Pgeneric.det()*Dgeneric.adjugate()-s.trace(Pgeneric*Dgeneric)*Pgeneric)

# Distinct incident radial ratios give a nonzero obstruction at all pivots.
wedges = []
for k in range(3):
    rr = [j for j in range(3) if j != k]
    v, w = K.extract(rr,[k]), Az.extract(rr,[k])
    val = s.det(s.Matrix.hstack(v, w)) ** 2
    check(val > 0)
    wedges.append(str(val))

result = {
    'status': 'PASS', 'exact_assertions': checks,
    'example_det_A': str(A.det()),
    'example_exterior_det': str(A[1:,1:].det()),
    'example_curvature_display': str(s.N(curvature(K,A), 35)),
    'distinct_ratio_wedge_squares': wedges,
    'scope': 'Finite secant identity, sharp transverse cost, and Schur-flow obstruction; full real three-site case remains open.'
}
(OUT/'certificate.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
