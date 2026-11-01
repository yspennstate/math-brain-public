#!/usr/bin/env python3
from fractions import Fraction as F
from math import comb, factorial, isqrt
from itertools import combinations_with_replacement

# HARD7-05 exact checker: Jensen-Craig equal-angle minorant, N=8.
# All decisive comparisons use exact rational arithmetic plus rigorous
# square-root/arcsine/trigonometric enclosures. No path simulation.

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

DROOT=10**8
def sqrt_interval(x):
    assert x>0
    m=isqrt((DROOT*DROOT*x.numerator)//x.denominator)
    lo,hi=F(m,DROOT),F(m+1,DROOT)
    assert lo*lo<=x<hi*hi
    return lo,hi

NASIN=8
def asin_point_interval_pos(x):
    assert 0<=x<1
    s=F(0)
    for n in range(NASIN+1):
        a=F(comb(2*n,n),4**n*(2*n+1))
        s += a*x**(2*n+1)
    u=s+x**(2*NASIN+3)/(1-x*x)
    return s,u

def asin_point_interval(x):
    if x>=0: return asin_point_interval_pos(x)
    lo,hi=asin_point_interval_pos(-x); return -hi,-lo

def asin_interval(xlo,xhi):
    lo,_=asin_point_interval(xlo); _,hi=asin_point_interval(xhi); return lo,hi

pi_lo=F(333,106); pi_hi=F(355,113)
inv4pi_lo=F(1,4)/pi_hi; inv4pi_hi=F(1,4)/pi_lo

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

# Alternating Taylor enclosures on the angles used below.  With NPAIRS=3:
# sin lower ends at -x^11/11!, sin upper at +x^9/9!;
# cos lower ends at -x^10/10!, cos upper at +x^8/8!.
NPAIRS=3
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
    n=(x.numerator*den+x.denominator-1)//x.denominator
    return F(n,den)

# Craig-Jensen hierarchy.  theta_j=j*pi/(2N).  The singular first cell is
# discarded.  On cell j>=1 Jensen gives mass 1/(2N) at mean rate
# beta_bar_j=N/pi*(cot theta_j-cot theta_{j+1}).  The following constructs
# rigorous rational upper bounds beta_hat_j >= beta_bar_j.
N=8
RATE_DEN=100000
rate_upper_exact=[]; rates=[]
for j in range(1,N):
    alo=F(j,2*N)*pi_lo
    salo,_=sin_bounds(alo); _,cahi=cos_bounds(alo)
    cot_a_hi=cahi/salo
    if j+1==N:
        cot_b_lo=F(0)
    else:
        bhi=F(j+1,2*N)*pi_hi
        _,sbhi=sin_bounds(bhi); cblo,_=cos_bounds(bhi)
        cot_b_lo=cblo/sbhi
    mean_hi=F(N,1)/pi_lo*(cot_a_hi-cot_b_lo)
    assert mean_hi>0
    bhat=ceil_frac(mean_hi,RATE_DEN)
    assert bhat>=mean_hi
    rate_upper_exact.append(mean_hi); rates.append(bhat)

# Certified Slepian grid inherited from the preceding HARD7-05 covariance lemma.
r=F(287831,500000); z=r*r
def Qpoly(x): return 8*x**5+16*x**4+8*x**3-20*x*x-7*x+4
assert 2-3*z*z-2*z**3-2*z**4>0
assert 40*z**4+64*z**3+24*z*z-7<0
assert Qpoly(z)>0

# Six-cycle AR(1) loop and even-site conditional reduction.
sig2=1-r*r; diag=(1+r*r)/sig2; off=-r/sig2
Q6=[[F(0) for _ in range(6)] for _ in range(6)]
for i in range(6):
    Q6[i][i]=diag; Q6[i][(i+1)%6]=off; Q6[i][(i-1)%6]=off
S6=mat_inv(Q6); even=(0,2,4)
C=[[S6[i][j] for j in even] for i in even]; Cinv=mat_inv(C)
assert C[0][0]==C[1][1]==C[2][2]
assert C[0][1]==C[0][2]==C[1][2]
fac=r*r/(1-r**4)
vecs=((1,1,0),(0,1,1),(1,0,1))
B=[[[F(v[i]*v[j]) for j in range(3)] for i in range(3)] for v in vecs]

weight=F(1,2*N)
coeff=[F(1)]+[-weight for _ in rates]
rate=[F(0)]+rates

def tilt_interval(opts):
    A=[[F(0) for _ in range(3)] for _ in range(3)]
    for h,opt in enumerate(opts):
        if not opt: continue
        sc=rate[opt]*fac
        for i in range(3):
            for j in range(3): A[i][j]+=sc*B[h][i][j]
    M=mat_add(eye(3),mat_scale(mat_mul(C,A),F(2))); d=det(M); assert d>0
    plo,phi=sqrt_interval(F(1)/d)
    Ct=mat_inv(mat_add(Cinv,mat_scale(A,F(2))))
    olo,ohi=orth3_interval(Ct)
    return plo*olo,phi*ohi

P6_hi=F(0); terms=0; classes=0
for opts in combinations_with_replacement(range(N),3):
    if opts[0]==opts[2]: mult=1
    elif opts[0]==opts[1] or opts[1]==opts[2]: mult=3
    else: mult=6
    cf=F(mult)*coeff[opts[0]]*coeff[opts[1]]*coeff[opts[2]]
    lo,hi=tilt_interval(opts)
    P6_hi += cf*(hi if cf>=0 else lo)
    terms+=mult; classes+=1
assert terms==N**3
trace_hi=P6_hi/(1-r**6)

# theta=1427/10000: 24 theta=4281/1250.  Therefore trace<r^(4281/1250)
# is certified by the pure integer comparison below.
coarse=F(15083,100000)
target=F(1427,10000)
assert trace_hi<coarse
assert 24*target==F(4281,1250)
assert coarse**1250 < r**4281
width=F(1,4)-target

print('N =',N,'atoms =',N-1,'weight =',weight)
print('r =',r,'=',float(r))
print('rate bounds (rounded up to 1e-5):')
for j,(mhi,bh) in enumerate(zip(rate_upper_exact,rates),start=1):
    print(j,bh,float(bh),'rigorous_mean_upper~',float(mhi),'ok=',bh>=mhi)
print('classes =',classes,'terms =',terms)
print('P6 upper enclosure ~',float(P6_hi))
print('trace K^6 upper enclosure ~',float(trace_hi))
print('coarse trace upper =',coarse,'=',float(coarse))
print('power_certificate =',coarse**1250 < r**4281)
print('certified theta lower =',target,'=',float(target))
print('new bracket width =',width,'=',float(width))
print('ALL_EXACT_CHECKS_PASS = True')
