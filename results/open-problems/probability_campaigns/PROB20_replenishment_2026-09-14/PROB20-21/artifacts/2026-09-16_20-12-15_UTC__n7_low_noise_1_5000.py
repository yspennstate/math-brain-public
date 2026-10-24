#!/usr/bin/env python3
from fractions import Fraction
from hashlib import sha256

NV=7
N=1<<NV
FULL=(1<<N)-1
EXPECTED_HASH='9caace4fb804076a20a55c2e0b9fb3e1f860a7a7629f788a9e42fe1c1e77a50d'
KLOG=70
A0=Fraction(1,5000)

def ln2_bounds():
    t=Fraction(1,3)
    z=Fraction(0)
    for k in range(KLOG+1):
        z += Fraction(2,2*k+1)*t**(2*k+1)
    rem=Fraction(2,2*KLOG+3)*t**(2*KLOG+3)/(1-t*t)
    return z,z+rem
LN2_LO,LN2_HI=ln2_bounds()

def ln_bounds(q):
    q=Fraction(q); assert q>0
    if q==1: return Fraction(0),Fraction(0)
    e=q.numerator.bit_length()-q.denominator.bit_length()
    scale=Fraction(2**e,1) if e>=0 else Fraction(1,2**(-e))
    s=q/scale
    while s<1:
        s*=2; e-=1
    while s>=2:
        s/=2; e+=1
    t=(s-1)/(s+1)
    z=Fraction(0)
    for k in range(KLOG+1):
        z += Fraction(2,2*k+1)*t**(2*k+1)
    rem=Fraction(2,2*KLOG+3)*t**(2*KLOG+3)/(1-t*t)
    if e>=0:
        return z+e*LN2_LO,z+rem+e*LN2_HI
    return z+e*LN2_HI,z+rem+e*LN2_LO

def h_bounds(q):
    q=Fraction(q)
    if q in (0,1): return Fraction(0),Fraction(0)
    if q==Fraction(1,2): return LN2_LO,LN2_HI
    lq,uq=ln_bounds(q)
    r=1-q
    lr,ur=ln_bounds(r)
    return -q*uq-r*ur, -q*lq-r*lr

# Source pair-compressed family S_7.
succ=[0]*N
for i in range(NV):
    for base in range(N):
        if ((base>>i)&1)==0:
            succ[base] |= 1 << (base|(1<<i))
for i in range(NV):
    for j in range(i+1,NV):
        for base in range(N):
            if ((base>>i)&1)==0 and ((base>>j)&1)==0:
                succ[base|(1<<j)] |= 1 << (base|(1<<i))
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
        l=z&-z
        v=l.bit_length()-1
        z-=l
        pred[v] |= 1<<u
pm=[pred[v]|(1<<v) for v in range(N)]
sm=[succ[v]|(1<<v) for v in range(N)]
S=[]
def rec(inc,exc):
    undec=FULL & ~(inc|exc)
    if not undec:
        S.append(inc); return
    best=-1; score=-1; z=undec
    while z:
        l=z&-z
        v=l.bit_length()-1
        z-=l
        sc=(pm[v]&undec).bit_count()+(sm[v]&undec).bit_count()
        if sc>score:
            score=sc; best=v
    if pm[best]&exc==0:
        rec(inc|pm[best],exc)
    if sm[best]&inc==0:
        rec(inc,exc|sm[best])
rec(0,0)
S=sorted(set(S))
assert len(S)==44315
payload=''.join(f'{m:032x}\n' for m in S).encode()
assert sha256(payload).hexdigest()==EXPECTED_HASH

# D(A) = {x: complement(x) not in A}, known to preserve source compression.
def dual(m):
    allbits=(1<<NV)-1
    out=0
    for x in range(N):
        if ((m>>(x^allbits))&1)==0:
            out |= 1<<x
    return out
Sset=set(S)
reps=[]
fixed=0
for m in S:
    d=dual(m)
    assert d in Sset
    if m==d: fixed += 1
    if m<=d: reps.append(m)
assert fixed==135 and len(reps)==22225

def is_dictator(m):
    for i in range(NV):
        ok0=ok1=True
        for x in range(N):
            v=(m>>x)&1
            xi=(x>>i)&1
            if v!=xi: ok1=False
            if v!=(1-xi): ok0=False
            if not ok0 and not ok1: break
        if ok0 or ok1: return True
    return False

# Precompute logarithms of local degrees and endpoint quantities.
ln_d_hi={}
for d in range(1,NV+1):
    _,ln_d_hi[d]=ln_bounds(d)
L0_lo,_=ln_bounds(1/A0)
_,ln7_hi=ln_bounds(7)
assert L0_lo>ln7_hi
c0=(1-A0)**6

# For f, let d_y be sensitive degree, AS=E d_y, Elog=E[d_y log d_y].
# For alpha<=A0, e_y=P(f(X)!=f(y)|Y=y) obeys
# d_y alpha(1-alpha)^6 <= e_y <= 1-(1-alpha)^7 < 1/2.
# Hence h(e_y)>=h(d_y alpha c)>=d_y alpha c log(1/(d_y alpha c))
# >= d_y alpha c (log(1/alpha)-log d_y).
# Therefore
# D_f(alpha) >= base + alpha R_f(alpha),
# base=ln2-h(p),
# R_f=(c AS-1)L-c Elog-1.
#
# If c AS-1>0 and L>ln7, then R_f'(alpha)<0.
# If R>=0 the lower bound is >=base. Once R<0, alpha*R is decreasing
# because (alpha R)'=R+alpha R'<0. Thus the minimum of this lower bound
# on [0,A0] occurs either at alpha=0 (base>=0) or alpha=A0.
#
# Low-sensitivity functions with c0 AS<=1 are handled instead by
# D>=ln2-h(alpha)-h(p), checked exactly at A0.
# Pair compression transfers the S7 checks to every seven-bit Boolean f.

assert 1-(1-A0)**7 < Fraction(1,2)

min_coeff=None; min_coeff_mask=None
min_lb=None; min_lb_mask=None
min_R=None; min_R_mask=None
min_AS=None; min_AS_mask=None
checked=0
balanced=0
for m in reps:
    k=m.bit_count()
    if k in (0,N) or is_dictator(m):
        continue
    checked += 1
    p=Fraction(min(k,N-k),N)
    if p==Fraction(1,2):
        base_lo=Fraction(0)
        balanced += 1
    else:
        _,hp_hi=h_bounds(p)
        base_lo=LN2_LO-hp_hi
        assert base_lo>0

    counts=[0]*(NV+1)
    sdeg=0
    for x in range(N):
        fx=(m>>x)&1
        d=0
        for i in range(NV):
            d += fx != ((m>>(x^(1<<i)))&1)
        counts[d]+=1
        sdeg+=d
    AS=Fraction(sdeg,N)
    if min_AS is None or AS<min_AS:
        min_AS,min_AS_mask=AS,m

    coeff=c0*AS-1
    if min_coeff is None or coeff<min_coeff:
        min_coeff,min_coeff_mask=coeff,m

    if coeff <= 0:
        _,ha_hi=h_bounds(A0)
        entropy_only_lo=base_lo-ha_hi
        assert entropy_only_lo>0
        lb_lo=entropy_only_lo
        R_lo=None
    else:
        E_hi=Fraction(0)
        for d,cnt in enumerate(counts):
            if d:
                E_hi += Fraction(cnt*d,N)*ln_d_hi[d]

        R_lo=coeff*L0_lo-c0*E_hi-1
        lb_lo=base_lo+A0*R_lo
        assert lb_lo>0
        if min_R is None or R_lo<min_R:
            min_R,min_R_mask=R_lo,m

    if min_lb is None or lb_lo<min_lb:
        min_lb,min_lb_mask=lb_lo,m

print('PROB20-21 N=7 LOW-NOISE EXTENSION CERTIFICATE: PASS')
print('S7_count',len(S),'hash',EXPECTED_HASH,'dual_reps',len(reps),'dual_fixed',fixed)
print('alpha_interval','[0,1/5000]')
print('nontrivial_nondictator_reps_checked',checked,'balanced_reps',balanced)
print('endpoint_e_upper_lt_half',float(1-(1-A0)**7))
print('ln5000_minus_ln7_lower',float(L0_lo-ln7_hi))
print('min_AS',min_AS,'mask',f'{min_AS_mask:032x}')
print('min_cAS_minus_1_all_nondictators',min_coeff,'approx',float(min_coeff),'mask',f'{min_coeff_mask:032x}')
print('min_endpoint_R_lower_approx',float(min_R),'mask',f'{min_R_mask:032x}')
print('min_endpoint_defect_lower_nat_approx',float(min_lb),'mask',f'{min_lb_mask:032x}')
print('NOTE constants and dictators are trivial/equality cases; pair compression transfers S7 coverage to all Boolean functions.')
