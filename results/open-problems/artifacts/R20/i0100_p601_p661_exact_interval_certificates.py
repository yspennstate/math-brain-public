#!/usr/bin/env python3
"""R20/I0100 exact rational-interval primal/dual certificates at p=601 and p=661.

The symmetry-reduced LP is the source-normalized standard Lovasz theta of the
COMPLEMENT of the one-localized Paley graph.  All sign decisions are certified
by outward-rounded dyadic interval arithmetic after exact Sturm isolation of the
chosen real cyclotomic embedding.
"""
import sympy as sp
from dataclasses import dataclass

DATA={601: {'N': 300, 'NONEDGE': [5, 6, 9, 11, 12, 13, 15, 16, 19, 21, 26, 28, 30, 32, 33, 35, 37, 38, 39, 40, 41, 42, 43, 45, 46, 47, 48, 49, 52, 53, 57, 58, 61, 62, 63, 65, 67, 70, 72, 74, 75, 76, 78, 79, 80, 81, 82, 83, 88, 90, 91, 92, 96, 98, 103, 106, 107, 108, 114, 117, 118, 119, 120, 121, 122, 126, 127, 130, 136, 138, 139, 141, 142, 145, 147], 'SUPPORT': [0, 2, 3, 4, 6, 9, 10, 11, 12, 13, 14, 16, 18, 21, 24, 25, 27, 28, 29, 32, 34, 35, 36, 38, 39, 41, 42, 47, 49, 50, 51, 54, 60, 61, 65, 66, 67, 69, 70, 75, 77, 78, 80, 81, 82, 83, 86, 87, 88, 89, 90, 91, 96, 101, 103, 105, 107, 109, 114, 115, 117, 118, 121, 122, 123, 124, 127, 132, 133, 135, 136, 142, 144, 145, 146, 149]}, 661: {'N': 330, 'NONEDGE': [3, 8, 11, 12, 14, 15, 20, 21, 30, 32, 33, 34, 35, 37, 38, 41, 42, 45, 47, 48, 49, 50, 53, 54, 58, 60, 63, 64, 66, 67, 69, 74, 75, 76, 78, 79, 80, 81, 82, 83, 85, 87, 88, 89, 90, 92, 95, 97, 98, 99, 100, 101, 105, 106, 107, 111, 117, 118, 119, 121, 123, 125, 126, 130, 131, 136, 138, 140, 141, 145, 146, 148, 149, 151, 153, 154, 155, 157, 158, 159, 161, 162, 165], 'SUPPORT': [0, 1, 2, 3, 5, 9, 11, 12, 14, 15, 16, 18, 22, 23, 24, 28, 32, 35, 36, 38, 39, 42, 43, 44, 46, 51, 52, 54, 55, 57, 58, 59, 60, 64, 65, 67, 69, 70, 72, 73, 74, 76, 77, 82, 83, 85, 91, 95, 97, 99, 100, 101, 102, 103, 104, 106, 107, 108, 117, 121, 123, 126, 127, 128, 130, 133, 135, 137, 138, 141, 142, 144, 145, 146, 149, 150, 152, 154, 155, 156, 157, 159, 161, 165]}}
BITS=1280
SCALE=1<<BITS

def floordiv(a,b): assert b>0; return a//b
def ceildiv(a,b): assert b>0; return -((-a)//b)

@dataclass(frozen=True)
class IV:
    lo:int
    hi:int
    def __post_init__(self): assert self.lo<=self.hi
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
    q=sp.Rational(q); num=int(q.p); den=int(q.q)
    return IV(floordiv(num*SCALE,den),ceildiv(num*SCALE,den))

def diviv(a,b):
    assert not b.contains0(),(a,b)
    pairs=[]
    for x in (a.lo,a.hi):
        for y in (b.lo,b.hi):
            pairs.append((x,y) if y>0 else (-x,-y))
    return IV(min(floordiv(SCALE*x,y) for x,y in pairs),
              max(ceildiv(SCALE*x,y) for x,y in pairs))

def half(a): return IV(floordiv(a.lo,2),ceildiv(a.hi,2))
def maxabs_mid(iv): return abs(iv.mid())
def digits10_width(iv):
    if iv.width()==0: return 9999
    return int((BITS-iv.width().bit_length())*0.3010299956639812)

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
    a=generator_Q(p)
    vals=[pow(a,j,p) for j in range(n)]
    S={d for d in range(1,n) if (vals[d]-1)%p in Q}
    assert all((n-d) in S for d in S)
    return n,[d for d in range(1,n//2+1) if d not in S]

def solve_interval(A,b):
    m=len(A)
    M=[A[i][:]+[b[i]] for i in range(m)]
    for col in range(m):
        candidates=[r for r in range(col,m) if not M[r][col].contains0()]
        assert candidates,("no certified pivot",col)
        piv=max(candidates,key=lambda r:maxabs_mid(M[r][col]))
        M[col],M[piv]=M[piv],M[col]
        p=M[col][col]
        for j in range(col+1,m+1): M[col][j]=diviv(M[col][j],p)
        M[col][col]=ONE
        for r in range(m):
            if r==col: continue
            f=M[r][col]
            if f.lo==0 and f.hi==0: continue
            for j in range(col+1,m+1): M[r][j]=M[r][j]-f*M[col][j]
            M[r][col]=ZERO
    return [M[i][-1] for i in range(m)]

def certify(P):
    N=DATA[P]["N"]; NONEDGE=DATA[P]["NONEDGE"]; SUPPORT=DATA[P]["SUPPORT"]
    assert sp.isprime(P) and P%4==1
    n,Nchk=reduced_nonedge_diffs(P)
    assert n==N and Nchk==NONEDGE and len(SUPPORT)==len(NONEDGE)+1
    x=sp.Symbol("x")
    K=sp.QQ.algebraic_field(2*sp.cos(2*sp.pi/n))
    minpoly=sp.Poly.from_list(
        [sp.Rational(int(q.numerator),int(q.denominator)) for q in K.mod.to_list()],
        gens=x,
    )
    import mpmath as mp
    mp.mp.dps=200
    approx=2*mp.cos(2*mp.pi/n)
    ten=10**150
    lo_num=int(mp.floor(approx*ten)); hi_num=lo_num+1
    alo=sp.Rational(lo_num,ten); ahi=sp.Rational(hi_num,ten)
    assert minpoly.count_roots(alo,ahi)==1
    assert minpoly.count_roots(ahi,sp.oo)==0
    alpha=IV(from_rat(alo).lo,from_rat(ahi).hi)

    C=[ZERO]*(n//2+1); C[0]=TWO; C[1]=alpha
    for mm in range(1,n//2): C[mm+1]=alpha*C[mm]-C[mm-1]
    COS=[half(C[mm]) for mm in range(n//2+1)]
    def cosiv(mm):
        mm%=n; mm=min(mm,n-mm); return COS[mm]

    A=[[ONE for _ in SUPPORT]]
    A += [[cosiv(mm*d) for mm in SUPPORT] for d in NONEDGE]
    b=[ONE]+[ZERO]*len(NONEDGE)
    w=solve_interval(A,b)
    assert all(v.lo>0 for v in w)

    AT=[[A[j][i] for j in range(len(A))] for i in range(len(A))]
    rhs=[ONE if mm==0 else ZERO for mm in SUPPORT]
    y=solve_interval(AT,rhs); a=y[0]; lam=y[1:]
    positives=[]
    for mm in range(n//2+1):
        if mm in SUPPORT: continue
        q=a
        for coeff,d in zip(lam,NONEDGE): q=q+coeff*cosiv(mm*d)
        assert q.lo>0,("dual slack",P,mm,q.lo,q.hi,digits10_width(q))
        positives.append(q)

    w0=w[SUPPORT.index(0)]
    assert not(w0.hi<a.lo or a.hi<w0.lo)
    theta=IV(n*w0.lo,n*w0.hi)
    def dec(iv,dig=40):
        lo=sp.Rational(iv.lo,SCALE); hi=sp.Rational(iv.hi,SCALE)
        return str(sp.N((lo+hi)/2,dig))
    print("p",P,"n",n,"field_degree",minpoly.degree(),"bits",BITS)
    print("strict_positive_primal_weights",len(w))
    print("strict_positive_nonsupport_half_slacks",len(positives))
    print("theta_interval_mid",dec(theta))
    print("w0_digits",digits10_width(w0),"a_digits",digits10_width(a))
    print("min_weight",dec(min(w,key=lambda z:z.lo),25))
    print("min_slack",dec(min(positives,key=lambda z:z.lo),25))
    print("PASS_p",P)

def main():
    for P in (601,661):
        certify(P)
    print("covered_primes_before=[5,13,17,29,41,181,241,421,541]")
    print("covered_primes_after=[5,13,17,29,41,181,241,421,541,601,661]")
    print("largest_exact_prime=661")
    print("ALL_EXACT_CHECKS_PASS")

if __name__=="__main__":
    main()
