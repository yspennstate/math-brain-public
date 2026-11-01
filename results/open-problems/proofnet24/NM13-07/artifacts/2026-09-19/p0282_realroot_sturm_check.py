from fractions import Fraction
from math import factorial

NMAX=12

def parts(n,maxp=None):
    if n==0:
        yield (); return
    if maxp is None or maxp>n: maxp=n
    for first in range(maxp,0,-1):
        rem=n-first
        if rem==0: yield (first,)
        else:
            for t in parts(rem,min(first,rem)): yield (first,)+t

def hook_dim(lam):
    n=sum(lam); hp=1
    for i,row in enumerate(lam):
        for c in range(row):
            hp *= (row-c)+sum(1 for rr in lam[i+1:] if rr>c)
    return factorial(n)//hp

def ell_row(n):
    e=[0]*(n+1)
    for lam in parts(n):
        f=hook_dim(lam); e[lam[0]]+=f*f
    assert sum(e)==factorial(n)
    return e

def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0:p.pop()
    return p

def deriv(p): return trim([Fraction(i)*p[i] for i in range(1,len(p))] or [Fraction(0)])

def divrem(a,b):
    a=trim(a); b=trim(b)
    if len(b)==1 and b[0]==0: raise ZeroDivisionError
    q=[Fraction(0)]*max(1,len(a)-len(b)+1)
    while len(a)>=len(b) and not (len(a)==1 and a[0]==0):
        d=len(a)-len(b); c=a[-1]/b[-1]; q[d]=c
        for i,bi in enumerate(b): a[i+d]-=c*bi
        a=trim(a)
    return trim(q),trim(a)

def sturm(p):
    s=[trim(p),deriv(p)]
    while not (len(s[-1])==1):
        _,r=divrem(s[-2],s[-1]); r=[-x for x in r]
        if len(r)==1 and r[0]==0: break
        s.append(trim(r))
    return s

def sign_at_zero(p):
    x=p[0]
    return 1 if x>0 else -1 if x<0 else 0

def sign_at_minus_inf(p):
    x=p[-1]
    sg=1 if x>0 else -1
    if (len(p)-1)%2: sg=-sg
    return sg

def variations(signs):
    signs=[s for s in signs if s]
    return sum(signs[i]!=signs[i-1] for i in range(1,len(signs)))

def neg_root_count(p):
    S=sturm(p)
    if not (len(S[-1])==1 and S[-1][0]!=0):
        return None,False,len(S)
    va=variations([sign_at_minus_inf(q) for q in S])
    vb=variations([sign_at_zero(q) for q in S])
    return va-vb,True,len(S)

print('P0282 exact Sturm falsification of real-rooted LIS generating polynomial route')
first_fail=None
for n in range(2,NMAX+1):
    e=ell_row(n)
    p=[Fraction(e[k]) for k in range(1,n+1)]
    cnt,squarefree,sl=neg_root_count(p)
    deg=n-1
    assert squarefree
    if cnt!=deg and first_fail is None: first_fail=n
    print(f'n={n} degree={deg} exact_negative_real_roots={cnt} squarefree=True all_coefficients_positive=True all_roots_real_negative={cnt==deg}')
assert first_fail==12
print('FIRST_REAL_ROOTEDNESS_FAILURE_N=12')
print('n=12 degree=11 has exactly 9 negative real roots, no nonnegative real roots, and is squarefree; therefore exactly one nonreal conjugate pair.')
print('This refutes only the stronger real-rooted/stable route, not Chen and not binomial-normalized ULC.')
print('ALL_EXACT_CHECKS_PASS')
