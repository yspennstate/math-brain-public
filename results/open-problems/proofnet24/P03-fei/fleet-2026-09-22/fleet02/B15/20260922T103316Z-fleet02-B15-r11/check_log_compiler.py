#!/usr/bin/env python3
"""Deterministic checks for the log-magnitude/price compiler.

This checks:
  (1) sparse one-point character suspensions: degree alone recovers K_occ exactly,
      and H(g_m) <= 4 I(g_m);
  (2) depth-d recursive ternary majority for d<=4: the exact (degree, magnitude
      exponent) cell recursion recovers K_occ=Hmax-H, thereby retaining the
      multiscale credit missed by fixed low-degree projections.

The analytic theorems are proved in REPORT.md; this is only a self-check.
"""
from collections import defaultdict
import math

def h2(x):
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x*math.log2(x) - (1-x)*math.log2(1-x)

def sparse(m):
    p = 2.0**(1-m)
    J = m*p
    H = -((1-p)**2)*math.log2((1-p)**2) + (2*p-p*p)*(2*m-2)
    K = m*h2(p)-H

    Kdeg = 0.0
    for k in range(m+1):
        logq = (math.log2(math.comb(m,k)) + k*math.log2(p)
                + (m-k)*math.log2(1-p))
        if k == 0:
            pk = (1-p)**2
            logpk = 2*math.log2(1-p)
        else:
            pk = math.comb(m,k)*p*p
            logpk = math.log2(math.comb(m,k)) + 2*math.log2(p)
        Kdeg += pk*(logpk-logq)
    return p,J,H,K,Kdeg,4*J-H

def rm_cells(depth):
    cells = {(1,1): 3, (3,1): 1}
    for _ in range(2, depth+1):
        prev = cells
        new = defaultdict(int)
        for (k,a),N in prev.items():
            new[(k,a+1)] += 3*N
        items = list(prev.items())
        for (k1,a1),N1 in items:
            for (k2,a2),N2 in items:
                for (k3,a3),N3 in items:
                    new[(k1+k2+k3,a1+a2+a3+1)] += N1*N2*N3
        cells = dict(new)
    return cells

def solve_c_equal(n,r):
    def g(c):
        return 1-c-(1-c*r)**n
    lo, hi = 1e-15, 1.0
    assert g(lo) > 0 and g(hi) <= 0
    for _ in range(220):
        mid = (lo+hi)/2
        if g(mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2

def rm(depth):
    cells = rm_cells(depth)
    n = 3**depth
    r = 2.0**(-depth)
    I = (1.5)**depth
    c = solve_c_equal(n,r)
    lc = math.log2(c)
    lr = math.log2(r)
    l1 = math.log2(1-c*r)
    total = H = K = 0.0
    atoms = 0
    for (k,a),N in cells.items():
        mass = N*2.0**(-2*a)
        total += mass
        atoms += N
        H += mass*(2*a)
        logq = (k-1)*lc + k*lr + (n-k)*l1
        K += mass*((-2*a)-logq)
    Hmax = (n*h2(c*r)-h2(c))/c
    return n,I,c,len(cells),atoms,total,H,Hmax,K,K-(Hmax-H)

max_sparse_res = 0.0
min_four_slack = float("inf")
for m in range(2,31):
    p,J,H,K,Kdeg,slack = sparse(m)
    max_sparse_res = max(max_sparse_res,abs(K-Kdeg))
    min_four_slack = min(min_four_slack,slack)
    assert abs(K-Kdeg) < 1e-11
    assert slack > -1e-13

max_rm_res = 0.0
for d in range(1,5):
    n,I,c,ncells,atoms,total,H,Hmax,K,res = rm(d)
    max_rm_res = max(max_rm_res,abs(res),abs(total-1.0),abs(H-4*(I-1)))
    assert abs(total-1.0) < 1e-12
    assert abs(H-4*(I-1)) < 1e-11
    assert abs(res) < 1e-10

print("PASS")
print("sparse_max_abs_KminusKdegree =", format(max_sparse_res, ".17g"))
print("sparse_min_4I_minus_H =", format(min_four_slack, ".17g"))
for m in (4,8,16,24,30):
    p,J,H,K,Kdeg,slack = sparse(m)
    print("sparse", m,
          "J", format(J, ".15g"),
          "H/J", format(H/J, ".15g"),
          "K/J", format(K/J, ".15g"),
          "Kdeg/J", format(Kdeg/J, ".15g"),
          "4J-H", format(slack, ".15g"))
for d in range(1,5):
    n,I,c,ncells,atoms,total,H,Hmax,K,res = rm(d)
    print("rm3", d,
          "n", n,
          "I", format(I, ".15g"),
          "cells", ncells,
          "atoms", atoms,
          "H", format(H, ".15g"),
          "K", format(K, ".15g"),
          "Hmax", format(Hmax, ".15g"),
          "compiler_residual", format(res, ".3g"))
print("rm3_max_check_residual =", format(max_rm_res, ".17g"))
