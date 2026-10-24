#!/usr/bin/env python3
"""
R20 / I0100 exact continuation certificate
Afonso S. Bandeira, Randomstrasse 101 (2025), Conjecture 26.

This checker verifies, in exact algebraic arithmetic, matching primal and dual
certificates for the source-normalized quantity

    T_p = theta(complement G_{p,1})

at p = 181.

The previously certified primes {5,13,17,29,41} are preserved by the earlier
immutable checker artifacts/R20/i0100_exact_theta_certificates.py.  This file
adds p=181; it does not re-label finite evidence as a proof of the asymptotic
conjecture.

Symmetry-reduced Delsarte LP, n=(p-1)/2:

Primal
  maximize n*w_0
  subject to
    sum_m w_m = 1
    sum_m w_m cos(2*pi*m*d/n) = 0  for localized NONEDGE differences d
    w_m >= 0.

Here m runs over 0,...,n/2 and w_m is the combined Fourier mass of {m,-m}
(the endpoints are singletons as usual).

Dual
  minimize n*a
  subject to
    a + sum_d lambda_d cos(2*pi*m*d/n) >= 1_{m=0}
    for all m=0,...,n-1.
The lambda_d are free variables.

The certificate is encoded by the primal support.  Exact linear algebra over
Q(2*cos(2*pi/n)) reconstructs the primal weights and the dual multipliers.
Signs are certified using rational isolating intervals for the largest real
root of the exact minimal polynomial; no floating-point sign decision is used.
"""

import sympy as sp

P = 181
N_EXPECTED = [3,4,5,6,7,11,18,19,21,24,25,28,30,31,33,34,36,38,39,40,41,43,45]
SUPPORT = [0,1,6,7,8,9,10,12,13,17,19,20,21,23,24,28,31,34,36,37,41,43,44,45]

def factor(n):
    out=[]
    d=2
    x=n
    while d*d<=x:
        if x%d==0:
            out.append(d)
            while x%d==0:
                x//=d
        d+=1
    if x>1:
        out.append(x)
    return out

def generator_Q(p):
    for g in range(2,p):
        if all(pow(g,(p-1)//q,p)!=1 for q in factor(p-1)):
            return pow(g,2,p)
    raise AssertionError("primitive root not found")

def reduced_nonedge_diffs(p):
    n=(p-1)//2
    Q={x*x % p for x in range(1,p)}
    alpha=generator_Q(p)
    vals=[pow(alpha,j,p) for j in range(n)]
    S={d for d in range(1,n) if (vals[d]-1)%p in Q}
    assert all((n-d) in S for d in S)
    N=[d for d in range(1,n//2+1) if d not in S]
    return n,S,N

def field_cos_table(n):
    # The exact field embedding is alpha=2*cos(2*pi/n).
    K=sp.QQ.algebraic_field(2*sp.cos(2*sp.pi/n))
    alpha=K.unit
    C=[K.zero]*(n//2+1)
    C[0]=2*K.one
    C[1]=alpha
    # C_m(alpha)=2*cos(2*pi*m/n)
    for m in range(1,n//2):
        C[m+1]=alpha*C[m]-C[m-1]
    def cosK(m):
        m%=n
        m=min(m,n-m)
        return C[m]/2
    return K,cosK

def gauss_solve(A,b,K):
    A=[row[:] + [b[i]] for i,row in enumerate(A)]
    n=len(A)
    assert all(len(row)==n+1 for row in A)
    for col in range(n):
        piv=next(i for i in range(col,n) if A[i][col]!=K.zero)
        A[col],A[piv]=A[piv],A[col]
        inv=K.one/A[col][col]
        A[col]=[z*inv for z in A[col]]
        for i in range(n):
            if i==col:
                continue
            f=A[i][col]
            if f!=K.zero:
                A[i]=[A[i][j]-f*A[col][j] for j in range(n+1)]
    return [A[i][-1] for i in range(n)]

def rat(q):
    return sp.Rational(int(q.numerator),int(q.denominator))

def interval_mul(I,J):
    a,b=I; c,d=J
    vals=[a*c,a*d,b*c,b*d]
    return min(vals),max(vals)

def interval_eval(coeffs,I):
    out=(sp.Rational(0),sp.Rational(0))
    for c in coeffs:
        a,b=interval_mul(out,I)
        q=rat(c)
        out=(a+q,b+q)
    return out

def alpha_interval(K, digits=45):
    # Every conjugate of 2*cos(2*pi/n) is real.  The selected embedding
    # 2*cos(2*pi/n), n>2, is the largest real conjugate.
    x=sp.Symbol("x")
    mp=sp.Poly.from_list([rat(q) for q in K.mod.to_list()],gens=x)
    intervals=mp.intervals(eps=sp.Rational(1,10**digits))
    assert sum(mult for _,mult in intervals)==mp.degree()
    assert all(mult==1 for _,mult in intervals)
    return mp,max((iv for iv,_ in intervals),key=lambda I:I[0])

def sign_exact(e,K,I):
    if e==K.zero:
        return 0
    J=interval_eval(e.to_list(),I)
    if J[0]>0:
        return 1
    if J[1]<0:
        return -1
    raise AssertionError(("sign not separated by exact interval",J,e))

def main():
    assert P%4==1 and sp.isprime(P)
    n,S,N=reduced_nonedge_diffs(P)
    assert n==90
    assert N==N_EXPECTED
    assert len(S)==(P-5)//4
    assert len(SUPPORT)==len(N)+1

    K,cosK=field_cos_table(n)
    minpoly,I=alpha_interval(K)

    # Reconstruct exact primal from normalization + all nonedge equalities.
    Apr=[[K.one for m in SUPPORT]]
    Apr += [[cosK(m*d) for m in SUPPORT] for d in N]
    w=gauss_solve(Apr,[K.one]+[K.zero]*len(N),K)

    # Reconstruct exact dual from complementary-slackness equalities at SUPPORT.
    Adu=[[K.one]+[cosK(m*d) for d in N] for m in SUPPORT]
    y=gauss_solve(
        Adu,
        [K.one if m==0 else K.zero for m in SUPPORT],
        K
    )
    a=y[0]
    lam=y[1:]

    # Exact primal feasibility.
    assert sum(w,K.zero)==K.one
    assert all(sign_exact(v,K,I)>0 for v in w)
    for d in N:
        assert sum((v*cosK(m*d) for m,v in zip(SUPPORT,w)),K.zero)==K.zero

    # Exact dual feasibility.
    slacks=[]
    for m in range(n):
        lhs=a+sum((v*cosK(m*d) for v,d in zip(lam,N)),K.zero)
        slack=lhs-(K.one if m==0 else K.zero)
        assert sign_exact(slack,K,I)>=0
        slacks.append(slack)

    # Exact equality of objectives.
    w0=w[SUPPORT.index(0)]
    assert w0==a
    theta=n*w0
    assert n*a==theta

    # Complementary slackness exactly on every positive primal frequency.
    assert all(slacks[m]==K.zero for m in SUPPORT)

    print("I0100 / Conjecture 26 exact continuation certificate")
    print("p =",P," n =",n," field_degree =",minpoly.degree())
    print("nonedge_difference_reps =",N)
    print("primal_support =",SUPPORT)
    print("field_minpoly =",minpoly.as_expr())
    print("w0_ANP_descending_coefficients =",[str(q) for q in w0.to_list()])
    print("dual_a_equals_w0 =",a==w0)
    print("theta_ANP_descending_coefficients =",[str(q) for q in theta.to_list()])
    print("theta_numeric_30d =",sp.N(K.to_sympy(theta),30))
    print("sqrt(p/2)_numeric_30d =",sp.N(sp.sqrt(sp.Rational(P,2)),30))
    print("ratio_numeric_30d =",sp.N(K.to_sympy(theta)/sp.sqrt(sp.Rational(P,2)),30))
    print("strict_positive_primal_weights =",len(w))
    print("dual_zero_slacks =",sum(s==K.zero for s in slacks),"of",n)
    print("covered_primes_before = [5, 13, 17, 29, 41]")
    print("covered_primes_after = [5, 13, 17, 29, 41, 181]")
    print("largest_exact_prime = 181")
    print("PASS: matching exact primal/dual certificates at p=181")

if __name__=="__main__":
    main()
