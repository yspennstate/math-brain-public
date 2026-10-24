#!/usr/bin/env python3
"""Targeted finite regression for the B14 interaction-cover theorems.

Enumerates Boolean functions modulo global output sign through n=4.
Checks:
  (i) H(f) <= min_{vertex covers A} sum_{i in A} Psi(q_i);
  (ii) for centered H/J restriction-critical roots,
       sum_{i in B} Psi(p_i) <= D + R sum_{j<k in B} c_jk
       for every nonempty proper B.

This is only a regression check; the report gives the analytic proofs.
"""
import math
from itertools import combinations

TOL = 1e-9

def fwht(values):
    a = [float(x) for x in values]
    n = len(a)
    h = 1
    while h < n:
        for base in range(0, n, 2*h):
            x = a[base:base+h]
            y = a[base+h:base+2*h]
            a[base:base+h] = [u+v for u,v in zip(x,y)]
            a[base+h:base+2*h] = [u-v for u,v in zip(x,y)]
        h *= 2
    return [x/n for x in a]

def stats(values):
    n = (len(values)).bit_length() - 1
    a = fwht(values)
    mu = [x*x for x in a]
    H = sum(-x*math.log2(x) for x in mu if x > 1e-15)
    p = [sum(mu[s] for s in range(1<<n) if (s>>i)&1) for i in range(n)]
    q = [min(x, 1-x) for x in p]
    return H, p, q, mu

def h2(p):
    if p <= 0 or p >= 1:
        return 0.0
    return -p*math.log2(p) - (1-p)*math.log2(1-p)

def jfun(p):
    q = min(p, 1-p)
    r = 0.5 + math.sqrt(max(0.0, q*(1-q)))
    return 1.0 - h2(r)

def psi(p):
    return h2(p) + jfun(p)

def restrict_values(values, n, fixed_mask, fixed_bits):
    remaining = [i for i in range(n) if not ((fixed_mask>>i)&1)]
    out = []
    for y in range(1<<len(remaining)):
        x = fixed_bits & fixed_mask
        for r, i in enumerate(remaining):
            if (y>>r)&1:
                x |= 1<<i
        out.append(values[x])
    return out

def max_proper_descendant_ratio(values, n):
    ans = -1.0
    for fixed_mask in range(1, 1<<n):
        fixed_positions = [i for i in range(n) if (fixed_mask>>i)&1]
        for raw in range(1<<len(fixed_positions)):
            fixed_bits = 0
            for r, i in enumerate(fixed_positions):
                if (raw>>r)&1:
                    fixed_bits |= 1<<i
            child = restrict_values(values, n, fixed_mask, fixed_bits)
            H, _, q, _ = stats(child)
            J = sum(q)
            if J > 1e-12:
                ans = max(ans, H/J)
    return ans

def center(values, n, p):
    char = sum((1<<i) for i, x in enumerate(p) if x > 0.5 + 1e-12)
    return [
        v * (-1 if ((char & x).bit_count() & 1) else 1)
        for x, v in enumerate(values)
    ]

def mixed_face_probability(values, n, j, k):
    count = 0
    for x in range(1<<n):
        eta = values[x] != values[x ^ (1<<j)]
        y = x ^ (1<<k)
        eta2 = values[y] != values[y ^ (1<<j)]
        count += (eta != eta2)
    return count / (1<<n)

def interaction_matrix(values, n):
    c = [[0.0 for _ in range(n)] for _ in range(n)]
    for j, k in combinations(range(n), 2):
        c[j][k] = c[k][j] = mixed_face_probability(values, n, j, k)
    return c

def is_cover(mask, c, n):
    for j, k in combinations(range(n), 2):
        if c[j][k] > 1e-12 and not (((mask>>j)&1) or ((mask>>k)&1)):
            return False
    return True

def run(n):
    total = 1 << ((1<<n)-1)  # global output sign fixed by f(0)=+1
    critical = 0
    max_cover_violation = -1e100
    max_subset_violation = -1e100

    for truth_mask in range(total):
        values = [1] + [
            -1 if ((truth_mask>>(x-1))&1) else 1
            for x in range(1, 1<<n)
        ]
        H, p, q, _ = stats(values)
        c = interaction_matrix(values, n)

        for A in range(1<<n):
            if is_cover(A, c, n):
                rhs = sum(psi(q[i]) for i in range(n) if (A>>i)&1)
                max_cover_violation = max(max_cover_violation, H-rhs)

        J = sum(q)
        if J <= 1e-12:
            continue
        R0 = H/J
        if R0 + TOL < max_proper_descendant_ratio(values, n):
            continue

        critical += 1
        g = center(values, n, p)
        Hc, pc, _, _ = stats(g)
        I = sum(pc)
        R = Hc/I
        W = sum(psi(x) for x in pc)
        D = W - R*I
        cc = interaction_matrix(g, n)

        for B in range(1, (1<<n)-1):
            lhs = sum(psi(pc[i]) for i in range(n) if (B>>i)&1)
            K = sum(
                cc[j][k] for j,k in combinations(range(n),2)
                if ((B>>j)&1) and ((B>>k)&1)
            )
            max_subset_violation = max(
                max_subset_violation, lhs - (D + R*K)
            )

    return total, critical, max_cover_violation, max_subset_violation

def main():
    print("n,total_sign_normalized,critical_roots,max_cover_violation,max_subset_violation")
    for n in (2,3,4):
        total, critical, vc, sub = run(n)
        print(f"{n},{total},{critical},{vc:.17g},{sub:.17g}")

if __name__ == "__main__":
    main()
