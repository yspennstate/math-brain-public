#!/usr/bin/env python3
import json, math, random, hashlib
from fractions import Fraction

SEED=20260920
random.seed(SEED)

def fwht(vals):
    a=[float(x) for x in vals]
    h=1
    n=len(a)
    while h<n:
        for i in range(0,n,2*h):
            for j in range(i,i+h):
                x=a[j]; y=a[j+h]
                a[j]=x+y; a[j+h]=x-y
        h*=2
    return a

def h2(t):
    if t<=0.0 or t>=1.0:
        return 0.0
    return -t*math.log2(t)-(1-t)*math.log2(1-t)

def influence(signs,n,i):
    diff=sum(1 for x in range(1<<n) if signs[x]!=signs[x^(1<<i)])
    return Fraction(diff,1<<n)

def folded(signs,n,i):
    a=influence(signs,n,i)
    return min(a,1-a)

def mult(a,b): return [x*y for x,y in zip(a,b)]

def selector(g,c):
    # new selector bit is top bit; z=0 branch g, z=1 branch constant c
    N=len(g)
    return list(g)+[c]*N

def B_selector_direct(g,c):
    n=(len(g)).bit_length()-1
    F=selector(g,c)
    hats=fwht(F)
    scale=1/(1<<(n+1))
    p=[(x*scale)**2 for x in hats]
    bit=n
    B=0.0
    for T in range(1<<n):
        x=p[T]; y=p[T|(1<<bit)]; m=x+y
        if m>0:
            B += m*h2(y/m)
    return B

def selector_formula(delta):
    j=min(delta,1-delta)
    m=(1-j)**2+j*j
    return m*h2(j*j/m)+2*j*(1-j) if m>0 else 0.0

# 1) Exact one-point weighted-degree obstruction formula.
one_point=[]
for n in range(2,17):
    I=Fraction(n*(2),1<<n)  # n*2^(1-n)
    D=Fraction(n*(n-1),2)*Fraction(2,1<<n)
    ratio=D/I
    assert ratio==Fraction(n-1,2)
    one_point.append({"n":n,"I":str(I),"D_deg":str(D),"ratio":str(ratio)})

# 2) Folded-influence triangle, exhaustive all pairs through n=3.
triangle_checks=0
triangle_failures=[]
for n in range(1,4):
    N=1<<n
    funcs=[]
    for truth in range(1<<N):
        funcs.append([1 if ((truth>>x)&1)==0 else -1 for x in range(N)])
    for f in funcs:
        for g in funcs:
            fg=mult(f,g)
            for i in range(n):
                jf=folded(f,n,i); jg=folded(g,n,i); jfg=folded(fg,n,i)
                triangle_checks+=1
                if not (abs(jf-jg) <= jfg <= jf+jg):
                    triangle_failures.append((n,i,str(jf),str(jg),str(jfg)))
                    raise AssertionError(triangle_failures[-1])

# additional random n=4 pairs
n=4; N=1<<n
for _ in range(5000):
    f=[random.choice([-1,1]) for _ in range(N)]
    g=[random.choice([-1,1]) for _ in range(N)]
    fg=mult(f,g)
    for i in range(n):
        jf=folded(f,n,i); jg=folded(g,n,i); jfg=folded(fg,n,i)
        triangle_checks+=1
        assert abs(jf-jg) <= jfg <= jf+jg

# 3) Selector formula and B<=4j: exhaustive g through n=3, sampled n=4.
selector_checks=0
max_ratio=0.0
max_case=None
for n in range(0,4):
    N=1<<n
    for truth in range(1<<N):
        g=[1 if ((truth>>x)&1)==0 else -1 for x in range(N)]
        for c in (-1,1):
            delta=sum(1 for x in range(N) if g[x]!=c)/N
            B=B_selector_direct(g,c)
            formula=selector_formula(delta)
            if abs(B-formula)>2e-11:
                raise AssertionError((n,truth,c,B,formula))
            j=min(delta,1-delta)
            if B>4*j+2e-11:
                raise AssertionError((n,truth,c,B,j))
            if j>0 and B/j>max_ratio:
                max_ratio=B/j; max_case=(n,truth,c,delta,B)
            selector_checks+=1

n=4; N=1<<n
for _ in range(2000):
    g=[random.choice([-1,1]) for _ in range(N)]
    c=random.choice([-1,1])
    delta=sum(1 for x in range(N) if g[x]!=c)/N
    B=B_selector_direct(g,c)
    formula=selector_formula(delta)
    assert abs(B-formula)<2e-11
    j=min(delta,1-delta)
    assert B<=4*j+2e-11
    selector_checks+=1

# 4) Low-degree phase corollary sanity on exhaustive n=3 pairs, using actual phase folded costs.
# This is already implied by triangle, but record the lower-bound consequence where derivative is nonconstant.
# Compute ANF and derivative degree for phase q.
def mobius(bits,n):
    a=list(bits)
    for i in range(n):
        for mask in range(1<<n):
            if mask&(1<<i):
                a[mask]^=a[mask^(1<<i)]
    return a

def der_degree(bits,n,i):
    # derivative restricted to x_i=0, remapped to n-1 variables
    vals=[]
    for y in range(1<<(n-1)):
        lo=y&((1<<i)-1); hi=y>>i
        x=lo|(hi<<(i+1))
        vals.append(bits[x]^bits[x^(1<<i)])
    if all(v==vals[0] for v in vals):
        return None
    a=mobius(vals,n-1)
    return max(mask.bit_count() for mask,v in enumerate(a) if v)

rm_transfer_checks=0
n=3; N=1<<n
funcs=[]
bitfuncs=[]
for truth in range(1<<N):
    bits=[(truth>>x)&1 for x in range(N)]
    signs=[1-2*b for b in bits]
    funcs.append(signs); bitfuncs.append(bits)
for qi,q in enumerate(funcs):
    qbits=bitfuncs[qi]
    for i in range(n):
        r=der_degree(qbits,n,i)
        if r is None: continue
        jq=folded(q,n,i)
        assert jq >= Fraction(1,1<<r)
        # sample all h but only this coordinate
        for h in funcs:
            F=mult(q,h)
            jF=folded(F,n,i); jh=folded(h,n,i)
            assert jF >= Fraction(1,1<<r)-jh
            rm_transfer_checks+=1

out={
  "status":"PASS",
  "seed":SEED,
  "one_point_weighted_degree_obstruction":one_point,
  "folded_triangle_checks":triangle_checks,
  "folded_triangle_failures":len(triangle_failures),
  "selector_checks":selector_checks,
  "selector_max_observed_B_over_j":max_ratio,
  "selector_max_case":max_case,
  "reed_muller_transfer_checks_n3":rm_transfer_checks,
  "scope":"Finite self-checks only. Universal claims rely on written proofs; no independent audit or Lean verification."
}
raw=json.dumps(out,indent=2,sort_keys=True)
print(raw)
print("SCRIPT_SHA256",hashlib.sha256(open(__file__,'rb').read()).hexdigest())
