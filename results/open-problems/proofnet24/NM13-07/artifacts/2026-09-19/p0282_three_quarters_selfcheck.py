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

def E(j,n):
    if j==0: return 1
    N=n-j
    assert N>=max(j,1)
    return sum(fdim((N,)+mu)**2 for mu in parts(j))

def ceil_threshold(j):
    n=max(2*j,1)
    while n**3 < 512*(j+1)**4: n+=1
    return n

def interp_coeff(vals):
    xs=[Fraction(x) for x,y in vals]; ys=[Fraction(y) for x,y in vals]
    out=[Fraction(0)]*len(vals)
    for i,(xi,yi) in enumerate(zip(xs,ys)):
        poly=[Fraction(1)]; den=Fraction(1)
        for m,xm in enumerate(xs):
            if m==i: continue
            den*=xi-xm
            nxt=[Fraction(0)]*(len(poly)+1)
            for d,a in enumerate(poly):
                nxt[d]-=a*xm; nxt[d+1]+=a
            poly=nxt
        sc=yi/den
        for d,a in enumerate(poly): out[d]+=sc*a
    return out

def logR_remainder_bound_check(j,n,mu):
    h=[]
    mu1=mu[0] if mu else 0
    for c in range(1,mu1+1):
        h.append(sum(1 for r in mu if r>=c))
    assert sum(h)==j
    for c,hc in enumerate(h,1):
        a=j+c-1; d=n-a
        assert d*2 >= n
        assert 2*hc <= d
    C1=sum((c-1)*hc for c,hc in enumerate(h,1))
    Q=sum(hc*hc for hc in h)
    coeff2=-j*j-C1+Fraction(Q,2)
    assert coeff2 == Fraction(-j*j,1)+Fraction(j,2)-content(mu)

print('P0282 three-quarters-window exact self-check')
for j in range(1,MAXJ+1):
    ps=list(parts(j))
    W=sum(fdim(mu)**2 for mu in ps)
    assert W==factorial(j)
    Csum=sum(fdim(mu)**2*content(mu) for mu in ps)
    assert Csum==0
    vals=[(n,E(j,n)) for n in range(2*j,4*j+1)]
    co=interp_coeff(vals)
    assert len(co)==2*j+1
    assert co[-1]==Fraction(1,factorial(j))
    assert co[-2]==Fraction(-j*(j+1),factorial(j))
    c2=Fraction(j*(3*j**3+4*j**2-6*j+5),6*factorial(j))
    assert co[-3]==c2
    n0=ceil_threshold(j)
    for mu in ps: logR_remainder_bound_check(j,n0,mu)
    ejm=E(j-1,n0) if j>1 else E(0,n0)
    ej=E(j,n0); ejp=E(j+1,n0)
    margin=ej*ej-ejm*ejp
    assert margin>0
    print(f'j={j} partitions={len(ps)} threshold_n={n0} content_mean_num={Csum} source_margin_positive=True')
print('ALL_EXACT_CHECKS_PASS')
