from fractions import Fraction
from math import factorial

MAXJ=12

def parts(n,maxv=None):
    if n==0:
        yield (); return
    if maxv is None or maxv>n: maxv=n
    for a in range(maxv,0,-1):
        for r in parts(n-a,a): yield (a,)+r

def fdim(part):
    n=sum(part); hp=1
    for r,row in enumerate(part):
        for c in range(row):
            below=sum(1 for rr in range(r+1,len(part)) if part[rr]>c)
            hp *= (row-c)+below
    return factorial(n)//hp

def content(mu):
    return sum(c-r for r,row in enumerate(mu) for c in range(row))

def content2(mu):
    return sum((c-r)**2 for r,row in enumerate(mu) for c in range(row))

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

def b2_formula(j,mu):
    return -j*j+Fraction(j,2)-content(mu)

def b3_formula(j,mu):
    return -j**3+j**2-Fraction(j,3)+(1-2*j)*content(mu)-content2(mu)

def E(j,n):
    if j==0: return 1
    N=n-j
    assert N>=j
    return sum(fdim((N,)+mu)**2 for mu in parts(j))

def threshold_new(j):
    n=max(2*j,1)
    while n**4 < 256*(j+1)**5: n+=1
    return n

def threshold_old(j):
    n=max(2*j,1)
    while n**3 < 512*(j+1)**4: n+=1
    return n

print('P0282 four-fifths-window exact self-check')
print('checks: Plancherel mass, E[C]=0, E[S2]=binom(j,2), exact B2/B3 identities, exact Chen margin at new threshold')
for j in range(1,MAXJ+1):
    ps=list(parts(j))
    W=sum(fdim(mu)**2 for mu in ps)
    assert W==factorial(j)
    Csum=sum(fdim(mu)**2*content(mu) for mu in ps)
    S2sum=sum(fdim(mu)**2*content2(mu) for mu in ps)
    assert Csum==0
    assert S2sum==factorial(j)*j*(j-1)//2
    for mu in ps:
        assert b2_cols(j,mu)==b2_formula(j,mu)
        assert b3_cols(j,mu)==b3_formula(j,mu)
    n0=threshold_new(j)
    old=threshold_old(j)
    ejm=E(j-1,n0)
    ej=E(j,n0)
    ejp=E(j+1,n0)
    margin=ej*ej-ejm*ejp
    assert margin>0
    print(f'j={j} partitions={len(ps)} E_C_num={Csum} E_S2={S2sum//factorial(j)} '
          f'new_threshold_n={n0} old_three_quarters_threshold_n={old} source_margin_positive=True')
for j in range(1,50):
    f2=lambda r: -2*r*r+r
    f3=lambda r: Fraction(-2*r**3+r*r,1)+Fraction(r,3)
    assert 2*f2(j)-f2(j-1)-f2(j+1)==4
    assert 2*f3(j)-f3(j-1)-f3(j+1)==12*j-2
print('D3_discrete_curvature_identity=PASS')
print('ALL_EXACT_CHECKS_PASS')
