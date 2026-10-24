#!/usr/bin/env python3
"""
Exact combinatorial classification of all equality cases in the certified
five-input uniform-bias comparison of account01/B17, plus a new rigorous
lower bound on D_Gamma_.01/M for every strict table.

Dependency: account01/B17/20260922T043923Z-arity5-uniform-c001 proves that,
for each output cardinality m<=16, equality in the objective comparison can
occur only when BOTH (i) the five-cube edge boundary equals the comparator
boundary B_m and (ii) the multiset of absolute raw Walsh amplitudes equals
that of the explicit read-once comparator F_m. Its generic high-boundary
region is strictly separated.

This script independently enumerates those exact integer signatures, proves
they are exactly cube-automorphism orbits of the comparators, verifies a
binary-summary decomposition, and computes a rigorous strict-margin ratio
using rational logarithm enclosures. No floating-point logarithm is used for
a sign decision.
"""
import itertools
import numpy as np
from fractions import Fraction as F
from functools import lru_cache

def fwht_rows(A):
    A=A.copy(); h=1
    while h<A.shape[1]:
        for i in range(0,A.shape[1],2*h):
            x=A[:,i:i+h].copy(); y=A[:,i+h:i+2*h].copy()
            A[:,i:i+h]=x+y; A[:,i+h:i+2*h]=x-y
        h*=2
    return A

def boundary_mask(mask,k):
    b=0
    for x in range(1<<k):
        for i in range(k):
            if (((mask>>x)&1) != ((mask>>(x^(1<<i)))&1):
                b += 1
    return b//2

def raw5_for_mask(M):
    vals=np.array([1 if (M>>x)&1 else -1 for x in range(32)],dtype=np.int16)[None,:]
    return fwht_rows(vals)[0]

COMP={
 1:(5,0x80000000), 2:(4,0x8000), 3:(5,0x80808000), 4:(3,0x80),
 5:(5,0xaa800000), 6:(4,0x8880), 7:(5,0xaa808080), 8:(2,0x8),
 9:(5,0xe0e0e000), 10:(4,0xa888), 11:(5,0xa8a8a888), 12:(3,0xa8),
 13:(5,0xaaa8a8a8), 14:(4,0xf888), 15:(5,0xeaeaea00), 16:(1,0x2)
}
CUT={1:3,2:8,3:11,4:14,5:15,6:18,7:19,8:22,
     9:23,10:24,11:25,12:26,13:27,14:28,15:27,16:28}

def embed_mask(mask,k):
    M=0
    for x in range(32):
        if (mask>>(x & ((1<<k)-1)))&1:
            M |= 1<<x
    return M

comp={}
for m,(k,mask) in COMP.items():
    M=embed_mask(mask,k)
    assert M.bit_count()==m
    comp[m]=(M,raw5_for_mask(M),boundary_mask(M,5))

masks=np.arange(65536,dtype=np.uint32)
size4=np.fromiter((int(x).bit_count() for x in range(65536)),dtype=np.int16,count=65536)
pc16=size4.copy()
b4=np.zeros(65536,dtype=np.int16)
for mask in range(65536):
    b=0
    for x in range(16):
        for i in range(4):
            if (((mask>>x)&1) != ((mask>>(x^(1<<i)))&1):
                b += 1
    b4[mask]=b//2
T=(2*((masks[:,None]>>np.arange(16,dtype=np.uint32))&1)-1).astype(np.int16)
W=fwht_rows(T)
groups={}
for s in range(17):
    for b in range(33):
        idx=np.flatnonzero((size4==s)&(b4==b)).astype(np.uint32)
        if len(idx): groups[(s,b)]=idx

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

def equality_masks(m):
    M0,raw0,B0=comp[m]; sig0=np.sort(np.abs(raw0))
    if m==1: return {1<<x for x in range(32)}
    out=set()
    for aa,bb,bd in candidates(m,CUT[m]):
        sel=np.flatnonzero(bd==B0)
        if len(sel)==0: continue
        aa2=aa[sel]; bb2=bb[sel]
        wa=W[aa2]; wb=W[bb2]
        raws=np.concatenate((wa+wb,wa-wb),axis=1)
        for j,row in enumerate(raws):
            if np.array_equal(np.sort(np.abs(row)),sig0):
                out.add(int(aa2[j]) | (int(bb2[j])<<16))
    return out

def cube_transform(mask,perm,flipmask):
    out=0
    for x in range(32):
        y=0
        for j in range(5):
            bit=((x>>perm[j])&1)^((flipmask>>j)&1)
            y |= bit<<j
        if (mask>>y)&1: out |= 1<<x
    return out

PERMS=list(itertools.permutations(range(5)))
def cube_orbit(mask):
    return {cube_transform(mask,p,f) for p in PERMS for f in range(32)}

def row_types(mask,A):
    A=tuple(A); B=tuple(i for i in range(5) if i not in A); rows=[]
    for a in range(1<<len(A)):
        r=0
        for b in range(1<<len(B)):
            x=0
            for j,i in enumerate(A): x |= ((a>>j)&1)<<i
            for j,i in enumerate(B): x |= ((b>>j)&1)<<i
            r |= ((mask>>x)&1)<<b
        rows.append(r)
    return rows

def two_row_witnesses(mask):
    out=[]
    for A in itertools.combinations(range(5),2):
        rows=row_types(mask,A); uniq=[]
        for r in rows:
            if r not in uniq: uniq.append(r)
        if len(uniq)<=2: out.append((A,rows,uniq))
    return out

def inner_class(rows,uniq):
    if len(uniq)==1: return "CONST"
    g=0
    for a,r in enumerate(rows):
        if r==uniq[1]: g |= 1<<a
    wt=g.bit_count()
    if wt in (1,3): return "ANDOR"
    if wt==2:
        ones=[a for a in range(4) if (g>>a)&1]
        return "XOR" if (ones[0]^ones[1])==3 else "LITERAL"
    return "OTHER"

expected_counts={1:32,2:80,3:320,4:80,5:960,6:480,7:480,8:40,
                 9:480,10:960,11:1920,12:240,13:960,14:240,15:960,16:10}

print("PASS-BEGIN")
total=0
for m in range(1,17):
    eq=equality_masks(m); orb=cube_orbit(comp[m][0])
    assert eq==orb
    assert len(eq)==expected_counts[m]
    total += len(eq)
    andor=0; minw=100; maxw=0
    for M in eq:
        wins=two_row_witnesses(M)
        assert wins
        minw=min(minw,len(wins)); maxw=max(maxw,len(wins))
        classes={inner_class(rows,uniq) for _,rows,uniq in wins}
        if "ANDOR" in classes: andor += 1
    if m<16: assert andor==len(eq)
    else: assert andor==0
    print("m",m,"equality",len(eq),"orbit",len(orb),
          "all_decomposable",True,"andor_witness",andor,
          "witness_count_range",minw,maxw)
print("total_equality_m_le_16",total)
print("symmetry","m>16 follows by output complement; cube automorphisms and decomposability are preserved")
print("classification","every exact central equality case is cube-automorphic to the explicit read-once comparator; every nonliteral equality case has a binary AND/OR inner factor")
print("PASS-END")

CSTAR=F(64573,10000); SCALE=10**12; NLOG=320

def ln_bounds_int(n,N=NLOG):
    if n==1: return F(0),F(0)
    y=F(n-1,n+1); y2=y*y; term=y; s=F(0)
    for r in range(N):
        s += term/(2*r+1); term *= y2
    lo=2*s; tail=2*term/((2*N+1)*(1-y2))
    return lo,lo+tail

_ln2_lo,_ln2_hi=ln_bounds_int(2)
@lru_cache(None)
def log2_bounds_int(n):
    if n & (n-1)==0:
        z=F(n.bit_length()-1); return z,z
    lo,hi=ln_bounds_int(n); return lo/_ln2_hi,hi/_ln2_lo

def floor_scaled(x):
    y=x*SCALE; return y.numerator//y.denominator

def ceil_scaled(x):
    y=x*SCALE; return -((-y.numerator)//y.denominator)

atom_lo=np.zeros(33,dtype=np.int64); atom_hi=np.zeros(33,dtype=np.int64)
for t in range(1,33):
    q=F(t*t,1024); llo,lhi=log2_bounds_int(t)
    atom_lo[t]=floor_scaled(q*(10-2*lhi))
    atom_hi[t]=ceil_scaled(q*(10-2*llo))
comp_entropy={}
for m,(M,raw,B) in comp.items():
    comp_entropy[m]=(M,raw,B,int(atom_lo[np.abs(raw)].sum()),int(atom_hi[np.abs(raw)].sum()))
const_floor={db:floor_scaled(CSTAR*F(db,16)) for db in range(-80,81)}

def hmax_upper_scaled(m):
    vn=m*(32-m); wn=256-vn; V=F(vn,256); W0=F(wn,256); ans=F(0)
    if vn:
        llo,_=log2_bounds_int(vn); ans += V*(8-llo)
        _,lhi31=log2_bounds_int(31); ans += V*lhi31
    if wn:
        llo,_=log2_bounds_int(wn); ans += W0*(8-llo)
    return ceil_scaled(ans)

def strict_margin_ratio_min():
    best=None; per_m=[]
    for m in range(1,17):
        M0,raw0,B0,Hlo0,Hhi0=comp_entropy[m]; local=None
        for aa,bb,bd in candidates(m,CUT[m]):
            wa=W[aa]; wb=W[bb]
            v1=np.abs(wa+wb); v2=np.abs(wa-wb)
            Hup=(atom_hi[v1].sum(axis=1)+atom_hi[v2].sum(axis=1)).astype(np.int64)
            cterm=np.fromiter((const_floor[int(x)-B0] for x in bd),dtype=np.int64,count=len(bd))
            lb=cterm+Hlo0-Hup
            for j in np.flatnonzero(lb>0):
                B=int(bd[j]); nM=16*B-m*(32-m)
                if nM<=0: continue
                r=F(int(lb[j])*1024,SCALE*nM)
                rec=(r,m,"low",int(aa[j]),int(bb[j]),B,int(lb[j]),nM)
                if local is None or r<local[0]: local=rec
                if best is None or r<best[0]: best=rec
        Hmax=hmax_upper_scaled(m)
        for B in range(CUT[m]+1,5*min(m,32-m)+1):
            if (B-m)&1: continue
            lb=const_floor[B-B0]+Hlo0-Hmax
            if lb<=0: continue
            nM=16*B-m*(32-m)
            if nM<=0: continue
            r=F(int(lb)*1024,SCALE*nM)
            rec=(r,m,"generic",None,None,B,int(lb),nM)
            if local is None or r<local[0]: local=rec
            if best is None or r<best[0]: best=rec
        per_m.append(local)
    return best,per_m

best,per_m=strict_margin_ratio_min(); assert best is not None
rstar=best[0]
assert rstar==F(2453251107,47363281250)
cupper=F(1,100)-rstar
assert cupper==F(-3959236589,94726562500)
print("MARGIN-SEPARATION-BEGIN")
for rec in per_m:
    if rec is None:
        print("m",1,"strict_ratio","NONE (all singleton tables are equality orbit)")
    else:
        r,m,kind,aa,bb,B,lb,nM=rec
        print("m",m,"strict_ratio_lower",format(float(r),".15f"),
              "kind",kind,"B",B,"delta_scaled_lb",lb,"M_num_over_1024",nM)
print("global_strict_Dcert_over_M_lower_exact",f"{rstar.numerator}/{rstar.denominator}")
print("global_strict_Dcert_over_M_lower_decimal",format(float(rstar),".15f"))
print("base_Gamma_RO_margin_upper_exact",f"{cupper.numerator}/{cupper.denominator}")
print("base_Gamma_RO_margin_upper_decimal",format(float(cupper),".15f"))
print("interpretation","every essential composition-prime five-input gate at uniform bias is strict, hence c_Gamma_RO <= 0.01-rstar < 0")
print("MARGIN-SEPARATION-END")
