#!/usr/bin/env python3
from collections import defaultdict
from fractions import Fraction
import sympy as sp

V = tuple(range(7))
E = (
    (0,1),(0,2),(0,3),(0,4),(0,5),
    (1,2),(1,3),(1,4),(1,6),(5,6),
)
DIST = 0
M = len(E)

x, q = sp.symbols('x q')


def component_count(mask):
    parent = list(V)

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    for i, (u, v) in enumerate(E):
        if (mask >> i) & 1:
            a, b = find(u), find(v)
            if a != b:
                parent[b] = a
    return len({find(v) for v in V})


# Exact enumeration of the random-cluster partition polynomial after the
# source-valid change of variables x = p/[q(1-p)].  The common positive
# prefactor in p is irrelevant for edge marginals.
D = 0
N = 0
all_count = defaultdict(int)
edge_count = defaultdict(int)
for mask in range(1 << M):
    r = mask.bit_count()
    k = component_count(mask)
    c = r - len(V) + k
    assert c >= 0
    all_count[(r, c)] += 1
    D += x**r * q**c
    if (mask >> DIST) & 1:
        edge_count[(r, c)] += 1
        N += x**r * q**c

D = sp.expand(D)
N = sp.expand(N)
assert sum(all_count.values()) == 1 << M

# M_q(x) = N/D. Its derivative has numerator G.
G = sp.expand(sp.diff(N, x) * D - N * sp.diff(D, x))
positive_square = (q*x**2 + 2*x + 1)**2
P = sp.cancel(G / positive_square)
assert sp.denom(P) == 1
P = sp.Poly(sp.expand(P), x, q).as_expr()
assert sp.expand(G - positive_square * P) == 0

expected_P = (
    q**5*x**14
    +14*q**4*x**13 +10*q**4*x**12 +2*q**4*x**11
    +81*q**3*x**12 +114*q**3*x**11 +61*q**3*x**10 +14*q**3*x**9 +q**3*x**8
    +248*q**2*x**11 +636*q**2*x**10 +804*q**2*x**9 +630*q**2*x**8
    +308*q**2*x**7 +85*q**2*x**6 +10*q**2*x**5
    +304*q*x**10 +1184*q*x**9 +2384*q*x**8 +3000*q*x**7 +2445*q*x**6
    +1290*q*x**5 +428*q*x**4 +82*q*x**3 +7*q*x**2
    -12*x**8 +124*x**7 +473*x**6 +702*x**5 +573*x**4 +282*x**3 +84*x**2 +14*x +1
)
assert sp.expand(P - expected_P) == 0
assert sp.expand(P.subs(x, 0) - 1) == 0
assert sp.Poly(P, x).LC() == q**5

# Forest boundary q=0: the negative derivative pocket is already visible.
P0 = sp.factor(P.subs(q, 0))
expected_P0 = -(2*x + 1)**2 * (3*x**6 - 34*x**5 - 85*x**4 - 82*x**3 - 40*x**2 - 10*x - 1)
assert sp.expand(P0 - expected_P0) == 0

# Multiple positive roots can occur only at resultant zeros.
R = sp.factor(sp.resultant(P, sp.diff(P, x), x))
Q = sp.Poly(
    92694159707929024*q**21
    -2391589630941253288*q**20
    +29746205595411967893*q**19
    -237584429857878700128*q**18
    +1368080890353907048044*q**17
    -6039373752940080693090*q**16
    +21204939066099517868732*q**15
    -60619470428749841791133*q**14
    +143269171746836332047798*q**13
    -282721908167836957015421*q**12
    +468637137631262035601528*q**11
    -654323732181611169153936*q**10
    +769297561572927490222677*q**9
    -758772176437803896017347*q**8
    +622783815342824868970470*q**7
    -419479318411046356889281*q**6
    +226682317220292450964951*q**5
    -94757337900579248668608*q**4
    +28805272039611809516928*q**3
    -5663605479498043130880*q**2
    +538678727161928773632*q
    -16509457795645440,
    q,
)
expected_R = -8707129344 * q**29 * (q - 2)**3 * (q - 1)**21 * Q.as_expr()
assert sp.expand(R - expected_R) == 0

# Exact Sturm root counts in rational q intervals.
def roots_open_interval(poly, a, b):
    return int(poly.count_roots(sp.Rational(a.numerator, a.denominator),
                                sp.Rational(b.numerator, b.denominator)))

qL = Fraction(1, 32618)
qR = Fraction(1, 32617)
chambers = [
    (Fraction(0), qL),
    (qL, qR),
    (qR, Fraction(1, 2)),
    (Fraction(1, 2), Fraction(3, 5)),
    (Fraction(3, 5), Fraction(1)),
]
counts = [roots_open_interval(Q, a, b) for a, b in chambers]
assert counts == [0, 1, 0, 1, 0]
assert Q.eval(sp.Rational(qL.numerator, qL.denominator)) < 0
assert Q.eval(sp.Rational(qR.numerator, qR.denominator)) > 0

# Approximate roots are printed only for orientation; the proof uses exact
# Sturm counts and rational brackets above.
real_Q_roots = sorted([
    complex(z).real for z in sp.nroots(Q.as_expr(), n=50, maxsteps=200)
    if abs(complex(z).imag) < 1e-30 and 0 < complex(z).real < 1
])
assert len(real_Q_roots) == 2
qstar_approx = real_Q_roots[0]

# Positive-x root counts in each q chamber. Exact Sturm counts.
def positive_x_roots_at(qval):
    px = sp.Poly(sp.expand(P.subs(q, sp.Rational(qval.numerator, qval.denominator))), x)
    return int(px.count_roots(0, sp.oo))

samples = [Fraction(1, 40000), Fraction(1, 1000), Fraction(3, 4)]
pos_counts = [positive_x_roots_at(t) for t in samples]
assert pos_counts == [2, 0, 0]

# Why this decides the whole first chamber: for q>0, P(0,q)=1 and the
# leading x coefficient is q^5>0, so roots cannot enter through x=0 or
# infinity. The number of positive simple roots is constant between positive
# resultant roots. Therefore the 2-root chamber is exactly (0,q_*), where
# q_* is the smallest positive root of Q. P is negative between its two roots,
# so dM_q/dx<0 there. Since x=p/[q(1-p)] is increasing in p, the source edge
# marginal is nonmonotone in p for every 0<q<q_*.
# In the other chambers there are no positive roots, and P(0,q)>0, hence P>0.

print('vertices', len(V))
print('edges', M)
print('edge_list', E)
print('distinguished_edge', E[DIST])
print('enumerated_configurations', 1 << M)
print('derivative_factorization_verified', True)
print('P_degree_x', sp.degree(P, x))
print('P_degree_q', sp.degree(P, q))
print('resultant_factorization_verified', True)
print('Q_degree', Q.degree())
print('Q_roots_in_0_1_by_chambers', counts)
print('qstar_bracket', qL, qR)
print('Q_at_left_sign', sp.sign(Q.eval(sp.Rational(qL.numerator, qL.denominator))))
print('Q_at_right_sign', sp.sign(Q.eval(sp.Rational(qR.numerator, qR.denominator))))
print('qstar_decimal', f'{qstar_approx:.34f}')
print('positive_x_root_counts_samples', [(str(t), c) for t, c in zip(samples, pos_counts)])
print('conclusion', 'edge marginal is nonmonotone for every 0<q<qstar and has no negative derivative for qstar<=q<1')
print('ALL_EXACT_CHECKS_PASS')
