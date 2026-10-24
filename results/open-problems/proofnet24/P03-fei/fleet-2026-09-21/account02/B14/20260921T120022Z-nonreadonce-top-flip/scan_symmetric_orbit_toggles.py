#!/usr/bin/env python3
"""Symmetry-orbit toggle search around 8 width-two tribes (16 variables).

The 45 orbits are indexed by (a,b,c):
a=# pairs equal 00, b=# pairs with exactly one 1, c=# pairs equal 11.
For each choice of up to three whole orbits, toggle f on the union and compute
rho0 = min_i Delta_i H / Inf_i. Whole-orbit toggles preserve transitivity of
the 16 physical coordinates, so one representative coordinate suffices.

Walsh transforms are exact int64. Entropies are exploratory float64, so this
search is not a rigorous strict-ranking certificate. It is used only to find
candidate witnesses; the selected top-flip witness is separately verified at
80/110 decimal digits by verify_top_flip_witness.py.
"""
import itertools, json, math
from collections import defaultdict
import numpy as np

N_BITS=16
TRIBES=8
N=1<<N_BITS
N2=float(N*N)

idx=np.arange(N,dtype=np.uint32)
safe=np.ones(N,dtype=bool)
for j in range(TRIBES):
    safe &= ~(((idx>>(2*j))&3)==3)
base=np.where(safe,1,-1).astype(np.int64)

def fwht(v):
    a=v.copy()
    h=1
    while h<N:
        for s in range(0,N,2*h):
            u=a[s:s+h].copy()
            w=a[s+h:s+2*h].copy()
            a[s:s+h]=u+w
            a[s+h:s+2*h]=u-w
        h*=2
    return a

def h2(q):
    out=np.zeros_like(q,dtype=np.float64)
    m=(q>0)&(q<1)
    z=q[m]
    out[m]=-(z*np.log(z)+(1-z)*np.log1p(-z))/math.log(2.0)
    return out

def psi(q):
    z=0.5+np.sqrt(q*(1-q))
    return h2(q)+(1-h2(z))

low=np.arange(N,dtype=np.int64)
low=low[(low&1)==0]
up=low|1

def rho(A):
    aa=A[low].astype(np.float64)**2
    bb=A[up].astype(np.float64)**2
    den=aa+bb
    q=np.divide(bb,den,out=np.zeros_like(bb),where=den>0)
    p=np.sum(bb)/N2
    d=np.sum(den*psi(q))/N2
    return float(d/p),float(p)

orbits=defaultdict(list)
for x in range(N):
    a=b=c=0
    for j in range(TRIBES):
        z=(x>>(2*j))&3
        if z==0: a+=1
        elif z==3: c+=1
        else: b+=1
    orbits[(a,b,c)].append(x)
keys=sorted(orbits)
assert len(keys)==45

A0=fwht(base)
delta=[]
for key in keys:
    v=np.zeros(N,dtype=np.int64)
    xs=np.asarray(orbits[key],dtype=np.int64)
    v[xs]=-2*base[xs]
    delta.append(fwht(v))

baseline=rho(A0)
single=[]
for i,key in enumerate(keys):
    r,p=rho(A0+delta[i])
    single.append((r,key,p,len(orbits[key])))
single.sort(reverse=True)

pair_best=(-1.0,None)
for i,j in itertools.combinations(range(len(keys)),2):
    r,p=rho(A0+delta[i]+delta[j])
    item=(r,keys[i],keys[j],p,len(orbits[keys[i]]),len(orbits[keys[j]]))
    if r>pair_best[0]:
        pair_best=(r,item)

triple_best=(-1.0,None)
for i,j,k in itertools.combinations(range(len(keys)),3):
    r,p=rho(A0+delta[i]+delta[j]+delta[k])
    item=(r,keys[i],keys[j],keys[k],p,
          len(orbits[keys[i]]),len(orbits[keys[j]]),len(orbits[keys[k]]))
    if r>triple_best[0]:
        triple_best=(r,item)

out={
  "status":"PASS",
  "numeric_status":"exact int64 Walsh; exploratory float64 entropy; not a directed-rounding strict-ranking certificate",
  "orbit_definition":"(a,b,c) = counts of pair states 00, single, 11; a+b+c=8",
  "orbit_count":len(keys),
  "baseline":{"rho0":baseline[0],"influence":baseline[1]},
  "best_single":{"rho0":single[0][0],"orbit":single[0][1],"influence":single[0][2],"orbit_size":single[0][3]},
  "best_pair":{"rho0":pair_best[1][0],"orbits":[pair_best[1][1],pair_best[1][2]],"influence":pair_best[1][3],"orbit_sizes":[pair_best[1][4],pair_best[1][5]]},
  "best_triple":{"rho0":triple_best[1][0],"orbits":[triple_best[1][1],triple_best[1][2],triple_best[1][3]],"influence":triple_best[1][4],"orbit_sizes":[triple_best[1][5],triple_best[1][6],triple_best[1][7]]},
  "top_10_single":[{"rho0":r,"orbit":key,"influence":p,"orbit_size":sz} for r,key,p,sz in single[:10]],
  "number_pairs_checked":math.comb(45,2),
  "number_triples_checked":math.comb(45,3)
}
print(json.dumps(out,indent=2,sort_keys=True))
