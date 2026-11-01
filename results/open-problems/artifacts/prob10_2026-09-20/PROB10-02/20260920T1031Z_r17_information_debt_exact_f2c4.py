#!/usr/bin/env python3
from fractions import Fraction
from itertools import product

LOWER = Fraction(99083249,125000000)

def bits(n):
    return range(1<<n)

def head(x,n):
    return (x>>(n-1))&1

def sh(x,n,u):
    return ((x<<1)&((1<<n)-1))|u

def ordinary_keys(n):
    return [(a,b) for a in bits(n) for b in bits(n)]

def debt_keys(n):
    return [(a,b,s) for a in bits(n) for b in bits(n) for s in (0,1,2)] # N,A0,A1

def T(h,n):
    out={}
    for a,b in ordinary_keys(n):
        if head(a,n)==head(b,n):
            out[a,b]=Fraction(1)+sum((h[sh(a,n,u),sh(b,n,v)] for u in (0,1) for v in (0,1)),Fraction(0))/4
        else:
            A=sum((h[sh(a,n,u),b] for u in (0,1)),Fraction(0))/2
            B=sum((h[a,sh(b,n,v)] for v in (0,1)),Fraction(0))/2
            out[a,b]=max(A,B)
    return out

def F(h,n):
    out={}
    for a,b,s in debt_keys(n):
        eq=head(a,n)==head(b,n)
        if s==0:
            if eq:
                out[a,b,s]=Fraction(1)+sum((h[sh(a,n,u),sh(b,n,v),0] for u in (0,1) for v in (0,1)),Fraction(0))/4
            else:
                # ordinary no-peek actions
                A=sum((h[sh(a,n,u),b,0] for u in (0,1)),Fraction(0))/2
                B=sum((h[a,sh(b,n,v),0] for v in (0,1)),Fraction(0))/2
                # reveal only the next A bit u, then choose A or B.
                # If B is chosen, u remains exposed and unconsumed as debt A_u.
                P=Fraction(0)
                for u in (0,1):
                    consumeA=h[sh(a,n,u),b,0]
                    consumeB=sum((h[a,sh(b,n,v),1+u] for v in (0,1)),Fraction(0))/2
                    P += max(consumeA,consumeB)/2
                out[a,b,s]=max(A,B,P)
        else:
            u=s-1
            if eq:
                out[a,b,s]=Fraction(1)+sum((h[sh(a,n,u),sh(b,n,v),0] for v in (0,1)),Fraction(0))/2
            else:
                consumeA=h[sh(a,n,u),b,0]
                consumeB=sum((h[a,sh(b,n,v),s] for v in (0,1)),Fraction(0))/2
                out[a,b,s]=max(consumeA,consumeB)
    return out

def iterate(op, keys, n, steps):
    h={k:Fraction(0) for k in keys}
    lo=hi=None
    for _ in range(steps):
        hn=op(h,n)
        inc=[hn[k]-h[k] for k in keys]
        lo,hi=min(inc),max(inc)
        h=hn
    return lo,hi,h

def dec(x,d=15):
    return f"{float(x):.{d}f}"

def gamma_from_r(r):
    return 2*r/(1+r)

def lcs(x,y):
    m=len(y)
    dp=[0]*(m+1)
    for cx in x:
        nd=[0]*(m+1)
        for j,cy in enumerate(y,1):
            nd[j]=dp[j-1]+1 if cx==cy else max(dp[j],nd[j-1])
        dp=nd
    return dp[m]

def runlen(s):
    z=s[0]
    k=0
    for c in s:
        if c!=z: break
        k+=1
    return k

print("R17 PROB10-02 exact information-debt / one-sided-peek checker")
print("SECTION no_free_peek_deterministic_projection")
good=[]
for mask in range(16):
    p={(u,v):(mask>>(2*u+v))&1 for u in (0,1) for v in (0,1)}
    # Exact memoryless freshness equations for both possible unconsumed bits.
    ok=(p[0,0]==p[0,1] and p[1,0]==p[1,1]
        and (1-p[0,0])==(1-p[1,0])
        and (1-p[0,1])==(1-p[1,1]))
    if ok: good.append(mask)
print("freshness_preserving_deterministic_masks=",good)
assert good==[0,15]
print("NO_FREE_PEEK_DETERMINISTIC_PASS")

print("SECTION run_prefix_dominance_counterexample")
first=None
for n in range(2,7):
    words=[''.join(z) for z in product('01',repeat=n)]
    bad=None
    for A in words:
        for B in words:
            if A[0]==B[0]: continue
            i,j=runlen(A),runlen(B)
            if i<j:
                va=lcs(A[1:],B)
                vb=lcs(A,B[1:])
                if va<vb:
                    bad=(A,B,i,j,va,vb)
                    break
        if bad: break
    print("n=",n,"first_bad=",bad)
    if first is None and bad is not None:
        first=(n,)+bad
assert first==(6,'010011','110100',1,2,3,4)
print("RUN_PREFIX_COUNTEREXAMPLE_PASS")

print("SECTION exact_collatz_subsolutions")
STEPS=35
for n in range(1,7):
    _,_,ho=iterate(T,ordinary_keys(n),n,STEPS)
    Tho=T(ho,n)
    odiffs=[Tho[k]-ho[k] for k in ordinary_keys(n)]
    olo,ohi=min(odiffs),max(odiffs)
    _,_,h=iterate(F,debt_keys(n),n,STEPS)
    Fh=F(h,n)
    diffs=[Fh[k]-h[k] for k in debt_keys(n)]
    qlo,qhi=min(diffs),max(diffs)
    assert olo<=ohi and qlo<=qhi
    # h itself is exactly the displayed Bellman sub/supersolution.
    assert all(Fh[k]-h[k]>=qlo for k in debt_keys(n))
    assert all(Fh[k]-h[k]<=qhi for k in debt_keys(n))
    g=gamma_from_r(qlo)
    print("ell=",n,
          "ordinary=[",dec(olo),",",dec(ohi),"]",
          "debt=[",dec(qlo),",",dec(qhi),"]",
          "gamma_from_debt_lower=",dec(g),
          "beats_current_L=",g>LOWER)
    if n<=5:
        # At these widths the exact one-sided-debt lower certificate is already
        # strictly better than the ordinary upper Collatz bracket at the same width.
        assert qlo>ohi
    assert g<LOWER
print("EXACT_SUBSOLUTION_AND_NONMOVEMENT_PASS")
print("current_L=",LOWER.numerator,"/",LOWER.denominator,dec(LOWER))
print("ALL_EXACT_CHECKS_PASS")
