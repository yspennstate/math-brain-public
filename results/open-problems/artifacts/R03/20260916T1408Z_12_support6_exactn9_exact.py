#!/usr/bin/env python3
from itertools import product, combinations
from fractions import Fraction
from math import gcd, comb
from functools import reduce

def det_bareiss(A):
    A=[list(map(int,row)) for row in A]
    n=len(A)
    if n==0: return 1
    sign=1
    denom=1
    for k in range(n-1):
        if A[k][k]==0:
            sw=None
            for i in range(k+1,n):
                if A[i][k]!=0:
                    sw=i;break
            if sw is None: return 0
            A[k],A[sw]=A[sw],A[k]
            sign*=-1
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j]=(A[i][j]*pivot-A[i][k]*A[k][j])//denom
        denom=pivot
        for i in range(k+1,n):
            A[i][k]=0
    return sign*A[n-1][n-1]

def cofactor_normal(selected):
    # selected: five length-6 projective sign columns, first all-one
    M=[[selected[j][i] for j in range(5)] for i in range(6)] # 6x5
    a=[]
    for i in range(6):
        sub=[M[r] for r in range(6) if r!=i]
        a.append(((-1)**i)*det_bareiss(sub))
    if all(v==0 for v in a): return None
    # exact kernel check
    assert all(sum(a[i]*M[i][j] for i in range(6))==0 for j in range(5))
    g=reduce(gcd,(abs(v) for v in a if v))
    a=[v//g for v in a]
    first=next(v for v in a if v)
    if first<0: a=[-v for v in a]
    return tuple(a)

def atom_count(a):
    return sum(sum(x*e for x,e in zip(a,eps))==0
               for eps in product((1,-1),repeat=len(a)))

# Projective sign columns in R^6 represented by first coordinate +1.
cols=[(1,)+tail for tail in product((1,-1),repeat=5)]
one=(1,1,1,1,1,1)
others=[v for v in cols if v!=one]

rank5=0
minimal=0
types={}
atoms={}
for four in combinations(others,4):
    a=cofactor_normal((one,)+four)
    if a is None: continue
    rank5+=1
    if 0 in a: continue
    minimal+=1
    typ=tuple(sorted(map(abs,a),reverse=True))
    ac=atom_count(a)
    types[(typ,ac)]=types.get((typ,ac),0)+1
    atoms[ac]=atoms.get(ac,0)+1

expected={
    ((2,2,1,1,1,1),14):900,
    ((1,1,1,1,1,1),20):810,
    ((3,2,2,1,1,1),10):300,
    ((3,1,1,1,1,1),10):30,
}
assert rank5==27990
assert minimal==2040
assert types==expected
assert atoms=={14:900,20:810,10:330}

# All original-row-sign/permutation normal directions: safe upper counts.
direction_counts={
    (1,1,1,1,1,1):32,
    (2,2,1,1,1,1):comb(6,2)*32,
    (3,1,1,1,1,1):6*32,
    (3,2,2,1,1,1):6*comb(5,2)*32,
}
assert direction_counts[(2,2,1,1,1,1)]==480
assert direction_counts[(3,1,1,1,1,1)]==192
assert direction_counts[(3,2,2,1,1,1)]==1920
assert sum(direction_counts.values())==2624

# Published exact counts m_d of nonsingular dxd 0/1 matrices, d<=8:
# M. Zivkovic, LAA 414 (2006), Table 3 / OEIS A055165.
m01=[1,1,6,174,22560,12514320,28836612000,
     270345669985440,10160459763342013440]
# Sign nonsingular count relation: N_pm(n)=2^(2n-1)m01[n-1].
print("SUPPORT-6 EXACT CLASSIFICATION")
print("projective frames total", comb(31,4))
print("rank-5 frames",rank5)
print("minimal-support-6 frames",minimal)
for key in sorted(types):
    print("type",key[0],"zero_columns",key[1],"frame_count",types[key])
print("safe original normal-direction counts",direction_counts)
print("fixed-row-set union bound:")
print("  32*(5/16)^n + 480*(7/32)^n + 2112*(5/32)^n")
print("target-scale coefficient after choosing six rows:")
print("  C(n,6)*[32*(5/8)^n + 480*(7/16)^n + 2112*(5/16)^n]")

print("\nEXACT IID SIGN SINGULARITY VALUES FROM PUBLISHED 0/1 COUNTS")
for n in range(1,10):
    nons=2**(2*n-1)*m01[n-1]
    total=2**(n*n)
    assert nons <= total
    psing=Fraction(total-nons,total)
    b=2**n*psing-2*n*(n-1)
    print(n, "Psing", f"{psing.numerator}/{psing.denominator}" if psing.denominator!=1 else str(psing.numerator),
          "b", f"{b.numerator}/{b.denominator}" if b.denominator!=1 else str(b),
          "b_float", format(float(b),".15g"))

# Check n<=6 values retained from previous R03 run.
retained_b=[
    Fraction(0),Fraction(-2),Fraction(-7),Fraction(-215,16),
    Fraction(-1217,64),Fraction(-651073,32768)
]
for n,b0 in enumerate(retained_b,1):
    nons=2**(2*n-1)*m01[n-1]
    ps=Fraction(2**(n*n)-nons,2**(n*n))
    b=2**n*ps-2*n*(n-1)
    assert b==b0

print("\nSELF-CHECK PASS")
