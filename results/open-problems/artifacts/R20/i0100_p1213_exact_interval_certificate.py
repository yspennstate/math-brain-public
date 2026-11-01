#!/usr/bin/env python3
import sympy as sp, mpmath as mp, time
from dataclasses import dataclass
P=1213
N=606
NONEDGE=[2, 6, 9, 10, 14, 15, 16, 20, 21, 24, 27, 29, 30, 35, 36, 38, 39, 41, 42, 43, 44, 46, 47, 49, 52, 54, 57, 58, 59, 60, 61, 62, 63, 65, 68, 69, 72, 75, 76, 78, 81, 84, 89, 94, 96, 97, 98, 99, 100, 102, 103, 104, 110, 115, 121, 122, 128, 130, 131, 132, 133, 135, 136, 137, 138, 140, 142, 145, 146, 148, 149, 152, 153, 156, 157, 158, 165, 166, 168, 169, 170, 171, 175, 177, 179, 180, 182, 183, 187, 189, 191, 192, 194, 196, 197, 199, 200, 202, 204, 209, 212, 213, 214, 218, 220, 222, 224, 228, 229, 230, 231, 232, 233, 237, 239, 240, 241, 243, 244, 245, 246, 248, 249, 252, 253, 255, 257, 259, 260, 262, 268, 269, 272, 277, 279, 280, 281, 283, 284, 285, 287, 289, 291, 294, 295, 296, 297, 298, 300, 301, 302, 303]
SUPPORT=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 14, 15, 16, 17, 20, 21, 22, 23, 25, 26, 27, 29, 33, 34, 35, 41, 44, 46, 48, 49, 52, 53, 56, 57, 59, 62, 64, 66, 67, 73, 75, 76, 77, 78, 82, 85, 90, 91, 92, 95, 97, 98, 99, 101, 102, 103, 105, 107, 108, 109, 112, 113, 114, 118, 120, 121, 126, 129, 130, 132, 133, 134, 137, 138, 140, 141, 144, 147, 148, 150, 152, 153, 155, 157, 158, 160, 161, 162, 163, 164, 165, 166, 168, 170, 171, 173, 174, 177, 180, 181, 182, 184, 186, 190, 191, 192, 193, 196, 197, 198, 201, 203, 207, 211, 213, 214, 215, 217, 220, 221, 224, 227, 228, 229, 230, 235, 236, 239, 240, 241, 242, 244, 245, 248, 249, 251, 253, 255, 258, 261, 262, 263, 267, 272, 274, 275, 277, 282, 288, 292, 293, 301]
BITS=1152
SCALE=1<<BITS
def floordiv(a,b): return a//b
def ceildiv(a,b): return -((-a)//b)
@dataclass(frozen=True)
class IV:
    lo:int
    hi:int
    def __post_init__(self): assert self.lo<=self.hi
    def __add__(self,o): return IV(self.lo+o.lo,self.hi+o.hi)
    def __sub__(self,o): return IV(self.lo-o.hi,self.hi-o.lo)
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
    for x0 in (a.lo,a.hi):
        for y0 in (b.lo,b.hi):
            x,y=x0,y0
            if y<0: x,y=-x,-y
            pairs.append((x,y))
    return IV(min(floordiv(SCALE*x,y) for x,y in pairs),max(ceildiv(SCALE*x,y) for x,y in pairs))
def half(a): return IV(floordiv(a.lo,2),ceildiv(a.hi,2))
def digits10_width(iv):
    if iv.width()==0: return 9999
    return int((BITS-iv.width().bit_length())*0.3010299956639812)
def solve_interval(A,b):
    m=len(A); M=[A[i][:]+[b[i]] for i in range(m)]
    for col in range(m):
        candidates=[r for r in range(col,m) if not M[r][col].contains0()]
        assert candidates,("no certified pivot",col)
        piv=max(candidates,key=lambda r:abs(M[r][col].mid()))
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
def factor(n): return list(sp.factorint(n).keys())
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
def dec(iv,dig=50):
    return str(sp.N(sp.Rational(iv.lo+iv.hi,2*SCALE),dig))
def main():
    t=time.time()
    assert sp.isprime(P) and P%4==1
    n,nchk=reduced_nonedge_diffs(P)
    assert n==N and nchk==NONEDGE
    assert len(SUPPORT)==len(NONEDGE)+1
    x=sp.Symbol("x")
    K=sp.QQ.algebraic_field(2*sp.cos(2*sp.pi/n))
    minpoly=sp.Poly.from_list([sp.Rational(int(q.numerator),int(q.denominator)) for q in K.mod.to_list()],gens=x)
    mp.mp.dps=260
    approx=2*mp.cos(2*mp.pi/n)
    ten=10**230
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
        assert q.lo>0,("dual slack",mm,dec(q,30),digits10_width(q))
        slacks.append(q)
    w0=w[SUPPORT.index(0)]
    assert not (w0.hi<a.lo or a.hi<w0.lo)
    theta=IV(n*w0.lo,n*w0.hi)
    target=sp.sqrt(sp.Rational(P,2))
    overshoot=2*theta.lo*theta.lo>P*SCALE*SCALE
    print("I0100 / Conjecture 26 exact continuation certificate")
    print("p =",P,"n =",n,"field_degree =",minpoly.degree(),"bits =",BITS)
    print("nonedge_half_constraints =",len(NONEDGE))
    print("strict_positive_primal_half_weights =",len(w))
    print("strict_positive_nonsupport_half_slacks =",len(slacks))
    print("theta_interval_mid =",dec(theta,60))
    print("sqrt_p_over_2 =",sp.N(target,60))
    print("ratio_mid =",sp.N(sp.Rational(theta.mid(),SCALE)/target,50))
    print("min_weight =",dec(min(w,key=lambda z:z.lo),30))
    print("min_slack =",dec(min(slacks,key=lambda z:z.lo),30))
    print("min_weight_digits =",min(digits10_width(v) for v in w))
    print("min_slack_digits =",min(digits10_width(v) for v in slacks))
    print("certified_theta_gt_sqrt_p_over_2 =",overshoot)
    print("elapsed_seconds =",time.time()-t)
    print("PASS_p",P)
    print("ALL_EXACT_CHECKS_PASS")
if __name__=="__main__": main()
