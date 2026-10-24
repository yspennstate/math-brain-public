#!/usr/bin/env python3
from fractions import Fraction as F
from math import comb, isqrt
from itertools import combinations_with_replacement

# Exact checker for HARD7-05 run: sharpened six-cycle certificate.
# Analytic inputs isolated in report: Slepian, Polya erf inequality,
# centered trivariate Gaussian orthant formula, 333/106 < pi < 355/113.

def mat_inv(A):
    n=len(A); M=[[F(A[i][j]) for j in range(n)]+[F(int(i==j)) for j in range(n)] for i in range(n)]
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

DROOT=10**9
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

# Push r much closer to the exact covariance-comparison boundary while
# retaining a fully rational admissibility proof.
r=F(287831,500000)          # 0.575662
beta=F(191,300)
z=r*r
assert F(212,333)<beta      # because pi > 333/106 => 2/pi < 212/333

def Ppoly(x): return 2+2*x-3*x*x-2*x**3-2*x**4
def Qpoly(x): return 8*x**5+16*x**4+8*x**3-20*x*x-7*x+4
assert 2-3*z*z-2*z**3-2*z**4>0
assert 40*z**4+64*z**3+24*z*z-7<0
assert Qpoly(z)>0

sig2=1-r*r; diag=(1+r*r)/sig2; off=-r/sig2
Q6=[[F(0) for _ in range(6)] for _ in range(6)]
for i in range(6):
    Q6[i][i]=diag; Q6[i][(i+1)%6]=off; Q6[i][(i-1)%6]=off
S6=mat_inv(Q6); even=(0,2,4); C=[[S6[i][j] for j in even] for i in even]; Cinv=mat_inv(C)
assert C[0][0]==C[1][1]==C[2][2]
assert C[0][1]==C[0][2]==C[1][2]
fac=r*r/(1-r**4)
vecs=((1,1,0),(0,1,1),(1,0,1))
B=[]
for v in vecs: B.append([[F(v[i]*v[j]) for j in range(3)] for i in range(3)])

def tilt_interval(ks):
    A=[[F(0) for _ in range(3)] for _ in range(3)]
    for h,k in enumerate(ks):
        if not k: continue
        sc=beta*F(k)*fac
        for i in range(3):
            for j in range(3): A[i][j]+=sc*B[h][i][j]
    M=mat_add(eye(3),mat_scale(mat_mul(C,A),F(2))); d=det(M); assert d>0
    plo,phi=sqrt_interval(F(1)/d)
    Ct=mat_inv(mat_add(Cinv,mat_scale(A,F(2))))
    olo,ohi=orth3_interval(Ct)
    return plo*olo,phi*ohi

def catalan(n): return comb(2*n,n)//(n+1)
m=13
a=[F(1)]+[-F(catalan(k-1),4**k) for k in range(1,m+1)]
assert sum((-a[k] for k in range(1,m+1)),F(0))<F(1,2)
P6_hi=F(0); terms=0; classes=0
for ks in combinations_with_replacement(range(m+1),3):
    if ks[0]==ks[2]: mult=1
    elif ks[0]==ks[1] or ks[1]==ks[2]: mult=3
    else: mult=6
    cf=F(mult)*a[ks[0]]*a[ks[1]]*a[ks[2]]
    lo,hi=tilt_interval(ks)
    P6_hi += cf*(hi if cf>=0 else lo)
    terms+=mult; classes+=1
assert terms==(m+1)**3
trace_hi=P6_hi/(1-r**6)
coarse=F(15145,100000)
assert trace_hi<coarse
# target theta = 14241/100000. 24 theta = 42723/12500.
target=F(14241,100000)
assert 24*target == F(42723,12500)
assert coarse**12500 < r**42723
width=F(1,4)-target

print('r =',r,'=',float(r))
print('beta =',beta,'=',float(beta))
print('Q(z) > 0 =',Qpoly(z)>0,'Q(z) ~',float(Qpoly(z)))
print('m =',m,'classes =',classes,'terms =',terms)
print('P6 upper enclosure ~',float(P6_hi))
print('trace K^6 upper enclosure ~',float(trace_hi))
print('coarse trace upper =',coarse,'=',float(coarse))
print('power_certificate =',coarse**12500 < r**42723)
print('certified theta lower =',target,'=',float(target))
print('new bracket width =',width,'=',float(width))
print('ALL_EXACT_CHECKS_PASS = True')
