#!/usr/bin/env python3
"""Exact rational-interval primal/dual certificate for R20 / I0100 at p=421.

All acceptance decisions use integer/rational interval arithmetic.  Floating
point is not used.  The exact certificates are defined as the unique exact
solutions of the symmetry-reduced primal and dual interpolation systems in
Q(alpha), alpha=2*cos(2*pi/210).  Rational root isolation identifies the
chosen real embedding; dyadic interval Gaussian elimination proves
invertibility and strictly encloses every primal weight and every nonsupport
dual slack.  Complementary slackness then proves exact equality of objectives.
"""
import sympy as sp
from dataclasses import dataclass

P=421
N=210
NONEDGE=[6,8,10,11,12,13,14,16,21,22,25,27,30,31,34,38,39,40,42,43,44,45,47,49,50,51,52,53,58,59,63,65,68,70,74,75,76,78,79,85,86,88,89,90,91,92,93,95,98,100,101,102,105]
SUPPORT=[0,1,2,3,6,7,8,10,11,12,13,15,18,22,24,26,30,31,34,38,41,44,45,46,47,51,52,53,55,57,58,60,63,65,67,70,71,72,73,74,79,81,82,83,85,87,88,89,91,92,95,96,97,98]
BITS=896
SCALE=1<<BITS

# ---------- fixed-precision exact dyadic interval arithmetic ----------
def floordiv(a,b):
    assert b>0
    return a//b

def ceildiv(a,b):
    assert b>0
    return -((-a)//b)

@dataclass(frozen=True)
class IV:
    lo:int
    hi:int
    def __post_init__(self):
        assert self.lo<=self.hi
    def __add__(self,o): return IV(self.lo+o.lo,self.hi+o.hi)
    def __sub__(self,o): return IV(self.lo-o.hi,self.hi-o.lo)
    def __neg__(self): return IV(-self.hi,-self.lo)
    def __mul__(self,o):
        vals=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        return IV(floordiv(min(vals),SCALE),ceildiv(max(vals),SCALE))
    def contains0(self): return self.lo<=0<=self.hi
    def mid(self): return (self.lo+self.hi)//2
    def width(self): return self.hi-self.lo

def exact_int(k): return IV(k*SCALE,k*SCALE)
ZERO=exact_int(0); ONE=exact_int(1); TWO=exact_int(2)

def from_rat(q):
    q=sp.Rational(q)
    num=int(q.p); den=int(q.q)
    return IV(floordiv(num*SCALE,den),ceildiv(num*SCALE,den))

def diviv(a,b):
    assert not b.contains0(), (a,b)
    pairs=[]
    for x in (a.lo,a.hi):
        for y in (b.lo,b.hi):
            if y>0:
                pairs.append((x,y))
            else:
                pairs.append((-x,-y))
    los=[floordiv(SCALE*x,y) for x,y in pairs]
    his=[ceildiv(SCALE*x,y) for x,y in pairs]
    return IV(min(los),max(his))

def half(a):
    return IV(floordiv(a.lo,2),ceildiv(a.hi,2))

def maxabs_mid(iv): return abs(iv.mid())

def digits10_width(iv):
    if iv.width()==0: return 9999
    import math
    return int((BITS - iv.width().bit_length())*0.3010299956639812)

# ---------- exact source graph reconstruction ----------
def factor(n):
    out=[];d=2;x=n
    while d*d<=x:
        if x%d==0:
            out.append(d)
            while x%d==0:x//=d
        d+=1
    if x>1:out.append(x)
    return out

def generator_Q(p):
    for g in range(2,p):
        if all(pow(g,(p-1)//q,p)!=1 for q in factor(p-1)):
            return pow(g,2,p)
    raise AssertionError

def reduced_nonedge_diffs(p):
    n=(p-1)//2
    Q={x*x%p for x in range(1,p)}
    a=generator_Q(p); vals=[pow(a,j,p) for j in range(n)]
    S={d for d in range(1,n) if (vals[d]-1)%p in Q}
    assert all((n-d) in S for d in S)
    return n,[d for d in range(1,n//2+1) if d not in S]

# ---------- interval linear solve ----------
def solve_interval(A,b):
    """Gauss-Jordan enclosure for the exact system A(alpha)x=b.

    Pivot cells are set to exact 1 and eliminated cells to exact 0 after the
    corresponding algebraic row operation; this is dependency-aware and valid
    because those entries are algebraically exactly 1/0 in the transformed
    exact system.  All other entries are outward-rounded dyadic intervals.
    """
    m=len(A); assert m and all(len(r)==m for r in A) and len(b)==m
    M=[A[i][:]+[b[i]] for i in range(m)]
    min_piv=None
    for col in range(m):
        candidates=[r for r in range(col,m) if not M[r][col].contains0()]
        assert candidates, ("no certified pivot",col)
        piv=max(candidates,key=lambda r:maxabs_mid(M[r][col]))
        M[col],M[piv]=M[piv],M[col]
        p=M[col][col]
        if min_piv is None or abs(p.mid())<min_piv: min_piv=abs(p.mid())
        for j in range(col+1,m+1): M[col][j]=diviv(M[col][j],p)
        M[col][col]=ONE
        for r in range(m):
            if r==col: continue
            f=M[r][col]
            if f.lo==0 and f.hi==0: continue
            for j in range(col+1,m+1):
                M[r][j]=M[r][j]-f*M[col][j]
            M[r][col]=ZERO
    return [M[i][-1] for i in range(m)],min_piv

def main():
    assert sp.isprime(P) and P%4==1
    n,Nchk=reduced_nonedge_diffs(P)
    assert n==N and Nchk==NONEDGE
    assert len(SUPPORT)==len(NONEDGE)+1
    assert len(set(SUPPORT))==len(SUPPORT)

    # alpha is the largest real conjugate of 2*cos(2*pi/n).
    x=sp.Symbol('x')
    K=sp.QQ.algebraic_field(2*sp.cos(2*sp.pi/n))
    minpoly=sp.Poly.from_list([sp.Rational(int(q.numerator),int(q.denominator)) for q in K.mod.to_list()],gens=x)
    assert minpoly.degree()==24
    print('minpoly ready',flush=True)
    roots=minpoly.intervals(eps=sp.Rational(1,10**300))
    assert len(roots)==24 and all(mult==1 for _,mult in roots)
    alo,ahi=max((iv for iv,_ in roots),key=lambda z:z[0])
    print('roots isolated',flush=True)
    alpha=IV(from_rat(alo).lo,from_rat(ahi).hi)
    assert alpha.lo>0

    # Chebyshev recurrence C_m(alpha)=2*cos(2*pi*m/n).
    C=[ZERO]*(n//2+1); C[0]=TWO; C[1]=alpha
    for m in range(1,n//2): C[m+1]=alpha*C[m]-C[m-1]
    COS=[half(C[m]) for m in range(n//2+1)]
    def cosiv(m):
        m%=n; m=min(m,n-m); return COS[m]

    # A has rows: normalization, then each nonedge Fourier equality;
    # columns: active primal frequencies.
    A=[[ONE for _ in SUPPORT]]
    A += [[cosiv(m*d) for m in SUPPORT] for d in NONEDGE]
    b=[ONE]+[ZERO]*len(NONEDGE)
    print('solve primal',flush=True)
    w,minp=solve_interval(A,b)
    print('primal solved',flush=True)
    assert all(v.lo>0 for v in w), [(SUPPORT[i],v.lo,v.hi) for i,v in enumerate(w) if v.lo<=0]

    # Dual interpolation A^T y = e_{m=0}; q(s)=1_{s=0} exactly on SUPPORT.
    AT=[[A[j][i] for j in range(len(A))] for i in range(len(A))]
    rhs=[ONE if m==0 else ZERO for m in SUPPORT]
    print('solve dual',flush=True)
    y,mind=solve_interval(AT,rhs)
    print('dual solved',flush=True)
    a=y[0]; lam=y[1:]
    assert a.lo>0

    # For nonsupport frequencies in the half spectrum, certify strict positivity.
    # Evenness then covers the whole Z_n spectrum.  On SUPPORT, q is exactly
    # delta_0 by definition of the exact interpolation system.
    positives=[]
    for m in range(n//2+1):
        if m in SUPPORT: continue
        q=a
        for coeff,d in zip(lam,NONEDGE): q=q+coeff*cosiv(m*d)
        assert q.lo>0, ("dual slack not certified",m,q.lo,q.hi,digits10_width(q))
        positives.append((m,q))

    # Exact objective equality follows algebraically from complementary slackness:
    # sum_s w_s q(s)=w_0, while primal moment equations make the same sum equal a.
    # We additionally print overlapping interval enclosures for diagnostics.
    w0=w[SUPPORT.index(0)]
    assert not (w0.hi<a.lo or a.hi<w0.lo)
    theta=IV(n*w0.lo,n*w0.hi)

    # Rational lower/upper decimal display only; proof decisions above use integers.
    def dec(iv,dig=18):
        lo=sp.Rational(iv.lo,SCALE); hi=sp.Rational(iv.hi,SCALE)
        return str(sp.N((lo+hi)/2,dig))
    min_w=min(w,key=lambda z:z.lo)
    min_q=min((q for _,q in positives),key=lambda z:z.lo)
    print('I0100 / Conjecture 26 exact rational-interval continuation certificate')
    print('p =',P,'n =',n,'field_degree =',minpoly.degree(),'bits =',BITS)
    print('nonedge_difference_reps =',NONEDGE)
    print('primal_support =',SUPPORT)
    print('strict_positive_primal_weights =',len(w))
    print('strict_positive_nonsupport_half_slacks =',len(positives))
    print('exact_support_zero_slacks_half =',len(SUPPORT)-1,'plus q(0)=1')
    print('theta_interval_mid =',dec(theta,30))
    print('w0_interval_decimal_digits =',digits10_width(w0))
    print('dual_a_interval_decimal_digits =',digits10_width(a))
    print('min_weight_mid =',dec(min_w,20))
    print('min_positive_slack_mid =',dec(min_q,20))
    print('covered_primes_before = [5, 13, 17, 29, 41, 181, 241]')
    print('covered_primes_after = [5, 13, 17, 29, 41, 181, 241, 421]')
    print('largest_exact_prime = 421')
    print('PASS: exact matching primal/dual certificate at p=421')

if __name__=='__main__': main()
