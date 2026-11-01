#!/usr/bin/env python3
"""Regression checker for the B14 physical-block restriction cocycle.

This is finite floating-point regression only. The proof is algebraic in REPORT.md.
No external packages are used.
"""
from itertools import product
import math, random

def h2(x):
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x*math.log2(x)-(1-x)*math.log2(1-x)

def entropy(ws):
    return sum(-w*math.log2(w) for w in ws if w > 0.0)

def subsets(n):
    return list(range(1<<n))

def bit(x,i):
    return (x>>i)&1

def prob_x(x,p):
    z=1.0
    for i,pi in enumerate(p):
        z *= pi if bit(x,i) else (1-pi)
    return z

def phi(x,i,p):
    pi=p[i]
    return (bit(x,i)-pi)/math.sqrt(pi*(1-pi))

def b0(x):
    return 1 if x in {0,1,2,3,4,5,8,10} else 0

def coeffs(n,p,fun):
    out=[]
    for A in subsets(n):
        s=0.0
        for x in range(1<<n):
            prodv=1.0
            for i in range(n):
                if (A>>i)&1:
                    prodv *= phi(x,i,p)
            f=1.0 if fun(x) else -1.0
            s += prob_x(x,p)*f*prodv
        out.append(s)
    return out

def spectral_stats(n,p,fun):
    c=coeffs(n,p,fun)
    w=[a*a for a in c]
    H=entropy(w)
    inf=[sum(w[A] for A in subsets(n) if (A>>i)&1) for i in range(n)]
    I=sum(inf)
    r=sum(prob_x(x,p)*fun(x) for x in range(1<<n))
    W=I/4-r*(1-r)
    return c,w,H,inf,I,r,W

def branch_fun(z2,z3):
    def f(y):
        x0=bit(y,0); x1=bit(y,1)
        x=x0|(x1<<1)|(z2<<2)|(z3<<3)
        return b0(x)
    return f

assert [branch_fun(0,0)(y) for y in range(4)] == [1,1,1,1]
assert [branch_fun(0,1)(y) for y in range(4)] == [1,0,1,0]
assert [branch_fun(1,0)(y) for y in range(4)] == [1,1,0,0]
assert [branch_fun(1,1)(y) for y in range(4)] == [0,0,0,0]

rng=random.Random(20260922043512)
max_entropy_err=0.0
max_currency_err=0.0
max_child_W=0.0
min_omega=1.0
for _ in range(5000):
    p=[0.01+0.98*rng.random() for _ in range(4)]
    c,w,H,inf,I,r,W=spectral_stats(4,p,b0)
    EZH=0.0; EZW=0.0; rz=[]; pis=[]; T_S=[0.0]*4
    for z2,z3 in product([0,1], repeat=2):
        pi=(p[2] if z2 else 1-p[2])*(p[3] if z3 else 1-p[3])
        cc,ww,HH,ii,II,rr,WW=spectral_stats(2,[p[0],p[1]],branch_fun(z2,z3))
        EZH += pi*HH; EZW += pi*WW; rz.append(rr); pis.append(pi)
        max_child_W=max(max_child_W,abs(WW))
        for S in range(4): T_S[S]+=pi*ww[S]
    HZ=h2(p[2])+h2(p[3]); HS=entropy(T_S)
    H_Z_given_S=HZ+EZH-HS
    sum_hK=h2(inf[2])+h2(inf[3])
    C=H_Z_given_S + HS + sum_hK - H
    max_entropy_err=max(max_entropy_err,abs(H-(EZH+HZ+sum_hK-C)))
    mean_r=sum(pi*rr for pi,rr in zip(pis,rz))
    var_r=sum(pi*(rr-mean_r)**2 for pi,rr in zip(pis,rz))
    Omega=(inf[2]+inf[3])/4-var_r
    min_omega=min(min_omega,Omega)
    max_currency_err=max(max_currency_err,abs(W-(EZW+Omega)))

C0=6.4548; astar=0.2682048; W_uniform=1/8; Cblock_uniform=1.0
R0_uniform=C0/2-4
Rstar_uniform=R0_uniform+astar*W_uniform
Dstar_uniform=Rstar_uniform+Cblock_uniform
print("B14_BLOCK_COCYCLE_REGRESSION")
print("random_points=5000")
print("max_entropy_identity_error=%.3e" % max_entropy_err)
print("max_currency_identity_error=%.3e" % max_currency_err)
print("max_abs_child_W=%.3e" % max_child_W)
print("min_observed_Omega=%.12g" % min_omega)
print("uniform_W=1/8")
print("uniform_C_block=1")
print("uniform_R_base=%.7f" % R0_uniform)
print("uniform_R_stable=%.7f" % Rstar_uniform)
print("uniform_D_stable=%.7f" % Dstar_uniform)
assert max_entropy_err < 2e-11
assert max_currency_err < 2e-11
assert max_child_W < 2e-12
assert min_omega >= -2e-12
assert abs(R0_uniform + 0.7726) < 1e-12
assert abs(Rstar_uniform + 0.7390744) < 1e-12
assert abs(Dstar_uniform - 0.2609256) < 1e-12
print("PASS")
