from math import factorial, comb, gcd
from functools import lru_cache
import sys

def parts(n,maxp=None):
    if n==0:
        yield (); return
    if maxp is None or maxp>n: maxp=n
    for first in range(maxp,0,-1):
        rem=n-first
        if rem==0: yield (first,)
        else:
            for t in parts(rem,min(first,rem)): yield (first,)+t

def dim_data(j,mu):
    r=1+len(mu); num=1; den=1
    for a in range(len(mu)):
        for b in range(a+1,len(mu)):
            num *= mu[a]-mu[b]+(b-a)
    for t,val in enumerate(mu): den *= factorial(val+r-t-2)
    roots=list(range(max(0,j-r+1)))
    for t,val in enumerate(mu,start=1): roots.append(j+val-t)
    assert len(roots)==j
    g=gcd(num,den); return num//g,den//g,tuple(roots)

@lru_cache(None)
def shape_data(q):
    if q==0: return ((1,1,()),)
    return tuple(dim_data(q,mu) for mu in parts(q))

def eval_E(q,n):
    if q==0: return 1
    ans=0
    for num,den,roots in shape_data(q):
        v=num
        for a in roots: v*=n-a
        assert v%den==0
        v//=den
        ans += v*v
    return ans

def rook_total(q,n): return factorial(q)*comb(n,q)**2

def density_margin(j,n):
    Em,Ej,Ep=(eval_E(q,n) for q in (j-1,j,j+1))
    Rm,Rj,Rp=(rook_total(q,n) for q in (j-1,j,j+1))
    return Ej*Ej*Rm*Rp - Em*Ep*Rj*Rj

def certify(j):
    assert 27<=j<=32
    n0=2*j+2; deg_bound=8*j
    vals=[density_margin(j,n0+m) for m in range(deg_bound+1)]
    coeff=[]; cur=vals
    while cur:
        coeff.append(cur[0]); cur=[cur[i+1]-cur[i] for i in range(len(cur)-1)]
    assert coeff[0]>0
    assert coeff[-2:]==[0,0]
    assert all(c>0 for c in coeff[:-2])
    print(f'j={j} n0={n0} degree_bound={deg_bound} newton_coeffs={len(coeff)} '
          f'positive={len(coeff)-2} trailing_zeros=2 '
          f'partitions=({len(shape_data(j-1))},{len(shape_data(j))},{len(shape_data(j+1))}) '
          f'constant_bits={coeff[0].bit_length()} top_nonzero_bits={coeff[-3].bit_length()}')
    print('ALL_EXACT_CHECKS_PASS')

if len(sys.argv)!=2:
    raise SystemExit('usage: python p0282_shadow_density_newton_j27_32.py J, with 27<=J<=32')
certify(int(sys.argv[1]))
