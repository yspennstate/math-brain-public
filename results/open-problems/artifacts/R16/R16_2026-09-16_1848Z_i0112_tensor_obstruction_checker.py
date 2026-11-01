#!/usr/bin/env python3
"""
R16 / I0112 exact self-check.

This checker is not the proof. It exactly verifies the finite algebra used in
the first I0112 run:
  (1) the trace lower-bound threshold showing that the tensor-square of a
      sufficiently large 6-regular graph is not 36-regular Ramanujan;
  (2) the strict long-range-growth base (d-1)^2/(d^2-1)=(d-1)/(d+1)<1;
  (3) the elementary total-variation tensor inequalities on an exhaustive
      rational test grid.

All arithmetic in (1)-(3) is rational/integer.
"""
from fractions import Fraction

print("R16 I0112 exact checker: start")

def nonram_trace_cert(d,n):
    return d**3*(n-d) > 4*(d*d-1)*(n-1)

d=6
vals=[n for n in range(d+1,100) if nonram_trace_cert(d,n)]
assert vals and vals[0]==16
assert not nonram_trace_cert(6,15)
assert nonram_trace_cert(6,16)
print("C01 finite trace threshold: d=6 => n0=16: PASS")

for d in range(6,13):
    n0=next(n for n in range(d+1,10000) if nonram_trace_cert(d,n))
    print(f"  d={d}: first certified n={n0}")

for d in range(3,101):
    lhs=Fraction((d-1)**2,d*d-1)
    rhs=Fraction(d-1,d+1)
    assert lhs==rhs
    assert lhs < 1
print("C01 long-range base identity and strict loss for d=3..100: PASS")
print("  d=6 ratio =", Fraction(5,7))

def comps(total,k):
    if k==1:
        yield (total,)
    else:
        for x in range(total+1):
            for rest in comps(total-x,k-1):
                yield (x,)+rest

laws=[tuple(Fraction(x,4) for x in c) for c in comps(4,3)]

def tv(p,q):
    return sum(abs(a-b) for a,b in zip(p,q))/2

def tensor(p,q):
    return tuple(a*b for a in p for b in q)

count=0
for mu in laws:
  for pi in laws:
    for nu in laws:
      for rho in laws:
        a=tv(mu,pi); b=tv(nu,rho)
        prod=tv(tensor(mu,nu),tensor(pi,rho))
        assert prod >= max(a,b)
        assert prod <= a+b
        count += 1
print(f"C01 TV tensor inequalities exhaustive denominator-4 grid: PASS ({count} quadruples)")
print("ALL_EXACT_CHECKS_PASS")
