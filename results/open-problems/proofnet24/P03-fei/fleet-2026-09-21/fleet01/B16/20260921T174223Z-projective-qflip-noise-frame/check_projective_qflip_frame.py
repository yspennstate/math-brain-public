#!/usr/bin/env python3
from fractions import Fraction

P_GRID = (Fraction(1,64), Fraction(1,16), Fraction(1,4), Fraction(1,2))

def corr_numerators(mask,n):
    N=1<<n
    f=[1 if (mask>>x)&1 else -1 for x in range(N)]
    return [sum(f[x]*f[x^u] for x in range(N)) for u in range(N)]

def beta_from_s(s,N):
    return Fraction(N-abs(s),2*N)

def e_from_s(s,N):
    return Fraction(N*N-s*s,4*N*N)

functions=0
triangle_checks=0
scalar_checks=0
noise_checks=0
max_ratio=Fraction(0)
max_witness=None

for n in range(1,5):
    N=1<<n
    for mask in range(1<<N):
        s=corr_numerators(mask,n)
        beta=[beta_from_s(z,N) for z in s]
        E=[e_from_s(z,N) for z in s]
        functions+=1

        for u in range(N):
            scalar_checks+=1
            assert E[u]*E[u] <= Fraction(4,27)*beta[u]
            for v in range(N):
                triangle_checks+=1
                assert beta[u^v] <= beta[u]+beta[v]

        J=sum(beta[1<<i] for i in range(n))
        if J:
            for p in P_GRID:
                lhs=Fraction(0)
                for u in range(N):
                    k=u.bit_count()
                    lhs += (p**k)*((1-p)**(n-k))*E[u]*E[u]
                rhs=Fraction(4,27)*p*J
                noise_checks+=1
                assert lhs <= rhs
                ratio=lhs/(p*J)
                if ratio>max_ratio:
                    max_ratio=ratio
                    max_witness=(n,mask,p)

print("PASS")
print("functions",functions)
print("triangle_checks",triangle_checks)
print("scalar_checks",scalar_checks)
print("noise_checks",noise_checks)
print("max_observed_E2_over_pJ",f"{max_ratio.numerator}/{max_ratio.denominator}",float(max_ratio))
print("max_witness",max_witness)
print("theoretical_constant",f"{Fraction(4,27).numerator}/{Fraction(4,27).denominator}",float(Fraction(4,27)))
