"""Exact identities for C031's one-coherent-pair endpoint theorem.

Run from any directory.  Symbolic identities prove the displayed example's
channel and conditional-kernel formulas; numerical entropies only illustrate
the analytic nonnegative decomposition proved in agents/C031.md.
"""
from pathlib import Path
from itertools import product
import json

import sympy as S
import mpmath as mp

HERE = Path(__file__).resolve().parent
t, r = S.symbols("t r", real=True)
I = S.I
R = S.Rational
states = list(product((0, 1), repeat=4))
ostates = list(product((0, 1), repeat=2))
ustates = ostates

D = S.Matrix([[24,6,0,0],[6,30,0,0],[0,0,20,0],[0,0,0,36]]) / 60
K = S.Matrix([[30,-3+2*I,6,2+I],[-3-2*I,27,1+3*I,-4],
              [6,1-3*I,24,3-I],[2-I,-4,3+I,33]]) / 60
B, D0 = D[:2,:2], D[2:,2:]
A, V, C = K[:2,:2], K[:2,2:], K[2:,2:]

def atom(M, x):
    return S.expand((-1)**x.count(0) *
                    (M-S.diag(*[1-a for a in x])).det())

def law(M, space):
    return [S.cancel(atom(M,x)) for x in space]

def matrix_json(M):
    return [[str(S.cancel(v)) for v in row] for row in M.tolist()]

def coeffs(p):
    return [str(v) for v in reversed(S.Poly(S.expand(p),t).all_coeffs())]

def outside_reset_prob(x, y):
    ans = S.Integer(1)
    for j in range(2):
        d = D0[j,j]
        mu = d if y[j] else 1-d
        ans *= t*int(x[j] == y[j]) + (1-t)*mu
    return S.expand(ans)

pK, pD = law(K,states), law(D,states)
assert all(p > 0 for p in pK+pD)
assert sum(pK) == sum(pD) == 1
assert V.det() == (-23-7*I)/3600
assert (A-B).det() == -R(103,3600)
assert (C-D0).det() == -R(11,1800)

# Rational absolute-row-sum bounds use |a+ib| <= |a|+|b|.
def gershgorin_l1(M):
    lower, upper = [], []
    for i in range(M.rows):
        rad = sum(abs(S.re(M[i,j]))+abs(S.im(M[i,j]))
                  for j in range(M.cols) if j != i)
        lower.append(M[i,i]-rad)
        upper.append(M[i,i]+rad)
    return min(lower),max(upper)

k_bounds, d_bounds = gershgorin_l1(K), gershgorin_l1(D)
assert k_bounds == (R(1,6),R(11,15))
assert d_bounds == (R(3,10),R(3,5))

Kt = D+t*(K-D)
pKt = law(Kt,states)
Mt_r = A.row_join(r*V).col_join((r*V.conjugate().T).row_join(D0+r*r*(C-D0)))
pMr = law(Mt_r,states)
pMt = []
for p in pMr:
    poly = S.Poly(p,r)
    assert all(power[0] % 2 == 0 for power,coef in poly.terms())
    pMt.append(S.expand(sum(coef*t**(power[0]//2) for power,coef in poly.terms())))

# The measured outside-only Gaussian attenuation is exactly classical reset.
pReset = []
for y in states:
    p = sum(pK[i]*outside_reset_prob(x[2:],y[2:])
            for i,x in enumerate(states) if x[:2] == y[:2])
    pReset.append(S.expand(p))
assert all(S.expand(a-b)==0 for a,b in zip(pMt,pReset))
assert S.expand(sum(pMt)) == S.expand(sum(pKt)) == 1
for u in ustates:
    assert S.expand(sum(pMt[i] for i,x in enumerate(states) if x[:2]==u)-atom(A,u)) == 0
    assert S.expand(sum(pKt[i] for i,x in enumerate(states) if x[:2]==u)-atom(B+t*(A-B),u)) == 0

Ct = D0+t*(C-D0)
q0, q1, qt = law(D0,ostates),law(C,ostates),law(Ct,ostates)
assert all(S.expand(sum(pMt[i] for i,x in enumerate(states) if x[2:]==y)-qt[j]) == 0
           for j,y in enumerate(ostates))

# Conditional covariance identity and all conditional atom identities.
conditionals = []
for yi,y in enumerate(ostates):
    Q = Ct-S.diag(*[1-a for a in y])
    MY = S.simplify(A-t*V*Q.inv()*V.conjugate().T)
    NY = S.simplify(B+t*(MY-B))
    direct_N = S.simplify(B+t*(A-B)-t*t*V*Q.inv()*V.conjugate().T)
    assert S.simplify(NY-direct_N) == S.zeros(2)
    for u in ustates:
        index = states.index(u+y)
        assert S.cancel(qt[yi]*atom(MY,u)-pMt[index]) == 0
        assert S.cancel(qt[yi]*atom(NY,u)-pKt[index]) == 0
    conditionals.append((MY,NY))

mp.mp.dps = 80
def num(x):
    return mp.mpf(str(S.N(x,85)))
def H(ps):
    out = mp.mpf(0)
    for p in ps:
        v = num(p)
        assert v >= 0
        if v:
            out -= v*mp.log(v)
    return out
def sublaw(ps, tt):
    return [S.cancel(p.subs(t,tt)) for p in ps]

hB, hA, hC, hD0 = H(law(B,ustates)), H(law(A,ustates)), H(q1), H(q0)
hK, hD = H(pK),H(pD)
miK = hA+hC-hK
rows = []
for tt in (R(1,4),R(1,2),R(3,4)):
    q = sublaw(qt,tt)
    p = sublaw(pKt,tt)
    pm = sublaw(pMt,tt)
    tm = num(tt)
    gap = H(p)-(1-tm)*hD-tm*hK
    exterior_gap = H(q)-(1-tm)*hD0-tm*hC
    miM = hA+H(q)-H(pm)
    information_term = tm*(miK-miM)
    conditional_gap = mp.mpf(0)
    definite_bound = mp.mpf(0)
    for yi,(MY,NY) in enumerate(conditionals):
        M = MY.subs(t,tt)
        N = NY.subs(t,tt)
        jgap = H(law(N,ustates))-(1-tm)*hB-tm*H(law(M,ustates))
        assert jgap > 0
        conditional_gap += num(q[yi])*jgap
        delta = S.cancel((M-B).det())
        if delta > 0:
            definite_bound += 4*tm*(1-tm)*num(q[yi]*delta)
    residual = gap-exterior_gap-information_term-conditional_gap
    assert abs(residual) < mp.mpf('1e-70')
    assert exterior_gap > 0 and information_term > 0 and conditional_gap > 0
    reset_bound = tm*(1-tm)**2*miK
    assert information_term >= reset_bound
    assert conditional_gap >= definite_bound
    row = dict(t=str(tt), entropy_gap=str(gap), exterior_gap=str(exterior_gap),
               information_loss_term=str(information_term),
               conditional_pair_gap=str(conditional_gap),
               information_lower_bound=str(reset_bound),
               definite_direction_lower_bound=str(definite_bound),
               decomposition_residual=str(residual))
    rows.append(row)

certificate = dict(
    K=matrix_json(K), D=matrix_json(D),
    K_spectral_bounds=list(map(str,k_bounds)), D_spectral_bounds=list(map(str,d_bounds)),
    det_cross=str(V.det()), det_inside_direction=str((A-B).det()),
    det_outside_direction=str((C-D0).det()),
    inside_commutator=matrix_json(A*B-B*A),
    full_direction_determinant=str(S.cancel((K-D).det())),
    atom_order=[list(x) for x in states],
    pK=list(map(str,pK)),pD=list(map(str,pD)),
    pKt_coefficients=[coeffs(p) for p in pKt],
    pMt_coefficients=[coeffs(p) for p in pMt],
    outside_order=[list(x) for x in ostates],
    qt_coefficients=[coeffs(p) for p in qt],
    midpoint_conditional_kernels=[dict(M=matrix_json(M.subs(t,R(1,2))),
                                       N=matrix_json(N.subs(t,R(1,2))))
                                 for M,N in conditionals],
)
(HERE/'exact_certificate.json').write_text(json.dumps(certificate,indent=2)+'\n')
(HERE/'results.json').write_text(json.dumps(dict(mutual_information_K=str(miK),checks=rows),indent=2)+'\n')
print(json.dumps(dict(symbolic_identities='all passed', mutual_information_K=str(miK),checks=rows),indent=2))
