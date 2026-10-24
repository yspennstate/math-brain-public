#!/usr/bin/env python3
"""Exact five-input composition-prime central-gap certificate plus tube arithmetic.

Dependencies used mathematically:
- the certified read-once comparator family from account01/B17;
- composition-prime criterion: an essential gate is prime iff no coordinate
  block A with 2 <= |A| <= n-1 has at most two row types.

This script independently rebuilds the low-boundary enumeration and exact
outward log intervals used by the arity-five certificate.  It proves that
every row whose certified objective gap is <= 0.039 is decomposable.  The
generic high-boundary lower bounds are also > 0.039.  Hence every essential
composition-prime five-input gate has
    Ccert*I-H - [Ccert*I(F_m)-H(F_m)] > 0.039
at uniform bias, where F_m is the read-once comparator of the same volume.
"""
from fractions import Fraction as F
from functools import lru_cache
import itertools
import numpy as np

CSTAR = F(64573, 10000)
SCALE = 10**12
THRESH = F(39,1000)
THRESH_S = int(THRESH*SCALE)
NLOG = 320

def ln_bounds_int(n, N=NLOG):
    if n == 1:
        return F(0),F(0)
    y=F(n-1,n+1); y2=y*y; term=y; s=F(0)
    for r in range(N):
        s += term/F(2*r+1)
        term *= y2
    lo=2*s
    hi=lo + 2*term/F((2*N+1)) / (1-y2)
    return lo,hi

_ln2_lo,_ln2_hi=ln_bounds_int(2)

@lru_cache(None)
def log2_bounds_int(n):
    if n & (n-1) == 0:
        z=F(n.bit_length()-1)
        return z,z
    lo,hi=ln_bounds_int(n)
    return lo/_ln2_hi, hi/_ln2_lo

def floor_scaled(x):
    y=x*SCALE
    return y.numerator//y.denominator

def ceil_scaled(x):
    y=x*SCALE
    return -((-y.numerator)//y.denominator)

atom_lo=np.zeros(33,dtype=np.int64)
atom_hi=np.zeros(33,dtype=np.int64)
for t in range(1,33):
    q=F(t*t,1024)
    llo,lhi=log2_bounds_int(t)
    atom_lo[t]=floor_scaled(q*(10-2*lhi))
    atom_hi[t]=ceil_scaled(q*(10-2*llo))

def fwht_rows(A):
    A=A.copy()
    h=1
    while h<A.shape[1]:
        for i in range(0,A.shape[1],2*h):
            x=A[:,i:i+h].copy()
            y=A[:,i+h:i+2*h].copy()
            A[:,i:i+h]=x+y
            A[:,i+h:i+2*h]=x-y
        h*=2
    return A

def raw5(M):
    vals=np.array([1 if (M>>x)&1 else -1 for x in range(32)],dtype=np.int16)[None,:]
    return fwht_rows(vals)[0]

def boundary(M,n=5):
    b=0
    for x in range(1<<n):
        for i in range(n):
            if ((M>>x)&1) != ((M>>(x^(1<<i)))&1):
                b += 1
    return b//2

COMP={
 1:(5,0x80000000), 2:(4,0x8000), 3:(5,0x80808000), 4:(3,0x80),
 5:(5,0xaa800000), 6:(4,0x8880), 7:(5,0xaa808080), 8:(2,0x8),
 9:(5,0xe0e0e000), 10:(4,0xa888), 11:(5,0xa8a8a888), 12:(3,0xa8),
 13:(5,0xaaa8a8a8), 14:(4,0xf888), 15:(5,0xeaeaea00), 16:(1,0x2)
}
def embed(mask,k):
    M=0
    for x in range(32):
        if (mask>>(x & ((1<<k)-1)))&1:
            M |= 1<<x
    return M

comp={}
for m,(k,mask) in COMP.items():
    M=mask if k==5 else embed(mask,k)
    assert M.bit_count()==m
    r=raw5(M)
    B=boundary(M)
    comp[m]=(M,r,B,int(atom_lo[np.abs(r)].sum()),int(atom_hi[np.abs(r)].sum()))

masks=np.arange(65536,dtype=np.uint32)
size4=np.fromiter((int(x).bit_count() for x in range(65536)),dtype=np.int16,count=65536)
pc16=size4.copy()
b4=np.zeros(65536,dtype=np.int16)
for M in range(65536):
    b=0
    for x in range(16):
        for i in range(4):
            if ((M>>x)&1) != ((M>>(x^(1<<i)))&1):
                b += 1
    b4[M]=b//2
T=(2*((masks[:,None]>>np.arange(16,dtype=np.uint32))&1)-1).astype(np.int16)
W=fwht_rows(T)
groups={}
for s in range(17):
    for b in range(33):
        idx=np.flatnonzero((size4==s)&(b4==b)).astype(np.uint32)
        if len(idx):
            groups[(s,b)]=idx

CUT={1:3,2:8,3:11,4:14,5:15,6:18,7:19,8:22,
     9:23,10:24,11:25,12:26,13:27,14:28,15:27,16:28}

def candidates(m,cut,chunk=256):
    for (s0,b0),A in groups.items():
        s1=m-s0
        if not 0<=s1<=16:
            continue
        for (ss,b1),B in groups.items():
            if ss!=s1 or b0+b1>cut:
                continue
            mx=cut-b0-b1
            for st in range(0,len(A),chunk):
                aa=A[st:st+chunk]
                px=pc16[np.bitwise_xor(aa[:,None],B[None,:])]
                ii,jj=np.nonzero(px<=mx)
                if len(ii):
                    yield aa[ii],B[jj],(b0+b1+px[ii,jj]).astype(np.int16)

def bit(mask,x):
    return (mask>>x)&1

def essential(mask,n=5):
    for i in range(n):
        if not any(bit(mask,x)!=bit(mask,x^(1<<i)) for x in range(1<<n)):
            return False
    return True

def block_patterns(mask,A,n=5):
    A=tuple(A)
    B=tuple(i for i in range(n) if i not in A)
    pats=[]
    for aa in range(1<<len(A)):
        vec=0
        for bb in range(1<<len(B)):
            x=0
            for k,i in enumerate(A):
                if (aa>>k)&1:
                    x |= 1<<i
            for k,i in enumerate(B):
                if (bb>>k)&1:
                    x |= 1<<i
            vec |= bit(mask,x)<<bb
        pats.append(vec)
    return pats

def is_composition_prime(mask,n=5):
    if not essential(mask,n):
        return False
    for r in range(2,n):
        for A in itertools.combinations(range(n),r):
            if len(set(block_patterns(mask,A,n)))<=2:
                return False
    return True

def hmax_upper_scaled(m):
    vn=m*(32-m); wn=256-vn
    V=F(vn,256); W0=F(wn,256); ans=F(0)
    if vn:
        llo,_=log2_bounds_int(vn)
        _,lhi31=log2_bounds_int(31)
        ans += V*(8-llo) + V*lhi31
    if wn:
        llo,_=log2_bounds_int(wn)
        ans += W0*(8-llo)
    return ceil_scaled(ans)

const_floor={db:floor_scaled(CSTAR*F(db,16)) for db in range(-80,81)}

total_low=0
total_danger=0
rows=[]
for m in range(2,17):
    _,raw0,B0,Hlo0,Hhi0=comp[m]
    checked=danger=0
    for aa,bb,bd in candidates(m,CUT[m]):
        checked += len(aa); total_low += len(aa)
        wa=W[aa]; wb=W[bb]
        v1=np.abs(wa+wb); v2=np.abs(wa-wb)
        Hup=(atom_hi[v1].sum(axis=1)+atom_hi[v2].sum(axis=1)).astype(np.int64)
        cterm=np.fromiter((const_floor[int(x)-B0] for x in bd),dtype=np.int64,count=len(bd))
        lb=cterm+Hlo0-Hup
        idx=np.flatnonzero(lb<=THRESH_S)
        danger += len(idx); total_danger += len(idx)
        for j in idx:
            M=int(aa[j]) | (int(bb[j])<<16)
            if is_composition_prime(M,5):
                raise AssertionError(("prime below threshold",m,M,int(bd[j]),int(lb[j])))
    bnext=CUT[m]+1
    while (bnext-m)&1:
        bnext += 1
    generic_lb=const_floor[bnext-B0]+Hlo0-hmax_upper_scaled(m)
    assert generic_lb>THRESH_S,(m,generic_lb)
    rows.append((m,checked,danger,generic_lb/SCALE))

assert total_low==3425314
assert total_danger==9490

eps=F(1,25000)
loss=966*eps+6480*eps*eps
reserve=THRESH-loss
assert reserve>0
print("PASS")
print("prime_central_gap_floor", float(THRESH))
print("low_boundary_rows_checked", total_low)
print("rows_with_certified_lb_le_0.039", total_danger)
print("prime_rows_among_them", 0)
for m,checked,danger,generic in rows:
    print("m",m,"checked",checked,"danger",danger,"generic_lb",f"{generic:.12f}")
print("central_margin_cG_upper", -0.0212)
print("tube_epsilon", float(eps))
print("tube_deterministic_loss", float(loss))
print("tube_reserve_before_KL_credit", float(reserve))
print("tube_reserve_fraction", reserve)
