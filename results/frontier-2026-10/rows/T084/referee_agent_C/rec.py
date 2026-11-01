"""Own recursion: Z(K_n minus D) for D among special vertices, bivariate in lam (flint) and q (list index).
N = Ze Zf - Z Zef by deletion: Ze = Z0 - Z{e}, Zef = Z0 - Z{e} - Z{f} + Z{ef}. Then Bernstein check of N/u."""
import sys, itertools
from functools import lru_cache
from math import comb
from flint import fmpz_poly
L1 = fmpz_poly([1,1])
def bpow(k): return L1**k

def Zgraph(n, S, D):
    S=tuple(S); D=set(frozenset(x) for x in D)
    def dcount(B): return sum(1 for x in D if x<=B)
    @lru_cache(None)
    def T(B,t): return bpow(comb(len(B)+t,2)-dcount(B))
    @lru_cache(None)
    def C0(t):
        tot=bpow(comb(t,2))
        for k in range(1,t): tot -= comb(t-1,k-1)*C0(k)*bpow(comb(t-k,2))
        return tot
    def splits(B):
        b0=min(B); rest=sorted(B-{b0})
        for r in range(len(rest)+1):
            for c in itertools.combinations(rest,r):
                yield frozenset((b0,)+c)
    @lru_cache(None)
    def Conn(B,t):
        if not B: return C0(t)
        tot=T(B,t)
        for Bp in splits(B):
            for tp in range(t+1):
                if Bp==B and tp==t: continue
                tot -= comb(t,tp)*Conn(Bp,tp)*T(B-Bp,t-tp)
        return tot
    def padd(a,b):
        r=[fmpz_poly(0)]*max(len(a),len(b))
        for i,x in enumerate(a): r[i]+=x
        for i,x in enumerate(b): r[i]+=x
        return r
    def shiftmul(a,c):  # q * c * a
        return [fmpz_poly(0)]+[c*x for x in a]
    @lru_cache(None)
    def Zord(t):
        if t==0: return (fmpz_poly(1),)
        r=[]
        for k in range(1,t+1): r=padd(r,shiftmul(list(Zord(t-k)),comb(t-1,k-1)*C0(k)))
        return tuple(r)
    @lru_cache(None)
    def Zq(B,t):
        if not B: return Zord(t)
        r=[]
        for Bp in splits(B):
            for tp in range(t+1):
                r=padd(r,shiftmul(list(Zq(B-Bp,t-tp)),comb(t,tp)*Conn(Bp,tp)))
        return tuple(r)
    return list(Zq(frozenset(S), n-len(S)))

def lin(*terms):
    r=[]
    for c,a in terms:
        m=max(len(r),len(a)); r=r+[fmpz_poly(0)]*(m-len(r))
        for i,x in enumerate(a): r[i]+=c*x
    return r
def mulq(a,b):
    r=[fmpz_poly(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): r[i+j]+=x*y
    return r
def q_to_u(a):  # sum a_k q^k, q=1-u
    r=[fmpz_poly(0)]*len(a)
    for k,x in enumerate(a):
        for j in range(k+1): r[j]+=x*(comb(k,j)*(-1)**j)
    return r
def Npoly(n, kind):
    if kind=='adj': S=(0,1,2); e=(0,1); f=(0,2)
    else: S=(0,1,2,3); e=(0,1); f=(2,3)
    Z0=Zgraph(n,S,[]); Ze_=Zgraph(n,S,[e]); Zf_=Zgraph(n,S,[f]); Zef_=Zgraph(n,S,[e,f])
    Ze=lin((1,Z0),(-1,Ze_)); Zf=lin((1,Z0),(-1,Zf_)); Zef=lin((1,Z0),(-1,Ze_),(-1,Zf_),(1,Zef_))
    N=lin((1,mulq(Ze,Zf)),(-1,mulq(Z0,Zef)))
    N=q_to_u(N)
    while N and N[-1]==0: N.pop()
    return N
def bern(N):
    assert N[0]==0
    a=N[1:]; d=len(a)-1
    out=[]
    for j in range(d+1):
        bj=fmpz_poly(0)
        for i in range(j+1): bj+=a[i]*comb(d-i,j-i)
        out.append(bj)
    return d,out
if __name__=='__main__':
    kind=sys.argv[1]
    for n in range(int(sys.argv[2]),int(sys.argv[3])+1):
        N=Npoly(n,kind); d,b=bern(N)
        neg=[(j,i) for j,bj in enumerate(b) for i,c in enumerate(bj.coeffs()) if c<0]
        zero=[j for j,bj in enumerate(b) if bj==0]
        print(kind,n,'deg N/u',d,'neg coeffs',len(neg),neg[:3],'zero b_j',zero,'b0',b[0].coeffs()[:3],'lowlam', min(bj.coeffs().__len__() and next(i for i,c in enumerate(bj.coeffs()) if c) for bj in b if bj!=0), flush=True)
