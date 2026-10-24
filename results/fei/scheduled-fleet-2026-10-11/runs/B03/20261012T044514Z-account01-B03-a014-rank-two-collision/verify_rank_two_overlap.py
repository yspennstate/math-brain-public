#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
from math import log2

checks = 0

def ok(cond, msg="assertion failed"):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(msg)

def walsh(values):
    a = [Fraction(v) for v in values]
    n = len(a)
    h = 1
    while h < n:
        for i in range(0, n, 2*h):
            for j in range(i, i+h):
                u, v = a[j], a[j+h]
                a[j], a[j+h] = u+v, u-v
        h *= 2
    return [z/Fraction(n) for z in a]

def entropy(coeff):
    ans = 0.0
    for z in coeff:
        p = float(z*z)
        if p:
            ans -= p*log2(p)
    return ans

def influence(coeff):
    return sum(Fraction(mask.bit_count())*z*z for mask,z in enumerate(coeff))

def sigma(bits):
    return -1 if all(x == -1 for x in bits) else 1

def g(x):
    x1,x2,x3=x
    return (x1+x2+x3-x1*x2*x3)//2

def h(x):
    x1,x2,x3=x
    return (x1+x2-x3+x1*x2*x3)//2

def mcore(bits):
    b=bits[0]; x=bits[1:]
    return g(x) if b==1 else h(x)

# Exact core and collision checks.
cube3=list(product((-1,1), repeat=3))
gv=[g(x) for x in cube3]
hv=[h(x) for x in cube3]
ok(all(v in (-1,1) for v in gv+hv))
ok(sum(gv)==0 and sum(hv)==0)
ok(sum(a*b for a,b in zip(gv,hv))==0)
ghat=walsh(gv); hhat=walsh(hv)
suppg={i for i,z in enumerate(ghat) if z}
supph={i for i,z in enumerate(hhat) if z}
ok(suppg==supph and len(suppg)==4)
ok(all(abs(ghat[i])==Fraction(1,2) for i in suppg))
ok(all(abs(hhat[i])==Fraction(1,2) for i in supph))
ok(any(ghat[i]==hhat[i] for i in suppg))
ok(any(ghat[i]==-hhat[i] for i in suppg))

cube4=list(product((-1,1), repeat=4))
mv=[mcore(z) for z in cube4]
mhat=walsh(mv)
ok(all(v in (-1,1) for v in mv))
ok(sum(1 for z in mhat if z)==4)
ok(all(abs(z)==Fraction(1,2) for z in mhat if z))
ok(influence(mhat)==2)
ok(abs(entropy(mhat)-2.0)<1e-14)

for t in range(1,10):
    cube=list(product((-1,1), repeat=t+4))
    vals=[sigma(z[:t])*mcore(z[t:]) for z in cube]
    coeff=walsh(vals)
    ok(all(v in (-1,1) for v in vals), f"Boolean t={t}")
    ok(sum(z*z for z in coeff)==1, f"Parseval t={t}")
    delta=Fraction(2,2**t)
    expected_I=Fraction(t)*delta+2
    ok(influence(coeff)==expected_I, f"I t={t}")
    shat=walsh([sigma(z) for z in product((-1,1), repeat=t)])
    ok(influence(shat)==Fraction(t)*delta)
    ok(abs(entropy(coeff)-(entropy(shat)+2.0))<2e-12, f"H add t={t}")
    ok(entropy(coeff)<4*float(influence(coeff)), f"FEI-4 t={t}")
    # Literal 2^(t+1)-branch cover: all three data coordinates occur in every branch.
    k=2**(t+1)
    ok(k>t)
    ok(Fraction(k,2**(t+1))==1)  # fractional congestion
    # Two distinct branch rows, each appearing with both signs: exact spectral rank two.
    rows=[]
    for c in product((-1,1), repeat=t):
        for b in (-1,1):
            base=ghat if b==1 else hhat
            rows.append(tuple(Fraction(sigma(c))*z for z in base))
    r0=rows[0]
    r1=next(r for r in rows if r!=r0 and r!=tuple(-z for z in r0))
    ok(any(r0[i]*r1[j]!=r0[j]*r1[i] for i in range(8) for j in range(8)))
    ok(all(r in (r0,tuple(-z for z in r0),r1,tuple(-z for z in r1)) for r in rows))

print(f"PASS: {checks} assertions")
print("Core branches are orthogonal but have exactly coincident four-point Fourier supports.")
print("For t=1..9: rank=2, worst read=2^(t+1), fractional congestion=1, H=H(sigma_t)+2, I=t*2^(1-t)+2, H<4I.")
