#!/usr/bin/env python3
import itertools, math, random
import numpy as np


def e3_minors(M):
    M=np.asarray(M,float)
    out=0.0
    for I in itertools.combinations(range(M.shape[0]),3):
        for J in itertools.combinations(range(M.shape[1]),3):
            out += np.linalg.det(M[np.ix_(I,J)])**2
    return out

rng=random.Random(20260923)
min_seen=float('inf')
for _ in range(5000):
    s=10**rng.uniform(-3,3)
    t=10**rng.uniform(-3,3)
    a,b,c,d=[rng.uniform(0,2*math.pi) for _ in range(4)]
    u=np.array([math.cos(a),math.sin(a)])
    v=np.array([math.cos(b),math.sin(b)])
    x=np.array([math.cos(c),math.sin(c)])
    y=np.array([math.cos(d),math.sin(d)])
    U=s*np.outer(u,v)
    V=t*np.outer(x,y)
    N=np.block([[np.eye(2),U],[V,np.eye(2)]])
    z=e3_minors(N)
    min_seen=min(min_seen,z)
    assert z >= 3.5-1e-8

s=1/math.sqrt(2)
Nsharp=np.block([[np.eye(2),np.diag([s,0])],[np.diag([s,0]),np.eye(2)]])
assert abs(e3_minors(Nsharp)-3.5)<1e-10

for eps in [1e-1,1e-2,1e-3,1e-4]:
    R=1/eps
    U=np.diag([R,eps])
    V=np.diag([eps,R])
    M=np.block([[np.eye(2),U],[V,np.eye(2)]])
    assert np.linalg.matrix_rank(M,tol=1e-8)==2
    assert e3_minors(M)<1e-16

kappa=math.sqrt(3/5)-3/128
cfrac=(3/8)*kappa-1/64
Crec=(9*math.sqrt(3)*math.e/2)*(7/2)**(-1/6)
Cbound=Crec/cfrac
anchor=(7/6)*cfrac**6

print('random_min_E3',repr(min_seen))
print('sharp_E3',repr(e3_minors(Nsharp)))
print('C_rec',repr(Crec))
print('kappa_star',repr(kappa))
print('c_over_L',repr(cfrac))
print('paid_bound_over_1/L',repr(Cbound))
print('bicolop_anchor_over_L6',repr(anchor))
print('QFORM_B08_RECOLOR_CHECK_PASS')
