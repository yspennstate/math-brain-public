#!/usr/bin/env python3
"""Independent finite sanity checker for R20 audit of R01/I0024 run 3.
Checks a reversible chain with self-loops and the antisymmetric projection factor.
The theorem proof is in the R20 audit note; this checker is only the exact finite core.
"""
import random
import sympy as sp

# Reversible 3-state chain with self-loops and nonuniform stationary law.
P=sp.Matrix([
    [sp.Rational(1,2),sp.Rational(1,2),0],
    [sp.Rational(1,4),sp.Rational(1,2),sp.Rational(1,4)],
    [0,sp.Rational(1,2),sp.Rational(1,2)]])
pi=sp.Matrix([sp.Rational(1,4),sp.Rational(1,2),sp.Rational(1,4)])
Pi=sp.diag(*pi)
B=sp.Matrix([[1,0],[-1,1],[0,-1]])
C=sp.diag(sp.Rational(1,8),sp.Rational(1,8))
L=B*C*B.T
assert L==Pi*(sp.eye(3)-P)
assert P.eigenvals()=={sp.Integer(1):1,sp.Rational(1,2):1,sp.Integer(0):1}
tau2=sp.Integer(2)

# Electrical centered state-to-stationarity flow family.
Lp=L.pinv()
Psi=C*B.T*Lp*(sp.eye(3)-pi*sp.ones(1,3))
assert B*Psi==sp.eye(3)-pi*sp.ones(1,3)
assert Psi*pi==sp.zeros(2,1)
G=Psi.T*C.inv()*Psi
# Pi*G is similar to Pi^(1/2) G Pi^(1/2), avoiding radicals.
evs=(Pi*G).eigenvals()
assert evs=={sp.Integer(2):1,sp.Integer(1):1,sp.Integer(0):1}
assert max(evs.keys())==tau2
print('LOOPED_CHAIN_GRAM_PASS tau2=',tau2,'eigenvalues=',sorted(evs.keys()))

# Independent exact checks of the antisymmetric projection inequality
# Var_pi(g) <= (1/2) E[D_XY^2].
rng=random.Random(202609161607)
for trial in range(500):
    raw=[rng.randint(1,9) for _ in range(5)]
    den=sum(raw)
    q=[sp.Rational(x,den) for x in raw]
    D=sp.zeros(5)
    for i in range(5):
        for j in range(i+1,5):
            a=sp.Rational(rng.randint(-9,9),rng.randint(1,9))
            D[i,j]=a; D[j,i]=-a
    g=sp.Matrix([sum(q[j]*D[i,j] for j in range(5)) for i in range(5)])
    mean=sum(q[i]*g[i] for i in range(5))
    assert mean==0
    V=sum(q[i]*g[i]**2 for i in range(5))
    ED2=sum(q[i]*q[j]*D[i,j]**2 for i in range(5) for j in range(5))
    cross=sum(q[i]*q[j]*D[i,j]*(g[i]-g[j]) for i in range(5) for j in range(5))
    diff2=sum(q[i]*q[j]*(g[i]-g[j])**2 for i in range(5) for j in range(5))
    assert cross==2*V
    assert diff2==2*V
    assert 2*V<=ED2
print('ANTISYMMETRIC_PROJECTION_PASS trials=500 seed=202609161607')
print('ALL_EXACT_AUDIT_CHECKS_PASS')
