#!/usr/bin/env python3
"""
R20 / I0100 exact certificate checker
Afonso Bandeira, Randomstrasse 2025, Conjecture 26.

Target quantity:
    T_p = vartheta(complement of G_{p,1})
where G_{p,1} is the Paley graph induced on the nonzero quadratic
residues (the neighbors of 0).

For each covered prime, this checks matching exact primal and dual
certificates in the symmetry-reduced Delsarte LP.  All arithmetic used
in certificate verification is symbolic/exact (SymPy algebraic
numbers/trigonometric constants), not floating point.

Reduced LP.  Let n=(p-1)/2 and identify the quadratic-residue group Q
with Z_n using a generator alpha.  Let N be the set of nonzero
difference classes corresponding to NONEDGES of the localized graph
(i.e. edges of its complement), reduced modulo d ~ -d.

Primal:
    maximize n*w_0
    sum_m w_m = 1
    sum_m w_m cos(2*pi*m*d/n) = 0,  d in N
    w_m >= 0
where m ranges 0..floor(n/2); w_m is the combined Fourier mass of
the pair {m,-m} (singletons at 0 and n/2).

Dual:
    minimize n*a
    a + sum_{d in N} lambda_d cos(2*pi*m*d/n) >= 1_{m=0}
    for every Fourier frequency m=0,...,n-1.

Matching objectives certify the exact theta value.
"""
import sympy as sp

PI = sp.pi
SQ2 = sp.sqrt(2)
SQ5 = sp.sqrt(5)

def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d*d <= n:
        if n % d == 0:
            return n == d
        d += 1
    return True

def factor(n):
    out=[]
    d=2
    while d*d<=n:
        if n%d==0:
            out.append(d)
            while n%d==0:
                n//=d
        d+=1
    if n>1: out.append(n)
    return out

def generator_Q(p):
    """Canonical generator alpha=g^2, where g is the least primitive root of F_p^*."""
    for g in range(2,p):
        if all(pow(g,(p-1)//q,p)!=1 for q in factor(p-1)):
            return pow(g,2,p)
    raise AssertionError("no primitive root")

def reduced_nonedge_diffs(p):
    assert is_prime(p) and p % 4 == 1
    n=(p-1)//2
    Q={x*x % p for x in range(1,p)}
    a=generator_Q(p)
    vals=[pow(a,j,p) for j in range(n)]
    S=set()
    for d in range(1,n):
        if (vals[d]-1) % p in Q:
            S.add(d)
    assert all(((n-d) in S) for d in S)
    N=[]
    for d in range(1,n//2+1):
        if d not in S:
            N.append(d)
    return n,S,N

def ezero(expr):
    return sp.simplify(sp.radsimp(sp.expand_trig(sp.trigsimp(expr, method='fu'))))

def nonnegative(expr):
    e=ezero(expr)
    if e == 0:
        return True
    q=sp.ask(sp.Q.nonnegative(e))
    if q is not None:
        return bool(q)
    c=sp.cos(PI/7)
    if ezero(e-(-1+2*c)) == 0:
        return True
    if ezero(e-4*c*(1-c)) == 0:
        return True
    raise AssertionError(f"sign not certified exactly: {e}")

c7=sp.cos(PI/7)
a29=c7/(2*(1+c7))
b29=1/(2*(1+c7))

sA=sp.sqrt(10+2*SQ5)
sB=sp.sqrt(50+10*SQ5)
w41_1= -sA/16 - SQ5/20 + sB/80 + sp.Rational(1,4)
w41_9= -SQ5/20 - sB/80 + sA/16 + sp.Rational(1,4)

CERTS = {
    5: {
        "primal": {0:sp.Rational(1,2),1:sp.Rational(1,2)},
        "dual_a": sp.Rational(1,2),
        "dual_lam": {1:sp.Rational(1,2)},
        "theta": sp.Integer(1),
    },
    13: {
        "primal": {0:sp.Rational(1,3),1:sp.Rational(1,2),2:sp.Rational(1,6)},
        "dual_a": sp.Rational(1,3),
        "dual_lam": {2:sp.Rational(2,3)},
        "theta": sp.Integer(2),
    },
    17: {
        "primal": {0:1-1/SQ2,1:SQ2-1,2:1-1/SQ2},
        "dual_a": 1-1/SQ2,
        "dual_lam": {2:1-1/SQ2,3:SQ2-1},
        "theta": 8-4*SQ2,
    },
    29: {
        "primal": {0:a29,3:b29,4:b29,7:a29},
        "dual_a": a29,
        "dual_lam": {2:b29,5:b29,7:a29},
        "theta": 7*c7/(1+c7),
    },
    41: {
        "primal": {
            0:SQ5/10,
            1:w41_1,
            4:SQ5/40+sp.Rational(1,8),
            5:SQ5/10,
            6:sp.Rational(3,8)-SQ5/8,
            9:w41_9,
        },
        "dual_a": SQ5/10,
        "dual_lam": {2:(5-SQ5)/20,6:(5+SQ5)/20,8:(5-SQ5)/10},
        "theta": 2*SQ5,
    },
}

def check_prime(p, cert):
    n,S,N=reduced_nonedge_diffs(p)
    w=cert["primal"]
    assert all(0 <= m <= n//2 for m in w)
    assert all(d in N for d in cert["dual_lam"])
    assert ezero(sum(w.values())-1) == 0
    for val in w.values():
        assert nonnegative(val)
    for d in N:
        lhs=sum(val*sp.cos(2*PI*m*d/n) for m,val in w.items())
        assert ezero(lhs) == 0, (p,d,ezero(lhs))
    pobj=ezero(n*w.get(0,0))
    assert ezero(pobj-cert["theta"]) == 0

    a=cert["dual_a"]
    lam=cert["dual_lam"]
    assert nonnegative(a)
    for m in range(n):
        lhs=a+sum(val*sp.cos(2*PI*m*d/n) for d,val in lam.items())
        rhs=1 if m==0 else 0
        slack=ezero(lhs-rhs)
        assert nonnegative(slack), (p,m,slack)
    dobj=ezero(n*a)
    assert ezero(dobj-cert["theta"]) == 0
    assert ezero(pobj-dobj) == 0

    assert len(S) == (p-5)//4
    assert len(N) == (n-1-len(S))//2 + (1 if n%2==0 and (n//2 not in S) else 0)
    return n,N,pobj

def main():
    covered=[]
    for p in sorted(CERTS):
        n,N,T=check_prime(p,CERTS[p])
        covered.append(p)
        print(f"p={p:2d} n={n:2d} N={N} theta_exact={sp.sstr(T)} "
              f"theta_numeric={sp.N(T,18)} ratio={sp.N(T/sp.sqrt(sp.Rational(p,2)),18)}")
    print("covered_primes =",covered)
    print("largest_exact_prime =",max(covered))
    print("PASS: matching exact primal/dual certificates for every covered prime")

if __name__ == "__main__":
    main()
