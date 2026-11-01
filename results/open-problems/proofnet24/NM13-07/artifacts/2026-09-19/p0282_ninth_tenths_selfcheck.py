from fractions import Fraction
from math import factorial, comb
from itertools import product
from collections import Counter

MAXJ=12
ORDER=8

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

def b8_formula(j,mu):
    C=content(mu,1); S2=content(mu,2); S3=content(mu,3); S4=content(mu,4)
    S5=content(mu,5); S6=content(mu,6); S7=content(mu,7)
    return (
        -j**8 + Fraction(7,2)*j**7 - 7*j**6 + Fraction(35,4)*j**5 - 7*j**4
        + Fraction(7,2)*j**3 - j**2 + Fraction(j,8)
        +(-7*j**6+21*j**5-35*j**4+35*j**3-21*j**2+7*j-1)*C
        +(-21*j**5+Fraction(105,2)*j**4-70*j**3+Fraction(105,2)*j**2-21*j+Fraction(7,2))*S2
        +(-35*j**4+70*j**3-70*j**2+35*j-7)*S3
        +(-35*j**3+Fraction(105,2)*j**2-35*j+Fraction(35,4))*S4
        +(-21*j**2+21*j-7)*S5
        +(-7*j+Fraction(7,2))*S6
        -S7
    )

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
        -Fraction(j*(24*j**7+168*j**6-574*j**5-546*j**4+3761*j**3-4990*j**2+2504*j-344),12),
    ]

def E(j,n):
    if j==0:
        return 1
    N=n-j
    assert N>=j
    return sum(fdim((N,)+mu)**2 for mu in parts(j))

def threshold9(j):
    n=max(2*j,1)
    while n**9 < (2**29)*(j+1)**10:
        n+=1
    return n

def threshold8(j):
    n=max(2*j,1)
    while n**8 < (2**26)*(j+1)**9:
        n+=1
    return n

# Permutation helpers for exact bounded star-word pattern counts.
def compose(p,q):
    return tuple(p[q[i]] for i in range(len(p)))

def transposition_perm(size,a,b):
    p=list(range(size)); p[a],p[b]=p[b],p[a]; return tuple(p)

def cycle_type(p):
    seen=[False]*len(p); lens=[]
    for i in range(len(p)):
        if not seen[i]:
            j=i; l=0
            while not seen[j]:
                seen[j]=True; l+=1; j=p[j]
            if l>1: lens.append(l)
    return tuple(sorted(lens,reverse=True))

def exact_support_type_count(s,L,target_type):
    size=s+1; center=s
    gens=[transposition_perm(size,a,center) for a in range(s)]
    ident=tuple(range(size)); count=0
    for w in product(range(s), repeat=L):
        if len(set(w))!=s: continue
        p=ident
        for a in w: p=compose(gens[a],p)
        if cycle_type(p)==target_type: count+=1
    return count

# Expected exact-support pattern constants used in the class-algebra derivations.
# L=5, product a transposition: support sizes 1,2,3 give 1,30,60.
assert [exact_support_type_count(s,5,(2,)) for s in (1,2,3)]==[1,30,60]
# L=4, product a 3-cycle: support sizes 2,3 give 10,24.
assert [exact_support_type_count(s,4,(3,)) for s in (2,3)]==[10,24]
# L=3: transposition support sizes 1,2 give 1,6; 4-cycle support size3 gives 6.
assert [exact_support_type_count(s,3,(2,)) for s in (1,2)]==[1,6]
assert exact_support_type_count(3,3,(4,))==6

print("P0282 ninth-tenths-window exact self-check")
print("bounded_star_word_pattern_counts=PASS")

for j in range(1,MAXJ+1):
    ps=list(parts(j)); fact=factorial(j)
    W=sum(fdim(mu)**2 for mu in ps)
    assert W==fact

    sC4=sum(fdim(mu)**2*content(mu,1)**4 for mu in ps)
    sCS5=sum(fdim(mu)**2*content(mu,1)*content(mu,5) for mu in ps)
    sS2S4=sum(fdim(mu)**2*content(mu,2)*content(mu,4) for mu in ps)
    sS3sq=sum(fdim(mu)**2*content(mu,3)**2 for mu in ps)

    EC4=Fraction(j*(j-1)*(3*j*j+j-12),4)
    ECS5=Fraction(j*(j-1)*(5*j*j-15*j+11),2)
    ES2S4=Fraction(j*(j-1)*(4*j**3+3*j*j-35*j+32),12)
    ES3sq=Fraction(j*(j-1)*(9*j*j-29*j+24),4)

    assert sC4==fact*EC4
    assert sCS5==fact*ECS5
    assert sS2S4==fact*ES2S4
    assert sS3sq==fact*ES3sq

    # Independent class/word-count formulas.
    N=comb(j,2)
    # T^2: identity N; every 3-cycle coefficient 3; every double-transposition coefficient 2.
    assert EC4 == N*N + 18*comb(j,3) + 12*comb(j,4)
    # P5 transposition coefficient mass from star centers.
    assert ECS5 == sum(Fraction(m*(10*m*m-15*m+6)) for m in range(j))
    # P2 = N e + K3; P4 coefficient on each 3-cycle is 3j-4.
    ES4=Fraction(j*(j-1)*(4*j-5),6)
    assert ES2S4 == N*ES4 + 2*comb(j,3)*(3*j-4)
    # P3 = (2j-3)T + K4.
    assert ES3sq == N*(2*j-3)**2 + 6*comb(j,4)

    for mu in ps:
        assert bm_cols(8,j,mu)==b8_formula(j,mu), (j,mu)

    LA=log1(A_series(j)); dc=dcoeffs(j)
    for q in range(1,9):
        assert LA[q]==dc[q], (j,q,LA[q],dc[q])

    n0=threshold9(j); old=threshold8(j)
    margin=E(j,n0)**2-E(j-1,n0)*E(j+1,n0)
    assert margin>0
    print(f"j={j} partitions={len(ps)} EC4={EC4} ECS5={ECS5} ES2S4={ES2S4} ES3sq={ES3sq} ninth_tenths_threshold_n={n0} old_eight_ninths_threshold_n={old} source_margin_positive=True")

for j in range(1,120):
    f8=lambda r: dcoeffs(r)[8]
    curv=2*f8(j)-f8(j-1)-f8(j+1)
    expected=Fraction(224*j**6+1176*j**5-2310*j**4+140*j**3+4876*j**2-5508*j+1905,2)
    m=j-1
    shifted=Fraction(224*m**6+2520*m**5+6930*m**4+7140*m**3+6556*m**2+2648*m+503,2)
    assert curv==expected==shifted
    assert curv>0

print("D8_discrete_curvature_identity=PASS")
print("D8_shifted_positive_coefficients=PASS")
print("analytic_tail_claim_used_in_report=tail_after_order8 < 2^26*j^9/n^9 for n>=12j")
print("chen_second_difference_tail_bound=<2^28*(j+1)^9/n^9")
print("theorem_threshold_used_in_report=n^9 >= 2^29*(j+1)^10")
print("simple_corollary=j+1 <= n^(9/10)/8")
print("ALL_EXACT_CHECKS_PASS")
