#!/usr/bin/env python3
"""Exact primal/dual certificate for R20 I0100 at p=241.

The high-precision embedding solves are used only to generate rational power-basis
coefficients. Acceptance uses exact arithmetic in Q(2*cos(2*pi/120)) plus
rational root-isolation sign checks for every primal weight and all dual slacks.
"""
import math
from fractions import Fraction
import mpmath as mp
import sympy as sp

P=241
N_EXPECTED=[5,6,11,12,13,14,16,19,23,27,28,30,32,33,34,36,37,39,40,41,42,43,45,47,48,49,52,53,55,57]
SUPPORT=[0,1,2,4,5,6,10,11,12,13,14,15,16,19,24,28,29,31,33,34,35,38,39,41,45,47,49,50,54,58,60]
PREC=230
MAXDEN=10**110

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
    alpha=generator_Q(p)
    vals=[pow(alpha,j,p) for j in range(n)]
    S={d for d in range(1,n) if (vals[d]-1)%p in Q}
    assert all((n-d) in S for d in S)
    return n,[d for d in range(1,n//2+1) if d not in S]

def conjugate_coeffs(n,N,support,dual):
    ks=[k for k in range(1,n//2+1) if math.gcd(k,n)==1]
    assert len(ks)==int(sp.totient(n)//2)
    mp.mp.dps=PREC
    sols=[]; q=len(support)
    for k in ks:
        A=mp.matrix(q); b=mp.matrix(q,1)
        if not dual:
            for j,m in enumerate(support): A[0,j]=1
            b[0]=1
            for i,d in enumerate(N,1):
                for j,m in enumerate(support):
                    A[i,j]=mp.cos(2*mp.pi*k*m*d/n)
                b[i]=0
        else:
            for i,m in enumerate(support):
                A[i,0]=1
                for j,d in enumerate(N,1):
                    A[i,j]=mp.cos(2*mp.pi*k*m*d/n)
                b[i]=1 if m==0 else 0
        sols.append(mp.lu_solve(A,b))
    alphas=[2*mp.cos(2*mp.pi*k/n) for k in ks]
    V=mp.matrix([[alphas[i]**r for r in range(len(ks))] for i in range(len(ks))])
    Vinv=V**-1
    coeff=[]
    for j in range(q):
        vals=mp.matrix([sols[i][j] for i in range(len(ks))])
        c=Vinv*vals
        coeff.append([Fraction(mp.nstr(c[r],PREC-5)).limit_denominator(MAXDEN) for r in range(len(ks))])
    return coeff

def rat(q): return sp.Rational(int(q.numerator),int(q.denominator))
def interval_mul(I,J):
    a,b=I; c,d=J; vals=[a*c,a*d,b*c,b*d]; return min(vals),max(vals)
def interval_eval(coeffs,I):
    out=(sp.Rational(0),sp.Rational(0))
    for c in coeffs:
        lo,hi=interval_mul(out,I); q=rat(c); out=(lo+q,hi+q)
    return out

def main():
    assert sp.isprime(P) and P%4==1
    n,N=reduced_nonedge_diffs(P)
    assert n==120 and N==N_EXPECTED and len(SUPPORT)==len(N)+1
    pc=conjugate_coeffs(n,N,SUPPORT,False)
    dc=conjugate_coeffs(n,N,SUPPORT,True)

    K=sp.QQ.algebraic_field(2*sp.cos(2*sp.pi/n)); alpha=K.unit
    assert K.mod.degree()==16
    C=[K.zero]*(n//2+1); C[0]=2*K.one; C[1]=alpha
    for m in range(1,n//2): C[m+1]=alpha*C[m]-C[m-1]
    def cosK(m):
        m%=n; m=min(m,n-m); return C[m]/2
    def elem(fracs):
        z=K.zero; pw=K.one
        for fr in fracs:
            z += K.convert(sp.Rational(fr.numerator,fr.denominator))*pw
            pw *= alpha
        return z
    w=[elem(v) for v in pc]; y=[elem(v) for v in dc]; a=y[0]; lam=y[1:]

    # Exact reconstruction/feasibility checks.
    assert sum(w,K.zero)==K.one
    for d in N:
        assert sum((v*cosK(m*d) for m,v in zip(SUPPORT,w)),K.zero)==K.zero
    assert a==w[0]
    for m in SUPPORT:
        lhs=a+sum((v*cosK(m*d) for v,d in zip(lam,N)),K.zero)
        assert lhs==(K.one if m==0 else K.zero)

    # Exact selected-embedding signs using rational root isolation.
    x=sp.Symbol('x')
    minpoly=sp.Poly.from_list([rat(q) for q in K.mod.to_list()],gens=x)
    intervals=minpoly.intervals(eps=sp.Rational(1,10**55))
    assert len(intervals)==minpoly.degree() and all(mult==1 for _,mult in intervals)
    I=max((iv for iv,_ in intervals),key=lambda J:J[0])
    def sign_exact(e):
        if e==K.zero: return 0
        J=interval_eval(e.to_list(),I)
        if J[0]>0: return 1
        if J[1]<0: return -1
        raise AssertionError(('interval does not separate sign',J))

    assert all(sign_exact(v)>0 for v in w)
    slacks=[]
    for m in range(n):
        lhs=a+sum((v*cosK(m*d) for v,d in zip(lam,N)),K.zero)
        slack=lhs-(K.one if m==0 else K.zero)
        assert sign_exact(slack)>=0
        slacks.append(slack)

    theta=n*w[0]
    maxden=max(len(str(fr.denominator)) for row in pc+dc for fr in row)
    print('I0100 / Conjecture 26 exact continuation certificate')
    print('p =',P,'n =',n,'field_degree =',minpoly.degree())
    print('nonedge_difference_reps =',N)
    print('primal_support =',SUPPORT)
    print('max_reconstructed_denominator_digits =',maxden)
    print('dual_a_equals_w0 =',a==w[0])
    print('theta_numeric_30d =',sp.N(K.to_sympy(theta),30))
    print('sqrt(p/2)_numeric_30d =',sp.N(sp.sqrt(sp.Rational(P,2)),30))
    print('ratio_numeric_30d =',sp.N(K.to_sympy(theta)/sp.sqrt(sp.Rational(P,2)),30))
    print('strict_positive_primal_weights =',len(w))
    print('dual_zero_slacks =',sum(s==K.zero for s in slacks),'of',n)
    print('covered_primes_before = [5, 13, 17, 29, 41, 181]')
    print('covered_primes_after = [5, 13, 17, 29, 41, 181, 241]')
    print('largest_exact_prime = 241')
    print('PASS: matching exact primal/dual certificates at p=241')

if __name__=='__main__': main()
