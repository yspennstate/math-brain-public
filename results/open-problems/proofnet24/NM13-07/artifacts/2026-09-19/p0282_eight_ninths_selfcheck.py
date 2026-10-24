from fractions import Fraction
from math import factorial, comb
from itertools import product

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

def b7_formula(j,mu):
    C=content(mu,1); S2=content(mu,2); S3=content(mu,3)
    S4=content(mu,4); S5=content(mu,5); S6=content(mu,6)
    return (-j**7+3*j**6-5*j**5+5*j**4-3*j**3+j**2-Fraction(j,7)
            +(-6*j**5+15*j**4-20*j**3+15*j**2-6*j+1)*C
            +(-15*j**4+30*j**3-30*j**2+15*j-3)*S2
            +(-20*j**3+30*j**2-20*j+5)*S3
            +(-15*j**2+15*j-5)*S4
            +(-6*j+3)*S5
            -S6)

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
        for q in range(ORDER+1):
            out[q]+=s*p[q]
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
        for q in range(ORDER+1):
            A[q]+=w*R2[q]
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
        -Fraction(j*(84*j**6+378*j**5-1470*j**4+399*j**3+2996*j**2-3591*j+1216),42),
    ]

def E(j,n):
    if j==0:
        return 1
    N=n-j
    assert N>=j
    return sum(fdim((N,)+mu)**2 for mu in parts(j))

def threshold8(j):
    n=max(2*j,1)
    while n**8 < (2**26)*(j+1)**9:
        n+=1
    return n

def threshold7(j):
    n=max(2*j,1)
    while n**7 < (2**24)*(j+1)**8:
        n+=1
    return n

# Direct finite self-check of the length-six star-transposition word count.
# Permutations are tuples of images on {0,...,m}; star center is m.
def compose(p,q):
    return tuple(p[q[i]] for i in range(len(p)))

def transposition_perm(size,a,b):
    p=list(range(size)); p[a],p[b]=p[b],p[a]; return tuple(p)

def star_return_count(m):
    size=m+1
    gens=[transposition_perm(size,a,m) for a in range(m)]
    ident=tuple(range(size))
    count=0
    for w in product(range(m), repeat=6):
        p=ident
        for g in w:
            p=compose(gens[g],p)
        if p==ident:
            count+=1
    return count

print("P0282 eight-ninths-window exact self-check")
print("checks: star-word identity counts; Plancherel E[S6]; E[C^2*S2]; exact B7; log(A_j) through n^-7; D7 curvature; exact Chen margins")
for m in range(1,6):
    got=star_return_count(m)
    expected=m*(5*m*m-5*m+1)
    assert got==expected, (m,got,expected)
    print(f"star_leaves={m} length6_identity_words={got} formula={expected}")

for j in range(1,MAXJ+1):
    ps=list(parts(j))
    W=sum(fdim(mu)**2 for mu in ps)
    assert W==factorial(j)

    sS6=sum(fdim(mu)**2*content(mu,6) for mu in ps)
    sC2S2=sum(fdim(mu)**2*content(mu,1)**2*content(mu,2) for mu in ps)
    ES6=Fraction(j*(j-1)*(15*j*j-35*j+16),12)
    EC2S2=Fraction(j*(j-1)*(j*j+3*j-8),4)
    assert sS6==factorial(j)*ES6
    assert sC2S2==factorial(j)*EC2S2

    J=comb(j,2)
    assert ES6==sum(Fraction(m*(5*m*m-5*m+1)) for m in range(j))
    assert EC2S2==J*J+6*comb(j,3)

    for mu in ps:
        assert bm_cols(7,j,mu)==b7_formula(j,mu), (j,mu)

    LA=log1(A_series(j))
    dc=dcoeffs(j)
    for q in range(1,8):
        assert LA[q]==dc[q], (j,q,LA[q],dc[q])

    n0=threshold8(j)
    old=threshold7(j)
    margin=E(j,n0)**2-E(j-1,n0)*E(j+1,n0)
    assert margin>0
    print(f"j={j} partitions={len(ps)} E_S6={ES6} E_C2S2={EC2S2} eight_ninths_threshold_n={n0} old_seven_eighths_threshold_n={old} source_margin_positive=True")

for j in range(1,100):
    f7=lambda r: dcoeffs(r)[7]
    curv=2*f7(j)-f7(j-1)-f7(j+1)
    expected=2*(42*j**5+135*j**4-280*j**3+192*j**2+53*j-67)
    shifted=2*(42*(j-1)**5+345*(j-1)**4+680*(j-1)**3+582*(j-1)**2+347*(j-1)+75)
    assert curv==expected==shifted
    assert curv>0

print("D7_discrete_curvature_identity=PASS")
print("D7_shifted_positive_coefficients=PASS")
print("analytic_tail_claim_used_in_report=tail_after_order7 <= 2^23*j^8/n^8 for n>=12j")
print("theorem_threshold_used_in_report=n^8 >= 2^26*(j+1)^9")
print("ALL_EXACT_CHECKS_PASS")
