#!/usr/bin/env python3
import sympy as sp, mpmath as mp
from dataclasses import dataclass
P=1201
N=600
NONEDGE=[3, 4, 5, 7, 8, 10, 11, 12, 13, 14, 18, 19, 20, 26, 29, 32, 35, 36, 39, 40, 42, 43, 44, 46, 48, 49, 50, 51, 52, 56, 57, 58, 59, 60, 61, 63, 67, 69, 71, 74, 78, 79, 80, 83, 86, 87, 89, 90, 91, 92, 94, 95, 96, 97, 101, 103, 105, 107, 108, 113, 114, 115, 116, 118, 119, 122, 123, 124, 125, 126, 128, 129, 130, 132, 133, 138, 141, 142, 143, 149, 153, 154, 156, 159, 161, 164, 165, 166, 167, 170, 174, 180, 183, 184, 185, 186, 190, 191, 192, 195, 199, 203, 206, 207, 209, 211, 214, 215, 218, 220, 221, 223, 226, 233, 234, 235, 236, 238, 240, 244, 246, 248, 249, 250, 251, 253, 255, 256, 258, 263, 264, 265, 268, 270, 272, 275, 276, 277, 278, 279, 281, 284, 286, 288, 289, 291, 292, 294, 297, 298]
SUPPORT=[0, 2, 3, 7, 8, 9, 16, 17, 18, 21, 23, 24, 25, 27, 30, 32, 34, 35, 37, 39, 42, 44, 45, 47, 48, 49, 50, 53, 54, 55, 57, 64, 65, 66, 70, 71, 74, 75, 76, 77, 78, 79, 80, 81, 83, 85, 86, 90, 93, 94, 99, 102, 103, 104, 108, 109, 110, 111, 112, 115, 116, 118, 119, 122, 124, 126, 128, 129, 132, 133, 134, 136, 140, 141, 142, 143, 144, 146, 147, 149, 150, 155, 156, 158, 164, 170, 174, 175, 176, 178, 179, 180, 182, 189, 191, 192, 194, 195, 198, 199, 200, 202, 203, 205, 206, 211, 213, 214, 215, 217, 219, 220, 221, 225, 230, 231, 232, 233, 236, 238, 240, 241, 246, 248, 252, 255, 257, 259, 264, 266, 267, 269, 270, 271, 272, 274, 277, 278, 279, 280, 281, 282, 283, 284, 288, 289, 291, 292, 293, 294, 297]
BITS=1024
SCALE=1<<BITS
def floordiv(a,b): return a//b
def ceildiv(a,b): return -((-a)//b)
@dataclass(frozen=True)
class IV:
    lo:int; hi:int
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
    return IV(min(floordiv(SCALE*x,y) for x,y in pairs),max(ceildiv(SCALE*x,y) for x,y in pairs))
def half(a): return IV(floordiv(a.lo,2),ceildiv(a.hi,2))
def maxabs_mid(iv): return abs(iv.mid())
def digits10_width(iv):
    if iv.width()==0: return 9999
    return int((BITS-iv.width().bit_length())*0.3010299956639812)
def factor(n):
    return list(sp.factorint(n).keys())
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
    m=len(A); M=[A[i][:]+[b[i]] for i in range(m)]
    for col in range(m):
        candidates=[r for r in range(col,m) if not M[r][col].contains0()]
        assert candidates,("no certified pivot",col)
        piv=max(candidates,key=lambda r:maxabs_mid(M[r][col]))
        M[col],M[piv]=M[piv],M[col]
        pp=M[col][col]
        for r in range(col+1,m):
            f=diviv(M[r][col],pp)
            if f.lo==0 and f.hi==0: continue
            for j in range(col+1,m+1):
                M[r][j]=M[r][j]-f*M[col][j]
            M[r][col]=ZERO
    x=[ZERO]*m
    for i in range(m-1,-1,-1):
        s=M[i][-1]
        for j in range(i+1,m): s=s-M[i][j]*x[j]
        x[i]=diviv(s,M[i][i])
    return x

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
    minpoly=sp.Poly.from_list([sp.Rational(int(q.numerator),int(q.denominator)) for q in K.mod.to_list()],gens=x)
    mp.mp.dps=220
    approx=2*mp.cos(2*mp.pi/n)
    ten=10**180
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
    A=[[ONE for _ in SUPPORT]]+[[cosiv(mm*d) for mm in SUPPORT] for d in NONEDGE]
    rhs=[ONE]+[ZERO]*len(NONEDGE)
    w=solve_interval(A,rhs)
    assert all(v.lo>0 for v in w)
    AT=[[A[j][i] for j in range(len(A))] for i in range(len(A))]
    dual_rhs=[ONE if mm==0 else ZERO for mm in SUPPORT]
    y=solve_interval(AT,dual_rhs)
    a=y[0]; lam=y[1:]
    slacks=[]
    for mm in range(n//2+1):
        if mm in SUPPORT: continue
        q=a
        for coeff,d in zip(lam,NONEDGE): q=q+coeff*cosiv(mm*d)
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
    print("PASS_p",P)
    print("ALL_EXACT_CHECKS_PASS")
if __name__=="__main__": main()
