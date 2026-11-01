#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import permutations

S4=list(permutations(range(4)))
S3=list(permutations(range(3)))
PAIR_CLASSES=(
    frozenset((frozenset((0,1)),frozenset((2,3)))),
    frozenset((frozenset((0,2)),frozenset((1,3)))),
    frozenset((frozenset((0,3)),frozenset((1,2)))),
)
PCIDX={pc:i for i,pc in enumerate(PAIR_CLASSES)}

def rho_of(p):
    out=[]
    for pc in PAIR_CLASSES:
        image=frozenset(frozenset(p[i] for i in S) for S in pc)
        out.append(PCIDX[image])
    return tuple(out)

def cmul(z,w):
    return (z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])

def cadd(z,w):
    return (z[0]+w[0],z[1]+w[1])

def support_endpoint(a,b,eta,sigma):
    z=(1,0)
    for i in range(4):
        z=cmul(z,cadd(a[i],b[sigma[i]]))
    return F(eta[0]*z[0]-eta[1]*z[1])

def external_value(f,tau,rhop):
    rt=rho_of(tau)
    Bt=sum((f[p] for p in S4 if rho_of(p)==rt),F(0))/4
    Bp=sum((f[p] for p in S4 if rho_of(p)==rhop),F(0))/4
    return F(2,3)*(Bt+Bp)-F(1,3)*f[tau]

# fleet02/B09 r15 genuinely-complex datum, later sharpened by fleet03/B20.
a=((0,-6),(0,5),(3,5),(1,0))
b=((7,4),(1,7),(1,-5),(-3,0))
eta=(-1,2)
f={p:support_endpoint(a,b,eta,p) for p in S4}
M=max(f.values())
assert M==F(7470)

vals=[]
for tau in S4:
    rt=rho_of(tau)
    ders=[rp for rp in S3 if all(rp[i]!=rt[i] for i in range(3))]
    assert len(ders)==2
    for rp in ders:
        vals.append((external_value(f,tau,rp),tau,rp))
assert len(vals)==48
E,tau,rp=max(vals,key=lambda x:x[0])
assert E==F(8414,3)
margin=M-E
assert margin==F(13996,3)>0

print('PASS MOC4-TRANSPORT-DATUM-EXTERNAL-CLOSURE-v1')
print('endpoint_M =',M)
print('external_count =',len(vals))
print('external_max =',E)
print('external_margin =',margin)
print('max_external_tau =',tau)
print('max_external_rho_prime =',rp)
print('conclusion = Drury/Saxl 72-vertex outer criterion closes this support direction for every true unitary')
