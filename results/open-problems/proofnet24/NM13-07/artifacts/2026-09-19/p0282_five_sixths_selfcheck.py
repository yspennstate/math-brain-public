from fractions import Fraction
from math import factorial

MAXJ=12
ORDER=5

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

def b2_cols(j,mu):
    h=cols(mu)
    return -sum(hc*(j+c-1) for c,hc in enumerate(h,1)) + Fraction(sum(hc*hc for hc in h),2)

def b3_cols(j,mu):
    h=cols(mu)
    return (-sum(hc*(j+c-1)**2 for c,hc in enumerate(h,1))
            +sum(hc*hc*(j+c-1) for c,hc in enumerate(h,1))
            -Fraction(sum(hc**3 for hc in h),3))

def b4_cols(j,mu):
    h=cols(mu)
    return (-sum(hc*(j+c-1)**3 for c,hc in enumerate(h,1))
            +Fraction(3,2)*sum(hc**2*(j+c-1)**2 for c,hc in enumerate(h,1))
            -sum(hc**3*(j+c-1) for c,hc in enumerate(h,1))
            +Fraction(sum(hc**4 for hc in h),4))

def b2_formula(j,mu):
    return -j*j+Fraction(j,2)-content(mu,1)

def b3_formula(j,mu):
    return -j**3+j**2-Fraction(j,3)+(1-2*j)*content(mu,1)-content(mu,2)

def b4_formula(j,mu):
    return (-j**4+Fraction(3,2)*j**3-j**2+Fraction(j,4)
            +(-3*j*j+3*j-1)*content(mu,1)
            +(-3*j+Fraction(3,2))*content(mu,2)
            -content(mu,3))

def E(j,n):
    if j==0: return 1
    N=n-j
    assert N>=j
    return sum(fdim((N,)+mu)**2 for mu in parts(j))

def threshold5(j):
    n=max(2*j,1)
    while n**5 < 1024*(j+1)**6: n+=1
    return n

def threshold4(j):
    n=max(2*j,1)
    while n**4 < 256*(j+1)**5: n+=1
    return n

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
    powu=[Fraction(0)]*(ORDER+1); powu[0]=1
    for m in range(1,ORDER+1):
        powu=mul(powu,u)
        s=Fraction(1 if m%2 else -1,m)
        for q in range(ORDER+1): out[q]+=s*powu[q]
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
        Fraction(-2*j**3+j*j,1)+Fraction(j,3),
        Fraction(-2*j**4,1)+Fraction(7*j*j,2)-2*j,
    ]

print('P0282 five-sixths-window exact self-check')
print('checks: Plancherel mass, E[C]=0, E[S2]=binom(j,2), E[S3]=0, E[C^2]=binom(j,2), exact B2/B3/B4 identities, exact log(A_j) coefficients through n^-4, exact Chen margin at new threshold')
for j in range(1,MAXJ+1):
    ps=list(parts(j)); W=sum(fdim(mu)**2 for mu in ps)
    assert W==factorial(j)
    Csum=sum(fdim(mu)**2*content(mu,1) for mu in ps)
    S2sum=sum(fdim(mu)**2*content(mu,2) for mu in ps)
    S3sum=sum(fdim(mu)**2*content(mu,3) for mu in ps)
    C2sum=sum(fdim(mu)**2*content(mu,1)**2 for mu in ps)
    J=j*(j-1)//2
    assert Csum==0
    assert S2sum==factorial(j)*J
    assert S3sum==0
    assert C2sum==factorial(j)*J
    for mu in ps:
        assert b2_cols(j,mu)==b2_formula(j,mu)
        assert b3_cols(j,mu)==b3_formula(j,mu)
        assert b4_cols(j,mu)==b4_formula(j,mu)
    LA=log1(A_series(j))
    dc=dcoeffs(j)
    for q in range(1,5):
        assert LA[q]==dc[q], (j,q,LA[q],dc[q])
    n0=threshold5(j); old=threshold4(j)
    ejm=E(j-1,n0); ej=E(j,n0); ejp=E(j+1,n0)
    margin=ej*ej-ejm*ejp
    assert margin>0
    print(f'j={j} partitions={len(ps)} E_C=0 E_S2={J} E_S3=0 E_C2={J} five_sixths_threshold_n={n0} old_four_fifths_threshold_n={old} source_margin_positive=True')

for j in range(1,50):
    f2=lambda r: -2*r*r+r
    f3=lambda r: Fraction(-2*r**3+r*r,1)+Fraction(r,3)
    f4=lambda r: Fraction(-2*r**4,1)+Fraction(7*r*r,2)-2*r
    assert 2*f2(j)-f2(j-1)-f2(j+1)==4
    assert 2*f3(j)-f3(j-1)-f3(j+1)==12*j-2
    assert 2*f4(j)-f4(j-1)-f4(j+1)==24*j*j-3
print('D4_discrete_curvature_identity=PASS')
print('ALL_EXACT_CHECKS_PASS')
