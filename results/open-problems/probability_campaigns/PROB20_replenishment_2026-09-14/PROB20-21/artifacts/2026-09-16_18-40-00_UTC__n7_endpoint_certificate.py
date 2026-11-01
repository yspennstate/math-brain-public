#!/usr/bin/env python3
from fractions import Fraction
from hashlib import sha256

NV=7
N=1<<NV
FULL=(1<<N)-1
EXPECTED_HASH='9caace4fb804076a20a55c2e0b9fb3e1f860a7a7629f788a9e42fe1c1e77a50d'
KLOG=55

def ln2_bounds():
    t=Fraction(1,3); z=Fraction(0)
    for k in range(KLOG+1): z += Fraction(2,2*k+1)*t**(2*k+1)
    rem=Fraction(2,2*KLOG+3)*t**(2*KLOG+3)/(1-t*t)
    return z,z+rem
LN2_LO,LN2_HI=ln2_bounds()

def ln_bounds(q):
    q=Fraction(q); assert q>0
    if q==1: return Fraction(0),Fraction(0)
    e=q.numerator.bit_length()-q.denominator.bit_length()
    scale=Fraction(2**e,1) if e>=0 else Fraction(1,2**(-e))
    s=q/scale
    while s<1: s*=2; e-=1
    while s>=2: s/=2; e+=1
    t=(s-1)/(s+1); z=Fraction(0)
    for k in range(KLOG+1): z += Fraction(2,2*k+1)*t**(2*k+1)
    rem=Fraction(2,2*KLOG+3)*t**(2*KLOG+3)/(1-t*t)
    if e>=0: return z+e*LN2_LO,z+rem+e*LN2_HI
    return z+e*LN2_HI,z+rem+e*LN2_LO

def h_bounds(q):
    q=Fraction(q)
    if q in (0,1): return Fraction(0),Fraction(0)
    lq,uq=ln_bounds(q); r=1-q; lr,ur=ln_bounds(r)
    return -q*uq-r*ur, -q*lq-r*lr

# Source pair-compressed family S_7.
succ=[0]*N
for i in range(NV):
    for base in range(N):
        if ((base>>i)&1)==0: succ[base] |= 1 << (base|(1<<i))
for i in range(NV):
    for j in range(i+1,NV):
        for base in range(N):
            if ((base>>i)&1)==0 and ((base>>j)&1)==0:
                succ[base|(1<<j)] |= 1 << (base|(1<<i))
for k in range(N):
    bk=1<<k; sk=succ[k]
    for i in range(N):
        if succ[i]&bk: succ[i] |= sk
pred=[0]*N
for u in range(N):
    z=succ[u]
    while z:
        l=z&-z; v=l.bit_length()-1; z-=l; pred[v] |= 1<<u
pm=[pred[v]|(1<<v) for v in range(N)]
sm=[succ[v]|(1<<v) for v in range(N)]
S=[]
def rec(inc,exc):
    undec=FULL & ~(inc|exc)
    if not undec: S.append(inc); return
    best=-1; score=-1; z=undec
    while z:
        l=z&-z; v=l.bit_length()-1; z-=l
        sc=(pm[v]&undec).bit_count()+(sm[v]&undec).bit_count()
        if sc>score: score=sc; best=v
    if pm[best]&exc==0: rec(inc|pm[best],exc)
    if sm[best]&inc==0: rec(inc,exc|sm[best])
rec(0,0)
S=sorted(set(S))
assert len(S)==44315
payload=''.join(f'{m:032x}\n' for m in S).encode()
assert sha256(payload).hexdigest()==EXPECTED_HASH

# D symmetry count as a continuity sanity check, but no coverage reduction is needed here.
def dual(m):
    allbits=(1<<NV)-1; out=0
    for x in range(N):
        if ((m>>(x^allbits))&1)==0: out |= 1<<x
    return out
Sset=set(S)
duals=[dual(m) for m in S]
assert all(d in Sset for d in duals)
fixed=sum(m==d for m,d in zip(S,duals))
reps=sum(m<=d for m,d in zip(S,duals))
assert (fixed,reps)==(135,22225)

# Dictator detection.
def is_dictator(m):
    for i in range(NV):
        for bit in (0,1):
            ok=True
            for x in range(N):
                if (((m>>x)&1) != (((x>>i)&1)==bit)):
                    ok=False; break
            if ok: return True
    return False

# ---------- LOW NOISE ----------
a0=Fraction(1,1<<17)
# biased case: by output complement p<=63/128
_,ha_hi=h_bounds(a0)
_,hp_hi=h_bounds(Fraction(63,128))
biased_gap_lo=LN2_LO-ha_hi-hp_hi
assert biased_gap_lo>0

# balanced nondictators: exact local degree profile.
c0=(1-a0)**6
l0_lo=17*LN2_LO
_,ln7_hi=ln_bounds(7)
assert l0_lo-ln7_hi>0
balanced=[m for m in S if m.bit_count()==64 and not is_dictator(m)]
assert len(balanced)==1006
min_AS=None; min_AS_mask=None
min_margin=None; min_margin_mask=None
for m in balanced:
    counts=[0]*(NV+1)
    sdeg=0
    for x in range(N):
        fx=(m>>x)&1
        d=0
        for i in range(NV): d += fx != ((m>>(x^(1<<i)))&1)
        counts[d]+=1; sdeg+=d
    AS=Fraction(sdeg,N)
    if min_AS is None or AS<min_AS: min_AS,min_AS_mask=AS,m
    E_hi=Fraction(0)
    for d,cnt in enumerate(counts):
        if d:
            _,ld_hi=ln_bounds(d)
            E_hi += Fraction(cnt*d,N)*ld_hi
    coeff=c0*AS-1
    assert coeff>0
    # Since AS*L-E >= AS*(L-ln 7)>0, the bracket is increasing in c;
    # since coeff>0 it is increasing in L. Therefore c0,L0 are worst.
    margin=coeff*l0_lo-c0*E_hi-1
    assert margin>0
    if min_margin is None or margin<min_margin:
        min_margin,min_margin_mask=margin,m
assert min_AS==Fraction(37,32)

# ---------- HIGH NOISE ----------
r0=Fraction(1,135)
M=N-1
# Coordinate half masks for exact level-one Walsh coefficients.
half1=[]
for i in range(NV):
    mm=0
    for x in range(N):
        if (x>>i)&1: mm |= 1<<x
    half1.append(mm)

min_delta=None; min_delta_mask=None
min_L=None; min_L_mask=None
min_sq=None; min_sq_mask=None
for m in S:
    if m in (0,FULL) or is_dictator(m): continue
    k=m.bit_count()
    mu_num=2*k-N
    mu=Fraction(mu_num,N)
    V=1-mu*mu
    W1=Fraction(0)
    for i in range(NV):
        ones=(m&half1[i]).bit_count()
        zeros=k-ones
        c=zeros-ones
        hi=Fraction(2*c,N)
        W1 += hi*hi
    Delta=V-W1
    assert Delta>0
    L=(1-r0*r0)*Delta-M*r0*r0*V
    sq=L*L-4*mu*mu*r0*r0*M*V
    assert L>0 and sq>0
    if min_delta is None or Delta<min_delta: min_delta,min_delta_mask=Delta,m
    if min_L is None or L<min_L: min_L,min_L_mask=L,m
    if min_sq is None or sq<min_sq: min_sq,min_sq_mask=sq,m
assert min_delta==Fraction(15,512)

print('PROB20-21 N=7 ENDPOINT CERTIFICATE: PASS')
print('S7_count',len(S),'hash',EXPECTED_HASH,'dual_reps',reps)
print('low_noise_alpha0',a0)
print('biased_low_noise_gap_lower_nat',float(biased_gap_lo))
print('balanced_count',len(balanced),'min_AS',min_AS,'mask',f'{min_AS_mask:032x}')
print('balanced_low_noise_min_normalized_margin_lower',float(min_margin),'mask',f'{min_margin_mask:032x}')
print('high_noise_rho0',r0,'alpha_start',Fraction(1-r0,2))
print('high_noise_min_Delta',min_delta,'mask',f'{min_delta_mask:032x}')
print('high_noise_min_L',min_L,'mask',f'{min_L_mask:032x}')
print('high_noise_min_square',min_sq,'mask',f'{min_sq_mask:032x}')
print('middle_remaining','[1/131072, 67/135]')
