from fractions import Fraction
from math import factorial, comb

MAXJ=12
ORDER=7

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
        ans += -Fraction(a**m-(a-h)**m,m)
    return ans

def b6_formula(j,mu):
    C=content(mu,1); S2=content(mu,2); S3=content(mu,3); S4=content(mu,4); S5=content(mu,5)
    return (j*(-j**5+Fraction(5,2)*j**4-Fraction(10,3)*j**3+Fraction(5,2)*j**2-j+Fraction(1,6))
            +(-5*j**4+10*j**3-10*j**2+5*j-1)*C
            +(-10*j**3+15*j**2-10*j+Fraction(5,2))*S2
            +(-10*j**2+10*j-Fraction(10,3))*S3
            +(Fraction(5,2)-5*j)*S4
            -S5)

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
        -Fraction(j*(6*j**5+15*j**4-65*j**3+51*j**2+13*j-19),3),
    ]

def E(j,n):
    if j==0: return 1
    N=n-j
    assert N>=j
    return sum(fdim((N,)+mu)**2 for mu in parts(j))

def threshold7(j):
    n=max(2*j,1)
    while n**7 < (2**24)*(j+1)**8: n+=1
    return n

def threshold6(j):
    n=max(2*j,1)
    while n**6 < (2**21)*(j+1)**7: n+=1
    return n

print('P0282 seven-eighths-window exact self-check')
print('checks: Plancherel mass; E[S2^2]; E[C*S3]; exact B6 identity; exact log(A_j) coefficients through n^-6; D6 curvature; exact Chen margin at theorem threshold')
for j in range(1,MAXJ+1):
    ps=list(parts(j)); W=sum(fdim(mu)**2 for mu in ps)
    assert W==factorial(j)
    sS2sq=sum(fdim(mu)**2*content(mu,2)**2 for mu in ps)
    sCS3=sum(fdim(mu)**2*content(mu,1)*content(mu,3) for mu in ps)
    ES2sq=Fraction(j*(j-1)*(3*j*j+j-8),12)
    ECS3=Fraction(j*(j-1)*(2*j-3),2)
    assert sS2sq==factorial(j)*ES2sq
    assert sCS3==factorial(j)*ECS3
    for mu in ps:
        assert bm_cols(6,j,mu)==b6_formula(j,mu)
    LA=log1(A_series(j)); dc=dcoeffs(j)
    for q in range(1,7):
        assert LA[q]==dc[q], (j,q,LA[q],dc[q])
    n0=threshold7(j); old=threshold6(j)
    margin=E(j,n0)**2-E(j-1,n0)*E(j+1,n0)
    assert margin>0
    print(f'j={j} partitions={len(ps)} E_S2sq={ES2sq} E_C_S3={ECS3} seven_eighths_threshold_n={n0} old_six_sevenths_threshold_n={old} source_margin_positive=True')

for j in range(1,100):
    f6=lambda r: -Fraction(r*(6*r**5+15*r**4-65*r**3+51*r**2+13*r-19),3)
    curv=2*f6(j)-f6(j-1)-f6(j+1)
    expected=Fraction(4*(45*j**4+75*j**3-150*j**2+114*j-23),3)
    assert curv==expected
    assert curv>0
print('D6_discrete_curvature_identity=PASS')
print('ALL_EXACT_CHECKS_PASS')
