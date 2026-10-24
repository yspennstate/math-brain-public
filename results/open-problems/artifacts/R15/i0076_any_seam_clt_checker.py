#!/usr/bin/env python3
from fractions import Fraction
from itertools import product

print("I0076 R15 arbitrary-seam elimination self-check")

# Represent Z_j (with Z_0=0) as an exact integer linear form in independent
# formal increment labels. The source uses Z_{k+1}-Z_k=V_k.
def add_forms(a,b,scale=1):
    out=dict(a)
    for k,v in b.items():
        out[k]=out.get(k,0)+scale*v
        if out[k]==0:
            del out[k]
    return out

def z_form(j, Vmap):
    out={}
    if j>0:
        for k in range(0,j):
            lab=Vmap.get(k,("v",k))
            out[lab]=out.get(lab,0)+1
    elif j<0:
        for k in range(j,0):
            lab=Vmap.get(k,("v",k))
            out[lab]=out.get(lab,0)-1
    return {k:v for k,v in out.items() if v}

count=0
bound_count=0
for c in range(2,9):
    for a in range(-c+1,0):
        for b in range(1,c):
            for d in range(1,10):
                # Source copy: V_k = V_{k-a+d+b+1}, k=a-d,...,a-1.
                Vmap={}
                for k in range(a-d,a):
                    Vmap[k]=("v", k-a+d+b+1)
                L=a-d
                R=b+d
                lhs=add_forms(z_form(L,Vmap), z_form(R,Vmap))
                rhs=add_forms(z_form(a,Vmap), z_form(b+1,Vmap))
                # Exact endpoint identity has one missing last right increment.
                lab=Vmap.get(b+d,("v",b+d))
                rhs[lab]=rhs.get(lab,0)-1
                if rhs[lab]==0:
                    del rhs[lab]
                assert lhs==rhs, (a,b,d,lhs,rhs)
                count += 1

                # Under |a| vee b < c the RHS has l1 coefficient mass <=2c,
                # hence |Z_{a-d}+Z_{b+d}|<=2c for every sign realization.
                l1=sum(abs(v) for v in rhs.values())
                assert l1 <= 2*c, (c,a,b,d,l1,rhs)
                bound_count += 1

print("copy endpoint-sum identity: PASS", count)
print("2c deterministic bound: PASS", bound_count)

# Exhaustive sign-value verification on representative finite cases.
exhaustive=0
for a,b,d in [(-1,1,1),(-2,1,2),(-2,2,2),(-3,2,3)]:
    labels=set()
    Vmap={}
    for k in range(a-d,a):
        Vmap[k]=("v", k-a+d+b+1)
    for j in [a-d, b+d, a, b+1]:
        labels.update(z_form(j,Vmap))
    labels.add(("v",b+d))
    labels=sorted(labels, key=repr)
    for signs in product((-1,1), repeat=len(labels)):
        val=dict(zip(labels,signs))
        def evalf(f):
            return sum(co*val[lab] for lab,co in f.items())
        L=a-d
        R=b+d
        lhs=evalf(add_forms(z_form(L,Vmap),z_form(R,Vmap)))
        rhs=evalf(add_forms(z_form(a,Vmap),z_form(b+1,Vmap))) - val[("v",b+d)]
        assert lhs==rhs
        exhaustive += 1
print("exhaustive sign realizations: PASS", exhaustive)

# Independent N(0,1) limits have sum variance exactly 2.
var_g1=Fraction(1)
var_g2=Fraction(1)
cov=Fraction(0)
var_sum=var_g1+var_g2+2*cov
assert var_sum==2
print("independent Gaussian sum variance: PASS", var_sum)

# Source scale (6.7): 4c/sqrt(d) <= eps/2 implies
# 2c/sqrt(d) <= eps/4. Check the squared exact implication.
scale_checks=0
for c in range(1,20):
    for d in range(1,200):
        eps2=Fraction(64*c*c,d)
        assert Fraction(16*c*c,d) <= eps2/4
        assert Fraction(4*c*c,d) <= eps2/16
        scale_checks += 1
print("source-scale squared implication: PASS", scale_checks)

print("PASS")
