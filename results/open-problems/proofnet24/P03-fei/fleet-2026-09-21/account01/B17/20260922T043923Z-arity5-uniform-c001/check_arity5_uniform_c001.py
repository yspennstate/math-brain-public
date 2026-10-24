#!/usr/bin/env python3
"""Rigorous uniform-bias arity-five certificate for CERTIFIED-READONCE-LIFT-c0.01.

For every Boolean G on five uniform inputs, prove
    Ccert I(G) - H(G) >= Gamma_cert(Pr[G=-1])
for the inherited certified read-once potential Gamma_cert,
using only the already-certified read-once admissibility of Gamma_cert plus
an exact finite comparison.  The finite comparison proves that at every
output cardinality m<=16, Ccert*I-H is minimized by an explicit read-once gate.

All sign decisions use integer Walsh transforms and rational log intervals.
"""
from fractions import Fraction as F
from functools import lru_cache
import re
import numpy as np

CSTAR = F(64573, 10000)   # 6.4573
SCALE = 10**12
NLOG = 320

def ln_bounds_int(n, N=NLOG):
    if n == 1:
        return F(0), F(0)
    y = F(n-1, n+1)
    y2 = y*y
    term = y
    s = F(0)
    for r in range(N):
        s += term / (2*r+1)
        term *= y2
    lo = 2*s
    tail = 2*term / ((2*N+1)*(1-y2))
    return lo, lo+tail

_ln2_lo, _ln2_hi = ln_bounds_int(2)

@lru_cache(None)
def log2_bounds_int(n):
    assert n >= 1
    if n & (n-1) == 0:
        z = F(n.bit_length()-1)
        return z,z
    lo,hi = ln_bounds_int(n)
    return lo/_ln2_hi, hi/_ln2_lo

def floor_scaled(x):
    return (x*SCALE).numerator // (x*SCALE).denominator

def ceil_scaled(x):
    y=x*SCALE
    return -((-y.numerator)//y.denominator)

# entropy atom for a raw 5-cube Walsh amplitude t: q=t^2/1024
atom_lo=np.zeros(33,dtype=np.int64)
atom_hi=np.zeros(33,dtype=np.int64)
for t in range(1,33):
    q=F(t*t,1024)
    llo,lhi=log2_bounds_int(t)
    lo=q*(10-2*lhi)
    hi=q*(10-2*llo)
    atom_lo[t]=floor_scaled(lo)
    atom_hi[t]=ceil_scaled(hi)

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

def raw_walsh_mask(mask,k):
    vals=np.array([1 if (mask>>x)&1 else -1 for x in range(1<<k)],dtype=np.int16)[None,:]
    return fwht_rows(vals)[0]

def boundary_mask(mask,k):
    b=0
    for x in range(1<<k):
        if not ((mask>>x)&1):
            continue
        for i in range(k):
            if ((x>>i)&1)==0 and ((mask>>(x|(1<<i)))&1)==0:
                b += 1
            elif ((x>>i)&1)==1:
                pass
    b=0
    for x in range(1<<k):
        for i in range(k):
            y=x^(1<<i)
            if (((mask>>x)&1) != ((mask>>y)&1)):
                b += 1
    return b//2

@lru_cache(None)
def ro_masks(k):
    if k==1:
        return {0b10:"x1"}
    out={}
    for a in range(1,k):
        b=k-a
        for ma,ea in ro_masks(a).items():
            for mb,eb in ro_masks(b).items():
                def shift(expr,s):
                    return re.sub(r'x(\d+)',lambda mm:"x%d"%(int(mm.group(1))+s),expr)
                eb2=shift(eb,a)
                for op in ("&","|"):
                    m=0
                    for x in range(1<<k):
                        va=(ma>>(x&((1<<a)-1)))&1
                        vb=(mb>>(x>>a))&1
                        v=(va&vb) if op=="&" else (va|vb)
                        m |= int(v)<<x
                    out.setdefault(m,"(%s%s%s)"%(ea,op,eb2))
    return out

COMP={
 1:(5,0x80000000), 2:(4,0x8000), 3:(5,0x80808000), 4:(3,0x80),
 5:(5,0xaa800000), 6:(4,0x8880), 7:(5,0xaa808080), 8:(2,0x8),
 9:(5,0xe0e0e000), 10:(4,0xa888), 11:(5,0xa8a8a888), 12:(3,0xa8),
 13:(5,0xaaa8a8a8), 14:(4,0xf888), 15:(5,0xeaeaea00), 16:(1,0x2)
}

def embed_mask(mask,k):
    M=0
    for x in range(32):
        if (mask>>(x & ((1<<k)-1)))&1:
            M |= 1<<x
    return M

def raw5_for_mask(M):
    vals=np.array([1 if (M>>x)&1 else -1 for x in range(32)],dtype=np.int16)[None,:]
    return fwht_rows(vals)[0]

comp={}
for m,(k,mask) in COMP.items():
    assert mask in ro_masks(k)
    M=embed_mask(mask,k)
    assert M.bit_count()==m
    raw=raw5_for_mask(M)
    B=boundary_mask(M,5)
    Hlo=int(atom_lo[np.abs(raw)].sum())
    Hhi=int(atom_hi[np.abs(raw)].sum())
    comp[m]=(k,mask,ro_masks(k)[mask],M,raw,B,Hlo,Hhi)

for m in range(1,17):
    k=COMP[m][0]
    dummies=5-k
    target=m>>dummies
    _,_,_,_,raw0,B0,Hlo0,Hhi0=comp[m]
    U0_hi=ceil_scaled(CSTAR*F(B0,16))-Hlo0
    for mask,expr in ro_masks(k).items():
        if mask.bit_count()!=target:
            continue
        M=embed_mask(mask,k)
        raw=raw5_for_mask(M)
        B=boundary_mask(M,5)
        Hhi=int(atom_hi[np.abs(raw)].sum())
        U_lo=floor_scaled(CSTAR*F(B,16))-Hhi
        if U_lo < U0_hi:
            if not (B==B0 and np.array_equal(np.sort(np.abs(raw)),np.sort(np.abs(raw0)))):
                raise AssertionError(("RO comparator not certified minimal",m,mask,expr,U_lo,U0_hi))

masks=np.arange(65536,dtype=np.uint32)
size4=np.fromiter((int(x).bit_count() for x in range(65536)),dtype=np.int16,count=65536)
pc16=size4.copy()
b4=np.zeros(65536,dtype=np.int16)
for mask in range(65536):
    b=0
    for x in range(16):
        for i in range(4):
            y=x^(1<<i)
            if (((mask>>x)&1) != ((mask>>y)&1)):
                b += 1
    b4[mask]=b//2
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
        if not 0<=s1<=16: continue
        for (ss,b1),B in groups.items():
            if ss!=s1 or b0+b1>cut: continue
            mx=cut-b0-b1
            for st in range(0,len(A),chunk):
                aa=A[st:st+chunk]
                px=pc16[np.bitwise_xor(aa[:,None],B[None,:])]
                ii,jj=np.nonzero(px<=mx)
                if len(ii):
                    yield aa[ii],B[jj],(b0+b1+px[ii,jj]).astype(np.int16)

def hmax_upper_scaled(m):
    vn=m*(32-m)
    wn=256-vn
    V=F(vn,256); W0=F(wn,256)
    ans=F(0)
    if vn:
        llo,_=log2_bounds_int(vn)
        ans += V*(8-llo)
        _,lhi31=log2_bounds_int(31)
        ans += V*lhi31
    if wn:
        llo,_=log2_bounds_int(wn)
        ans += W0*(8-llo)
    return ceil_scaled(ans)

const_floor={}
for db in range(-80,81):
    const_floor[db]=floor_scaled(CSTAR*F(db,16))

total_low=0
result=[]
for m in range(1,17):
    k,mask,expr,M0,raw0,B0,Hlo0,Hhi0=comp[m]
    eq=0
    min_strict=None
    checked=0
    for aa,bb,bd in candidates(m,CUT[m]):
        checked += len(aa); total_low += len(aa)
        wa=W[aa]; wb=W[bb]
        v1=np.abs(wa+wb)
        v2=np.abs(wa-wb)
        Hup=(atom_hi[v1].sum(axis=1)+atom_hi[v2].sum(axis=1)).astype(np.int64)
        cterm=np.fromiter((const_floor[int(x)-B0] for x in bd),dtype=np.int64,count=len(bd))
        lb=cterm + Hlo0 - Hup
        bad=np.flatnonzero(lb<=0)
        for j in bad:
            raw=np.concatenate((wa[j]+wb[j],wa[j]-wb[j]))
            if int(bd[j])==B0 and np.array_equal(np.sort(np.abs(raw)),np.sort(np.abs(raw0))):
                eq += 1
            else:
                raise AssertionError(("uncertified low-boundary row",m,int(aa[j]),int(bb[j]),int(bd[j]),int(lb[j])))
        pos=lb[lb>0]
        if len(pos):
            z=int(pos.min())
            min_strict=z if min_strict is None else min(min_strict,z)

    bnext=CUT[m]+1
    while (bnext-m)&1:
        bnext += 1
    generic_lb=const_floor[bnext-B0] + Hlo0 - hmax_upper_scaled(m)
    if m==1:
        assert B0==5
        eq=32
        generic_lb=0
    else:
        assert generic_lb>0, (m,generic_lb)
        min_strict=generic_lb if min_strict is None else min(min_strict,generic_lb)
    result.append((m,k,mask,expr,B0,checked,eq,min_strict,generic_lb))

print("PASS")
print("candidate", "CERTIFIED-READONCE-LIFT-c0.01", "Ccert", float(CSTAR))
print("total_low_boundary_tables_m_le_16", total_low)
for r in result:
    m,k,mask,expr,B0,checked,eq,min_strict,generic_lb=r
    print("m",m,"k",k,"mask",hex(mask),"Bcomp",B0,
          "low_checked",checked,"exact_equal",eq,
          "min_strict_lb",None if min_strict is None else min_strict/SCALE,
          "generic_lb",generic_lb/SCALE,"expr",expr)
print("symmetry", "m>16 follows by output complementation")
print("conclusion", "all five-input gates at uniform bias satisfy D_Gamma_cert>=0 and hence c_G<=0.01")
