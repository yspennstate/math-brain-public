"""Exhaustive tests over all monotone Boolean functions of n <= 6 variables (7,828,354 at n = 6).

For every monotone f (relevant coordinates only matter):
  - H, I, influences (exact integer Walsh transform);
  - the desirability preorder, whether it is total (f regular = shifted), its width w and the
    dominance profile K = max_d #{j : |D(j)| <= d}/d;
  - the key step of Theorem 1: for j in D(i) - {i}, the pivotal set of i contains no j-edge;
  - Lemma 3 with U_i = D(i) - {i}: value / L1;
  - Lemma 4 with the order by |D| ascending: Sigma_r / ((L1 + ln K) I);
  - Theorem 2: H/I against C(K).
Usage: python exhaust.py N
"""
import sys, time, math
import numpy as np
import numba as nb
from monolib import *

Bc = 3.0 * math.sqrt(3.0 / math.pi)
L1 = 2.0 * math.log(Bc) + 2.0


def C_of_K(K):
    L = L1 + math.log(K)
    a = (1.0 + math.sqrt(1.0 + 4.0 / L)) / 2.0
    return 3.0 + (1.0 + math.log(a / (a - 1.0)) + a * L) / math.log(2.0)


@nb.njit(cache=True)
def pivotal_edge_violation(tt, n, dom, rel):
    """Return 1 if some relevant i and j in D(i)-{i} have i pivotal at both x and x+e_j."""
    N = 1 << n
    for i in range(n):
        if not ((rel >> i) & 1):
            continue
        bi = 1 << i
        for j in range(n):
            if j == i or not dom[i, j]:
                continue
            bj = 1 << j
            for x in range(N):
                if (x & bi) or (x & bj):
                    continue
                # i pivotal at x (x_i = 0 here) : f(x+e_i) = 1, f(x) = 0
                p1 = ((tt >> np.uint64(x | bi)) & np.uint64(1)) == 1 and ((tt >> np.uint64(x)) & np.uint64(1)) == 0
                y = x | bj
                p2 = ((tt >> np.uint64(y | bi)) & np.uint64(1)) == 1 and ((tt >> np.uint64(y)) & np.uint64(1)) == 0
                if p1 and p2:
                    return 1
    return 0


@nb.njit(cache=True)
def run_all(tabs, n, L1, CK_table):
    M = tabs.size
    HI = np.zeros(M)
    Hs = np.zeros(M)
    Is = np.zeros(M)
    regular = np.zeros(M, dtype=np.bool_)
    widths = np.zeros(M, dtype=np.int64)
    Ks = np.zeros(M)
    viol = 0
    lem3max = 0.0
    lem4max = 0.0
    thm2max = 0.0
    thm2arg = -1
    nrel = np.zeros(M, dtype=np.int64)
    for t in range(M):
        tt = tabs[t]
        W = wht_int(tt, n)
        H, I = entropy_influence(W, n)
        Hs[t] = H
        Is[t] = I
        if I <= 0.0:
            continue
        HI[t] = H / I
        rel = relevant_mask(tt, n)
        nrel[t] = popcount(rel)
        dom = desirability(tt, n)
        w, K, dsz = width_and_profile(dom, rel, n)
        widths[t] = w
        Ks[t] = K
        regular[t] = (w == 1)
        viol += pivotal_edge_violation(tt, n, dom, rel)
        # Lemma 3 with U_i = D(i) - {i} (relevant coordinates only)
        Umask = np.zeros(n, dtype=np.int64)
        for i in range(n):
            if (rel >> i) & 1:
                m = 0
                for j in range(n):
                    if j != i and dom[i, j] and ((rel >> j) & 1):
                        m |= (1 << j)
                Umask[i] = m
        l3, inf = lemma3_values(W, n, Umask)
        for i in range(n):
            if (rel >> i) & 1:
                if l3[i] / L1 > lem3max:
                    lem3max = l3[i] / L1
        # order by |D| ascending among relevant coordinates; irrelevant ones get the last ranks
        keys = np.empty(n)
        for i in range(n):
            keys[i] = dsz[i] if (rel >> i) & 1 else 1e9
        order = np.argsort(keys, kind='mergesort')
        rank = np.zeros(n)
        for pos in range(n):
            rank[order[pos]] = pos + 1
        sig = sigma_rank(W, n, rank)
        r4 = sig / ((L1 + np.log(K)) * I)
        if r4 > lem4max:
            lem4max = r4
        # Theorem 2 constant: CK_table indexed by round(K*60)
        idx = int(round(K * 60.0))
        CK = CK_table[idx]
        r2 = (H / I) / CK
        if r2 > thm2max:
            thm2max = r2
            thm2arg = t
    return HI, Hs, Is, regular, widths, Ks, viol, lem3max, lem4max, thm2max, thm2arg, nrel


def main():
    setup_process()
    n = int(sys.argv[1])
    t0 = time.time()
    tabs = monotone_tables(n)
    print(f"n={n}: {tabs.size} monotone functions (enumerated in {time.time()-t0:.1f}s)", flush=True)
    # K is a rational c/d with c, d <= 6: tabulate C(K) on a grid of step 1/60 (exact for d | 60)
    CK_table = np.array([C_of_K(max(k / 60.0, 1.0)) if k >= 60 else C_of_K(1.0) for k in range(60 * 7 + 1)])
    t0 = time.time()
    HI, Hs, Is, regular, widths, Ks, viol, lem3max, lem4max, thm2max, thm2arg, nrel = run_all(tabs, n, L1, CK_table)
    print(f"computed in {time.time()-t0:.1f}s", flush=True)
    print(f"L1 = {L1:.10f}; C(1) = {C_of_K(1.0):.10f}; C(2) = {C_of_K(2.0):.6f}; C(3) = {C_of_K(3.0):.6f}; C(6) = {C_of_K(6.0):.6f}")
    print(f"pivotal-edge violations of the key step (must be 0): {viol}")
    print(f"Lemma 3 (U_i = D(i)-i): max value / L1 = {lem3max:.6f}")
    print(f"Lemma 4' (order by |D|): max Sigma_r / ((L1 + ln K) I) = {lem4max:.6f}")
    print(f"Theorem 2: max (H/I) / C(K) = {thm2max:.6f} at table {int(tabs[thm2arg]) if thm2arg>=0 else -1}")
    nonconst = Is > 0
    i_all = int(np.argmax(HI))
    print(f"max H/I over all monotone: {HI[i_all]:.6f} (H={Hs[i_all]:.6f}, I={Is[i_all]:.6f}, table {int(tabs[i_all])}, width {widths[i_all]}, K {Ks[i_all]:.4f})")
    reg = regular & nonconst
    print(f"regular (shifted) nonconstant: {int(reg.sum())}")
    ir = int(np.argmax(np.where(reg, HI, -1.0)))
    print(f"max H/I over regular: {HI[ir]:.6f} (table {int(tabs[ir])}, relevant {nrel[ir]})")
    for w in range(1, n + 1):
        sel = nonconst & (widths == w)
        if sel.sum():
            j = int(np.argmax(np.where(sel, HI, -1.0)))
            print(f"  width {w}: {int(sel.sum())} functions, max H/I {HI[j]:.6f} (table {int(tabs[j])}, K {Ks[j]:.4f})")
    Kvals = np.unique(np.round(Ks[nonconst], 6))
    for K in Kvals:
        sel = nonconst & (np.abs(Ks - K) < 1e-6)
        j = int(np.argmax(np.where(sel, HI, -1.0)))
        print(f"  K = {K:.4f}: {int(sel.sum())} functions, max H/I {HI[j]:.6f}, bound C(K) = {C_of_K(K):.4f}")
    np.savez_compressed(f"../logs/exhaust_n{n}.npz", tabs=tabs, HI=HI, regular=regular, widths=widths, Ks=Ks)


if __name__ == "__main__":
    main()
