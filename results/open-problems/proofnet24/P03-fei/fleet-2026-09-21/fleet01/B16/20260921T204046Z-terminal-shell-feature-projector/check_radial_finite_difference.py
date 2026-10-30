#!/usr/bin/env python3
"""Finite checks for B16 radial finite-difference supplement."""
from fractions import Fraction
from math import comb, exp, lgamma, pi

def chi(A, q):
    return -1 if ((A & q).bit_count() & 1) else 1

def mfrac(q, N):
    return Fraction(N - 2*q.bit_count(), N)

def pbin(m, j):
    if j < 0 or j > m:
        return Fraction(0)
    return Fraction(comb(m, j), 1 << m)

def nabla_p(m, a, r):
    return sum(
        Fraction(((-1)**j)*comb(r, j), 1) * pbin(m, a-j)
        for j in range(r+1)
    )

def lambda_threshold_direct(N, k, a):
    hi = Fraction((N-2*a)**2, N*N)
    lo = Fraction((N-2*(a+1))**2, N*N)
    u = (hi+lo)/2
    A = (1 << k)-1 if k else 0
    G = 1 << N
    return Fraction(sum(
        chi(A, q)
        for q in range(G)
        if mfrac(q, N)**2 >= u
    ), G)

def lambda_threshold_formula(N, k, a):
    if k & 1:
        return Fraction(0)
    if k == 0:
        raise ValueError("boundary formula is for k>=2")
    return Fraction(1, 1 << (k-1)) * nabla_p(N-k, a, k-1)

def mu_direct(N, k):
    vals = sorted({mfrac(q, N)**2 for q in range(1 << N)})
    ans = Fraction(0)
    A = (1 << k)-1 if k else 0
    for lo, hi in zip(vals[:-1], vals[1:]):
        u = (lo+hi)/2
        lam = Fraction(sum(
            chi(A, q)
            for q in range(1 << N)
            if mfrac(q, N)**2 >= u
        ), 1 << N)
        ans += (hi-lo)*lam*lam
    return ans

def mu_formula(N, k):
    s = sum(
        Fraction(N-2*a-1, 1) * nabla_p(N-k, a, k-1)**2
        for a in range(N//2)
    )
    return Fraction(16, (4**k)*N*N) * s

def beta_bound(N, k):
    logB = lgamma(k-0.5)+lgamma(N-k+0.5)-lgamma(N)
    return 4.0/(pi*N)*exp(logB)

def lambda_laplace_direct(N, k, t):
    A=(1<<k)-1 if k else 0
    return sum(
        exp(-t*float(mfrac(q,N)**2))*chi(A,q)
        for q in range(1<<N)
    )/(1<<N)

def lambda_laplace_fd(N, k, t):
    m=N-k
    return (2**(-k))*sum(
        comb(m,j)/(2**m)*
        sum(
            ((-1)**ell)*comb(k,ell)*
            exp(-t*(1-2*(j+ell)/N)**2)
            for ell in range(k+1)
        )
        for j in range(m+1)
    )

def main():
    threshold_checks=0
    mu_checks=0
    beta_checks=0
    laplace_checks=0

    for N in (4,8):
        for k in range(1,N+1):
            for a in range(N//2):
                got=lambda_threshold_direct(N,k,a)
                want=Fraction(0) if (k&1) else lambda_threshold_formula(N,k,a)
                assert got==want, (N,k,a,got,want)
                threshold_checks += 1
        for k in range(2,N+1,2):
            md=mu_direct(N,k)
            mf=mu_formula(N,k)
            assert md==mf, (N,k,md,mf)
            mu_checks += 1
            assert float(md) <= beta_bound(N,k)+1e-15
            beta_checks += 1

    N=8
    for k in range(N+1):
        for t in (0.1,0.7,2.0,5.0):
            a=lambda_laplace_direct(N,k,t)
            b=lambda_laplace_fd(N,k,t)
            assert abs(a-b)<2e-14, (k,t,a,b)
            laplace_checks += 1

    print("PASS")
    print("threshold_boundary_checks",threshold_checks)
    print("integrated_mu_checks",mu_checks)
    print("beta_envelope_checks",beta_checks)
    print("laplace_finite_difference_checks",laplace_checks)

if __name__=="__main__":
    main()
