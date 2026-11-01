#!/usr/bin/env python3
"""
PROB20-21 n=7 exact symmetry/extremizer/counterexample checker.

Finite claims certified here:
  * reconstruct source pair-compressed family S_7 exactly;
  * direct-check every singleton/pair lex-compressed section;
  * certify |S_7|=44315;
  * certify the exact involution D(A)={x: 1-x notin A} preserves S_7;
  * enumerate its 22225 orbits and 135 fixed points;
  * compute exact distance-to-dictator distribution and identify the unique
    distance-one full-symmetry class inside S_7 (two D-related representatives);
  * compute exact finite Fourier/sensitivity invariants;
  * exhaustive rigorous no-counterexample search at alpha=1/4 over one
    representative from every D-orbit, with exact transition numerators and
    rational logarithm enclosures.

This DOES NOT certify the entire alpha interval and therefore does NOT move
the frozen fleet metric beyond n=6.
"""
from fractions import Fraction
from hashlib import sha256
from collections import Counter
import numpy as np

NV=7
N=1<<NV
FULL=(1<<N)-1

# ---------- source S_n reconstruction ----------
succ=[0]*N
for i in range(NV):
    for base in range(N):
        if ((base>>i)&1)==0:
            succ[base] |= 1 << (base|(1<<i))
for i in range(NV):
    for j in range(i+1,NV):
        for base in range(N):
            if ((base>>i)&1)==0 and ((base>>j)&1)==0:
                # Courtade-Kumar lex section order 00 < 01 < 10 < 11:
                # membership is an initial segment, so 10 -> 01.
                u=base|(1<<j)
                v=base|(1<<i)
                succ[u] |= 1<<v

# transitive closure of implication poset
for k in range(N):
    bk=1<<k
    sk=succ[k]
    for i in range(N):
        if succ[i]&bk:
            succ[i] |= sk

pred=[0]*N
for u in range(N):
    z=succ[u]
    while z:
        l=z & -z
        v=l.bit_length()-1
        pred[v] |= 1<<u
        z-=l
pm=[pred[v]|(1<<v) for v in range(N)]
sm=[succ[v]|(1<<v) for v in range(N)]

S=[]
def rec(inc,exc):
    undec=FULL & ~(inc|exc)
    if not undec:
        S.append(inc)
        return
    best=None; score=-1
    z=undec
    while z:
        l=z & -z; v=l.bit_length()-1; z-=l
        sc=(pm[v]&undec).bit_count()+(sm[v]&undec).bit_count()
        if sc>score:
            score=sc; best=v
    if pm[best]&exc == 0:
        rec(inc|pm[best],exc)
    if sm[best]&inc == 0:
        rec(inc,exc|sm[best])
rec(0,0)
S=sorted(set(S))

assert len(S)==44315
# Vectorized direct verification of every generating singleton/pair implication.
membership_full=np.zeros((len(S),N),dtype=np.int8)
for r,m in enumerate(S):
    for x in range(N):
        membership_full[r,x]=(m>>x)&1
for u in range(N):
    z=succ[u]
    # It suffices (and is stronger) to verify every transitive implication
    # encoded by the reconstructed poset: initial-set membership requires u>=v.
    while z:
        l=z & -z; v=l.bit_length()-1; z-=l
        assert np.all(membership_full[:,u] >= membership_full[:,v])
Sset=set(S)
payload=''.join(f'{m:032x}\n' for m in S).encode()
S_hash=sha256(payload).hexdigest()

# ---------- exact compressed-family dual symmetry ----------
def dual(m):
    # output complement after flipping all input bits
    out=0
    allbits=(1<<NV)-1
    for x in range(N):
        if ((m>>(x^allbits))&1)==0:
            out |= 1<<x
    return out

duals=[dual(m) for m in S]
assert all(d in Sset for d in duals)
dual_map=dict(zip(S,duals))
assert all(dual_map[dual_map[m]]==m for m in S)
fixed=[m for m,d in zip(S,duals) if d==m]
reps=[m for m,d in zip(S,duals) if m<=d]
assert len(fixed)==135
assert len(reps)==22225
assert 2*len(reps)-len(fixed)==len(S)
assert all(m.bit_count()==N//2 for m in fixed)

# ---------- dictator orbit / extremal structure ----------
dictators=[]
for i in range(NV):
    for bit in (0,1):
        m=0
        for x in range(N):
            if ((x>>i)&1)==bit:
                m |= 1<<x
        dictators.append(m)
dictator_set=set(dictators)

def dist_dict(m):
    return min((m^d).bit_count() for d in dictators)

dist_hist=Counter(dist_dict(m) for m in S)
dist1=[m for m in S if dist_dict(m)==1]
assert len(dist1)==2
assert dual_map[dist1[0]]==dist1[1]
assert sorted(m.bit_count() for m in dist1)==[63,65]

# ---------- exact Fourier/sensitivity invariants ----------
# Vectorize exact integer Walsh level-one numerators. For f=+1 on A, -1 off A,
# sum_x f(x) chi_i(x) = 2 sum_{x in A} chi_i(x), because sum_x chi_i=0.
sizes=membership_full.sum(axis=1,dtype=np.int64)
chi=np.empty((N,NV),dtype=np.int8)
for x in range(N):
    for i in range(NV):
        chi[x,i]=1 if ((x>>i)&1)==0 else -1
c1=membership_full.astype(np.int64) @ chi.astype(np.int64)
hat_num=2*c1
mu_num=2*sizes-N
# delta numerator over N^2:
delta_num=N*N - mu_num*mu_num - np.sum(hat_num*hat_num,axis=1,dtype=np.int64)
valid=np.array([
    (m not in (0,FULL)) and (m not in dictator_set)
    for m in S
],dtype=bool)
min_delta_num=int(delta_num[valid].min())
assert Fraction(min_delta_num,N*N)==Fraction(15,512)
min_delta_masks=[S[i] for i in range(len(S)) if valid[i] and int(delta_num[i])==min_delta_num]
assert len(min_delta_masks)==4
assert sorted(m.bit_count() for m in min_delta_masks)==[1,63,65,127]
min_delta=Fraction(min_delta_num,N*N)

# Average sensitivity only needs balanced nondictators (1006 after dictator removal).
def avg_sensitivity(m):
    s=0
    for x in range(N):
        for i in range(NV):
            s += ((m>>x)&1) != ((m>>(x^(1<<i)))&1)
    return Fraction(s,N)
balanced_nd=[m for m in S if m.bit_count()==N//2 and m not in dictator_set]
sensvals=[(avg_sensitivity(m),m) for m in balanced_nd]
min_bal_sens=min(v for v,_ in sensvals)
min_bal_masks=[m for v,m in sensvals if v==min_bal_sens]
assert min_bal_sens==Fraction(37,32)
assert len(min_bal_masks)==1

# ---------- rigorous rational logarithm / entropy enclosures ----------
# For s in [1,2), t=(s-1)/(s+1) in [0,1/3]:
# log s = 2 sum_{k>=0} t^(2k+1)/(2k+1).
# Tail after K is <= 2 t^(2K+3)/((2K+3)(1-t^2)).
SERIES_K=25

def log2_bounds():
    t=Fraction(1,3)
    s=Fraction(0)
    for k in range(SERIES_K+1):
        s += Fraction(2,2*k+1)*t**(2*k+1)
    rem=Fraction(2,2*SERIES_K+3)*t**(2*SERIES_K+3)/(1-t*t)
    return s,s+rem
LN2_LO,LN2_HI=log2_bounds()

def ln_frac_bounds(q):
    q=Fraction(q)
    assert q>0
    if q==1: return Fraction(0),Fraction(0)
    e=q.numerator.bit_length()-q.denominator.bit_length()
    twoe=Fraction(2**e,1) if e>=0 else Fraction(1,2**(-e))
    s=q/twoe
    while s<1:
        e-=1; s*=2
    while s>=2:
        e+=1; s/=2
    t=(s-1)/(s+1)
    a=Fraction(0)
    for k in range(SERIES_K+1):
        a += Fraction(2,2*k+1)*t**(2*k+1)
    rem=Fraction(2,2*SERIES_K+3)*t**(2*SERIES_K+3)/(1-t*t)
    ls,us=a,a+rem
    if e>=0:
        return e*LN2_LO+ls, e*LN2_HI+us
    return e*LN2_HI+ls, e*LN2_LO+us

def entropy_bounds(q):
    q=Fraction(q)
    if q in (0,1): return Fraction(0),Fraction(0)
    lq,uq=ln_frac_bounds(q)
    r=1-q
    lr,ur=ln_frac_bounds(r)
    return -q*uq-r*ur, -q*lq-r*lr

# Convert rational enclosures to a common exact fixed-point lattice.
FP_BITS=100
SCALE=1<<FP_BITS
def floor_frac(x): return x.numerator//x.denominator
def ceil_frac(x): return -((-x.numerator)//x.denominator)
def scaled_entropy(num,den):
    lo,hi=entropy_bounds(Fraction(int(num),int(den)))
    return floor_frac(lo*SCALE),ceil_frac(hi*SCALE)

LN2_LO_I=floor_frac(LN2_LO*SCALE)
LN2_HI_I=ceil_frac(LN2_HI*SCALE)

# ---------- exact counterexample-first scan at alpha=1/4 ----------
# D-orbit reduction is source-valid because D is an objective symmetry and
# preserves S_7. We nevertheless retain full S_7 counts above.
A=1; B=4
DEN=B**NV
kernel=np.empty((N,N),dtype=np.int64)
for x in range(N):
    for y in range(N):
        d=(x^y).bit_count()
        kernel[x,y]=(A**d)*((B-A)**(NV-d))

membership=np.zeros((len(reps),N),dtype=np.int8)
for r,m in enumerate(reps):
    for x in range(N):
        membership[r,x]=(m>>x)&1
qnums=membership.astype(np.int64) @ kernel
assert int(qnums.min())>=0 and int(qnums.max())<=DEN

unique_q=sorted(set(int(v) for v in qnums.ravel()))
hcache={q:scaled_entropy(q,DEN) for q in unique_q}
hp_cache={k:scaled_entropy(k,N) for k in set(m.bit_count() for m in reps)}

# Store rigorous [lower,upper] defect intervals on the common scale SCALE*N.
gap_interval={}
min_gap_num=None; worst=None; negative=0; inconclusive=0
H_ALPHA_LO,H_ALPHA_HI=scaled_entropy(A,B)
for r,m in enumerate(reps):
    sum_h_lo=sum(hcache[int(q)][0] for q in qnums[r])
    sum_h_hi=sum(hcache[int(q)][1] for q in qnums[r])
    hp_lo,hp_hi=hp_cache[m.bit_count()]
    gap_lo=N*(LN2_LO_I-H_ALPHA_HI-hp_hi)+sum_h_lo
    gap_hi=N*(LN2_HI_I-H_ALPHA_LO-hp_lo)+sum_h_hi
    gap_interval[m]=(gap_lo,gap_hi)
    if m in (0,FULL) or m in dictator_set:
        continue
    if gap_lo<0:
        negative += 1
    if gap_lo<=0:
        inconclusive += 1
    if min_gap_num is None or gap_lo<min_gap_num:
        min_gap_num=gap_lo; worst=m

assert negative==0
assert inconclusive==0
assert worst in dist1
assert min_gap_num>0

# ---------- B24: exact lexicographic extremizer check at alpha=1/4 ----------
# Global lex order has coordinate 0 most significant, matching the source's
# two-coordinate section convention 00<01<10<11 for i<j.
lex_vertices=sorted(range(N),key=lambda x: tuple((x>>i)&1 for i in range(NV)))
def lex_mask(k):
    m=0
    for x in lex_vertices[:k]:
        m |= 1<<x
    return m
assert all(lex_mask(k) in Sset for k in range(N+1))

strict_size_wins=0
min_lex_separation=None
min_lex_sep_size=None
for k in range(1,N//2):
    lm=lex_mask(k)
    lc=min(lm,dual_map[lm])
    assert lc in gap_interval
    lex_hi=gap_interval[lc][1]
    others=[]
    for m,(lo,hi) in gap_interval.items():
        if min(m.bit_count(),N-m.bit_count())==k and m!=lc:
            others.append(lo)
    if others:
        sep=min(others)-lex_hi
        assert sep>0
        strict_size_wins += 1
        if min_lex_separation is None or sep<min_lex_separation:
            min_lex_separation=sep; min_lex_sep_size=k
    else:
        strict_size_wins += 1

# Balanced size: source lex set is the compressed dictator and has exact zero
# defect; every other balanced compressed representative has positive lower gap.
balanced_lex=lex_mask(N//2)
assert balanced_lex in dictator_set
balanced_other_los=[
    lo for m,(lo,hi) in gap_interval.items()
    if m.bit_count()==N//2 and m not in dictator_set
]
assert balanced_other_los and min(balanced_other_los)>0
assert strict_size_wins==63

print("PROB20-21 N7 SYMMETRY/EXTREMIZER EXACT CHECK: PASS")
print("metric_before=6")
print("metric_after=6")
print("metric_movement=NO_MOVEMENT")
print("S7_count=",len(S),sep='')
print("S7_sorted_mask_sha256=",S_hash,sep='')
print("balanced_S7_count=",sum(m.bit_count()==64 for m in S),sep='')
print("dual_fixed_count=",len(fixed),sep='')
print("dual_orbit_count=",len(reps),sep='')
print("distance1_count=",len(dist1),sep='')
print("distance1_masks=",','.join(f'{m:032x}' for m in dist1),sep='')
print("distance1_sizes=",','.join(str(m.bit_count()) for m in dist1),sep='')
print("min_higher_level_mass=",f"{min_delta.numerator}/{min_delta.denominator}",sep='')
print("min_higher_level_mass_masks=",','.join(f'{m:032x}' for m in min_delta_masks),sep='')
print("min_balanced_avg_sensitivity=",f"{min_bal_sens.numerator}/{min_bal_sens.denominator}",sep='')
print("min_balanced_sensitivity_mask=",f"{min_bal_masks[0]:032x}",sep='')
print("alpha_scan=1/4")
print("alpha_scan_dual_representatives=",len(reps),sep='')
print("alpha_scan_nontrivial_negative=0")
print("alpha_scan_nontrivial_inconclusive=0")
print("alpha_scan_unique_posterior_rationals=",len(unique_q),sep='')
print("alpha_scan_min_gap_lower_nats=",float(Fraction(min_gap_num,SCALE*N)),sep='')
print("alpha_scan_worst_mask=",f"{worst:032x}",sep='')
print("alpha_scan_worst_distance_to_dictator=",dist_dict(worst),sep='')
print("lex_extremizer_sizes_strict=63")
print("lex_balanced_dictator_exact_equality=PASS")
print("lex_min_strict_separation_lower_nats=",float(Fraction(min_lex_separation,SCALE*N)),sep='')
print("lex_min_strict_separation_size=",min_lex_sep_size,sep='')
print("balanced_nondictator_min_gap_lower_nats=",float(Fraction(min(balanced_other_los),SCALE*N)),sep='')
print("log_series_terms=",SERIES_K+1,sep='')
print("fixed_point_bits=",FP_BITS,sep='')
print("NOTE=single-noise exhaustive certification is diagnostic only; entire interval n=7 remains open")
