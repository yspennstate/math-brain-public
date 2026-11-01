"""
PROB20-05 exact checker for the four- and five-consecutive-bin block theorems.

Mathematical dependencies:
- archived m<=3 block theorem;
- archived adjacent/disjoint adjacent surgeries;
- universal endpoint bound W2^2 <= 1/6 - J/2;
- local equal-slab block identity Delta/h^2 = C_m G - D H,
  C_m=m(m-1)/2;
- cellwise diagonal-residual certificate:
      15 W >= 7 n^2(n^2-1).

The script uses SciPy Hungarian matching only to FIND a balanced assignment.
Every matching certificate is then revalidated by exact integer arithmetic.
"""

import itertools
from fractions import Fraction
import numpy as np
import sympy as sp
from scipy.optimize import linear_sum_assignment

x = sp.symbols("x", real=True)

def D_sigma(perm):
    m = len(perm)
    d = [j-perm[j] for j in range(m)]
    mu = [Fraction(2*l+1-m,m) for l in range(m)]
    return sum(Fraction(v)*u for v,u in zip(sorted(d),mu))

def consecutive_components(perm):
    n=len(perm)
    comps=[]
    start=0
    for k in range(1,n+1):
        if set(perm[start:k]) == set(range(start,k)):
            comps.append((start,k))
            start=k
    assert start==n
    return comps

def psi12(k):
    k=abs(k)
    if k==0: return 8
    if k==1: return 13
    return 12*k

def J_fraction(perm):
    n=len(perm)
    S=0
    for i in range(n):
        for j in range(n):
            d=i-j
            e=perm[i]-perm[j]
            S += abs(d-e)*psi12(d+e)
    return Fraction(S,12*n**4)

def global_perm(n,k,local):
    p=list(range(n))
    for j,v in enumerate(local):
        p[k+j]=k+v
    return tuple(p)

def HG_interval(a,b):
    a=sp.Rational(a) if not isinstance(a,sp.Basic) else a
    b=sp.Rational(b) if not isinstance(b,sp.Basic) else b
    L=sp.simplify(b-a)
    mid=sp.simplify((a+b)/2)
    rt2=sp.sqrt(2)

    def Hleft(t):
        return rt2*sp.Rational(2,3)*t**sp.Rational(3,2)
    def Hright(t):
        return -rt2*sp.Rational(2,3)*(1-t)**sp.Rational(3,2)

    def Ileft(t):
        return (-t**2/sp.Integer(2) + mid*t
                + rt2*(sp.Rational(2,5)*t**sp.Rational(5,2)
                       - sp.Rational(2,3)*mid*t**sp.Rational(3,2)))
    def Iright(t):
        return (t**2/sp.Integer(2) - mid*t
                - rt2*(sp.Rational(2,3)*(mid-1)*(1-t)**sp.Rational(3,2)
                       + sp.Rational(2,5)*(1-t)**sp.Rational(5,2)))

    Hnum=sp.S(0)
    Inum=sp.S(0)
    half=sp.Rational(1,2)
    if bool(a < half):
        x2=b if bool(b <= half) else half
        Hnum += Hleft(x2)-Hleft(a)
        Inum += Ileft(x2)-Ileft(a)
    if bool(b > half):
        x1=a if bool(a >= half) else half
        Hnum += Hright(b)-Hright(x1)
        Inum += Iright(b)-Iright(x1)

    H=sp.simplify(Hnum/L)
    G=sp.simplify(4*Inum/L**2)
    return H,G

def matching_certificate(perm):
    n=len(perm)
    a=np.array([2*i+1-n for i in range(n)],dtype=np.int64)
    cells=[(r,s) for r in range(n) for s in range(n)]
    labels=[i for i in range(n) for _ in range(n)]
    M=np.empty((n*n,n*n),dtype=np.int64)
    for rr,(r,s) in enumerate(cells):
        for cc,i in enumerate(labels):
            M[rr,cc]=a[r]*a[i]+a[s]*a[perm[i]]
    rows,cols=linear_sum_assignment(-M)
    assert list(rows)==list(range(n*n))
    counts=[0]*n
    W=0
    for rr,cc in zip(rows,cols):
        i=labels[cc]
        counts[i]+=1
        r,s=cells[rr]
        # exact recomputation, independent of M lookup
        W += int(a[r])*int(a[i]) + int(a[s])*int(a[perm[i]])
    assert counts==[n]*n
    margin=15*W-7*n*n*(n*n-1)
    return W,margin

# ----------------------------------------------------------------------
# FOUR-BIN THEOREM
# ----------------------------------------------------------------------
S4=list(itertools.permutations(range(4)))
spec4={}
for p in S4:
    spec4.setdefault(D_sigma(p),[]).append(p)

expected4={
    Fraction(0):1, Fraction(3,2):3, Fraction(2):1, Fraction(5,2):4,
    Fraction(3):4, Fraction(7,2):2, Fraction(4):5,
    Fraction(9,2):3, Fraction(5):1
}
assert {D:len(v) for D,v in spec4.items()}==expected4

# D=5/2 cases are supported on a consecutive 3-bin component.
for p in spec4[Fraction(5,2)]:
    assert max(b-a for a,b in consecutive_components(p)) <= 3

# n=4: D in [3,4] endpoint-certified; D>=9/2 block-certified by 7/10 ratio.
n4_endpoint=[]
for D,ps in spec4.items():
    if Fraction(3)<=D<=Fraction(4):
        for p in ps:
            J=J_fraction(p)
            assert J>=Fraction(2,15)
            n4_endpoint.append((p,D,J))
assert Fraction(9,2) > Fraction(6)*Fraction(7,10)

# n=5,...,11: exact H-2G>0 for every possible 4-bin position.
four_min={}
for n in range(5,12):
    vals=[]
    for k in range(n-3):
        H,G=HG_interval(sp.Rational(k,n),sp.Rational(k+4,n))
        delta=sp.simplify(H-2*G)
        assert delta.is_positive is True
        vals.append((k,delta))
    four_min[n]=min(vals,key=lambda z:float(sp.N(z[1],30)))

# n>=12 is analytic: block mass L=4/n<=1/3.
# one-sided intervals: G/H<=2/5; crossing intervals:
# G/H<=L/[3(1-2L)]<=1/3. Hence D>=3 is more than enough.

# ----------------------------------------------------------------------
# FIVE-BIN THEOREM
# ----------------------------------------------------------------------
S5=list(itertools.permutations(range(5)))

# Every nonidentity local permutation with D<4 decomposes into
# consecutive components of size at most 4.
low5=[]
for p in S5:
    if p==tuple(range(5)):
        continue
    D=D_sigma(p)
    if D<Fraction(4):
        comps=consecutive_components(p)
        assert max(b-a for a,b in comps)<=4
        low5.append((p,D,comps))
assert len(low5)==24

# n=10,...,14: exact G/H<=2/5 for every 5-bin rank position.
five_ratio_min={}
for n in range(10,15):
    vals=[]
    for k in range(n-4):
        H,G=HG_interval(sp.Rational(k,n),sp.Rational(k+5,n))
        delta=sp.simplify(2*H-5*G)
        assert delta.is_nonnegative is True
        vals.append((k,delta))
    five_ratio_min[n]=min(vals,key=lambda z:float(sp.N(z[1],30)))

# n>=15 is analytic: L=5/n<=1/3, so G/H<=2/5.
# Since C_5=10, D>=4 suffices exactly.

# n=5,...,9: check every genuinely 5-bin (indecomposable) local permutation.
# Priority: block criterion, then endpoint criterion, then exact integer matching.
exceptional_matching=[]
summary={n:{"block":0,"endpoint":0,"matching":0} for n in range(5,10)}
for n in range(5,10):
    for k in range(n-4):
        H,G=HG_interval(sp.Rational(k,n),sp.Rational(k+5,n))
        for local in S5:
            if local==tuple(range(5)):
                continue
            if max(b-a for a,b in consecutive_components(local))<=4:
                continue
            D=D_sigma(local)
            assert D>=Fraction(4)
            diff=sp.simplify(sp.Rational(D.numerator,D.denominator)*H-10*G)
            if diff.is_nonnegative is True:
                summary[n]["block"]+=1
                continue
            gp=global_perm(n,k,local)
            J=J_fraction(gp)
            if J>=Fraction(2,15):
                summary[n]["endpoint"]+=1
                continue
            W,margin=matching_certificate(gp)
            assert margin>=0
            summary[n]["matching"]+=1
            exceptional_matching.append((n,k,local,D,J,W,margin))

# The only matching-residual local types are the two cyclic 5-shifts.
cyc1=(1,2,3,4,0)
cyc2=(4,0,1,2,3)
assert all(item[2] in (cyc1,cyc2) for item in exceptional_matching)
assert len(exceptional_matching)==14

print("EXACT FOUR/FIVE-BIN CHECKS PASSED")
print("\nS4 displacement spectrum:")
for D in sorted(spec4):
    print(" D =",D,"count =",len(spec4[D]))

print("\nFour-bin exact minima H-2G, n=5..11:")
for n in range(5,12):
    k,d=four_min[n]
    print(" n =",n,"k =",k,"min =",sp.factor(d),"≈",sp.N(d,12))

print("\nFive-bin low-D decomposable cases:",len(low5))
print("Five-bin exact minima 2H-5G, n=10..14:")
for n in range(10,15):
    k,d=five_ratio_min[n]
    print(" n =",n,"k =",k,"min =",sp.factor(d),"≈",sp.N(d,12))

print("\nFive-bin n=5..9 indecomposable certification summary:")
for n in range(5,10):
    print(" n =",n,summary[n])

print("\nExceptional matching certificates:",len(exceptional_matching))
for item in exceptional_matching:
    n,k,local,D,J,W,margin=item
    print(" n=",n,"k=",k,"local=",local,"D=",D,"J=",J,
          "W=",W,"integer margin=",margin)
