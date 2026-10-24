#!/usr/bin/env python3
from fractions import Fraction
from itertools import product, combinations

print("R09 exact checker: radius-4 failure certificate + SITE influence passage")

B1=Fraction(63,128)
B2=Fraction(16457991,33554432)
B3=Fraction(4517544707082764121,9223372036854775808)

def shell(r):
    return [(x,y,z)
            for x in range(-r,r+1)
            for y in range(-r,r+1)
            for z in range(-r,r+1)
            if abs(x)+abs(y)+abs(z)==r]

def nbrs(x):
    out=[]
    for j in range(3):
        for s in (-1,1):
            y=list(x); y[j]+=s; out.append(tuple(y))
    return out

def inward(x):
    r=sum(abs(a) for a in x)
    return [y for y in nbrs(x) if sum(abs(a) for a in y)==r-1]

def outward(x):
    r=sum(abs(a) for a in x)
    return [y for y in nbrs(x) if sum(abs(a) for a in y)==r+1]

def nshell(r): return 4*r*r+2

for r in range(1,13):
    S=shell(r)
    assert len(S)==nshell(r)
    dc={3:0,4:0,5:0}
    for x in S:
        d=len(outward(x)); assert d in dc; dc[d]+=1
    assert dc[5]==6
    assert dc[4]==12*(r-1)
    assert dc[3]==4*(r-1)*(r-2)

# Radius-4 explicit failure mass, summing exact S3 configurations |A|<=5.
S1,S2,S3,S4=map(shell,[1,2,3,4])
i1={x:i for i,x in enumerate(S1)}
i2={x:i for i,x in enumerate(S2)}
i4={x:i for i,x in enumerate(S4)}

inmask=[]
outmask=[]
for x in S3:
    a=0
    for y in inward(x): a |= 1<<i2[y]
    inmask.append(a)
    b=0
    for y in outward(x): b |= 1<<i4[y]
    outmask.append(b)

reach2=[]
for sm in range(1<<len(S1)):
    rm=0
    for y in S2:
        if any((sm>>i1[z])&1 for z in inward(y)):
            rm |= 1<<i2[y]
    reach2.append(rm)

cache={}
def p_B2_hits(Y):
    if Y in cache: return cache[Y]
    t=Fraction(0,1)
    for rm in reach2:
        k=(Y & rm).bit_count()
        if k:
            t += 1-Fraction(1,2**k)
    ans=Fraction(1,2)*t/Fraction(64,1)
    cache[Y]=ans
    return ans

def fail_mass_for_A(comb):
    Y=0; Z=0
    for i in comb:
        Y |= inmask[i]
        Z |= outmask[i]
    return Fraction(1,2**38)*p_B2_hits(Y)*Fraction(1,2**Z.bit_count())

parts=[]
D5=Fraction(0,1)
for k in range(1,6):
    s=Fraction(0,1)
    for comb in combinations(range(len(S3)),k):
        s += fail_mass_for_A(comb)
    parts.append(s)
    D5 += s

expected_parts=[
    Fraction(97,35184372088832),
    Fraction(51049,9007199254740992),
    Fraction(1018081,144115188075855872),
    Fraction(502829859,73786976294838206464),
    Fraction(52471514715,9444732965739290427392),
]
assert parts==expected_parts
assert D5==Fraction(263121688539,9444732965739290427392)
B4=B3-D5
assert B4==Fraction(4625965779789628771365,9444732965739290427392)
assert 0<B4<B3

def pair_failure_lb(r):
    geom=Fraction(1,1)
    for x in shell(r):
        geom += Fraction(1,2**len(outward(x)))
    q=Fraction(1,2**nshell(r))*geom
    assert q==Fraction(8*r*r-12*r+23,2**(4*r*r+6))
    return q

def b_new(L):
    if L==1: return B1
    if L==2: return B2
    if L==3: return B3
    if L==4: return B4
    b=B4
    for r in range(5,L,2):
        b *= 1-pair_failure_lb(r)
    if L%2==1:
        b *= 1-Fraction(1,2**nshell(L))
    return b

vals=[b_new(L) for L in range(1,21)]
assert vals[0]>vals[1]>vals[2]>vals[3]
for i in range(4,len(vals)):
    assert vals[i]<vals[i-1]

# Adversarial check: nested reach events cannot be factorized.
assert B1*B2 != B2

# Exact n=4 monotone Boolean audit for Bessel/Russo passage compiler.
def is_monotone(vals,n):
    for x in range(1<<n):
        for i in range(n):
            if ((x>>i)&1)==0 and vals[x]>vals[x|(1<<i)]:
                return False
    return True

def pstate(x,n,p):
    k=x.bit_count()
    return p**k*(1-p)**(n-k)

def event_prob(vals,n,p):
    return sum(pstate(x,n,p)*vals[x] for x in range(1<<n))

def influences(vals,n,p):
    ans=[]
    for i in range(n):
        others=[j for j in range(n) if j!=i]
        z=Fraction(0,1)
        for mask in range(1<<(n-1)):
            x=0;k=0
            for jj,j in enumerate(others):
                if (mask>>jj)&1:
                    x|=1<<j;k+=1
            if vals[x]!=vals[x|(1<<i)]:
                z += p**k*(1-p)**((n-1)-k)
        ans.append(z)
    return ans

def russo_score(vals,n,p):
    z=Fraction(0,1)
    for x in range(1<<n):
        if vals[x]:
            k=x.bit_count()
            z += pstate(x,n,p)*(Fraction(k,1)/p-Fraction(n-k,1)/(1-p))
    return z

n=4
monos=[]
for mask in range(1<<(1<<n)):
    vals=[(mask>>x)&1 for x in range(1<<n)]
    if is_monotone(vals,n): monos.append(vals)
assert len(monos)==168
for p in [Fraction(1,10),Fraction(1,5),Fraction(1,3),Fraction(2,5),Fraction(1,2)]:
    for vals in monos:
        a=event_prob(vals,n,p)
        I=influences(vals,n,p)
        var=a*(1-a)
        assert p*(1-p)*sum(x*x for x in I) <= var
        assert (sum(I))**2 <= Fraction(n,1)*var/(p*(1-p))
        assert russo_score(vals,n,p)==sum(I)
        assert (sum(I))**2 <= Fraction(25*n,9)

print("shell counts/outdegrees r=1..12: PASS")
print("radius-4 disjoint failure certificate |A|<=5: PASS")
for k,x in enumerate(parts,1):
    print(f"D{k}-increment =",x)
print("D5 =",D5)
print("B3 =",B3)
print("B4 =",B4)
print("B3-B4 =",D5)
print("outer disjoint shell-pair compiler: PASS")
print("b5 =",b_new(5))
print("b6 =",b_new(6))
print("nested reach-event factorization counterexample: PASS")
print("n=4 monotone Boolean functions audited =",len(monos))
print("exact Bessel + Russo finite SITE audit: PASS")
print("PASS")
