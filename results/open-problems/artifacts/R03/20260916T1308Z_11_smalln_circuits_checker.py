#!/usr/bin/env python3
from itertools import combinations, product
from fractions import Fraction
from math import comb, factorial, gcd
from functools import reduce

P=257
EXPECTED_N={1:1,2:1,3:4,4:58,5:3008,6:556192}
EXPECTED_S={1:0,2:8,3:320,4:43264,5:22003712,6:43090149376}


def det_mod(rows,p=P):
    n=len(rows)
    a=[list(map(lambda x:x%p,r)) for r in rows]
    det=1
    for j in range(n):
        piv=None
        for i in range(j,n):
            if a[i][j]%p:
                piv=i;break
        if piv is None:return 0
        if piv!=j:
            a[j],a[piv]=a[piv],a[j]
            det=-det
        pv=a[j][j]%p
        det=det*pv%p
        inv=pow(pv,p-2,p)
        for i in range(j+1,n):
            if a[i][j]%p:
                f=a[i][j]*inv%p
                # only update right entries
                for k in range(j+1,n):
                    a[i][k]=(a[i][k]-f*a[j][k])%p
    return det%p


def det_int(a):
    # Bareiss exact determinant
    n=len(a)
    if n==0:return 1
    M=[list(map(int,r)) for r in a]
    sign=1
    prev=1
    for k in range(n-1):
        piv=k
        while piv<n and M[piv][k]==0:piv+=1
        if piv==n:return 0
        if piv!=k:
            M[k],M[piv]=M[piv],M[k];sign*=-1
        pivot=M[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                M[i][j]=(M[i][j]*pivot-M[i][k]*M[k][j])//prev
        prev=pivot
        for i in range(k+1,n):M[i][k]=0
        if prev==0:return 0
    return sign*M[n-1][n-1]


def cube_simplex_count(n):
    if n==1:return 1,1
    d=n-1
    vecs=[tuple((mask>>j)&1 for j in range(d)) for mask in range(1,1<<d)]
    M=0
    for C in combinations(vecs,d):
        if det_mod(C)!=0:
            M+=1
    num=(1<<d)*M
    assert num%n==0
    return num//n,M

print('EXACT SMALL SIGN MATRICES')
small=[]
for n in range(1,7):
    N,M=cube_simplex_count(n)
    assert N==EXPECTED_N[n],(n,N)
    I=N*factorial(n)*(1<<n)
    total=1<<(n*n)
    S=total-I
    assert S==EXPECTED_S[n],(n,S)
    Psing=Fraction(S,total)
    coeff=(1<<n)*Psing
    b=coeff-2*n*(n-1)
    small.append((n,N,I,S,Psing,coeff,b))
    print(n,'N=',N,'I=',I,'S=',S,'P=',f'{Psing.numerator}/{Psing.denominator}',
          '2^nP=',f'{coeff.numerator}/{coeff.denominator}',
          'b=',f'{b.numerator}/{b.denominator}')

# matching lower bound from pair events, with explicit overlap correction
print('\nPAIR BONFERRONI LOWER BOUND')
for n in range(2,11):
    m=n*(n-1)
    lead=Fraction(2*m,1<<n)
    same=Fraction(2*(comb(m,2)-comb(n,2)),1<<(2*n))
    cross=Fraction(2*m*m,1<<(2*n))
    lower=lead-same-cross
    # exact singular probability if n<=6 should dominate
    if n<=6:
        p=small[n-1][4]
        assert p>=lower
    bracket_corr=Fraction(2*(comb(m,2)-comb(n,2))+2*m*m,1<<n)
    print(n,'lower=',f'{lower.numerator}/{lower.denominator}',
          'bracket_correction=',f'{bracket_corr.numerator}/{bracket_corr.denominator}')

# circuit normal classification using independent observed sign columns

def sign_vectors(s):
    return [tuple(v) for v in product((-1,1),repeat=s)]

def null_cofactor(cols,s):
    # cols: s-1 row vectors in R^s. Normal coordinates cofactors.
    a=[list(r) for r in cols]
    n=[]
    for j in range(s):
        minor=[row[:j]+row[j+1:] for row in a]
        n.append(((-1)**j)*det_int(minor))
    if all(x==0 for x in n):return None
    g=reduce(gcd,(abs(x) for x in n if x))
    n=[x//g for x in n]
    # deterministic sign modulo global sign
    for x in n:
        if x:
            if x<0:n=[-y for y in n]
            break
    return tuple(n)

print('\nMINIMAL CIRCUIT CLASSIFICATION')
for s,expected_abs,expected_atoms,expected_normals in [
    (4,(1,1,1,1),6,8),
    (5,(1,1,1,1,2),8,80),
]:
    vecs=sign_vectors(s)
    normals=set()
    tested=0
    fullrank=0
    minimal_normals=set()
    for cols in combinations(vecs,s-1):
        tested+=1
        a=null_cofactor(cols,s)
        if a is None:continue
        fullrank+=1
        if all(x!=0 for x in a):
            minimal_normals.add(a)
            assert tuple(sorted(abs(x) for x in a))==expected_abs,(s,a)
    # Generate all normal directions of expected type directly and verify atom count.
    if s==4:
        for signs in product((-1,1),repeat=4):
            a=tuple(signs)
            if a[0]<0:a=tuple(-x for x in a)
            normals.add(a)
    else:
        for heavy in range(5):
            for signs in product((-1,1),repeat=5):
                vals=[signs[i]*(2 if i==heavy else 1) for i in range(5)]
                if vals[0]<0:vals=[-x for x in vals]
                normals.add(tuple(vals))
    assert len(normals)==expected_normals,(s,len(normals))
    assert minimal_normals==normals,(s,len(minimal_normals),len(normals),list(normals-minimal_normals)[:3],list(minimal_normals-normals)[:3])
    atom_counts=set()
    for a in normals:
        atoms=sum(1 for v in vecs if sum(x*y for x,y in zip(a,v))==0)
        atom_counts.add(atoms)
    assert atom_counts=={expected_atoms},(s,atom_counts)
    print('support',s,'combos=',tested,'fullrank=',fullrank,'normal_directions=',len(normals),
          'abs_type=',expected_abs,'allowed_column_atoms=',expected_atoms,
          'fixed-relation probability=',f'({expected_atoms}/{1<<s})^n')

# explicit upper coefficients for supports 4,5
print('\nUNION UPPER BOUNDS FOR MINIMAL CIRCUITS')
for n in range(5,31,5):
    b4=8*comb(n,4)*Fraction(3,4)**n  # bracket coefficient relative 2^-n
    b5=80*comb(n,5)*Fraction(1,2)**n
    print(n,'support4 bracket <=',float(b4),'support5 bracket <=',float(b5))

print('\nPASS')
