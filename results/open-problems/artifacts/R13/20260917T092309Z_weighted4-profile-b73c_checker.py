#!/usr/bin/env python3
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import math

# Exact finite certificate for four balanced norm-cap profiles.
SIGNS=[(1,)+x for x in product((-1,1),repeat=3)]

def set_partitions(n):
    out=[]; blocks=[]
    def rec(i):
        if i==n:
            out.append(tuple(tuple(b) for b in blocks)); return
        for b in blocks:
            b.append(i); rec(i+1); b.pop()
        blocks.append([i]); rec(i+1); blocks.pop()
    rec(0); return out
PARTITIONS=set_partitions(8)
assert len(PARTITIONS)==4140

def orientation_options(block):
    k=len(block)
    for tail in product((-1,1),repeat=k-1):
        sg=(1,)+tail
        yield tuple(sg[j]*(block[j]+1) for j in range(k))

def oriented_vectors(key):
    out=[]
    for z in key:
        sg=1 if z>0 else -1
        s=SIGNS[abs(z)-1]
        out.append(tuple(sg*x for x in s))
    return out

@lru_cache(None)
def subset_data(key):
    vecs=oriented_vectors(key); k=len(vecs); out=[]
    for mask in range(1,1<<k):
        q=mask.bit_count(); v=[0,0,0,0]
        for i,t in enumerate(vecs):
            if (mask>>i)&1:
                for j in range(4): v[j]+=t[j]
        if v==[0,0,0,0]:
            return None  # block constraints infeasible for every diagonal weight
        out.append((q,tuple(v)))
    return tuple(out)

# Profile-specific finite diagonal-weight covers, found heuristically but VERIFIED below exactly.
PROFILES={
  10:{'caps':(3,3,2,2),'weights':[(5,5,3,3),(4,4,4,4),(5,5,1,5),(5,5,5,1),(7,7,1,1),(1,5,4,6),(7,1,4,4),(5,6,1,4),(5,6,4,1),(1,5,6,4)]},
  11:{'caps':(3,3,3,2),'weights':[(4,4,4,4),(5,5,5,1),(1,6,6,3),(5,4,4,3),(7,4,4,1),(5,1,5,5),(4,6,1,5),(3,5,5,3),(5,1,7,3),(5,7,1,3)]},
  13:{'caps':(4,3,3,3),'weights':[(4,4,4,4),(6,2,4,4),(5,5,3,3),(6,4,1,5),(6,4,5,1),(1,5,5,5),(5,1,5,5),(5,3,4,4),(7,1,1,7),(5,1,8,2),(5,8,1,2)]},
  15:{'caps':(4,4,4,3),'weights':[(4,4,4,4),(5,5,5,1),(1,5,6,4),(5,4,4,3),(5,1,5,5),(6,6,1,3),(3,5,5,3),(1,4,1,10),(1,4,10,1),(4,1,10,1)]},
}
for n,p in PROFILES.items():
    assert sum(p['caps'])==n
    for a in p['weights']:
        assert all(x>0 for x in a) and sum(a)==16

@lru_cache(None)
def block_lb(key,a,caps):
    data=subset_data(key)
    if data is None: return None
    P=a[0]*a[1]*a[2]*a[3]
    bn,bd=0,1
    for q,v in data:
        # Lambda_j=a_j/16 and D_j=Lambda_j/caps_j.
        # denom = sum v_j^2 / D_j = 16 sum v_j^2 caps_j/a_j.
        dn=16*sum(v[j]*v[j]*caps[j]*(P//a[j]) for j in range(4))
        nn=q*q*P
        if nn*bd > bn*dn:
            bn,bd=nn,dn
    return F(bn,bd)

def cert_config(keys,caps,weights,target):
    # If a block contains a zero-sum subset, its oriented constraints are infeasible.
    if any(subset_data(k) is None for k in keys):
        return ('infeasible',None,None)
    for a in weights:
        total=F(0,1)
        for k in keys:
            total += block_lb(k,a,caps)
            if total>=target:
                return ('weight',a,total)
    return None

def certify(n,p):
    caps=p['caps']; weights=tuple(p['weights']); target=F(4,3*n)
    count=0; infeasible=0; exact_target=0; smallest=None
    first_counts={a:0 for a in weights}
    for part in PARTITIONS:
        opts=[tuple(orientation_options(b)) for b in part]
        for keys in product(*opts):
            count+=1
            cert=cert_config(keys,caps,weights,target)
            if cert is None:
                raise AssertionError(f'UNCERTIFIED n={n} caps={caps} part={part} keys={keys}')
            if cert[0]=='infeasible':
                infeasible+=1
            else:
                a,val=cert[1],cert[2]
                first_counts[a]+=1
                if val==target: exact_target+=1
                if smallest is None or val<smallest: smallest=val
    assert count==75905
    assert smallest is not None and smallest>=target
    return count,infeasible,exact_target,smallest,first_counts

RESULTS={}
for n,p in PROFILES.items():
    RESULTS[n]=certify(n,p)
    count,inf,eq,small,fc=RESULTS[n]
    print(f'PROFILE n={n} caps={p["caps"]} t2={F(3*n,4)} rho={F(4,3*n)} configurations={count} infeasible={inf} exact_target={eq} smallest_selected={small} weights={len(p["weights"])}')
    print(' first_certificate_counts=',[(a,fc[a]) for a in p['weights']])

# Exact envelope propagation through the already-proved block composition theorem.
BASE_OLD={4:F(3),5:F(4),6:F(9,2),7:F(21,4),8:F(6),9:F(27,4)}
BASE_NEW=dict(BASE_OLD)
for n in PROFILES: BASE_NEW[n]=F(3*n,4)

def block2(n,bases):
    choices=[]
    for k,b2 in bases.items():
        q=(n+k-1)//k
        choices.append((b2*q,k))
    return min(choices)

# Rational Machin bracket for pi, used only for comparison with GFL squared constant 18*pi.
def atan_partial(x,N):
    s=F(0)
    for k in range(N+1):
        term=x**(2*k+1)/F(2*k+1)
        s += term if k%2==0 else -term
    return s
# atan alternating: odd N lower, even N upper.
pi_lo=16*atan_partial(F(1,5),13)-4*atan_partial(F(1,239),2)
pi_hi=16*atan_partial(F(1,5),12)-4*atan_partial(F(1,239),3)
assert pi_lo < pi_hi
assert pi_lo > F(333,106)
assert pi_hi < F(22,7)
GFL_lo=18*pi_lo; GFL_hi=18*pi_hi

moved=[]
for n in range(10,76):
    new2,k=block2(n,BASE_NEW)
    if n<=72:
        old2,_=block2(n,BASE_OLD)
        if new2<old2: moved.append((n,old2,new2,k))
    else:
        if new2<GFL_lo: moved.append((n,'GFL',new2,k))

assert block2(75,BASE_NEW)[0] < GFL_lo
assert block2(76,BASE_NEW)[0] > GFL_hi
print('MOVED_COUNT',len(moved))
for x in moved: print('MOVE',x)
for n in (10,11,13,15,22,25,26,33,37,38,39,50,55,65,73,74,75,76):
    print('ENVELOPE',n,block2(n,BASE_NEW))
print('PI_LOWER',pi_lo)
print('PI_UPPER',pi_hi)
print('CROSSOVER new_block_beats_GFL_through=75 universal_GFL_starts=76')
print('ALL_EXACT_CHECKS_PASS')
