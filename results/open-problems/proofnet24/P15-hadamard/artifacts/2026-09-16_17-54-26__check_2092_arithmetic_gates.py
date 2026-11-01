#!/usr/bin/env python3
"""Exact arithmetic gates for standard construction routes at n=2092.

This does NOT prove nonexistence in any family beyond the stated elementary
parameter gates. It only checks the integer facts used in the P15 report.
"""
from math import isqrt

N=2092
q1=N-1
q2=N//2-1
qM=N//4


def factor(n):
    out=[]
    d=2
    while d*d<=n:
        while n%d==0:
            out.append(d); n//=d
        d += 1 if d==2 else 2
    if n>1: out.append(n)
    return out


def is_prime(n):
    return n>=2 and factor(n)==[n]

print(f"N={N} factorization={factor(N)}")
print(f"v=N/4={qM} prime={is_prime(qM)} mod4={qM%4}")
print(f"Paley_I_parameter_q=N-1={q1} factorization={factor(q1)}")
print(f"Paley_II_parameter_q=N/2-1={q2} factorization={factor(q2)}")
print(f"Miyamoto_standard_q=N/4={qM} requires_q_mod4_eq_1 actual={qM%4}")
print(f"Cooper_Wallis_requires_t_times_w=N/4={qM}; since_prime_only_positive_factor_pairs=(1,{qM}),({qM},1)")
assert factor(N)==[2,2,523]
assert is_prime(523)
assert 523%4==3
assert factor(2091)==[3,17,41]
assert factor(1045)==[5,11,19]
print("VERDICT: arithmetic gates checked exactly")
print("SCOPE: these are only standard parameter-route exclusions/reductions, not nonexistence of H(2092)")
