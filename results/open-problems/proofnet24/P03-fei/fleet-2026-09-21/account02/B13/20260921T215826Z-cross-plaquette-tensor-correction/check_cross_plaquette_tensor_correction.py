#!/usr/bin/env python3
"""Exhaustive self-check for B13 cross-plaquette tensor-correction theorem.

Enumerates Boolean functions modulo global sign through n=4 and every directed
nontrivial block cut. Uses only the Python standard library.
"""
from math import log2

TOL = 1e-12


def bit_positions(mask, n):
    return [i for i in range(n) if (mask >> i) & 1]


def full_index(a, b, A, B):
    x = 0
    for j, i in enumerate(A):
        if (a >> j) & 1:
            x |= 1 << i
    for j, i in enumerate(B):
        if (b >> j) & 1:
            x |= 1 << i
    return x


def h2(q):
    if q <= 0.0 or q >= 1.0:
        return 0.0
    return -q * log2(q) - (1 - q) * log2(1 - q)


def phi(q):
    if q <= 0.0:
        return 0.0
    return 2 * q * log2(1 / q)


def cross_bank(vals, n, A_mask):
    """P_{A->B}; quotient-normalized support-boundary convention."""
    A = bit_positions(A_mask, n)
    B = [i for i in range(n) if not ((A_mask >> i) & 1)]
    total = 0.0
    for i in A:
        denom = 1 << (n - 1)
        for k in B:
            count = 0
            # Fix x_i=0; other n-1 bits uniform. Each k-edge is counted twice,
            # exactly as Pr_y[1_E(y) != 1_E(y+e_k)].
            for x in range(1 << n):
                if (x >> i) & 1:
                    continue
                ei = 1 << i
                ek = 1 << k
                e0 = vals[x] != vals[x ^ ei]
                e1 = vals[x ^ ek] != vals[x ^ ek ^ ei]
                if e0 != e1:
                    count += 1
            total += count / denom
    return total


def best_anchor(vals, n, A_mask):
    """Best anchor in B for theorem with correction entropy H(C|B)."""
    A = bit_positions(A_mask, n)
    B = [i for i in range(n) if not ((A_mask >> i) & 1)]
    na, nb = 1 << len(A), 1 << len(B)
    matrix = [[vals[full_index(a, b, A, B)] for b in range(nb)] for a in range(na)]
    best = None
    for b0 in range(nb):
        qs = []
        for b in range(nb):
            plus = 0
            for a in range(na):
                if matrix[a][b] * matrix[a][b0] == 1:
                    plus += 1
            minus = na - plus
            qs.append(min(plus, minus) / na)
        ph = sum(phi(q) for q in qs) / nb
        hh = sum(h2(q) for q in qs) / nb
        dd = sum(qs) / nb
        rec = (ph, hh, dd, b0)
        if best is None or rec < best:
            best = rec
    return best


def one_point_vals(n):
    vals = [1] * (1 << n)
    vals[0] = -1
    return vals


def main():
    cases = 0
    funcs = 0
    max_phi_excess = -1e100
    max_entropy_excess = -1e100
    max_distance_excess = -1e100
    pzero_bad = 0
    exact_sharp = 0
    by_n = []
    for n in range(2, 5):
        nfunc = 0
        ncases = 0
        N = 1 << n
        for code in range(1 << (N - 1)):
            vals = [1] * N
            for x in range(1, N):
                if (code >> (x - 1)) & 1:
                    vals[x] = -1
            nfunc += 1
            for A_mask in range(1, (1 << n) - 1):
                P = cross_bank(vals, n, A_mask)
                ph, hh, dd, _ = best_anchor(vals, n, A_mask)
                max_phi_excess = max(max_phi_excess, ph - P / 2)
                max_entropy_excess = max(max_entropy_excess, hh - P / 2)
                max_distance_excess = max(max_distance_excess, dd - P / 4)
                if abs(P) <= TOL and dd > TOL:
                    pzero_bad += 1
                if (P > TOL and abs(ph - P / 2) <= TOL and
                        abs(hh - P / 2) <= TOL and abs(dd - P / 4) <= TOL):
                    exact_sharp += 1
                cases += 1
                ncases += 1
        funcs += nfunc
        by_n.append((n, nfunc, ncases))

    vals = one_point_vals(2)
    P = cross_bank(vals, 2, 1)
    ph, hh, dd, anchor = best_anchor(vals, 2, 1)
    print("B13 cross-plaquette tensor-correction exhaustive self-check")
    for n, nfunc, ncases in by_n:
        print(f"n={n} functions_mod_global_sign={nfunc} directed_cuts={ncases}")
    print(f"total_functions={funcs}")
    print(f"total_directed_cut_cases={cases}")
    print(f"max_phi_excess={max_phi_excess:.3e}")
    print(f"max_conditional_entropy_excess={max_entropy_excess:.3e}")
    print(f"max_hamming_distance_excess={max_distance_excess:.3e}")
    print(f"P_zero_nonfactor_anchor_failures={pzero_bad}")
    print(f"exact_sharp_cases={exact_sharp}")
    print("sharp_witness_two_bit_one_point_defect:")
    print(f"  P={P:.12g}")
    print(f"  Phi={ph:.12g}")
    print(f"  Hcorr={hh:.12g}")
    print(f"  distance={dd:.12g}")
    print(f"  anchor={anchor}")
    ok = (max_phi_excess <= TOL and max_entropy_excess <= TOL and
          max_distance_excess <= TOL and pzero_bad == 0 and
          abs(P - 1) <= TOL and abs(ph - 0.5) <= TOL and
          abs(hh - 0.5) <= TOL and abs(dd - 0.25) <= TOL)
    print("PASS" if ok else "FAIL")
    if not ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
