#!/usr/bin/env python3
"""Self-check for B13 block-Holevo / support-boundary inequalities.

Analytic theorem checked numerically:
  Delta_A H = H(S_A|S_B) + JS_A
  JS_A <= P_{A->B}
  I(S_A;S_B) <= min(P_{A->B}, P_{B->A})
  P_{A->B}=0 iff f factors across A|B.
All Boolean functions are exhausted modulo global output sign through n=4.
"""
import math

TOL = 1e-11

def fwht(vals):
    a = [float(v) for v in vals]
    n = len(a)
    h = 1
    while h < n:
        for i in range(0, n, 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return [x/n for x in a]

def entropy(probs):
    return sum(-p*math.log2(p) for p in probs if p > 0.0)

def spectrum(vals):
    return [a*a for a in fwht(vals)]

def marginal(p, n, coords):
    coords = list(coords)
    out = [0.0]*(1 << len(coords))
    for s, mass in enumerate(p):
        t = 0
        for j, k in enumerate(coords):
            if (s >> k) & 1:
                t |= 1 << j
        out[t] += mass
    return out

def restriction(vals, n, A, assignment):
    A = list(A)
    B = [i for i in range(n) if i not in A]
    out = []
    for y in range(1 << len(B)):
        x = 0
        for t, i in enumerate(A):
            if (assignment >> t) & 1:
                x |= 1 << i
        for t, i in enumerate(B):
            if (y >> t) & 1:
                x |= 1 << i
        out.append(vals[x])
    return out

def js_restriction(vals, n, A):
    p = spectrum(vals)
    B = [i for i in range(n) if i not in A]
    hbar = entropy(marginal(p, n, B))
    hs = []
    for a in range(1 << len(A)):
        hs.append(entropy(spectrum(restriction(vals, n, A, a))))
    return hbar - sum(hs)/len(hs), sum(hs)/len(hs)

def spectral_mi(vals, n, A):
    p = spectrum(vals)
    B = [i for i in range(n) if i not in A]
    return entropy(marginal(p, n, A)) + entropy(marginal(p, n, B)) - entropy(p)

def support_cross(vals, n, A):
    A = set(A)
    B = [k for k in range(n) if k not in A]
    total = 0.0
    for i in A:
        others = [k for k in range(n) if k != i]
        pos = {k:t for t,k in enumerate(others)}
        e = [0]*(1 << (n-1))
        for z in range(1 << (n-1)):
            x0 = 0
            for t, k in enumerate(others):
                if (z >> t) & 1:
                    x0 |= 1 << k
            x1 = x0 | (1 << i)
            e[z] = int(vals[x0] != vals[x1])
        for k in B:
            bit = 1 << pos[k]
            total += sum(e[z] != e[z ^ bit] for z in range(1 << (n-1))) / (1 << (n-1))
    return total

def factors_across(vals, n, A):
    A = list(A)
    B = [i for i in range(n) if i not in A]
    def idx(a, b):
        x = 0
        for t, i in enumerate(A):
            if (a >> t) & 1:
                x |= 1 << i
        for t, i in enumerate(B):
            if (b >> t) & 1:
                x |= 1 << i
        return x
    base = vals[idx(0,0)]
    for a in range(1 << len(A)):
        for b in range(1 << len(B)):
            if vals[idx(a,b)] * vals[idx(a,0)] * vals[idx(0,b)] * base != 1:
                return False
    return True

def signed_cross_curvature(vals, n, A):
    A = set(A)
    B = [k for k in range(n) if k not in A]
    p_total = o_total = k_total = 0.0
    for i in A:
        others = [k for k in range(n) if k != i]
        pos = {k:t for t,k in enumerate(others)}
        g = [0.0]*(1 << (n-1))
        for z in range(1 << (n-1)):
            x0 = 0
            for t, k in enumerate(others):
                if (z >> t) & 1:
                    x0 |= 1 << k
            x1 = x0 | (1 << i)
            g[z] = (vals[x0] - vals[x1])/2.0
        e = [int(u != 0.0) for u in g]
        for k in B:
            bit = 1 << pos[k]
            p_total += sum(e[z] != e[z ^ bit] for z in range(1 << (n-1))) / (1 << (n-1))
            o_total += sum(g[z] == -g[z ^ bit] and g[z] != 0.0 for z in range(1 << (n-1))) / (1 << (n-1))
            k_total += sum((g[z]-g[z ^ bit])**2 for z in range(1 << (n-1))) / (1 << (n-1))
    return p_total, o_total, k_total

def and2(x0, x1):
    return -1 if (x0 and x1) else 1

def main():
    total_functions = 0
    total_cases = 0
    max_decomp_error = 0.0
    max_js_excess = 0.0
    max_mi_excess = 0.0
    factor_mismatches = 0

    for n in range(1,5):
        nf = 1 << ((1 << n)-1)
        total_functions += nf
        for code in range(nf):
            vals = [1]*(1 << n)
            for x in range(1, 1 << n):
                vals[x] = -1 if ((code >> (x-1)) & 1) else 1
            p = spectrum(vals)
            H = entropy(p)
            for mask in range(1, (1 << n)-1):
                A = [i for i in range(n) if (mask >> i) & 1]
                B = [i for i in range(n) if not ((mask >> i) & 1)]
                js, mean_restr_H = js_restriction(vals, n, A)
                cond = H - entropy(marginal(p, n, B))
                delta = H - mean_restr_H
                pab = support_cross(vals, n, A)
                pba = support_cross(vals, n, B)
                mi = spectral_mi(vals, n, A)
                max_decomp_error = max(max_decomp_error, abs(delta-(cond+js)))
                max_js_excess = max(max_js_excess, js-pab)
                max_mi_excess = max(max_mi_excess, mi-min(pab,pba))
                fac = factors_across(vals, n, A)
                if (pab <= TOL) != fac:
                    factor_mismatches += 1
                total_cases += 1

    sharp = [1,-1,1,1]
    sharp_js, _ = js_restriction(sharp, 2, [0])
    sharp_p = support_cross(sharp, 2, [0])

    prod = []
    for x in range(16):
        b = [(x >> i) & 1 for i in range(4)]
        prod.append(and2(b[0],b[1]) * and2(b[2],b[3]))
    prod_js, _ = js_restriction(prod, 4, [0,1])
    prod_p, prod_o, prod_kappa = signed_cross_curvature(prod, 4, [0,1])

    print("B13 block-Holevo/support-boundary self-check")
    print(f"functions_mod_global_sign={total_functions}")
    print(f"directed_nontrivial_block_cases={total_cases}")
    print(f"max_entropy_decomposition_error={max_decomp_error:.3e}")
    print(f"max_JS_minus_support_boundary={max_js_excess:.3e}")
    print(f"max_spectral_MI_minus_min_boundary={max_mi_excess:.3e}")
    print(f"factorization_zero_boundary_mismatches={factor_mismatches}")
    print(f"sharp_two_bit_JS={sharp_js:.12f}")
    print(f"sharp_two_bit_support_boundary={sharp_p:.12f}")
    print(f"tensor_product_JS={prod_js:.12f}")
    print(f"tensor_product_support_boundary={prod_p:.12f}")
    print(f"tensor_product_opposite_sign_overlap={prod_o:.12f}")
    print(f"tensor_product_signed_curvature={prod_kappa:.12f}")

    ok = (
        max_decomp_error <= TOL and
        max_js_excess <= TOL and
        max_mi_excess <= TOL and
        factor_mismatches == 0 and
        abs(sharp_js-1.0) <= TOL and
        abs(sharp_p-1.0) <= TOL and
        abs(prod_js) <= TOL and
        abs(prod_p) <= TOL and
        prod_kappa > 0.0
    )
    print("PASS" if ok else "FAIL")
    raise SystemExit(0 if ok else 1)

if __name__ == "__main__":
    main()
