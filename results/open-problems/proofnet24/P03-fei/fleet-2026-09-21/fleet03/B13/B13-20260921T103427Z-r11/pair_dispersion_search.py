#!/usr/bin/env python3
"""B13 FEI route-13/14 counterexample search for the pair-dispersion candidate.

No external dependencies beyond numpy. Exhaustive Boolean checks quotient
global output negation, which does not change the squared Fourier spectrum.
"""
import itertools, json, math
import numpy as np


def fwht(a):
    a = np.asarray(a, dtype=float).copy()
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            x = a[i:i+h].copy(); y = a[i+h:i+2*h].copy()
            a[i:i+h] = x+y; a[i+h:i+2*h] = x-y
        h *= 2
    return a


def metrics(vals):
    N = len(vals); n = int(math.log2(N))
    p = (fwht(vals)/N)**2
    nz = p > 1e-18
    H = float(-(p[nz]*np.log2(p[nz])).sum())
    ids = np.arange(N)
    q = np.array([float(p[((ids >> i) & 1) == 1].sum()) for i in range(n)])
    I = float(q.sum())
    J = float(np.minimum(q, 1-q).sum())
    D = float((q*(1-q)).sum())
    return H, I, J, D, q, p


def exhaustive(max_n=4):
    out = {}
    for n in range(1, max_n+1):
        N = 1 << n
        best = (-1, None)
        count = 1 << (N-1)
        for mask in range(count):
            vals = np.ones(N)
            for j in range(1, N):
                if (mask >> (j-1)) & 1:
                    vals[j] = -1
            H, I, J, D, q, p = metrics(vals)
            r = H/D if D > 1e-15 else 0.0
            if r > best[0]:
                best = (r, (mask, H, I, J, D, q, p))
        r, (mask, H, I, J, D, q, p) = best
        out[str(n)] = {
            "representatives": count,
            "max_H_over_D": r,
            "truth_table_integer_with_minus_one_bits": int(mask << 1),
            "H": H, "I": I, "J": J, "D": D,
            "influences": q.tolist(),
        }
    return out


def block_stats_width2(s):
    # AND of s OR_2 blocks, closed-form spectrum aggregation.
    w = 2
    a = 1-2.0**(1-w); c = 2.0**(1-w); m = 2**w-1
    tsum = w*2**(w-1)
    H = I = mass = 0.0
    p0 = (2.0**(1-s)*(1+a)**s-1)**2
    if p0 > 0:
        H -= p0*math.log2(p0)
    mass += p0
    for b in range(1, s+1):
        pS = 4.0**(1-s)*c**(2*b)*(1+a)**(2*(s-b))
        N = math.comb(s, b)*m**b
        ssum = math.comb(s, b)*b*tsum*m**(b-1)
        mass += N*pS
        if pS > 0:
            H -= N*pS*math.log2(pS)
        I += pS*ssum
    q = (1-2.0**(-w))**(s-1)*2.0**(-(w-1))
    D = 2*s*q*(1-q)
    return {"s": s, "n": 2*s, "H": H, "I": I, "D": D, "q": q,
            "H_over_I": H/I, "H_over_D": H/D, "mass": mass}


def tribes_scan():
    rows = [block_stats_width2(s) for s in range(2, 41)]
    return {"max": max(rows, key=lambda r: r["H_over_D"]), "rows": rows}


def doubled_star(n):
    vertical = 1 << n
    B = [0] + [1 << i for i in range(n)]
    return sorted(B + [vertical ^ b for b in B])


def autocorr_ok(A, signs, dim):
    sg = dict(zip(A, signs)); aset = set(A)
    for t in range(1, 1 << dim):
        corr = sum(sg[a]*sg[a ^ t] for a in A if (a ^ t) in aset)
        if corr:
            return False
    return True


def sign_search_doubled_star(max_n=5):
    out = {}
    for n in range(1, max_n+1):
        A = doubled_star(n); M = len(A); found = False
        # Global sign fixed at first support point.
        for mask in range(1 << (M-1)):
            signs = [1] + [-1 if (mask >> (j-1)) & 1 else 1 for j in range(1, M)]
            if autocorr_ok(A, signs, n+1):
                found = True
                break
        out[str(n)] = {"support_size": M, "perfect_autocorrelation_signs_exist": found}
    return out


if __name__ == "__main__":
    result = {
        "candidate": "H(f) <= C * D(f), D=sum_i Inf_i(f)(1-Inf_i(f))",
        "status": "finite_counterexample_search_only",
        "exhaustive": exhaustive(4),
        "width2_tribes": tribes_scan(),
        "doubled_star_sign_search": sign_search_doubled_star(5),
    }
    print(json.dumps(result, indent=2, sort_keys=True))
