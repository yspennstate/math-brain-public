#!/usr/bin/env python3
from fractions import Fraction

def ceil_div(a,b):
    return (a+b-1)//b

def check(N,W):
    assert N>=1 and W>=0 and 2*W+1<=N
    s=W+1
    K=ceil_div(N,s)
    q=N//K
    r=N-q*K
    lo=q
    hi=q+(1 if r else 0)
    assert q>=1
    assert q*K+r==N
    assert hi<=W+1

    # Exact lower bound q >= ceil((2W+1)/3).
    qlower=ceil_div(2*W+1,3)
    assert q>=qlower
    assert 2*(2*W+1) <= 6*q

    # Common GOE scale a^2=q/[2(2W+1)].
    v=Fraction(1,2*W+1)
    a2=Fraction(q,2*(2*W+1))
    for m in {lo,hi}:
        if m<=0: continue
        diag_goe=2*a2/Fraction(m,1)
        off_goe=a2/Fraction(m,1)
        assert diag_goe <= v
        assert off_goe <= v
        assert (v-diag_goe)>=0
        assert (v-off_goe)>=0
        assert diag_goe+(v-diag_goe)==v
        assert off_goe+(v-off_goe)==v

    ainv2=Fraction(2*(2*W+1),q)
    assert ainv2<=6
    return ainv2,(N,W,K,q,lo,hi)

tested=0
worst=(Fraction(0),None)
for N in range(1,501):
    for W in range(0,(N-1)//2+1):
        val,data=check(N,W)
        tested+=1
        if val>worst[0]:
            worst=(val,data)

assert worst[0]==6
assert worst[1][:4]==(3,1,2,1)

# Additional exact stress cases at large N and near congruence boundaries.
for N in [997,1000,1024,4093,4096,99991,100000]:
    candidates={0,(N-1)//2}
    for W in [1,2,3,7,11,31,63,127,255]:
        if 2*W+1<=N:
            candidates.add(W)
    for W in sorted(candidates):
        check(N,W)

print("SELF-CHECK PASS")
print("exhaustive_cases_N_le_500 =",tested)
print("worst_a_inverse_squared =",worst[0])
print("first_worst_case_(N,W,K,q,lo,hi) =",worst[1])
print("exact consequence: a^{-2}=2(2W+1)/q <= 6 on 2W+1<=N")
print("metric consequence: with PSSS Theorem-3 constant C,")
print("Y=2*pi*C/a <= 2*pi*sqrt(6)*C,")
print("E[X^2] <= Y+Y^2 <= 2*pi*sqrt(6)*C + 24*pi^2*C^2.")
print("NOTE: finite self-check verifies partition/covariance algebra only;")
print("PSSS Theorem 3 is an external published input, not machine-proved here.")
