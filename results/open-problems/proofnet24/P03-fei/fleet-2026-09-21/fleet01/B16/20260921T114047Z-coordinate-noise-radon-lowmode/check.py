#!/usr/bin/env python3
"""Checks for B16 coordinate-noise/Radon bridge and low-mode obstruction.

All exhaustive Boolean checks use exact Fraction arithmetic.
The H_c / kernel asymptotics are numerical diagnostics for an algebraically
proved formula in REPORT.md.
"""
from fractions import Fraction
from math import comb, log2

def walsh(vals):
    N=len(vals); n=(N.bit_length()-1)
    out=[]
    for U in range(N):
        s=0
        for x,v in enumerate(vals):
            s += v * (-1 if ((x & U).bit_count() & 1) else 1)
        out.append(s/Fraction(N))
    return out

def coord_noise(vals,n,i,t):
    a=(1+t)/2; b=(1-t)/2
    return [a*vals[x]+b*vals[x^(1<<i)] for x in range(1<<n)]

def reduced_eta(vals,n,i):
    others=[j for j in range(n) if j!=i]
    out=[]
    for xr in range(1<<(n-1)):
        x=0
        for q,j in enumerate(others):
            if (xr>>q)&1: x |= 1<<j
        out.append(Fraction(1-vals[x]*vals[x^(1<<i)],2))
    return out

def qflip_profile(eta):
    m=(len(eta).bit_length()-1)
    N=1<<m
    return [sum(Fraction(1 if eta[x]!=eta[x^w] else 0) for x in range(N))/N
            for w in range(N)]

def Hc(c):
    p0=(1-2**(1-c))**2
    p1=2**(2-2*c)
    phi=lambda p: -p*log2(p) if p else 0.0
    return phi(p0)+(2**c-1)*phi(p1)

def A_nr(n,r):
    # Unnormalised Walsh multiplier of the random-order raw generator-entropy
    # displacement kernel; REPORT.md derives this formula exactly.
    m=n-1
    s=0.0
    for c in range(2,n+1):
        k=c-1
        avoid=(comb(m-r,k)/comb(m,k)) if k<=m-r else 0.0
        s += Hc(c)*(2**(c-1)*avoid-1.0)
    return s/n

def main():
    coord_cases=0
    radon_cases=0
    for n in range(1,4):
        N=1<<n
        for mask in range(1<<N):
            vals=[1 if (mask>>x)&1 else -1 for x in range(N)]
            for i in range(n):
                eta_full=[Fraction(1-vals[x]*vals[x^(1<<i)],2) for x in range(N)]
                eta_hat=walsh(eta_full)
                alpha=sum(eta_full,Fraction())/N
                for t in (Fraction(0),Fraction(1,2),Fraction(2,3)):
                    g=coord_noise(vals,n,i,t)
                    C=walsh([z*z for z in g])
                    for U in range(N):
                        rhs=(1-(1-t*t)*alpha) if U==0 else -(1-t*t)*eta_hat[U]
                        assert C[U]==rhs
                    coord_cases += 1
    for n in range(2,4):
        N=1<<n
        for mask in range(1<<N):
            vals=[1 if (mask>>x)&1 else -1 for x in range(N)]
            for i in range(n):
                eta=reduced_eta(vals,n,i)
                eh=walsh(eta)
                alpha=sum(eta,Fraction())/len(eta)
                E=alpha*(1-alpha)
                p=qflip_profile(eta)
                ph=walsh(p)
                assert ph[0]==2*E
                for U in range(1,len(p)):
                    assert ph[U]==-2*eh[U]*eh[U]
                centered=sum((z-2*E)**2 for z in p)/len(p)
                assert centered<=4*E*E
                radon_cases += 1

    # Exact combinatorial singleton-multiplier identity, tested by two formulas.
    for n in range(3,16):
        m=n-1
        direct=0.0
        for k in range(1,m+1):
            W=sum(Hc(c)*comb(c-1,k)/comb(m,k) for c in range(k+1,n+1))/n
            direct += comb(m,k)*(1-2*k/m)*W
        assert abs(direct-A_nr(n,1)) < 1e-10

    print("PASS")
    print("coordinate_noise_exact_cases", coord_cases)
    print("radon_exact_cases", radon_cases)
    print("low_mode_table: n A_n1/n A_n2/n A_n3/n")
    for n in (10,20,40,80):
        vals=[A_nr(n,r)/n for r in (1,2,3)]
        print(n, *(f"{x:.12f}" for x in vals))
    print("predicted_limits", f"{2/3:.12f}", f"{1/3:.12f}", f"{1/5:.12f}")
    print("parity_switch_centered_pairing_ratio_to_Inf_i = A_n1")
    for n in (10,20,40,80):
        print(n, f"{A_nr(n,1):.12f}")

if __name__=="__main__":
    main()
