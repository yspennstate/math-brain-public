#!/usr/bin/env python3
"""
FEI route-1 / route-3 experiment:
  (i) ordered-spectral-set compression functional
      U = H(K) + I H(q) - E log2(K!), q_i=Inf_i/I;
  (ii) hypercontractive Palm-clustering inequality
      E[t^(|S|-1) | i in S] <= Inf_i^((1-t)/(1+t)).
No claim of full FEI.  All logarithms in reported entropies are base 2.
"""
import json, math
import numpy as np

T_GRID = [0.0, 0.10, 0.25, 0.50, 0.75, 0.90, 0.99]

def fwht(a):
    a = np.asarray(a, dtype=float).copy()
    h = 1
    while h < len(a):
        b = a.reshape(-1, 2*h)
        x = b[:, :h].copy()
        y = b[:, h:].copy()
        b[:, :h] = x + y
        b[:, h:] = x - y
        h *= 2
    return a

def entropy(prob):
    p = np.asarray(prob, dtype=float)
    p = p[p > 0]
    return float(-(p*np.log2(p)).sum())

def metrics(vals):
    vals = np.asarray(vals, dtype=float)
    N = len(vals)
    n = int(round(math.log2(N)))
    hats = fwht(vals)/N
    mu = hats*hats
    K = np.array([s.bit_count() for s in range(N)], dtype=int)
    I = float(mu @ K)
    H = entropy(mu)
    wk = np.bincount(K, weights=mu, minlength=n+1)
    HK = entropy(wk)
    p = []
    for i in range(n):
        mask = np.array([bool((s >> i) & 1) for s in range(N)])
        p.append(float(mu[mask].sum()))
    if I > 0:
        q = np.asarray(p)/I
        Hq = entropy(q)
    else:
        q = np.zeros(n)
        Hq = 0.0
    Elogfact = float(sum(wk[k]*math.lgamma(k+1)/math.log(2) for k in range(n+1)))
    U = HK + I*Hq - Elogfact
    return {
        "n": n, "mu": mu, "K": K, "I": I, "H": H, "wk": wk,
        "p": np.asarray(p), "Hq": Hq, "HK": HK,
        "Elogfact": Elogfact, "U": U,
        "H_over_I": (H/I if I > 0 else 0.0),
        "U_over_I": (U/I if I > 0 else 0.0),
    }

def palm_cluster_max_violation(m):
    mu, K, p = m["mu"], m["K"], m["p"]
    worst = -1e100
    witness = None
    for i, pi in enumerate(p):
        if pi <= 1e-15:
            continue
        bit = np.array([bool((s >> i) & 1) for s in range(len(mu))])
        for t in T_GRID:
            lhs = float(np.sum(mu[bit] * (t ** (K[bit]-1))) / pi)
            a = (1.0-t)/(1.0+t)
            rhs = float(pi ** a)
            v = lhs-rhs
            if v > worst:
                worst = v
                witness = [i, t, lhs, rhs]
    return worst, witness

def vals_from_mask(n, mask):
    N = 1 << n
    vals = np.ones(N)
    # quotient global negation by fixing f(0)=+1
    for x in range(1, N):
        if (mask >> (x-1)) & 1:
            vals[x] = -1
    return vals

def exhaustive_small():
    out = []
    for n in range(1, 5):
        N = 1 << n
        max_u = (-1.0, None)
        max_hi = (-1.0, None)
        max_comp_violation = -1e100
        max_palm_violation = -1e100
        palm_witness = None
        count = 1 << (N-1)
        for mask in range(count):
            m = metrics(vals_from_mask(n, mask))
            comp_v = m["H"] - m["U"]
            max_comp_violation = max(max_comp_violation, comp_v)
            if m["U_over_I"] > max_u[0] + 1e-12:
                max_u = (m["U_over_I"], mask)
            if m["H_over_I"] > max_hi[0] + 1e-12:
                max_hi = (m["H_over_I"], mask)
            pv, pw = palm_cluster_max_violation(m)
            if pv > max_palm_violation:
                max_palm_violation, palm_witness = pv, [mask, pw]
        out.append({
            "n": n,
            "functions_up_to_global_negation": count,
            "max_U_over_I": max_u[0],
            "max_U_mask": max_u[1],
            "max_H_over_I": max_hi[0],
            "max_H_mask": max_hi[1],
            "max_H_minus_U": max_comp_violation,
            "max_palm_cluster_lhs_minus_rhs": max_palm_violation,
            "palm_witness": palm_witness,
        })
    return out

def one_point(n):
    c = 2.0**(2-2*n)
    w0 = (1.0-2.0**(1-n))**2
    wk = np.array([w0] + [math.comb(n,k)*c for k in range(1,n+1)], dtype=float)
    I = n*2.0**(1-n)
    H = -(w0*math.log2(w0) if w0 > 0 else 0.0) - (2**n-1)*c*math.log2(c)
    HK = entropy(wk)
    Hq = math.log2(n)
    Elogfact = sum(wk[k]*math.lgamma(k+1)/math.log(2) for k in range(n+1))
    U = HK + I*Hq-Elogfact
    return {"n":n, "I":I, "H_over_I":H/I, "U_over_I":U/I}

def tribes2(s):
    # OR of s disjoint ANDs of two bits, in +/-1 encoding.
    n = 2*s
    base = np.array([9.0,2.0,1.0])/16.0
    poly = np.array([1.0])
    for _ in range(s):
        poly = np.convolve(poly, base)
    a = (3.0/4.0)**s
    wk = np.zeros(n+1)
    wk[0] = (1-2*a)**2
    wk[1:] = 4*poly[1:]
    I = s*(3.0/4.0)**(s-1)
    HK = entropy(wk)
    Hq = math.log2(n)
    Elogfact = sum(wk[k]*math.lgamma(k+1)/math.log(2) for k in range(n+1))
    U = HK + I*Hq-Elogfact

    b = np.array([9/16,1/16,1/16,1/16], dtype=float)
    total = (3/4)**s
    sum_w_logw = s*(3/4)**(s-1)*float(np.sum(b*np.log2(b)))
    all_product_phi4 = -4*(2*total + sum_w_logw)
    w0r = (9/16)**s
    phi4w0 = -4*w0r*math.log2(4*w0r)
    f0 = (1-2*total)**2
    phi_f0 = (-f0*math.log2(f0)) if f0 > 0 else 0.0
    H = phi_f0 + all_product_phi4 - phi4w0
    return {"s":s, "n":n, "I":I, "H_over_I":H/I, "U_over_I":U/I}

def majority(n):
    vals = np.array([1.0 if x.bit_count() >= (n+1)//2 else -1.0 for x in range(1<<n)])
    m = metrics(vals)
    return {"n":n, "I":m["I"], "H_over_I":m["H_over_I"], "U_over_I":m["U_over_I"]}

def addressing(m):
    d = 1 << m
    n = m+d
    vals = np.empty(1<<n)
    for x in range(1<<n):
        addr = x & (d-1)
        vals[x] = 1.0 if ((x >> (m+addr)) & 1) else -1.0
    z = metrics(vals)
    return {"address_bits":m, "n":n, "I":z["I"], "H_over_I":z["H_over_I"], "U_over_I":z["U_over_I"]}

def main():
    out = {
        "status": "OPEN_AUXILIARY_ROUTE_NOT_FEI_PROOF",
        "ordered_code_claim": "For every random subset S: H(S) <= H(|S|)+I H(p/I)-E log2(|S|!).",
        "palm_cluster_claim": "For Boolean spectral S: E[t^(|S|-1)|i in S] <= Inf_i^((1-t)/(1+t)), 0<=t<=1.",
        "exhaustive_n_le_4": exhaustive_small(),
        "one_point": [one_point(n) for n in [2,3,4,5,8,16,32]],
        "one_point_U_limit": 3.0 + math.log2(math.e),
        "width2_tribes": [tribes2(s) for s in [2,4,6,8,12,20,50,100]],
        "width2_tribes_U_limit": 3*math.log2(4/3)+1+math.log2(3)+math.log2(math.e),
        "majority": [majority(n) for n in [3,5,9,13,19]],
        "addressing": [addressing(m) for m in [1,2,3,4]],
        "beta_hod": 6.4547837,
    }
    print(json.dumps(out, sort_keys=True, indent=2))

if __name__ == "__main__":
    main()
