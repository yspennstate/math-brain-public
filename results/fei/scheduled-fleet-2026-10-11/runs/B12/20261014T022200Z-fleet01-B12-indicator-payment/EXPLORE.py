#!/usr/bin/env python3
import math
import random


def fwht(a):
    a=list(a);h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h];a[j],a[j+h]=x+y,x-y
        h*=2
    return a


def E(v):
    N=len(v); out=0.0
    for z in fwht(v):
        if z:
            u=(z/N)**2;out+=u*math.log2(1/u)
    return out


def I(v):
    N=len(v);n=N.bit_length()-1
    return sum(sum((v[x]-v[x^(1<<i)])**2 for x in range(N))/(4*N) for i in range(n))


def gap(v):
    p=sum(v)/len(v)
    return E(v)-2*I(v)-(p*math.log2(1/p) if p else 0)


best=(-1e9,None)
count=0
for n in range(1,5):
    N=1<<n
    for mask in range(1,1<<N):
        v=[(mask>>x)&1 for x in range(N)]
        g=gap(v);count+=1
        if g>best[0]:best=(g,(n,mask,v,E(v),I(v),sum(v)/N))
print('exhaustive',count,'best',best)

rng=random.Random(20261014022200)
for n in range(5,10):
    N=1<<n
    for _ in range(20000):
        # Include rare and balanced densities.
        p=2**(-rng.uniform(0, min(n,8)))
        v=[int(rng.random()<p) for _ in range(N)]
        if not any(v):v[rng.randrange(N)]=1
        g=gap(v);count+=1
        if g>best[0]:best=(g,(n,None,v,E(v),I(v),sum(v)/N))
best_v = best[1][2]
best_mask = sum(bit << i for i, bit in enumerate(best_v))
print('total',count,'best',best[:1],(best[1][0],best_mask),best[1][3:])
print('best_values', best_v)
print('best_walsh', fwht(best_v))
