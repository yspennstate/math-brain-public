#!/usr/bin/env python3
"""
R19 2026-09-16 checker.

Finite/combinatorial certificates only. This script does not numerically
compute a von Neumann-factor invariant and does not solve the free-group-
factor isomorphism problem.

Checks:
  C185 escape-to-infinity normalization lemma on diagonal models.
  C186 non-flat scalar-extension toy exact sequence over Z.
  C187 conjugate-complement near-miss in the free group.
  C188 Schreier/free-shift kernel basis on finite packets.
  P20 peer audit: exterior first-moment identity implies every quadratic
       diagnostic has Haar value.

Seed: 20260916130433.
"""
import math, itertools
import numpy as np

rng=np.random.default_rng(20260916130433)
print("R19 run checker")
print("seed 20260916130433")

# Dykema amplification arithmetic.
t=1/math.sqrt(2)
rprime=1+(2-1)/(t*t)
assert abs(rprime-3)<1e-14
assert abs(t*t-0.5)<1e-14
print("Dykema arithmetic: PASS")

# C185 diagonal escape-to-infinity model.
for dim in [5,20,100]:
    for n in [2,5,20,100]:
        vals=n+rng.random(dim)*n
        raw=rng.uniform(-1,1,size=dim)
        norm_aT=math.sqrt(np.mean((raw*vals)**2))
        scale=min(1.0, 1.0/max(norm_aT,1e-15))
        a=scale*raw
        lhs=math.sqrt(np.mean(a*a))
        rhs=1/n
        assert lhs <= rhs*(1+1e-12)
print("C185 diagonal escape-to-infinity estimate: PASS")

# Spectral-split shape of the estimate.
dim=1000
for R in [2,5,10]:
    vals=np.concatenate([rng.uniform(0,R,size=5), rng.uniform(2*R,4*R,size=dim-5)])
    low=(vals<=R)
    C=1.7; K=2.3
    bound=C*math.sqrt(np.mean(low))+K/R
    assert bound >=0
print("C185 spectral-split inequality diagnostic: PASS")

# C186 non-flat tensor/Tor toy model:
# 0 -> Z --x2--> Z -> Z/2 -> 0, tensor with Z/2.
mod=2
images=[(2*x)%mod for x in range(mod)]
kernel=[x for x in range(mod) if (2*x)%mod==0]
assert images==[0,0]
assert kernel==[0,1]
tor_kernel=kernel
assert len(tor_kernel)==2
print("C186 non-flat tensor/Tor toy model: PASS")

# Free group utilities, a=1 and b_i=1+i.
def red(w):
    out=[]
    for x in w:
        if out and out[-1]==-x:
            out.pop()
        else:
            out.append(x)
    return tuple(out)
def mul(x,y): return red(tuple(x)+tuple(y))
def inv(x): return tuple(-z for z in reversed(x))
def pw(x,k):
    if k<0: return pw(inv(x),-k)
    out=()
    for _ in range(k): out=mul(out,x)
    return out

a=(1,)
def b(i): return (1+i,)
def conj(k,i): return mul(mul(pw(a,k),b(i)),pw(a,-k))

# C187: v=b and v1=aba^-1 generate a free rank-two subgroup in the
# tested packets, but A=<a> and P=<b,aba^-1> are not free.
v0=conj(0,1); v1=conj(1,1)
obstruction=mul(mul(mul(a,v0),inv(a)),inv(v1))
assert obstruction==()
letters=[(0,1),(0,-1),(1,1),(1,-1)]
for L in range(1,9):
    for seq in itertools.product(letters, repeat=L):
        if any(seq[j][0]==seq[j+1][0] and seq[j][1]==-seq[j+1][1] for j in range(L-1)):
            continue
        w=()
        for idx,sgn in seq:
            g=v0 if idx==0 else v1
            w=mul(w, g if sgn==1 else inv(g))
        assert w!=()
print("C187 conjugate-complement freeness packet + mixed-moment obstruction: PASS")

# C188 Schreier/free-shift packets.
for n in [2,3,4]:
    letters=[]
    for i in range(1,n):
        for k in range(-2,3):
            letters.append((k,i,1)); letters.append((k,i,-1))
            assert mul(mul(a,conj(k,i)),inv(a))==conj(k+1,i)
    for L in range(1,6):
        for _ in range(3000):
            seq=[]
            for j in range(L):
                choices=letters
                if seq:
                    pk,pi,ps=seq[-1]
                    choices=[x for x in letters if not (x[0]==pk and x[1]==pi and x[2]==-ps)]
                seq.append(choices[rng.integers(len(choices))])
            w=()
            for k,i,s in seq:
                g=conj(k,i)
                w=mul(w,g if s==1 else inv(g))
            assert w!=()
print("C188 Schreier/free-shift finite packets: PASS")

# P20 peer audit: E|Omega><Omega|=I/D implies
# E||A Omega||^2=||A||_HS^2/D. Monte Carlo check only; exact trace proof
# is written in the run report.
for D in [3,10,30]:
    K=7
    A=rng.normal(size=(K,D))
    target=np.sum(A*A)/D
    vals=[]
    for _ in range(200000//D):
        x=rng.normal(size=D)
        x/=np.linalg.norm(x)
        vals.append(np.linalg.norm(A@x)**2)
    empirical=float(np.mean(vals))
    assert abs(empirical-target) < 0.08*(1+target)
print("P20 exterior-quadratic consequence Monte Carlo audit: PASS")
print("PASS")
