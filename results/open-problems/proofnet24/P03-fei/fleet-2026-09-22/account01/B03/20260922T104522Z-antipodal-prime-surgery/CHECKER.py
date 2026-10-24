#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations, product
import json, math

CSTAR = 6.5584452830718245

def fbit(mask,n):
    z1=(mask>>0)&1
    return z1 ^ (1 if mask==0 or mask==(1<<n)-1 else 0)

def fpm(bits):
    x1=bits[0]
    if all(x==1 for x in bits) or all(x==-1 for x in bits):
        return -x1
    return x1

def anf(vals,n):
    a=list(vals)
    for i in range(n):
        for s in range(1<<n):
            if s&(1<<i): a[s]^=a[s^(1<<i)]
    return a

def gf2_rank(rows,ncols):
    rows=list(rows); r=0
    for bit in range(ncols-1,-1,-1):
        piv=next((i for i in range(r,len(rows)) if (rows[i]>>bit)&1),None)
        if piv is None: continue
        rows[r],rows[piv]=rows[piv],rows[r]
        for i in range(len(rows)):
            if i!=r and ((rows[i]>>bit)&1): rows[i]^=rows[r]
        r+=1
    return r

def flatten_rank(coeff,n,A):
    A=tuple(A); B=tuple(i for i in range(n) if i not in A); rows=[]
    for ua in range(1<<len(A)):
        row=0
        for vb in range(1<<len(B)):
            s=0
            for j,i in enumerate(A):
                if (ua>>j)&1: s|=1<<i
            for j,i in enumerate(B):
                if (vb>>j)&1: s|=1<<i
            if coeff[s]: row|=1<<vb
        rows.append(row)
    return gf2_rank(rows,1<<len(B))

def row_patterns(n,A):
    A=tuple(A); B=tuple(i for i in range(n) if i not in A); assert len(B)==1
    j=B[0]; pats=set()
    for bitsA in product([0,1], repeat=len(A)):
        base=sum((bit<<i) for bit,i in zip(bitsA,A))
        pats.add((fbit(base,n),fbit(base|(1<<j),n)))
    return pats

def pbiased_spectral_masses(n,ps):
    probs={}
    for Smask in range(1<<n):
        S=[i for i in range(n) if (Smask>>i)&1]
        T=[i for i in range(n) if not ((Smask>>i)&1)]
        avg=Fraction(0)
        for tm in range(1<<len(T)):
            fixed={}; wt=Fraction(1)
            for k,i in enumerate(T):
                neg=(tm>>k)&1; fixed[i]=-1 if neg else 1
                wt*=ps[i] if neg else (1-ps[i])
            delta=0
            for sm in range(1<<len(S)):
                bits=[None]*n; parity=0
                for i in T: bits[i]=fixed[i]
                for k,i in enumerate(S):
                    neg=(sm>>k)&1; bits[i]=-1 if neg else 1; parity^=neg
                delta += (-1 if parity else 1)*fpm(bits)
            avg += wt*delta
        factor=Fraction(1)
        for i in S: factor*=ps[i]*(1-ps[i])
        probs[Smask]=factor*avg*avg
    assert sum(probs.values(),Fraction(0))==1
    return probs

def exact_onecore_expected(n,t,Smask):
    a=Fraction(4,1<<n); c=1-2*t; V=4*t*(1-t)
    if Smask==0: return c*c*(1-a)*(1-a)
    if Smask==1: return V*(1-a)*(1-a)
    has1=bool(Smask&1); k=(Smask>>1).bit_count()
    if not has1: return a*a if k%2==1 else a*a*c*c
    return a*a*V if k%2==0 else Fraction(0)

prime_checks=0
for n in range(3,9):
    coeff=anf([fbit(x,n) for x in range(1<<n)],n)
    for r in range(2,n):
        for A in combinations(range(n),r):
            B=[i for i in range(n) if i not in A]
            if len(B)>=2: assert flatten_rank(coeff,n,A)>=3
            else: assert len(row_patterns(n,A))>=3
            prime_checks+=1

spectral_checks=0
for n in range(3,8):
    for t in [Fraction(1,3),Fraction(2,5),Fraction(1,2),Fraction(5,9)]:
        ps=[t]+[Fraction(1,2)]*(n-1); sp=pbiased_spectral_masses(n,ps)
        for S,w in sp.items():
            assert w==exact_onecore_expected(n,t,S); spectral_checks+=1
        a=Fraction(4,1<<n); V=4*t*(1-t)
        infl=[sum(w for S,w in sp.items() if (S>>i)&1) for i in range(n)]
        assert infl[0]/V == 1-a
        for i in range(1,n): assert infl[i] == a

balanced=[]
for n in range(3,31):
    a=2**(2-n)
    D=a*(n-2)*(CSTAR-4+2*a)+2*(1-a)**2*math.log2(1-a)
    M=a*(n-2)/4
    assert D>0; balanced.append((n,D,-D/M))

print(json.dumps({
  "status":"PASS",
  "family":"antipodal two-point surgery of dictator",
  "prime_nontrivial_blocks_checked":prime_checks,
  "prime_n_range":[3,8],
  "exact_one_core_spectral_entries_checked":spectral_checks,
  "one_core_n_range":[3,7],
  "one_core_biases":["1/3","2/5","1/2","5/9"],
  "candidate_center_used_for_balanced_numeric_regression":CSTAR,
  "balanced_positive_checked_n_range":[3,30],
  "balanced_cG_n3":balanced[0][2],
  "balanced_cG_n30":balanced[-1][2],
  "theoretical_limit_cG":-4*(CSTAR-4),
  "full_FEI_status":"OPEN; theorem is a family-specific margin/primality result"
},indent=2))
