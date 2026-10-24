#!/usr/bin/env python3
from fractions import Fraction
import itertools, math, random

LN2=math.log(2.0)

def q(t):
    if t<=0: return 0.0
    return t*math.log2(1.0/t)+2.0*t/LN2

def signs(mask,n):
    return tuple(1 if (mask>>j)&1 else -1 for j in range(1<<n))

def coeff(vals,S):
    n=(len(vals)).bit_length()-1
    z=0
    for x,v in enumerate(vals):
        z += v * (-1 if ((x&S).bit_count()&1) else 1)
    return Fraction(z,1<<n)

def influence(vals,i):
    n=(len(vals)).bit_length()-1
    flips=0
    for x in range(1<<n):
        if vals[x]!=vals[x^(1<<i)]: flips+=1
    return Fraction(flips,1<<n)

def orbit(vals,X,S):
    sub=X; ans=Fraction(0)
    while True:
        c=coeff(vals,S|sub); ans+=c*c
        if sub==0: return ans
        sub=(sub-1)&X

def theta(vals,X):
    n=(len(vals)).bit_length()-1
    ans=0.0
    for i in range(n):
        if (X>>i)&1: ans+=q(float(influence(vals,i)))
        else: ans+=q(float(orbit(vals,X,1<<i)))
    return ans

def phi(vals):
    n=(len(vals)).bit_length()-1
    return sum(q(float(coeff(vals,1<<i)**2)) for i in range(n))

def restrict(vals,i,bit):
    n=(len(vals)).bit_length()-1
    return tuple(vals[x] for x in range(1<<n) if ((x>>i)&1)==bit)

def erase_bit(mask,i):
    return (mask&((1<<i)-1))|((mask>>(i+1))<<i)

def check_scalar():
    worst=-1e99; count=0
    for a in range(1001):
        for b in range(1001-a,1001,137):
            aa=a/1000; bb=b/1000
            gap=q(min(1.0,aa+bb))-q(aa)-q(bb)
            worst=max(worst,gap); count+=1
            assert gap<2e-12
    return count,worst

def check_reveal():
    cases=0; worst=-1e99
    for n in (1,2,3):
        for m in range(1<<(1<<n)):
            f=signs(m,n)
            for X in range(1,1<<n):
                for x in range(n):
                    if not ((X>>x)&1): continue
                    Xp=erase_bit(X^(1<<x),x)
                    lhs=(theta(restrict(f,x,0),Xp)+theta(restrict(f,x,1),Xp))/2
                    rhs=theta(f,X)-q(float(influence(f,x)))
                    gap=lhs-rhs; worst=max(worst,gap); cases+=1
                    assert gap<2e-11,(n,m,X,x,gap)
    return cases,worst

def product(f,g,k,u,v):
    out=[]
    for z in range(1<<(k+u+v)):
        X=z&((1<<k)-1)
        U=(z>>k)&((1<<u)-1)
        V=(z>>(k+u))&((1<<v)-1)
        out.append(f[X|(U<<k)]*g[X|(V<<k)])
    return tuple(out)

def check_products():
    # Different exhaustive geometry from the producer: one shared and two private bits per factor.
    k=u=v=1
    # First exhaust the producer-size geometry independently.
    fs=[signs(m,k+u) for m in range(1<<(1<<(k+u)))]
    gs=[signs(m,k+v) for m in range(1<<(1<<(k+v)))]
    count=0; worst=-1e99
    for f in fs:
        for g in gs:
            gap=phi(product(f,g,k,u,v))-theta(f,1)-theta(g,1)
            worst=max(worst,gap);count+=1;assert gap<2e-11
    # Seeded larger factors: one shared bit and two private bits each.
    rng=random.Random(19094); k=1;u=v=2
    for _ in range(12000):
        f=signs(rng.randrange(1<<(1<<(k+u))),k+u)
        g=signs(rng.randrange(1<<(1<<(k+v))),k+v)
        gap=phi(product(f,g,k,u,v))-theta(f,1)-theta(g,1)
        worst=max(worst,gap);count+=1;assert gap<3e-11
    return count,worst

def tree(vals,incoming,rng):
    n=(len(vals)).bit_length()-1
    if n==0: return 0.0,theta(vals,incoming),0
    x=rng.randrange(n)
    active=1<<x
    for j in range(n):
        if j!=x and rng.random()<0.55: active|=1<<j
    O=theta(vals,active)-theta(vals,incoming)
    residual=erase_bit(active^(1<<x),x)
    kids=[restrict(vals,x,b) for b in (0,1)]
    R=theta(vals,active)-sum(theta(h,residual) for h in kids)/2
    total=R-O; terminal=0.0; nodes=1
    for h in kids:
        t,l,c=tree(h,residual,rng)
        total+=t/2;terminal+=l/2;nodes+=c
    return total,terminal,nodes

def check_tree():
    rng=random.Random(19094023); cases=0; worst=0.0
    for n in range(1,7):
        for _ in range(100):
            f=tuple(rng.choice((-1,1)) for _ in range(1<<n))
            total,terminal,nodes=tree(f,0,rng)
            err=total-(phi(f)-terminal)
            worst=max(worst,abs(err));cases+=nodes
            assert abs(err)<5e-9,(n,err)
    return cases,worst

def point_defect():
    rows=[]
    for r in (4,8,16,32,64,128):
        eps=2.0**(1-r)
        ratio=q(eps)/eps
        opening_ratio=(q(eps)-q(eps*eps))/eps
        rows.append((r,ratio,opening_ratio))
        assert abs(ratio-((r-1)+2/LN2))<1e-10
    return rows

if __name__=='__main__':
    print('scalar',check_scalar())
    print('reveal',check_reveal())
    print('products',check_products())
    print('tree',check_tree())
    for row in point_defect(): print('point_defect',row)
    print('PASS')
