#!/usr/bin/env python3
"""R20/I0100 exact p=1093 localized-Paley theta certificate.

The candidate support was discovered numerically only. This proof-grade checker
independently recomputes the p=1093 Paley difference set, the intended
real-cyclotomic embedding, the primal basic solution, the matching dual basic
solution, every strict positivity/slack inequality, and overlapping primal/dual
objectives, using exact Sturm isolation plus outward-rounded 1024-bit dyadic
interval arithmetic.
"""
import sympy as sp
import mpmath as mp
from dataclasses import dataclass

P=1093
N=546
NONEDGE=[1, 3, 6, 7, 8, 9, 11, 14, 16, 19, 20, 21, 23, 25, 29, 31, 33, 36, 37, 40, 42, 43, 44, 46, 50, 52, 54, 58, 59, 60, 62, 63, 65, 66, 67, 68, 70, 73, 76, 78, 79, 80, 81, 82, 87, 88, 89, 90, 100, 101, 107, 109, 112, 113, 114, 119, 120, 122, 125, 126, 129, 130, 131, 132, 137, 143, 144, 146, 147, 148, 150, 151, 153, 155, 156, 157, 158, 160, 161, 164, 165, 167, 170, 172, 173, 174, 177, 179, 181, 182, 183, 184, 185, 187, 188, 192, 197, 198, 199, 201, 203, 205, 206, 211, 212, 214, 215, 216, 217, 219, 221, 227, 228, 230, 231, 232, 234, 235, 236, 237, 238, 239, 243, 246, 247, 251, 254, 255, 257, 259, 262, 263, 264, 267, 269, 272, 273]
SUPPORT=[0, 1, 4, 5, 6, 9, 10, 11, 13, 16, 17, 19, 20, 22, 23, 24, 27, 29, 31, 32, 34, 36, 37, 39, 40, 43, 44, 45, 46, 47, 51, 52, 57, 58, 59, 61, 64, 65, 66, 68, 69, 70, 71, 78, 79, 84, 85, 86, 89, 90, 93, 94, 95, 97, 98, 100, 103, 110, 117, 118, 120, 121, 123, 124, 125, 126, 127, 128, 129, 134, 138, 140, 143, 145, 150, 154, 155, 158, 159, 161, 162, 167, 169, 171, 172, 174, 176, 181, 182, 183, 184, 185, 192, 198, 199, 201, 203, 205, 206, 208, 212, 214, 216, 218, 220, 221, 222, 223, 224, 226, 227, 228, 230, 234, 237, 238, 240, 241, 242, 243, 246, 248, 249, 251, 252, 253, 254, 255, 256, 257, 258, 266, 267, 268, 269, 270, 271, 273]
BITS=1024
SCALE=1<<BITS

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
    out=[]; d=2; x=n
    while d*d<=x:
        if x%d==0:
            out.append(d)
            while x%d==0: x//=d
        d+=1
    if x>1: out.append(x)
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
        pp=M[col][col]
        for j in range(col+1,m+1):
            M[col][j]=diviv(M[col][j],pp)
        M[col][col]=ONE
        for r in range(m):
            if r==col: continue
            f=M[r][col]
            if f.lo==0 and f.hi==0: continue
            for j in range(col+1,m+1):
                M[r][j]=M[r][j]-f*M[col][j]
            M[r][col]=ZERO
    return [M[i][-1] for i in range(m)]

def dec(iv,dig=45):
    lo=sp.Rational(iv.lo,SCALE); hi=sp.Rational(iv.hi,SCALE)
    return str(sp.N((lo+hi)/2,dig))

def main():
    assert sp.isprime(P) and P%4==1
    n,nchk=reduced_nonedge_diffs(P)
    assert n==N and nchk==NONEDGE
    assert len(SUPPORT)==len(NONEDGE)+1

    x=sp.Symbol("x")
    K=sp.QQ.algebraic_field(2*sp.cos(2*sp.pi/n))
    minpoly=sp.Poly.from_list(
        [sp.Rational(int(q.numerator),int(q.denominator)) for q in K.mod.to_list()],
        gens=x)

    mp.mp.dps=180
    approx=2*mp.cos(2*mp.pi/n)
    ten=10**145
    lo_num=int(mp.floor(approx*ten)); hi_num=lo_num+1
    alo=sp.Rational(lo_num,ten); ahi=sp.Rational(hi_num,ten)
    assert minpoly.count_roots(alo,ahi)==1
    assert minpoly.count_roots(ahi,sp.oo)==0
    alpha=IV(from_rat(alo).lo,from_rat(ahi).hi)

    C=[ZERO]*(n//2+1)
    C[0]=TWO; C[1]=alpha
    for mm in range(1,n//2):
        C[mm+1]=alpha*C[mm]-C[mm-1]
    COS=[half(C[mm]) for mm in range(n//2+1)]
    def cosiv(mm):
        mm%=n
        mm=min(mm,n-mm)
        return COS[mm]

    A=[[ONE for _ in SUPPORT]] + [
        [cosiv(mm*d) for mm in SUPPORT] for d in NONEDGE]
    rhs=[ONE]+[ZERO]*len(NONEDGE)
    w=solve_interval(A,rhs)
    assert all(v.lo>0 for v in w)

    AT=[[A[j][i] for j in range(len(A))] for i in range(len(A))]
    dual_rhs=[ONE if mm==0 else ZERO for mm in SUPPORT]
    y=solve_interval(AT,dual_rhs)
    a=y[0]; lam=y[1:]
    slacks=[]
    for mm in range(n//2+1):
        if mm in SUPPORT:
            continue
        q=a
        for coeff,d in zip(lam,NONEDGE):
            q=q+coeff*cosiv(mm*d)
        assert q.lo>0,("dual slack",mm,q.lo,q.hi,digits10_width(q))
        slacks.append(q)

    w0=w[SUPPORT.index(0)]
    assert not (w0.hi<a.lo or a.hi<w0.lo)
    theta=IV(n*w0.lo,n*w0.hi)
    target=sp.sqrt(sp.Rational(P,2))
    overshoot=2*theta.lo*theta.lo > P*SCALE*SCALE

    print("I0100 exact certificate")
    print("p",P,"n",n,"field_degree",minpoly.degree(),"bits",BITS)
    print("nonedge_half_constraints",len(NONEDGE))
    print("strict_positive_primal_half_weights",len(w))
    print("strict_positive_nonsupport_half_slacks",len(slacks))
    print("theta_interval_mid",dec(theta))
    print("sqrt_p_over_2",sp.N(target,45))
    print("ratio_mid",sp.N(sp.Rational(theta.mid(),SCALE)/target,40))
    print("w0_digits",digits10_width(w0),"a_digits",digits10_width(a))
    print("min_weight",dec(min(w,key=lambda z:z.lo),30))
    print("min_slack",dec(min(slacks,key=lambda z:z.lo),30))
    print("certified_theta_gt_sqrt_p_over_2",overshoot)
    print("covered_primes_before=[5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061]")
    print("covered_primes_after=[5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093]")
    print("largest_exact_prime=1093")
    print("PASS_p",P)
    print("ALL_EXACT_CHECKS_PASS")

if __name__=="__main__":
    main()
