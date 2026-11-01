#!/usr/bin/env python3
"""
Exhaustive n<=4 checker for B12 thinned proxy-label code.

For each Boolean function modulo global sign:
- gauge by the minimizing coordinate character so all active influences <= 1/2;
- compute derivative-support rows eta_i and support-disagreement bank
    M = (1/4) sum_{i != k} Inf_k(eta_i);
- choose a best coordinate-subcube proxy for each row and mark it robust when
    mu(E_i Delta Q_i) <= (1/16) j_i;
- check the known support-depth load L_R <= (16/7) M;
- at the balanced survival s=J/(4M), verify the new resolved-label entropy
    E_A H(T_A(Z)|A) <= (17/14) t J,  t=1-s;
- verify the combined three-part robust code
    2 s t M + s^2 L_R + E H(T_A|A)
      <= (12/7) J - (2/7) J^2/M.

The checker is finite evidence only; the analytic proof is in REPORT.md.
"""
from itertools import combinations
import math

EPS = 1.0 / 16.0

def h2(q):
    if q <= 0.0 or q >= 1.0:
        return 0.0
    return -q * math.log2(q) - (1.0 - q) * math.log2(1.0 - q)

def gauge_truth(vals, n):
    N = 1 << n
    inf = []
    for i in range(n):
        c = sum(vals[x] != vals[x ^ (1 << i)] for x in range(N))
        inf.append(c / N)
    T = [i for i, p in enumerate(inf) if p > 0.5]
    out = []
    for x, v in enumerate(vals):
        parity = sum((x >> i) & 1 for i in T) & 1
        out.append(v * (-1 if parity else 1))
    inf2 = []
    for i in range(n):
        c = sum(out[x] != out[x ^ (1 << i)] for x in range(N))
        inf2.append(c / N)
    return out, inf2

def eta_row(vals, n, i):
    coords = [k for k in range(n) if k != i]
    m = 1 << (n - 1)
    eta = []
    for y in range(m):
        x = 0
        for pos, k in enumerate(coords):
            if (y >> pos) & 1:
                x |= 1 << k
        eta.append(1 if vals[x] != vals[x ^ (1 << i)] else 0)
    return coords, eta

def indicator_influence(eta, coords, k):
    pos = coords.index(k)
    m = len(eta)
    return sum(eta[y] != eta[y ^ (1 << pos)] for y in range(m)) / m

def best_subcube_proxy(eta, coords):
    m = len(eta)
    j = sum(eta) / m
    if j == 0.0:
        return None
    best = None
    d = len(coords)
    for r in range(d + 1):
        for Fpos in combinations(range(d), r):
            for a in range(1 << r):
                err = 0
                for y in range(m):
                    q = 1
                    for z, pos in enumerate(Fpos):
                        if ((y >> pos) & 1) != ((a >> z) & 1):
                            q = 0
                            break
                    err += (eta[y] != q)
                e = err / m
                key = (e, r, Fpos, a)
                if best is None or key[:2] < best[:2]:
                    best = key
    e, r, Fpos, a = best
    F = tuple(coords[p] for p in Fpos)
    return e, j, r, F, a

def main():
    functions = 0
    active_functions = 0
    robust_rows = 0
    checks = {
        "M_ge_J_over_2": 0,
        "support_depth_load": 0,
        "resolved_label_entropy": 0,
        "combined_three_part_code": 0,
    }
    min_M_over_J = float("inf")
    max_M_over_J = 0.0
    worst_label_fraction = 0.0
    worst_total_over_J = 0.0

    for n in range(1, 5):
        N = 1 << n
        # Quotient by global sign: f(0)=+1.
        for mask in range(1 << (N - 1)):
            vals = [1] + [1 if (mask >> (x - 1)) & 1 else -1 for x in range(1, N)]
            functions += 1
            g, j = gauge_truth(vals, n)
            J = sum(j)
            if J == 0.0:
                continue
            active_functions += 1

            p = {}
            proxies = {}
            for i in range(n):
                if j[i] == 0.0:
                    continue
                coords, eta = eta_row(g, n, i)
                for k in coords:
                    p[(i, k)] = indicator_influence(eta, coords, k)
                prox = best_subcube_proxy(eta, coords)
                if prox is not None:
                    e, ji, r, F, a = prox
                    if e <= EPS * ji + 1e-15:
                        proxies[i] = prox
                        robust_rows += 1

            M = sum(p.values()) / 4.0
            assert M + 1e-12 >= J / 2.0
            checks["M_ge_J_over_2"] += 1
            min_M_over_J = min(min_M_over_J, M / J)
            max_M_over_J = max(max_M_over_J, M / J)

            L_R = sum(j[i] * proxies[i][2] for i in proxies)
            assert L_R <= (16.0 / 7.0) * M + 1e-12
            checks["support_depth_load"] += 1

            if M == 0.0:
                continue
            s = J / (4.0 * M)
            t = 1.0 - s
            assert 0.0 <= s <= 0.5 + 1e-12

            # For a random reveal A_t, a robust row i contributes a resolved
            # proxy-label bit exactly when i survives and all r_i triggers are
            # revealed, probability s t^{r_i}. Conditional on that event the
            # bit is 1_{z_F=a}, hence Bernoulli(2^{-r_i}).
            label_entropy = 0.0
            for i, (e, ji, r, F, a) in proxies.items():
                if r >= 1:
                    label_entropy += s * (t ** r) * h2(2.0 ** (-r))

            label_bound = (17.0 / 14.0) * t * J
            assert label_entropy <= label_bound + 1e-12
            checks["resolved_label_entropy"] += 1
            if label_bound > 0.0:
                worst_label_fraction = max(worst_label_fraction, label_entropy / label_bound)

            # Conservative unresolved-address cost: one bit per surviving
            # robust trigger incidence.
            unresolved = s * s * L_R

            # Fleet02/B13 actual-anchor theorem averaged over Bernoulli cuts.
            anchor_correction = 2.0 * s * t * M

            total = anchor_correction + unresolved + label_entropy
            coarse = (12.0 / 7.0) * J - (2.0 / 7.0) * (J * J / M)
            assert total <= coarse + 1e-12
            checks["combined_three_part_code"] += 1
            worst_total_over_J = max(worst_total_over_J, total / J)

    print("PASS")
    print(f"functions_mod_global_sign={functions}")
    print(f"active_after_folded_gauge={active_functions}")
    print(f"robust_rows_tested={robust_rows}")
    for k, v in checks.items():
        print(f"{k}={v}")
    print(f"min_M_over_J={min_M_over_J:.12g}")
    print(f"max_M_over_J={max_M_over_J:.12g}")
    print(f"worst_exact_label_over_bound={worst_label_fraction:.12g}")
    print(f"worst_exact_three_part_over_J={worst_total_over_J:.12g}")

if __name__ == "__main__":
    main()
