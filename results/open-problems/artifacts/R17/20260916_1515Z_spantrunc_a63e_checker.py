#!/usr/bin/env python3
"""
R17 exact checker, 2026-09-16 15:15Z.

No Monte Carlo.

R17:
  C006: bounded-span block packing Q_{m,B} DP equals brute force on small cases,
        Q <= LCS <= Q + m floor(n/(B+1)).
  C007: superadditivity certificate for Q under concatenation (small exhaustive tests).

Independent R18 audit:
  R17-AUDIT-R18-I0080-C007-ENDTOEND-002 finite algebra:
  source normalization, global parameter identities, and every rational inequality
  used in the C007 high/low/high certificate.
"""
from itertools import product
from fractions import Fraction
from functools import lru_cache
from math import floor
import sympy as sp

def lcs(x,y):
    d=[0]*(len(y)+1)
    for a in x:
        prev=0
        for j,b in enumerate(y,1):
            old=d[j]
            d[j]=prev+1 if a==b else max(d[j],d[j-1])
            prev=old
    return d[-1]

def q_dp(x,y,m,B):
    assert len(x)%m==0
    r=len(x)//m
    n=len(y)
    D=[[0]*(n+1) for _ in range(r+1)]
    for j in range(1,r+1):
        block=x[(j-1)*m:j*m]
        for t in range(1,n+1):
            best=max(D[j][t-1],D[j-1][t])
            for ell in range(1,min(B,t)+1):
                best=max(best,D[j-1][t-ell]+lcs(block,y[t-ell:t]))
            D[j][t]=best
    return D[r][n]

def q_bruteforce(x,y,m,B):
    assert len(x)%m==0
    r=len(x)//m
    n=len(y)
    @lru_cache(None)
    def rec(j,start):
        if j==r:
            return 0
        block=x[j*m:(j+1)*m]
        best=rec(j+1,start)
        for s in range(start,n):
            for ell in range(1,min(B,n-s)+1):
                e=s+ell
                best=max(best,lcs(block,y[s:e])+rec(j+1,e))
        return best
    return rec(0,0)

checks=0
max_gap=0
families=[(1,3),(2,2),(2,3),(3,2)]
for m,r in families:
    n=m*r
    for B in range(1,n+1):
        for x in product((0,1),repeat=n):
            for y in product((0,1),repeat=n):
                q=q_dp(x,y,m,B)
                L=lcs(x,y)
                if n<=4 or B in (1,n):
                    qb=q_bruteforce(x,y,m,B)
                    assert q==qb
                assert q<=L
                err=m*floor(n/(B+1))
                assert L<=q+err
                if B>=n:
                    assert q==L
                max_gap=max(max_gap,L-q)
                checks+=1

print("C006 PASS")
print("  exhaustive (x,y,m,B) checks:",checks)
print("  largest observed LCS-Q gap:",max_gap)
print("  verified deterministic bound: 0 <= LCS-Q <= m*floor(n/(B+1))")

superchecks=0
for m,B,r1,r2 in [(1,1,1,2),(1,2,1,2),(2,1,1,1),(2,2,1,1)]:
    n1=m*r1; n2=m*r2
    for x1 in product((0,1),repeat=n1):
      for y1 in product((0,1),repeat=n1):
       q1=q_dp(x1,y1,m,B)
       for x2 in product((0,1),repeat=n2):
        for y2 in product((0,1),repeat=n2):
            q2=q_dp(x2,y2,m,B)
            qc=q_dp(x1+x2,y1+y2,m,B)
            assert qc>=q1+q2
            superchecks+=1
print("C007 PASS")
print("  exhaustive concatenation-superadditivity checks:",superchecks)

assert Fraction(333,106) < Fraction(355,113) < Fraction(22,7)
assert Fraction(202241,206250) > Fraction(19,20)
assert Fraction(26,81) > Fraction(11,70)+Fraction(4,25)
assert Fraction(118941,125000) > Fraction(19,20)
assert Fraction(523,8) > 59
assert Fraction(599,600)*Fraction(7,22) == Fraction(4193,13200)
assert Fraction(8,5)*Fraction(4193,13200) + Fraction(123,125)*Fraction(12,25) == Fraction(202241,206250)
assert Fraction(123,125)*Fraction(967,1000) == Fraction(118941,125000)
assert Fraction(19,20) / (Fraction(1,10)**2) == 95
assert Fraction(8,5)/100 == Fraction(2,125)

b, pi, D, a, t, qlog, S = sp.symbols('b pi D a t qlog S', positive=True)
A = pi/(pi-b)
cb = sp.sin(b)/(pi-b)
expr = sp.simplify((A/b*S)/cb - pi*S/(b*sp.sin(b)))
assert expr == 0
assert sp.simplify(pi*D/(b*sp.sin(b)) - (D/b)*pi/sp.sin(b)) == 0

d, ell = sp.symbols('d ell', positive=True)
Dexpr=d/ell
b2=pi*d*t/ell
aexpr=Dexpr/sp.sqrt(b2)
assert sp.simplify(b2/(pi*Dexpr)-t)==0
assert sp.simplify(aexpr*pi*t-sp.sqrt(b2))==0
assert sp.simplify((pi*sp.Rational(19,20)*t)/(95*pi*t)-sp.Rational(1,100))==0

print("R18 AUDIT FINITE CORE PASS")
print("  audit_id=R17-AUDIT-R18-I0080-C007-ENDTOEND-002")
print("  exact source-normalization algebra: PASS")
print("  exact global t-parameter algebra: PASS")
print("  exact high/low/high rational margins: PASS")
print("PASS")
