#!/usr/bin/env python3
from fractions import Fraction as F
from math import comb, factorial, isqrt
from itertools import combinations_with_replacement

# HARD7-05 exact checker, 2026-09-19.
# Nonuniform Craig-Jensen partition + range-reduced arcsine enclosures.
# All theorem-deciding comparisons are exact integer/rational arithmetic.

DROOT = 10**8
NATAN = 8
NPAIRS = 4
RATE_DEN = 10**6


def mat_inv(A):
    n=len(A)
    M=[[F(A[i][j]) for j in range(n)]+[F(int(i==j)) for j in range(n)] for i in range(n)]
    for c in range(n):
        p=next(i for i in range(c,n) if M[i][c])
        if p!=c: M[c],M[p]=M[p],M[c]
        pv=M[c][c]; M[c]=[x/pv for x in M[c]]
        for i in range(n):
            if i!=c and M[i][c]:
                q=M[i][c]; M[i]=[M[i][j]-q*M[c][j] for j in range(2*n)]
    return [row[n:] for row in M]


def mat_mul(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),F(0)) for j in range(len(B[0]))] for i in range(len(A))]

def mat_add(A,B): return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def mat_scale(A,c): return [[c*x for x in row] for row in A]
def eye(n): return [[F(int(i==j)) for j in range(n)] for i in range(n)]


def det(A):
    n=len(A); M=[[F(x) for x in row] for row in A]; ans=F(1)
    for c in range(n):
        p=next((i for i in range(c,n) if M[i][c]),None)
        if p is None: return F(0)
        if p!=c: M[c],M[p]=M[p],M[c]; ans=-ans
        pv=M[c][c]; ans*=pv
        for i in range(c+1,n):
            q=M[i][c]/pv
            for j in range(c+1,n): M[i][j]-=q*M[c][j]
    return ans


def sqrt_interval(x):
    assert x>0
    m=isqrt((DROOT*DROOT*x.numerator)//x.denominator)
    lo,hi=F(m,DROOT),F(m+1,DROOT)
    assert lo*lo<=x<hi*hi
    return lo,hi


def atan_series_bounds(x, m=NATAN):
    if x<0:
        lo,hi=atan_series_bounds(-x,m)
        return -hi,-lo
    assert 0<=x<=F(1,2)
    s=F(0)
    for k in range(m+1):
        s += F((-1)**k,2*k+1)*x**(2*k+1)
    nxt=F((-1)**(m+1),2*(m+1)+1)*x**(2*(m+1)+1)
    return min(s,s+nxt),max(s,s+nxt)


def atan_recip_bounds(q,m):
    return atan_series_bounds(F(1,q),m)

# Machin: pi = 16 atan(1/5) - 4 atan(1/239).
a5=atan_recip_bounds(5,16)
a239=atan_recip_bounds(239,4)
pi_lo=16*a5[0]-4*a239[1]
pi_hi=16*a5[1]-4*a239[0]
assert pi_lo < pi_hi


def atan_point_interval(t):
    if t<0:
        lo,hi=atan_point_interval(-t); return -hi,-lo
    if t<=F(1,2):
        return atan_series_bounds(t)
    if t<=2:
        u=(t-1)/(t+1)
        ulo,uhi=atan_series_bounds(u)
        return pi_lo/F(4)+ulo, pi_hi/F(4)+uhi
    alo,ahi=atan_series_bounds(1/t)
    return pi_lo/F(2)-ahi, pi_hi/F(2)-alo


def asin_point_interval(x):
    if x<0:
        lo,hi=asin_point_interval(-x); return -hi,-lo
    assert 0<=x<1
    if x==0: return F(0),F(0)
    slo,shi=sqrt_interval(1-x*x)
    tlo=x/shi; thi=x/slo
    lo,_=atan_point_interval(tlo)
    _,hi=atan_point_interval(thi)
    return lo,hi


def asin_interval(xlo,xhi):
    lo,_=asin_point_interval(xlo)
    _,hi=asin_point_interval(xhi)
    return lo,hi

inv4pi_lo=F(1,4)/pi_hi
inv4pi_hi=F(1,4)/pi_lo


def orth3_interval(C):
    aa=[]
    for i,j in ((0,1),(0,2),(1,2)):
        slo,shi=sqrt_interval(C[i][i]*C[j][j]); c=C[i][j]
        if c>=0: rlo,rhi=c/shi,c/slo
        else: rlo,rhi=c/slo,c/shi
        assert -1<rlo<=rhi<1
        aa.append(asin_interval(rlo,rhi))
    Slo=sum((x[0] for x in aa),F(0)); Shi=sum((x[1] for x in aa),F(0))
    vals=(Slo*inv4pi_lo,Slo*inv4pi_hi,Shi*inv4pi_lo,Shi*inv4pi_hi)
    return F(1,8)+min(vals),F(1,8)+max(vals)


def sin_bounds(x):
    Klo=2*NPAIRS-1; Kup=2*NPAIRS-2
    slo=sum((F((-1)**k)*x**(2*k+1)/F(factorial(2*k+1)) for k in range(Klo+1)),F(0))
    shi=sum((F((-1)**k)*x**(2*k+1)/F(factorial(2*k+1)) for k in range(Kup+1)),F(0))
    assert 0<slo<=shi
    return slo,shi


def cos_bounds(x):
    Klo=2*NPAIRS-1; Kup=2*NPAIRS-2
    clo=sum((F((-1)**k)*x**(2*k)/F(factorial(2*k)) for k in range(Klo+1)),F(0))
    chi=sum((F((-1)**k)*x**(2*k)/F(factorial(2*k)) for k in range(Kup+1)),F(0))
    assert clo<=chi
    return clo,chi


def ceil_frac(x,den):
    return F((x.numerator*den+x.denominator-1)//x.denominator,den)

# Rational multiples of pi/2. [0,14/250] is the only discarded Craig cell.
fracs=[F(14,250),F(28,250),F(42,250),F(57,250),F(72,250),F(87,250),
       F(105,250),F(127,250),F(152,250),F(186,250),F(218,250),F(1)]
weights=[]; rates=[]; mean_upper=[]
for af,bf in zip(fracs[:-1],fracs[1:]):
    delta=bf-af
    alo=af*pi_lo/F(2)
    salo,_=sin_bounds(alo); _,cahi=cos_bounds(alo)
    cot_a_hi=cahi/salo
    if bf==1:
        cot_b_lo=F(0)
    else:
        bhi=bf*pi_hi/F(2)
        _,sbhi=sin_bounds(bhi); cblo,_=cos_bounds(bhi)
        cot_b_lo=cblo/sbhi
    mh=(cot_a_hi-cot_b_lo)/(pi_lo*delta)
    assert mh>0
    mean_upper.append(mh)
    rates.append(ceil_frac(mh,RATE_DEN))
    weights.append(delta/F(2))

# Source-valid Slepian grid retained from the prior HARD7-05 covariance proof.
r=F(287831,500000); z=r*r
Q=lambda x: 8*x**5+16*x**4+8*x**3-20*x*x-7*x+4
assert 2-3*z*z-2*z**3-2*z**4>0
assert 40*z**4+64*z**3+24*z*z-7<0
assert Q(z)>0

# Six-cycle killed-AR(1) loop and 3-dimensional conditional reduction.
sig2=1-r*r; diag=(1+r*r)/sig2; off=-r/sig2
Q6=[[F(0) for _ in range(6)] for _ in range(6)]
for i in range(6):
    Q6[i][i]=diag; Q6[i][(i+1)%6]=off; Q6[i][(i-1)%6]=off
S6=mat_inv(Q6); even=(0,2,4)
C=[[S6[i][j] for j in even] for i in even]; Cinv=mat_inv(C)
fac=r*r/(1-r**4)
vecs=((1,1,0),(0,1,1),(1,0,1))
B=[[[F(v[i]*v[j]) for j in range(3)] for i in range(3)] for v in vecs]
coeff=[F(1)]+[-w for w in weights]
rate=[F(0)]+rates
n=len(coeff)


def tilt_interval(opts):
    A=[[F(0) for _ in range(3)] for _ in range(3)]
    for h,opt in enumerate(opts):
        if not opt: continue
        sc=rate[opt]*fac
        for i in range(3):
            for j in range(3): A[i][j]+=sc*B[h][i][j]
    d=det(mat_add(eye(3),mat_scale(mat_mul(C,A),F(2))))
    assert d>0
    plo,phi=sqrt_interval(F(1)/d)
    Ct=mat_inv(mat_add(Cinv,mat_scale(A,F(2))))
    olo,ohi=orth3_interval(Ct)
    return plo*olo,phi*ohi

P6_hi=F(0); classes=0; terms=0
for opts in combinations_with_replacement(range(n),3):
    if opts[0]==opts[2]: mult=1
    elif opts[0]==opts[1] or opts[1]==opts[2]: mult=3
    else: mult=6
    cf=F(mult)*coeff[opts[0]]*coeff[opts[1]]*coeff[opts[2]]
    lo,hi=tilt_interval(opts)
    P6_hi += cf*(hi if cf>=0 else lo)
    classes+=1; terms+=mult
assert terms==n**3
trace_hi=P6_hi/(1-r**6)

# Certify theta >= 143066/10^6.
target=F(143066,1000000)
coarse=F(15014436,100000000)
assert trace_hi < coarse
exp=24*target
assert exp==F(214599,62500)
assert coarse**62500 < r**214599
width=F(1,4)-target

print('pi interval width ~',float(pi_hi-pi_lo))
print('discarded Craig mass =',fracs[0]/2,'=',float(fracs[0]/2))
print('retained atoms =',len(rates),'options =',n)
print('weights =',[str(w) for w in weights])
print('rate bounds =',[str(x) for x in rates])
print('all rate majorizations =',all(b>=m for b,m in zip(rates,mean_upper)))
print('classes =',classes,'terms =',terms)
print('trace K^6 upper enclosure ~',float(trace_hi))
print('coarse trace upper =',coarse,'=',float(coarse))
print('power_certificate =',coarse**62500 < r**214599)
print('certified theta lower =',target,'=',float(target))
print('new bracket width =',width,'=',float(width))
print('ALL_EXACT_CHECKS_PASS = True')
