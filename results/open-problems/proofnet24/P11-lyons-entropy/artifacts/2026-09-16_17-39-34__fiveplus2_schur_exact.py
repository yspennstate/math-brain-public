#!/usr/bin/env python3
from sympy import Matrix, symbols, simplify, Rational
import random

NONEMPTY=[1,2,3,4,5,6,7]
W=Matrix([
    [1 if (S&1) else 0 for S in NONEMPTY],
    [1 if (S&2) else 0 for S in NONEMPTY],
    [1 if (S&4) else 0 for S in NONEMPTY],
    [-1 for S in NONEMPTY],
    [1 if S==7 else 0 for S in NONEMPTY],
    [1 if (S&3)==3 else 0 for S in NONEMPTY],
    [1 if (S&5)==5 else 0 for S in NONEMPTY],
])
assert W.det()==-1
assert all(x.q==1 for x in W.inv())

# Pair-count identity on every atom:
# 1_12+1_13+1_23 = X1+X2+X3+1_empty+1_full-1.
for S in range(8):
    lhs=sum(1 for P in [3,5,6] if (S&P)==P)
    rhs=sum(1 for bit in [1,2,4] if S&bit)+(1 if S==0 else 0)+(1 if S==7 else 0)-1
    assert lhs==rhs

# Covariance transforms exactly under W.
p=symbols('p1:8')
pv=Matrix(p)
V=Matrix.diag(*p)-pv*pv.T
Cov=W*V*W.T
assert Cov==Cov.T

# Exact integer Schur identity: for arbitrary SPD integer C and integer v,
# Psi2 = delta^2 * Phi. Also check the five-feature determinant lemma.
rng=random.Random(20260916173934)
for trial in range(20):
    L=Matrix([[rng.randint(-3,3) for _ in range(7)] for __ in range(7)])
    C=L*L.T+Matrix.eye(7)
    v=Matrix([rng.randint(-4,4) for _ in range(7)])
    A=C[:5,:5]
    B=C[:5,5:]
    D=C[5:,5:]
    u=v[:5,:]
    w=v[5:,:]
    delta=A.det()
    assert delta>0
    adjA=A.adjugate()
    Shat=delta*D-B.T*adjA*B
    rhat=delta*w-B.T*adjA*u
    ahat=(u.T*adjA*u)[0]
    psi2=(rhat.T*Shat.adjugate()*rhat)[0]-(2*delta-ahat)*Shat.det()
    phi=(v.T*C.adjugate()*v)[0]-2*C.det()
    assert simplify(psi2-phi*delta**2)==0

    # det(A - uu^T/2)=det(A)-u^T adj(A)u/2.
    G=A-u*u.T/Rational(2)
    assert simplify(G.det()-(delta-ahat/Rational(2)))==0

print("PASS")
print("claim=P11-LYONS-FIVEPLUS2-SCHUR-02")
print("feature_transform_det=-1")
print("feature_transform_inverse=INTEGER_EXACT")
print("pair_sum_relation=EXACT_ON_8_ATOMS")
print("schur_trials=20_EXACT_INTEGER")
print("identity=Psi2-delta^2*Phi==0")
print("five_feature_det_lemma=EXACT")
