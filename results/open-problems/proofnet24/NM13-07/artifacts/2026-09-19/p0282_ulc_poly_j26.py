from fractions import Fraction
from math import factorial, comb
from functools import lru_cache
JMIN=21
JMAX=26

def parts(n,maxp=None):
    if n==0:
        yield (); return
    if maxp is None or maxp>n: maxp=n
    for first in range(maxp,0,-1):
        rem=n-first
        if rem==0:
            yield (first,)
        else:
            yield from ((first,)+t for t in parts(rem,min(first,rem)))

def hook_dim(lam):
    n=sum(lam); hp=1
    for i,row in enumerate(lam):
        for c in range(row):
            hp *= (row-c) + sum(1 for rr in lam[i+1:] if rr>c)
    return factorial(n)//hp

def ptrim(a):
    while len(a)>1 and a[-1]==0: a.pop()
    return a

def padd(a,b):
    c=[Fraction(0)]*max(len(a),len(b))
    for i,x in enumerate(a): c[i]+=x
    for i,x in enumerate(b): c[i]+=x
    return ptrim(c)

def pscale(a,s): return [x*s for x in a]

def pmul(a,b):
    c=[Fraction(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if not x: continue
        for j,y in enumerate(b):
            if y: c[i+j]+=x*y
    return ptrim(c)

def pshift(a,c):
    b=[Fraction(0)]*len(a)
    for i,ai in enumerate(a):
        if not ai: continue
        for h in range(i+1): b[h]+=ai*comb(i,h)*(c**(i-h))
    return ptrim(b)

def plinear_mul(a,c):
    return padd(pscale(a,-c),[Fraction(0)]+a)

def peval(a,x): return sum(c*(x**i) for i,c in enumerate(a))

def dim_poly(j,mu):
    r=1+len(mu); C=Fraction(1)
    for a in range(len(mu)):
        for b in range(a+1,len(mu)):
            C *= mu[a]-mu[b]+(b-a)
    for t,val in enumerate(mu): C /= factorial(val+r-t-2)
    p=[Fraction(1)]
    for s in range(max(0,j-r+1)): p=pmul(p,[Fraction(-s),Fraction(1)])
    for t,val in enumerate(mu,start=1): p=pmul(p,[Fraction(-j-val+t),Fraction(1)])
    return pscale(p,C)

@lru_cache(None)
def Epoly(j):
    if j==0: return (Fraction(1),)
    s=[Fraction(0)]; count=0
    for mu in parts(j):
        d=dim_poly(j,mu); s=padd(s,pmul(d,d)); count+=1
    print(f'Epoly_j={j} partitions={count} degree={len(s)-1}',flush=True)
    return tuple(s)

def Mpoly(j):
    a=list(Epoly(j-1)); b=list(Epoly(j)); c=list(Epoly(j+1))
    t1=pscale(plinear_mul(pmul(b,b),j+1),j)
    t2=pscale(plinear_mul(pmul(a,c),j),j+1)
    return padd(t1,pscale(t2,-1))

print('P0282 exact shifted-coefficient ULC polynomial certificate for defects 21..26')
for j in range(JMIN,JMAX+1):
    M=Mpoly(j); n0=2*j+2; S=pshift(M,n0)
    assert all(c>0 for c in S), ('SHIFT_COEFF_NONPOS',j)
    for nn in (n0,n0+1,n0+3):
        Es=[]
        for q in (j-1,j,j+1):
            val=0
            for mu in parts(q):
                lam=(nn-q,)+mu if q else (nn,)
                val += hook_dim(lam)**2
            Es.append(val)
        direct=j*(nn-j-1)*Es[1]*Es[1]-(j+1)*(nn-j)*Es[0]*Es[2]
        assert direct==peval(M,nn) and direct>0, ('POLY_EVAL_MISMATCH',j,nn)
    print(f'j={j} shifted_degree={len(S)-1} coeffs={len(S)} all_positive=True constant={S[0]} leading={S[-1]}')
print('POLYNOMIAL_REGIME_CERTIFIED: ULC margin positive for every integer n>=2j+2 at defects 21..26')
print('ALL_EXACT_CHECKS_PASS')
