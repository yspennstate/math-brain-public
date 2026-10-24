from fractions import Fraction
from math import factorial, comb
from functools import lru_cache

JMAX=20
BOUND_N=2*JMAX+1


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


def ell_row(n):
    e=[0]*(n+1); count=0
    for lam in parts(n):
        f=hook_dim(lam); e[lam[0]] += f*f; count += 1
    return e,count

# Polynomials are ascending coefficient lists over Q.
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
    # a(n) -> a(m+c)
    b=[Fraction(0)]*len(a)
    for i,ai in enumerate(a):
        if not ai: continue
        for h in range(i+1): b[h]+=ai*comb(i,h)*(c**(i-h))
    return ptrim(b)

def plinear_mul(a,c):
    # (n-c)*a(n)
    return padd(pscale(a,-c), [Fraction(0)]+a)

def peval(a,x): return sum(c*(x**i) for i,c in enumerate(a))


def dim_poly(j,mu):
    # Weyl/hook dimension formula specialized to lambda=(n-j,mu), valid for n>=2j.
    r=1+len(mu)
    C=Fraction(1)
    for a in range(len(mu)):
        for b in range(a+1,len(mu)):
            C *= mu[a]-mu[b]+(b-a)
    for t,val in enumerate(mu):
        C /= factorial(val+r-t-2)
    p=[Fraction(1)]
    # n!/(n-j+r-1)! contributes j-r+1 linear factors (possibly zero).
    for s in range(max(0,j-r+1)):
        p=pmul(p,[Fraction(-s),Fraction(1)])
    # first-row Vandermonde factors.
    for t,val in enumerate(mu,start=1):
        p=pmul(p,[Fraction(-j-val+t),Fraction(1)])
    return pscale(p,C)

@lru_cache(None)
def Epoly(j):
    if j==0: return (Fraction(1),)
    s=[Fraction(0)]
    for mu in parts(j):
        d=dim_poly(j,mu)
        s=padd(s,pmul(d,d))
    return tuple(s)

def Mpoly(j):
    a=list(Epoly(j-1)); b=list(Epoly(j)); c=list(Epoly(j+1))
    t1=pscale(plinear_mul(pmul(b,b),j+1),j)
    t2=pscale(plinear_mul(pmul(a,c),j),j+1)
    return padd(t1,pscale(t2,-1))

print('P0282 exact stronger binomial-normalized ULC fixed-defect certificate')
print(f'JMAX={JMAX} finite_boundary_rows_through={BOUND_N}')

# Finite boundary and global small-row exact check.
rows={}
shape_total=0
ulc_cells=0
best=None
best_at=None
for n in range(1,BOUND_N+1):
    e,pc=ell_row(n); rows[n]=e; shape_total += pc
    assert sum(e)==factorial(n), ('mass',n)
    for k in range(2,n):
        lhs=e[k]*e[k]*comb(n-1,k-2)*comb(n-1,k)
        rhs=e[k-1]*e[k+1]*comb(n-1,k-1)**2
        assert lhs>rhs, ('ULC_FAIL',n,k,lhs,rhs)
        ulc_cells += 1
        rat=Fraction(lhs,rhs)
        if best is None or rat<best:
            best=rat; best_at=(n,k)
print(f'finite_shape_total={shape_total}')
print(f'all_small_row_ULC_cells={ulc_cells} all_strictly_positive=True')
print(f'small_row_min_normalized_ratio_at={best_at} exact={best.numerator}/{best.denominator} approx={float(best):.18g}')

# Large-n polynomial proof per fixed defect.
for j in range(1,JMAX+1):
    M=Mpoly(j)
    expected_deg=4*j
    assert len(M)-1<=expected_deg
    n0=2*j+2
    S=pshift(M,n0)
    assert all(c>0 for c in S), ('SHIFT_COEFF_NONPOS',j)
    # Independent exact evaluation check at two n values against direct residual hook sums.
    for nn in (n0,n0+3):
        Es=[]
        for q in (j-1,j,j+1):
            val=0
            for mu in parts(q):
                lam=(nn-q,)+mu if q else (nn,)
                # q=0 uses shape (n); parts(0) emits (), but special-case simpler.
                val += hook_dim(lam)**2
            Es.append(val)
        direct=j*(nn-j-1)*Es[1]*Es[1]-(j+1)*(nn-j)*Es[0]*Es[2]
        assert direct==peval(M,nn) and direct>0, ('POLY_EVAL_MISMATCH',j,nn)
    # Boundary n range has already been exhaustively covered in rows[]; assert exact cells again.
    for nn in range(j+2,2*j+2):
        k=nn-j
        e=rows[nn]
        lhs=e[k]*e[k]*comb(nn-1,k-2)*comb(nn-1,k)
        rhs=e[k-1]*e[k+1]*comb(nn-1,k-1)**2
        assert lhs>rhs, ('BOUNDARY_FAIL',j,nn,k)
    print(f'j={j} shifted_degree={len(S)-1} shifted_coeff_count={len(S)} all_shifted_coeffs_positive=True constant={S[0]} leading={S[-1]} boundary_n={j+2}..{2*j+1}')

print(f'THEOREM_CERTIFIED: natural binomial-normalized ULC holds for every source-valid n at defects 1<=j<={JMAX}')
print('ULC inequality: ell[n,k]^2 * C(n-1,k-2) * C(n-1,k) > ell[n,k-1]*ell[n,k+1]*C(n-1,k-1)^2')
print('This strictly implies Chen on this defect range.')
print('ALL_EXACT_CHECKS_PASS')
