#!/usr/bin/env python3
import itertools, math, random

LN2 = math.log(2.0)

def q(t):
    if t <= 0.0:
        return 0.0
    return t * math.log2(1.0 / t) + 2.0 * t / LN2

def walsh(vals):
    a = [float(v) for v in vals]
    n = (len(a)).bit_length() - 1
    for j in range(n):
        step = 1 << j
        for base in range(0, len(a), 2 * step):
            for r in range(step):
                u, v = a[base+r], a[base+r+step]
                a[base+r], a[base+r+step] = (u+v)/2.0, (u-v)/2.0
    return a

def restrict(vals, n, coord, bit):
    out=[]
    for mask in range(1 << n):
        if ((mask >> coord) & 1) == bit:
            out.append(vals[mask])
    return out

def remove_coord(mask, coord):
    lo = mask & ((1 << coord) - 1)
    hi = mask >> (coord + 1)
    return lo | (hi << coord)

def infs(vals):
    wh=walsh(vals); n=(len(vals)).bit_length()-1
    return [sum(c*c for m,c in enumerate(wh) if (m>>i)&1) for i in range(n)]

def orbit_energy(vals, X, base):
    wh=walsh(vals)
    total=0.0
    sub=X
    while True:
        total += wh[base | sub] ** 2
        if sub == 0: break
        sub = (sub - 1) & X
    return total

def theta(vals, X):
    n=(len(vals)).bit_length()-1
    ii=infs(vals)
    ans=sum(q(ii[i]) for i in range(n) if (X>>i)&1)
    for i in range(n):
        if not ((X>>i)&1):
            ans += q(orbit_energy(vals, X, 1<<i))
    return ans

def phi(vals):
    wh=walsh(vals); n=(len(vals)).bit_length()-1
    return sum(q(wh[1<<i]**2) for i in range(n))

def product_vals(f, g, k, u, v):
    out=[]
    for mask in range(1 << (k+u+v)):
        xm=mask & ((1<<k)-1)
        um=(mask>>k)&((1<<u)-1)
        vm=(mask>>(k+u))&((1<<v)-1)
        out.append(f[xm | (um<<k)] * g[xm | (vm<<k)])
    return out

def all_signs(n):
    for mask in range(1 << (1<<n)):
        yield [1 if (mask>>j)&1 else -1 for j in range(1<<n)]

def check_contraction():
    count=0; worst=0.0
    for n in range(1,4):
        for vals in all_signs(n):
            for X in range(1,1<<n):
                for x in range(n):
                    if not ((X>>x)&1): continue
                    Xp=remove_coord(X & ~(1<<x), x)
                    kids=[restrict(vals,n,x,b) for b in (0,1)]
                    lhs=sum(theta(kid,Xp) for kid in kids)/2
                    rhs=theta(vals,X)-q(infs(vals)[x])
                    worst=max(worst,lhs-rhs); count+=1
                    assert lhs <= rhs + 2e-11, (n,X,x,lhs,rhs)
    return count,worst

def check_product():
    count=0; worst=0.0
    for k,u,v in [(1,1,1),(2,1,1)]:
        X=(1<<k)-1
        fs=list(all_signs(k+u)); gs=list(all_signs(k+v))
        for f in fs:
            for g in gs:
                h=product_vals(f,g,k,u,v)
                gap=phi(h)-theta(f,X)-theta(g,X)
                worst=max(worst,gap); count+=1
                assert gap <= 2e-11, (k,gap)
    return count,worst

def recurse_ledger(vals, labels, rng, depth=0):
    n=len(labels)
    if n==0:
        return theta(vals,0), 0.0, 0.0, 1
    x=rng.randrange(n)
    # Active block contains the physical query; other live coordinates are arbitrary.
    X=1<<x
    for i in range(n):
        if i!=x and rng.random()<0.5: X|=1<<i
    P=theta(vals,X)
    Xres=remove_coord(X & ~(1<<x),x)
    kids=[restrict(vals,n,x,b) for b in (0,1)]
    R=P-sum(theta(k,Xres) for k in kids)/2
    C=0.0; child_R=0.0; child_C=0.0; leafP=0.0; nodes=1
    for kid in kids:
        nn=n-1
        if nn:
            Y=0
            for i in range(nn):
                if rng.random()<0.5: Y|=1<<i
            # The child's actual pre-query block will be chosen in its recursive call;
            # use a wrapper step with arbitrary changed ownership Y, then query there.
            C += (theta(kid,Y)-theta(kid,Xres))/2
            # Force recursion's first block via a small local implementation.
            lr,lc,lp,ct = recurse_with_root(kid,labels[:x]+labels[x+1:],Y,rng)
            child_R += lr/2; child_C += lc/2; leafP += lp/2; nodes += ct
        else:
            leafP += theta(kid,0)/2
            C += (theta(kid,0)-theta(kid,Xres))/2
    return R+child_R,C+child_C,leafP,nodes

def recurse_with_root(vals, labels, X, rng):
    n=len(labels)
    if n==0: return 0.0,0.0,theta(vals,X),0
    choices=[i for i in range(n) if (X>>i)&1]
    if not choices:
        x=rng.randrange(n); X|=1<<x
    else: x=rng.choice(choices)
    P=theta(vals,X); Xres=remove_coord(X & ~(1<<x),x)
    kids=[restrict(vals,n,x,b) for b in (0,1)]
    R=P-sum(theta(k,Xres) for k in kids)/2
    C=0.0; RR=R; CC=0.0; LP=0.0; nodes=1
    for kid in kids:
        nn=n-1; Y=0
        if nn:
            for i in range(nn):
                if rng.random()<0.5: Y|=1<<i
            if Y==0: Y=1<<rng.randrange(nn)
        Cedge=theta(kid,Y)-theta(kid,Xres)
        rr,cc,lp,ct=recurse_with_root(kid,labels[:x]+labels[x+1:],Y,rng)
        RR += rr/2; CC += (Cedge+cc)/2; LP += lp/2; nodes += ct
    return RR,CC,LP,nodes

def check_telescope():
    rng=random.Random(2026101405); count=0; worst=0.0
    for n in range(1,7):
        for _ in range(120):
            vals=[rng.choice((-1,1)) for _ in range(1<<n)]
            X=0
            for i in range(n):
                if rng.random()<0.5: X|=1<<i
            if X==0: X=1<<rng.randrange(n)
            rr,cc,lp,nodes=recurse_with_root(vals,list(range(n)),X,rng)
            err=(rr-cc)-(theta(vals,X)-lp)
            worst=max(worst,abs(err)); count+=nodes
            assert abs(err)<5e-9,(n,err,rr,cc,lp)
    return count,worst

if __name__=='__main__':
    c1,w1=check_contraction(); print('contraction_cases',c1,'worst_excess',w1)
    c2,w2=check_product(); print('product_pairs',c2,'worst_excess',w2)
    c3,w3=check_telescope(); print('tree_nodes',c3,'max_telescope_error',w3)
    print('PASS')
