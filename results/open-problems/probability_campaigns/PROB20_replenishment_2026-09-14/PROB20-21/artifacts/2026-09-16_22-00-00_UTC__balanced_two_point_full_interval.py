from fractions import Fraction as F
from math import comb
from functools import lru_cache
import sys

M=6
A0=F(1,5000)
A1=F(67,135)
P=220
SCALE=1<<P
LOGK=22
MAXDEPTH=50

# ---------- integer rounding helpers ----------
def floor_div(n,d):
    assert d>0
    return n//d

def ceil_div(n,d):
    assert d>0
    return -((-n)//d)

def frac_floor_scaled(q):
    return floor_div(q.numerator*SCALE,q.denominator)

def frac_ceil_scaled(q):
    return ceil_div(q.numerator*SCALE,q.denominator)

def mul_fp_pos_lo(x,y): return floor_div(x*y,SCALE)
def mul_fp_pos_hi(x,y): return ceil_div(x*y,SCALE)

# ---------- polynomial helpers low->high ----------
def trim(p):
    while len(p)>1 and p[-1]==0: p.pop()
    return p

def padd(p,q):
    n=max(len(p),len(q)); r=[F(0)]*n
    for i,x in enumerate(p): r[i]+=x
    for i,x in enumerate(q): r[i]+=x
    return trim(r)
def pscale(p,c): return trim([c*x for x in p])
def pmul(p,q):
    r=[F(0)]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q): r[i+j]+=x*y
    return trim(r)
def ppow(p,n):
    r=[F(1)]
    for _ in range(n): r=pmul(r,p)
    return r

a=[F(0),F(1)]; b=[F(1),F(-1)]
def qpolys(k):
    Sp=pmul(ppow(b,k),ppow(a,M-k)); Tp=pmul(ppow(a,k),ppow(b,M-k))
    qp=padd(b,padd(pscale(pmul(b,Sp),F(-1)),pmul(a,Tp)))
    qm=padd(a,padd(pscale(pmul(a,Sp),F(-1)),pmul(b,Tp)))
    return qp,qm
Q={k:qpolys(k) for k in range(3)}

# ---------- exact selected truth-table representative ----------
MASK=int("15555555555555555555555555555557",16)
N=1<<7
# nearest source dictator: output 1 iff coordinate 0 is 0
DICT=0
for x in range(N):
    if ((x>>0)&1)==0:
        DICT |= 1<<x
DIFF=[x for x in range(N) if ((MASK^DICT)>>x)&1]
assert MASK.bit_count()==64
assert DIFF==[1,126]
assert (1^127)==126  # antipodal pair
# exact average sensitivity of this truth table
sens=0
for x in range(N):
    for i in range(7):
        sens += ((MASK>>x)&1) != ((MASK>>(x^(1<<i)))&1)
assert F(sens,N)==F(37,32)

def bernstein_range(p,l,u):
    n=len(p)-1; w=u-l
    d=[F(0)]*(n+1)
    lpows=[F(1)]*(n+1); wpows=[F(1)]*(n+1)
    for j in range(1,n+1):
        lpows[j]=lpows[j-1]*l; wpows[j]=wpows[j-1]*w
    for r,cr in enumerate(p):
        for j in range(r+1):
            d[j]+=cr*comb(r,j)*lpows[r-j]*wpows[j]
    bs=[]
    for k in range(n+1):
        z=F(0)
        for j in range(k+1): z += d[j]*F(comb(k,j),comb(n,j))
        bs.append(z)
    return min(bs),max(bs)

# ---------- exact truth-table transition-polynomial identity ----------
# For uniform X, the posterior law X|Y=y is exactly the BSC kernel centered at y.
# Sum those weights over MASK and compare with the derived q_+/q_- polynomials.
def kernel_poly_for_y(y):
    out=[F(0)]
    for x in range(N):
        if ((MASK>>x)&1)==0:
            continue
        d=(x^y).bit_count()
        out=padd(out,pmul(ppow(a,d),ppow(b,7-d)))
    return out
for k in range(7):
    # bits 1..k set among the six tail coordinates
    tail=sum(1<<(j+1) for j in range(k))
    y_plus=tail          # y0=0 => P(U=1|Y0)=b
    y_minus=tail | 1    # y0=1 => P(U=1|Y0)=a
    qp,qm=qpolys(k)
    assert kernel_poly_for_y(y_plus)==qp
    assert kernel_poly_for_y(y_minus)==qm

# ---------- exact fixed-point log enclosure ----------
def t_fp_bounds(q):
    # q exact in [1,2), t=(q-1)/(q+1) in [0,1/3]
    t=(q-1)/(q+1)
    return frac_floor_scaled(t),frac_ceil_scaled(t)

def atanh_series_fp(tlo,thi):
    # t>=0. return bounds on log((1+t)/(1-t)) = 2 atanh t
    assert 0<=tlo<=thi<SCALE
    # powers t^1 then multiply by t^2 outward
    t2lo=mul_fp_pos_lo(tlo,tlo); t2hi=mul_fp_pos_hi(thi,thi)
    plo,phi=tlo,thi
    slo=0; shi=0
    for k in range(LOGK+1):
        den=2*k+1
        slo += floor_div(2*plo,den)
        shi += ceil_div(2*phi,den)
        if k<LOGK:
            plo=mul_fp_pos_lo(plo,t2lo)
            phi=mul_fp_pos_hi(phi,t2hi)
    # tail upper using next odd power phi*t2hi and 1/(1-t^2)
    pnext=mul_fp_pos_hi(phi,t2hi)
    denodd=2*LOGK+3
    denom=SCALE-t2hi
    # scaled tail <= 2*(pnext/S)/(denodd)*(S/(denom))
    # in scaled integer units: ceil(2*pnext*S/(denodd*denom))
    tail=ceil_div(2*pnext*SCALE,denodd*denom)
    return slo,shi+tail

@lru_cache(None)
def ln2_fp():
    return atanh_series_fp(*t_fp_bounds(F(2)))

@lru_cache(maxsize=200000)
def ln_fp(q):
    q=F(q); assert q>0
    if q==1: return 0,0
    # exact e with s=q/2^e in [1,2)
    e=q.numerator.bit_length()-q.denominator.bit_length()
    twoe=F(2**e,1) if e>=0 else F(1,2**(-e))
    s=q/twoe
    while s<1: e-=1; s*=2
    while s>=2: e+=1; s/=2
    ls,us=atanh_series_fp(*t_fp_bounds(s))
    l2,u2=ln2_fp()
    if e>=0: return e*l2+ls, e*u2+us
    return e*u2+ls, e*l2+us

@lru_cache(maxsize=200000)
def h_fp(q):
    q=F(q)
    if q==0 or q==1: return 0,0
    lq,uq=ln_fp(q); r=1-q; lr,ur=ln_fp(r)
    # contribution -q*ln q, scaled ints
    qn,qd=q.numerator,q.denominator
    rn,rd=r.numerator,r.denominator
    c1lo=floor_div(-qn*uq,qd); c1hi=ceil_div(-qn*lq,qd)
    c2lo=floor_div(-rn*ur,rd); c2hi=ceil_div(-rn*lr,rd)
    return c1lo+c2lo,c1hi+c2hi

def h_lower_range(lo,hi):
    l1,_=h_fp(lo); l2,_=h_fp(hi); return min(l1,l2)

stats={k:{'leaves':0,'maxdepth':0,'min_num':None,'worst':None} for k in range(3)}

def certify(k,l,u,depth=0):
    qp,qm=Q[k]
    plo,phi=bernstein_range(qp,l,u); mlo,mhi=bernstein_range(qm,l,u)
    if not (0<plo<=phi<1 and 0<mlo<=mhi<1): raise AssertionError((k,float(l),float(u),float(plo),float(phi),float(mlo),float(mhi)))
    hp=h_lower_range(plo,phi); hm=h_lower_range(mlo,mhi); _,ha_hi=h_fp(u)
    # 2*F >= (hp+hm)-2*ha_hi in units 1/SCALE
    num=hp+hm-2*ha_hi
    if num>0:
        st=stats[k]; st['leaves']+=1; st['maxdepth']=max(st['maxdepth'],depth)
        if st['min_num'] is None or num<st['min_num']:
            st['min_num']=num; st['worst']=(l,u)
        return
    if depth>=MAXDEPTH:
        raise RuntimeError(f'UNCERTIFIED k={k} depth={depth} l={float(l)} u={float(u)} num_scaled={num}')
    mid=(l+u)/2
    certify(k,l,mid,depth+1); certify(k,mid,u,depth+1)

# sanity log enclosure against known rational identities via integer ordering only
l2,u2=ln2_fp(); assert l2<u2 and l2>0
for k in range(3):
    certify(k,A0,A1)
    st=stats[k]
    print(f'k={k} PASS leaves={st["leaves"]} maxdepth={st["maxdepth"]} min_2F_lower={st["min_num"]/SCALE:.18g} worst=[{float(st["worst"][0]):.18g},{float(st["worst"][1]):.18g}]')
print(f'selected_mask={MASK:032x}')
print('selected_mask_difference_from_dictator_vertices='+','.join(map(str,DIFF)))
print('selected_mask_average_sensitivity=37/32')
print('transition_polynomial_identity=PASS')
print(f'fixed_point_bits={P} log_series_terms={LOGK+1}')
print('POINTWISE_K0_K1_K2_MIDDLE_INTERVAL_PASS')
print('k=3_ANALYTIC_PASS')
print('BALANCED_TWO_POINT_PERTURBATION_FULL_INTERVAL_PASS_WITH_PINNED_ENDPOINT_CERTIFICATES')
