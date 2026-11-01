#!/usr/bin/env python3
from fractions import Fraction
import json

def fwht(a):
    a=list(a); n=len(a); h=1
    while h<n:
        for i in range(0,n,2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]
                a[j],a[j+h]=x+y,x-y
        h*=2
    return a

def corr(vals,n,v):
    N=1<<n
    return Fraction(sum(vals[x]*vals[x^v] for x in range(N)), N)

def j(vals,n,v):
    return (1-abs(corr(vals,n,v)))/2

def q(vals,n,v):
    return (1-corr(vals,n,v))/2

def rank(vs,n):
    piv=[0]*n; r=0
    for x in vs:
        y=x
        while y:
            k=y.bit_length()-1
            if piv[k]:
                y ^= piv[k]
            else:
                piv[k]=y; r+=1; break
    return r

def min_basis(vals,n,cost):
    items=sorted((cost(vals,n,v),v) for v in range(1,1<<n))
    chosen=[]; total=Fraction(0); r=0
    for w,v in items:
        nr=rank(chosen+[v],n)
        if nr>r:
            chosen.append(v); total+=w; r=nr
            if r==n: break
    assert r==n
    return total, chosen

def tensor(f,n,g,m):
    mask=(1<<n)-1
    return [f[z&mask]*g[z>>n] for z in range(1<<(n+m))]

def canonical(n):
    N=1<<n
    for mask in range(1<<(N-1)):
        vals=[1]
        vals.extend(-1 if (mask>>(i-1))&1 else 1 for i in range(1,N))
        yield vals

def frac(x):
    return f"{x.numerator}/{x.denominator}"

tested=0
for f in canonical(3):
    Jf,_=min_basis(f,3,j)
    for g in canonical(2):
        Jg,_=min_basis(g,2,j)
        h=tensor(f,3,g,2)
        Jh,_=min_basis(h,5,j)
        assert Jh == Jf + Jg
        tested += 1

# Exact nontrivial counterexample to un-folded linear-basis additivity.
f=[1,-1,-1,-1,1,1,1,1]   # 3 bits
g=[1,-1,1,1]               # 2 bits
h=tensor(f,3,g,2)
Kf,Kfb=min_basis(f,3,q)
Kg,Kgb=min_basis(g,2,q)
Kh,Khb=min_basis(h,5,q)
Jf,Jfb=min_basis(f,3,j)
Jg,Jgb=min_basis(g,2,j)
Jh,Jhb=min_basis(h,5,j)
assert Kh < Kf+Kg
assert Jh == Jf+Jg

# Boundary families.
parity1=[1,-1]
J_parity,_=min_basis(parity1,1,j)
onept3=[-1]+[1]*7
J_onept,_=min_basis(onept3,3,j)
quad2=[1,1,1,-1]  # (-1)^(x0 x1)
J_quad,_=min_basis(quad2,2,j)

out={
    "exhaustive_3x2_product_pairs": tested,
    "all_folded_additivity_checks_passed": True,
    "unfolded_counterexample": {
        "f_values": f,
        "g_values": g,
        "K_f": frac(Kf),
        "K_g": frac(Kg),
        "K_tensor": frac(Kh),
        "K_saving": frac(Kf+Kg-Kh),
        "tensor_basis": Khb,
        "tensor_basis_q_costs": [frac(q(h,5,v)) for v in Khb],
        "J_f": frac(Jf),
        "J_g": frac(Jg),
        "J_tensor": frac(Jh),
        "folded_additivity": Jh == Jf+Jg,
    },
    "boundaries": {
        "character_J": frac(J_parity),
        "one_point_defect_n3_J": frac(J_onept),
        "quadratic_phase_n2_J": frac(J_quad),
    },
}
print(json.dumps(out,indent=2,sort_keys=True))
