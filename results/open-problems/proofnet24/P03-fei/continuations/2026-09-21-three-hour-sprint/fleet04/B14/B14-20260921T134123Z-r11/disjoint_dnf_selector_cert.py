#!/usr/bin/env python3
"""Scalar certificate and small direct-Walsh checks for the disjoint-clause DNF selector lemma.
Scientific status: supports REPORT.md in this run folder; full FEI remains open.
"""
from __future__ import annotations
import math
from typing import List
import mpmath as mp

iv = mp.iv
iv.dps = 60
LN2 = iv.log(iv.mpf(2))


def h_iv(t):
    return -(t * iv.log(t) + (1 - t) * iv.log(1 - t)) / LN2


def j_iv(t):
    return 1 - h_iv(iv.mpf('0.5') + iv.sqrt(t * (1 - t)))


def psi_iv(t):
    return h_iv(t) + j_iv(t)


def K_iv(k: int):
    if k == 1:
        return iv.mpf(4)  # 2*Psi(1/2)=4; avoids endpoint log(0) in interval arithmetic.
    D = (2**k - 1) ** 2 + 1
    t = iv.mpf(1) / D
    return D * psi_iv(t)


def U_iv(k: int, p):
    a = iv.mpf(2) ** (1-k)
    K = K_iv(k)
    return 4*(1-a) + K*(a-p) + p*(iv.log(1+p**-2)/LN2 + 3/LN2)


def Up_iv(k: int, p):
    K = K_iv(k)
    return iv.log(1+p**-2)/LN2 + 3/LN2 - K - 2/(LN2*(1+p*p))


def lo(x): return float(x.a)
def hi(x): return float(x.b)

P0 = {
    1: '0.6958702675119379',
    2: '0.1267740027701263',
    3: '0.05286466059789910',
    4: '0.02455658047631298',
    5: '0.01187061656334781',
    6: '0.005839777534752136',
    7: '0.002896739939416379',
}

print('INTERVAL_TANGENT_CERTIFICATE')
max_hi = -1.0
for k, s in P0.items():
    p0 = iv.mpf(s)
    a = 2.0**(1-k)
    u0 = U_iv(k, p0)
    d0 = Up_iv(k, p0)
    radius = max(float(s), a-float(s))
    tangent_hi = hi(u0) + max(abs(lo(d0)), abs(hi(d0))) * radius
    max_hi = max(max_hi, tangent_hi)
    print(f'k={k} p0={s} U_hi={hi(u0):.15f} d=[{lo(d0):.3e},{hi(d0):.3e}] tangent_hi={tangent_hi:.15f}')
print(f'finite_k_max_hi={max_hi:.15f}')
print('tail_k_ge_8_bound=4 + 2^(1-k)*(4*k + 3/ln(2) - 5), maximized at k=8')
tail8 = 4 + 2**(1-8)*(4*8 + 3/math.log(2) - 5)
print(f'tail_k_ge_8_hi_by_elementary_bound={tail8:.15f}')
print(f'global_U_hi={max(max_hi, tail8):.15f}')
print('claimed_round_constant=6.096')
assert max(max_hi, tail8) < 6.096

# Pure-Python direct Walsh checks for a few nonuniform disjoint-clause DNFs.
def h(t: float) -> float:
    if t <= 0.0 or t >= 1.0:
        return 0.0
    return -t*math.log2(t)-(1-t)*math.log2(1-t)

def j(t: float) -> float:
    if t <= 0.0 or t >= 1.0:
        return 0.0
    return 1-h(0.5+math.sqrt(t*(1-t)))

def psi(t: float) -> float:
    return h(t)+j(t)

def fib(x: float, y: float) -> float:
    w=x+y
    return 0.0 if w == 0 else w*psi(y/w)

def exact_delta(k: int, p: float) -> float:
    a=2.0**(1-k); m=2**k-1; D=m*m+1
    return 4*p*(1-a) + D*psi(1/D)*(a*p-p*p) + fib((1-m*p)**2,p*p)

def vals_for(widths: List[int]):
    clauses=[]; s=0
    for w in widths:
        clauses.append(list(range(s,s+w))); s += w
    out=[]
    for mask in range(1<<s):
        sat=False
        for C in clauses:
            if all((mask>>q)&1 for q in C):
                sat=True; break
        out.append(-1.0 if sat else 1.0)
    return out, clauses

def walsh(vals):
    z=[v/len(vals) for v in vals]
    step=1
    while step < len(z):
        for i in range(0,len(z),2*step):
            for j0 in range(step):
                x=z[i+j0]; y=z[i+j0+step]
                z[i+j0]=x+y; z[i+j0+step]=x-y
        step *= 2
    return z

def H(vals):
    return -sum(q*math.log2(q) for c in walsh(vals) if (q:=c*c)>0)

def restrict(vals,n,i,b):
    out=[]
    for m in range(1<<(n-1)):
        full=0; t=0
        for q in range(n):
            bit=b if q==i else ((m>>t)&1)
            if q != i: t += 1
            full |= bit<<q
        out.append(vals[full])
    return out

def influence(vals,n,i):
    return sum(vals[m] != vals[m^(1<<i)] for m in range(1<<n))/(1<<n)

def decrement(vals,n,i):
    return H(vals)-0.5*(H(restrict(vals,n,i,0))+H(restrict(vals,n,i,1)))

patterns=[[1,3],[2,3],[4],[1,2,3],[2,2,3]]
max_err=0.0
for widths in patterns:
    vals, clauses=vals_for(widths); n=sum(widths)
    for w,C in zip(widths,clauses):
        for i in C:
            p=influence(vals,n,i); d=decrement(vals,n,i); e=exact_delta(w,p)
            max_err=max(max_err,abs(d-e))
print(f'direct_walsh_patterns={patterns}')
print(f'direct_walsh_max_abs_error={max_err:.3e}')
assert max_err < 1e-12
