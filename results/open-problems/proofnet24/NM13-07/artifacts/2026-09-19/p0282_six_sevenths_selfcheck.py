from fractions import Fraction
from math import factorial, comb

MAXJ=12
ORDER=6

def parts(n,maxv=None):
    if n==0:
        yield (); return
    if maxv is None or maxv>n: maxv=n
    for a in range(maxv,0,-1):
        for r in parts(n-a,a):
            yield (a,)+r

def fdim(part):
    n=sum(part); hp=1
    for r,row in enumerate(part):
        for c in range(row):
            below=sum(1 for rr in range(r+1,len(part)) if part[rr]>c)
            hp *= (row-c)+below
    return factorial(n)//hp

def content(mu,p=1):
    return sum((c-r)**p for r,row in enumerate(mu) for c in range(row))

def cols(mu):
    m=mu[0] if mu else 0
    return [sum(1 for r in mu if r>=c) for c in range(1,m+1)]

def bm_cols(m,j,mu):
    ans=Fraction(0)
    for c,h in enumerate(cols(mu),1):
        a=j+c-1
        for r in range(1,m+1):
            ans += Fraction((-1)**r*comb(m-1,r-1),r)*(h**r)*(a**(m-r))
    return ans

def b5_formula(j,mu):
    C=content(mu,1); S2=content(mu,2); S3=content(mu,3); S4=content(mu,4)
    return (-j**5+2*j**4-2*j**3+j**2-Fraction(j,5)
            +(-4*j**3+6*j**2-4*j+1)*C
            +(-6*j**2+6*j-2)*S2
            +(-4*j+2)*S3-S4)

def mul(a,b):
    out=[Fraction(0) for _ in range(ORDER+1)]
    for i in range(ORDER+1):
        for k in range(ORDER+1-i):
            out[i+k]+=a[i]*b[k]
    return out

def inv(a):
    assert a[0]!=0
    out=[Fraction(0) for _ in range(ORDER+1)]
    out[0]=1/a[0]
    for n in range(1,ORDER+1):
        out[n]=-sum(a[k]*out[n-k] for k in range(1,n+1))/a[0]
    return out

def log1(a):
    assert a[0]==1
    u=a[:]; u[0]=0
    out=[Fraction(0) for _ in range(ORDER+1)]
    p=[Fraction(0)]*(ORDER+1); p[0]=1
    for m in range(1,ORDER+1):
        p=mul(p,u)
        s=Fraction(1 if m%2 else -1,m)
        for q in range(ORDER+1): out[q]+=s*p[q]
    return out

def A_series(j):
    A=[Fraction(0) for _ in range(ORDER+1)]
    for mu in parts(j):
        w=Fraction(fdim(mu)**2,factorial(j))
        R=[Fraction(1)]+[Fraction(0)]*ORDER
        for c,h in enumerate(cols(mu),1):
            a=j+c-1
            num=[Fraction(1),Fraction(-a)]+[Fraction(0)]*(ORDER-1)
            den=[Fraction(1),Fraction(h-a)]+[Fraction(0)]*(ORDER-1)
            R=mul(R,mul(num,inv(den)))
        R2=mul(R,R)
        for q in range(ORDER+1): A[q]+=w*R2[q]
    return A

def dcoeffs(j):
    return [
        Fraction(0),
        Fraction(-2*j),
        Fraction(-2*j*j+j),
        Fraction(-2*j**3+j*j)+Fraction(j,3),
        Fraction(-2*j**4)+Fraction(7*j*j,2)-2*j,
        Fraction(-2*j**5-2*j**4)+Fraction(32*j**3,3)-9*j*j+Fraction(29*j,15),
    ]

def E(j,n):
    if j==0: return 1
    N=n-j
    assert N>=j
    return sum(fdim((N,)+mu)**2 for mu in parts(j))

def threshold6(j):
    n=max(2*j,1)
    while n**6 < (2**21)*(j+1)**7: n+=1
    return n

def threshold5(j):
    n=max(2*j,1)
    while n**5 < (2**10)*(j+1)**6: n+=1
    return n

print('P0282 six-sevenths-window exact self-check')
print('checks: Plancherel mass; E[C]=0; E[S2]=binom(j,2); E[S3]=0; E[C^2]=binom(j,2); E[C*S2]=0; E[S4]=j(j-1)(4j-5)/6; exact B5 identity; exact log(A_j) coefficients through n^-5; D5 discrete curvature; exact Chen margin at theorem threshold')
for j in range(1,MAXJ+1):
    ps=list(parts(j)); W=sum(fdim(mu)**2 for mu in ps)
    assert W==factorial(j)
    J=j*(j-1)//2
    sC=sum(fdim(mu)**2*content(mu,1) for mu in ps)
    sS2=sum(fdim(mu)**2*content(mu,2) for mu in ps)
    sS3=sum(fdim(mu)**2*content(mu,3) for mu in ps)
    sC2=sum(fdim(mu)**2*content(mu,1)**2 for mu in ps)
    sCS2=sum(fdim(mu)**2*content(mu,1)*content(mu,2) for mu in ps)
    sS4=sum(fdim(mu)**2*content(mu,4) for mu in ps)
    S4=Fraction(j*(j-1)*(4*j-5),6)
    assert sC==0
    assert sS2==factorial(j)*J
    assert sS3==0
    assert sC2==factorial(j)*J
    assert sCS2==0
    assert sS4==factorial(j)*S4
    for mu in ps:
        assert bm_cols(5,j,mu)==b5_formula(j,mu)
    LA=log1(A_series(j)); dc=dcoeffs(j)
    for q in range(1,6):
        assert LA[q]==dc[q], (j,q,LA[q],dc[q])
    n0=threshold6(j); old=threshold5(j)
    margin=E(j,n0)**2-E(j-1,n0)*E(j+1,n0)
    assert margin>0
    print(f'j={j} partitions={len(ps)} E_S4={S4} six_sevenths_threshold_n={n0} old_five_sixths_threshold_n={old} source_margin_positive=True')

for j in range(1,80):
    f2=lambda r: Fraction(-2*r*r+r)
    f3=lambda r: Fraction(-2*r**3+r*r)+Fraction(r,3)
    f4=lambda r: Fraction(-2*r**4)+Fraction(7*r*r,2)-2*r
    f5=lambda r: Fraction(-2*r**5-2*r**4)+Fraction(32*r**3,3)-9*r*r+Fraction(29*r,15)
    assert 2*f2(j)-f2(j-1)-f2(j+1)==4
    assert 2*f3(j)-f3(j-1)-f3(j+1)==12*j-2
    assert 2*f4(j)-f4(j-1)-f4(j+1)==24*j*j-3
    assert 2*f5(j)-f5(j-1)-f5(j+1)==40*j**3+24*j**2-44*j+22
    assert 40*j**3+24*j**2-44*j+22>0
print('D5_discrete_curvature_identity=PASS')
print('ALL_EXACT_CHECKS_PASS')
