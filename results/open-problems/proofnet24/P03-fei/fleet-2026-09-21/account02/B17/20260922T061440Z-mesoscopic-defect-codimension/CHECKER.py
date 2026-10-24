#!/usr/bin/env python3
from fractions import Fraction
import math

C = 6.521851214

def fwt(vals):
    N=len(vals)
    out=[Fraction(v,N) for v in vals]
    h=1
    while h<N:
        for i in range(0,N,2*h):
            for j in range(i,i+h):
                x,y=out[j],out[j+h]
                out[j],out[j+h]=x+y,x-y
        h*=2
    return out

def HI(vals):
    a=fwt(vals)
    H=0.0
    I=Fraction(0)
    for S,x in enumerate(a):
        p=x*x
        if p:
            fp=float(p)
            H-=fp*math.log2(fp)
        I += S.bit_count()*p
    return H,I,a

MAJ3=[1 if x.bit_count()<=1 else -1 for x in range(8)]
Hm,Im,_=HI(MAJ3)
assert abs(Hm-2.0)<1e-14 and Im==Fraction(3,2)

def tensor(v,w):
    return [v[x%len(v)]*w[x//len(v)] for x in range(len(v)*len(w))]

def tensor_power(v,k):
    out=[1]
    for _ in range(k):
        out=tensor(out,v)
    return out

def rare_gate(k,m):
    f=tensor_power(MAJ3,k)
    d=3*k
    vals=[]
    for z in range(1<<(d+m+1)):
        x=z & ((1<<d)-1)
        v=(z>>d)&((1<<m)-1)
        y=(z>>(d+m))&1
        h=-1 if (f[x]==-1 and v==0) else 1
        vals.append((1 if y==0 else -1)*h)
    return vals

cases=[]
for k,m in [(1,1),(1,2),(2,1),(2,2)]:
    vals=rare_gate(k,m)
    H,I,_=HI(vals)
    delta=Fraction(1,2**m)
    e0=(1-float(delta))**2*math.log2(1/(1-float(delta))**2)
    Hpred=float(delta)*(2*k)+4*m*float(delta)-2*m*float(delta)**2+e0
    Ipred=Fraction(1)+delta*(Fraction(3*k,2)+m)
    assert I==Ipred
    assert abs(H-Hpred)<2e-13
    cases.append((k,m,H,float(I),H/(float(I)-1)))

def crude_bound(n,alpha):
    L=alpha*n
    return 2*(n+L-2+math.log2(math.e))/(L-1)

b20=crude_bound(20,0.5)
b21=crude_bound(21,0.5)
assert b20>C and b21<C

alpha_threshold=2/(C-2)
assert 0.44229 < alpha_threshold < 0.44230

print("PASS")
print("majority3_H",Hm)
print("majority3_I",float(Im))
for row in cases:
    print("rare_case",*row)
print("half_density_crude_n20",format(b20,".15f"))
print("half_density_crude_n21",format(b21,".15f"))
print("current_C",C)
print("asymptotic_alpha_threshold",format(alpha_threshold,".15f"))
print("majority_tensor_m_eq_k_limit",12/5)
