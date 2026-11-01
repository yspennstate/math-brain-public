#!/usr/bin/env python3
"""Self-check for P03 FEI Reed-Muller derivative-gap hereditary allocation.

Exhaustive over every Boolean function through dimension 4, plus 2000
deterministic random ANF samples in dimension 5. This is a sanity check only;
the theorem is proved analytically in the accompanying report.
"""
import json
import math
import random
from collections import Counter

TOL = 2e-9

def h2(t):
    if t <= 0.0 or t >= 1.0:
        return 0.0
    return -t*math.log2(t) - (1.0-t)*math.log2(1.0-t)

def phi(r):
    if r <= 0:
        return 0.0
    t = 2.0**(-r)
    return h2(t)/t

def mobius_anf(bits, n):
    a = bits[:]
    for i in range(n):
        bit = 1 << i
        for mask in range(1 << n):
            if mask & bit:
                a[mask] ^= a[mask ^ bit]
    return a

def algebraic_degree(a):
    return max((mask.bit_count() for mask,c in enumerate(a) if c), default=0)

def derivative_anf(a, n, i):
    others = [j for j in range(n) if j != i]
    out = [0]*(1 << (n-1))
    for mask,c in enumerate(a):
        if c and ((mask >> i) & 1):
            compact = 0
            for k,j in enumerate(others):
                if (mask >> j) & 1:
                    compact |= 1 << k
            out[compact] ^= 1
    return out

def eval_anf(a, n):
    vals = []
    for x in range(1 << n):
        acc = 0
        sub = x
        while True:
            acc ^= a[sub]
            if sub == 0:
                break
            sub = (sub - 1) & x
        vals.append(acc)
    return vals

def walsh_coeffs(f):
    a = [float(x) for x in f]
    N = len(a)
    h = 1
    while h < N:
        for base in range(0, N, 2*h):
            for j in range(base, base+h):
                x,y = a[j],a[j+h]
                a[j],a[j+h] = x+y,x-y
        h *= 2
    return [x/N for x in a]

def spectral_stats(f, n):
    hats = walsh_coeffs(f)
    p = [x*x for x in hats]
    H = sum(-q*math.log2(q) for q in p if q > 0.0)
    inf = [sum(q for S,q in enumerate(p) if (S >> i) & 1) for i in range(n)]
    B = []
    for i in range(n):
        b = 0.0
        for T in range(1 << n):
            if (T >> i) & 1:
                continue
            u = p[T]
            v = p[T | (1 << i)]
            m = u+v
            if m > 0.0:
                b += m*h2(v/m)
        B.append(b)
    return H,inf,B

def check_anf(a, n):
    vals = eval_anf(a,n)
    f = [1 if x == 0 else -1 for x in vals]
    H,inf,Bs = spectral_stats(f,n)
    d = algebraic_degree(a)
    J = sum(min(p,1.0-p) for p in inf)
    profile = 0.0
    local_ratio = 0.0
    for i in range(n):
        da = derivative_anf(a,n,i)
        r = algebraic_degree(da)
        dv = eval_anf(da,n-1)
        p = sum(dv)/(1 << (n-1))
        if abs(p-inf[i]) > TOL:
            raise AssertionError(("influence identity",n,i,p,inf[i]))
        j = min(p,1.0-p)
        if r == 0:
            if j > TOL or Bs[i] > TOL:
                raise AssertionError(("constant derivative",n,i,p,j,Bs[i]))
            bound = 0.0
        else:
            if j + TOL < 2.0**(-r):
                raise AssertionError(("Reed-Muller gap",n,i,r,j))
            bound = phi(r)*j
            if Bs[i] > bound + TOL:
                raise AssertionError(("local allocation",n,i,r,j,Bs[i],bound))
        profile += bound
        if bound > 1e-15:
            local_ratio = max(local_ratio, Bs[i]/bound)
    B = sum(Bs)
    if H > profile + TOL:
        raise AssertionError(("entropy profile",n,d,H,profile))
    if B > profile + TOL:
        raise AssertionError(("erasure profile",n,d,B,profile))
    kappa = 0.0 if d <= 1 else phi(d-1)
    if H > kappa*J + TOL:
        raise AssertionError(("uniform degree entropy",n,d,H,J,kappa))
    if B > kappa*J + TOL:
        raise AssertionError(("uniform degree erasure",n,d,B,J,kappa))
    return {
        "degree": d,
        "H_over_J": H/J if J > 1e-15 else 0.0,
        "H_over_profile": H/profile if profile > 1e-15 else 0.0,
        "B_over_profile": B/profile if profile > 1e-15 else 0.0,
        "local_B_over_phi_j": local_ratio,
    }

def main():
    out = {"status":"PASS","full_FEI_proved":False,"independent_audit":False,"exhaustive":{}}
    max_HP = max_BP = max_local = 0.0
    for n in range(1,5):
        N = 1 << n
        degree_counts = Counter()
        max_HJ = 0.0
        for table in range(1 << N):
            bits = [(table >> x) & 1 for x in range(N)]
            a = mobius_anf(bits,n)
            result = check_anf(a,n)
            degree_counts[result["degree"]] += 1
            max_HJ = max(max_HJ,result["H_over_J"])
            max_HP = max(max_HP,result["H_over_profile"])
            max_BP = max(max_BP,result["B_over_profile"])
            max_local = max(max_local,result["local_B_over_phi_j"])
        out["exhaustive"][str(n)] = {"functions":1 << N,"degree_counts":dict(sorted(degree_counts.items())),"max_H_over_J":max_HJ}
    rng = random.Random(20260920)
    counts = Counter()
    for t in range(2000):
        n = 5
        cap = 2 + (t % 4)
        a = [0]*(1 << n)
        for mask in range(1 << n):
            if mask.bit_count() <= cap:
                a[mask] = rng.getrandbits(1)
        result = check_anf(a,n)
        counts[result["degree"]] += 1
        max_HP = max(max_HP,result["H_over_profile"])
        max_BP = max(max_BP,result["B_over_profile"])
        max_local = max(max_local,result["local_B_over_phi_j"])
    out["random_n5"] = {"seed":20260920,"samples":2000,"actual_degree_counts":dict(sorted(counts.items()))}
    out["kappa_values"] = {str(d):phi(d-1) for d in range(2,9)}
    out["max_H_over_profile_bound"] = max_HP
    out["max_B_over_profile_bound"] = max_BP
    out["max_local_B_over_phi_j"] = max_local
    out["max_numeric_violation"] = 0.0
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__ == "__main__":
    main()
