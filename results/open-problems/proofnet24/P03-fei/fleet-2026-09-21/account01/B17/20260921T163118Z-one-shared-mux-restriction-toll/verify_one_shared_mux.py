#!/usr/bin/env python3
"""Self-checks for the B17 one-shared-variable MUX theorem and sharp local restriction toll."""
from __future__ import annotations
import itertools, math, hashlib

LN2 = math.log(2.0)

def phi(t: float) -> float:
    return 0.0 if t <= 0.0 else -t * math.log2(t)

def h2(p: float) -> float:
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p*math.log2(p) - (1-p)*math.log2(1-p)

def fwht(vals):
    a = [float(x) for x in vals]
    n = len(a)
    h = 1
    while h < n:
        for i in range(0,n,2*h):
            for j in range(i,i+h):
                x,y = a[j],a[j+h]
                a[j],a[j+h] = x+y,x-y
        h *= 2
    return [x/n for x in a]

def entropy(coeff):
    return sum(phi(x*x) for x in coeff)

def influence(coeff):
    n = len(coeff)
    k = n.bit_length()-1
    return sum((s.bit_count())*(coeff[s]**2) for s in range(n))

def psi(x,y):
    return (phi((x+y)**2/4.0)+phi((x-y)**2/4.0)
            -0.5*phi(x*x)-0.5*phi(y*y))

def omega(alpha,beta):
    A=sum(x*x for x in alpha); B=sum(y*y for y in beta)
    return 2-A-B+sum(psi(x,y) for x,y in zip(alpha,beta))

def mux_coeff(a,b):
    # coeff order: S without selector, then S with selector as top bit
    return [(x+y)/2 for x,y in zip(a,b)] + [(x-y)/2 for x,y in zip(a,b)]

def one_shared_core(branch_vals):
    # branch on (y,u), index y+2u. Return coefficients on empty and y.
    a=fwht(branch_vals)
    return (a[0],a[1]), a

def bent_vals(k):
    assert k%2==0
    out=[]
    for x in range(1<<k):
        q=0
        for j in range(0,k,2):
            q ^= ((x>>j)&1) & ((x>>(j+1))&1)
        out.append(1.0 if q==0 else -1.0)
    return out

# 1) Exhaustive one-shared-variable branch test.
# a(y,u), b(y,v), each has 16 possible Boolean truth tables.
max_formula_err=0.0
max_ratio=0.0
argmax=None
branches=[]
for mask in range(16):
    vals=[1.0 if (mask>>i)&1 else -1.0 for i in range(4)]
    core, coeff=one_shared_core(vals)
    branches.append((mask,vals,core,coeff))
for ma,va,ca,A in branches:
    for mb,vb,cb,B in branches:
        # Embed a(y,u) and b(y,v) in the common remaining cube (y,u,v).
        EA=[0.0]*8; EB=[0.0]*8
        for idx,val in enumerate(A):
            EA[idx]=val                  # bits y,u
        for idx,val in enumerate(B):
            ybit=idx & 1
            vbit=(idx >> 1) & 1
            EB[ybit | (vbit<<2)] = val   # bits y,v
        F=mux_coeff(EA,EB)
        Hf=entropy(F); If=influence(F)
        Ha,Hb=entropy(A),entropy(B)
        Ia,Ib=influence(A),influence(B)
        dot=ca[0]*cb[0]+ca[1]*cb[1]
        Om=omega(ca,cb)
        Hrhs=(Ha+Hb)/2+Om
        Irhs=(Ia+Ib)/2+(1-dot)/2
        max_formula_err=max(max_formula_err,abs(Hf-Hrhs),abs(If-Irhs))
        infz=(1-dot)/2
        if infz>1e-15:
            rr=Om/infz
            if rr>max_ratio:
                max_ratio=rr; argmax=(ma,mb,ca,cb)
        if Om > 3*(1-dot)+2e-12:
            raise AssertionError(("one-shared scalar theorem failed",ma,mb,Om,3*(1-dot)))
        if Hf > 6*If+2e-12:
            raise AssertionError(("one-shared H<=6I failed",ma,mb,Hf,If))

# 2) Universal restriction toll on all ordered pairs of 3-bit Boolean restrictions.
max_toll_gap=-1e99
min_toll_slack=1e99
max_toll_ratio=0.0
for ma in range(256):
    va=[1.0 if (ma>>i)&1 else -1.0 for i in range(8)]
    A=fwht(va)
    for mb in range(256):
        vb=[1.0 if (mb>>i)&1 else -1.0 for i in range(8)]
        B=fwht(vb)
        Om=omega(A,B)
        q=(1-sum(x*y for x,y in zip(A,B)))/2
        rhs=h2(q)+(2/LN2)*q
        slack=rhs-Om
        min_toll_slack=min(min_toll_slack,slack)
        if q>1e-15:
            max_toll_ratio=max(max_toll_ratio,Om/q)
        if slack < -2e-12:
            raise AssertionError(("universal restriction toll failed",ma,mb,q,Om,rhs))

# 3) Bent + one-point-flip family: sharpness of h(q)+(2/ln2)q.
bent_rows=[]
for k in (2,4,6,8,10,12):
    va=bent_vals(k)
    vb=va[:]; vb[0]*=-1
    A=fwht(va); B=fwht(vb)
    Om=omega(A,B)
    q=(1-sum(x*y for x,y in zip(A,B)))/2
    R=Om/q
    rhs_ratio=h2(q)/q+2/LN2
    bent_rows.append((k,q,R,rhs_ratio,R-k))
    if abs(q-2**(-k))>2e-12:
        raise AssertionError(("wrong bent flip selector influence",k,q))
    if Om > h2(q)+(2/LN2)*q+2e-11:
        raise AssertionError(("bent toll bound failed",k))

print("one_shared_pairs", len(branches)**2)
print("one_shared_max_formula_error", format(max_formula_err,'.17g'))
print("one_shared_max_Omega_over_Infz", format(max_ratio,'.15f'))
print("one_shared_argmax", argmax)
print("three_bit_restriction_pairs", 256*256)
print("universal_toll_min_slack", format(min_toll_slack,'.17g'))
print("universal_toll_max_Omega_over_q", format(max_toll_ratio,'.15f'))
print("bent_flip: k q Omega/q bound/q Omega/q-k")
for row in bent_rows:
    print(row[0], format(row[1],'.12g'), format(row[2],'.15f'),
          format(row[3],'.15f'), format(row[4],'.15f'))
print("limit_constant_3_over_ln2", format(3/LN2,'.15f'))
print("PASS")
