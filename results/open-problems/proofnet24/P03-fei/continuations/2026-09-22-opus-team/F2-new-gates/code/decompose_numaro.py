"""Decompose Numaro's balanced 18-variable g into a 9-variable partial core with
hole groups filled by auxiliary dictators, and verify the exact hole formulas.

Formulas checked (N = 2^m, m = 9 core bits, c0 in {-1,0,+1} the core with holes = 0):
  H(F) = sum_S phi(W0(S)/N) + sum_j sum_S phi(Wj(S)/N)
  I(F) = (1/2N) sum_{edges xy} (c0(x)-c0(y))^2 + sum_j ((m/2+1) k_j - E_j)/N
where W0 = Walsh(c0), Wj = Walsh(signed indicator of group j), E_j = sum over
within-group edges of sigma_x sigma_y.
"""
import sys, json
from fractions import Fraction
import numpy as np
import mpmath as mp

sys.path.insert(0, r"~/mop-fei-opus/proofnet24/P03-fei/fleet-2026-09-21/account01/B15/20260921T130641Z-carry-congruence-n18-profile")

BASE = r"~/mop-fei-opus/proofnet24/P03-fei/continuations/2026-09-22-opus-team"


def fwht(v):
    a = np.asarray(v, dtype=np.int64).copy()
    h = 1
    while h < len(a):
        b = a.reshape(-1, 2 * h)
        x = b[:, :h].copy(); y = b[:, h:].copy()
        b[:, :h] = x + y; b[:, h:] = x - y
        h *= 2
    return a


def popcount_arr(n):
    return np.array([bin(s).count("1") for s in range(1 << n)], dtype=np.int64)


def main():
    tab = np.load(BASE + "/inputs/numaro18_pm1_table.npy").astype(np.int64)
    n = 18; N = 1 << n
    assert tab.shape == (N,) and int(tab.sum()) == 0
    from n18_packet_carry_profile import reconstruct
    tab2, hosts = reconstruct()
    assert np.array_equal(tab, tab2)
    m = 9; Nc = 1 << m
    T = tab.reshape(1 << 9, 1 << 9)  # T[y, x]: y = aux bits (high), x = core bits (low)
    core = T[0].copy()
    # holes: cells whose value depends on aux
    c0 = core.copy()
    groups = []
    for j, cells in enumerate(hosts):
        groups.append(cells)
        for x in cells:
            assert core[x] == 1  # false when aux is false
            c0[x] = 0
    # check structure: F(x,y) = c0(x) off holes, -1 if y_j true (y_j bit = 1 -> -1) on group j
    for yv in range(1 << 9):
        row = T[yv]
        exp = c0.copy()
        for j, cells in enumerate(hosts):
            for x in cells:
                exp[x] = -1 if (yv >> j) & 1 else 1
        assert np.array_equal(row, exp)
    print("structure verified: F(x,y) = c0(x) off hosts, sigma*y_j on host j (sigma=+1 in +-1 convention)")
    # edges / directions of pairs
    info = []
    for j, (a, b) in enumerate(hosts):
        d = a ^ b
        info.append(dict(j=j, cells=[a, b], diff=d, weight_diff=bin(d).count("1"),
                         wa=bin(a).count("1"), wb=bin(b).count("1")))
    print("hosts:", info)
    # exact H and I via formulas
    W0 = fwht(c0)
    pc = popcount_arr(m)
    # influence via edges
    E2 = 0
    for x in range(Nc):
        for i in range(m):
            y = x ^ (1 << i)
            if y > x:
                E2 += int((c0[x] - c0[y]) ** 2)
    I_core = Fraction(E2, 2 * Nc)
    I_core_spec = Fraction(int((pc * W0 * W0).sum()), Nc * Nc)
    assert I_core == I_core_spec, (I_core, I_core_spec)
    I_aux = Fraction(0)
    Wg = []
    for cells in groups:
        ind = np.zeros(Nc, dtype=np.int64)
        for x in cells: ind[x] = 1
        k = len(cells)
        e = sum(1 for a in cells for b in cells if a < b and bin(a ^ b).count("1") == 1)
        I_aux += Fraction(int((m + 2) * k - 2 * e), 2 * Nc)
        W = fwht(ind)
        Wg.append(W)
        # spectral check of aux influence
        I_spec = Fraction(int(((pc + 1) * W * W).sum()), Nc * Nc)
        assert I_spec == Fraction(int((m + 2) * k - 2 * e), 2 * Nc)
    I_tot = I_core + I_aux
    print("I_core =", I_core, float(I_core), " I_aux =", I_aux, " I =", I_tot)
    # full spectrum check against the 18-variable transform
    Wfull = fwht(tab)
    # map: coefficient (S core, T aux): index S + 512*T; value Wfull/N
    # predicted: T=0 -> W0(S)/Nc ; T={j} -> Wg_j(S)/Nc * (sign: y_j true -> -1 = sigma*chi_y, coefficient of chi_{y_j} is +1)
    pred = np.zeros(N, dtype=np.int64)  # scaled by N
    scale = N // Nc
    pred[:Nc] = W0 * scale
    for j in range(9):
        pred[(1 << j) * Nc:(1 << j) * Nc + Nc] = Wg[j] * scale
    assert np.array_equal(pred, Wfull), "spectrum formula mismatch"
    print("full 18-variable Walsh spectrum equals the hole-formula spectrum exactly")
    I_full = Fraction(int((popcount_arr(n) * Wfull * Wfull).sum()), N * N)
    assert I_full == I_tot == Fraction(261, 128)
    mp.mp.dps = 60
    def Hsum(W, Nn):
        s = mp.mpf(0)
        vals, cnts = np.unique(np.abs(W[W != 0]), return_counts=True)
        for v, c in zip(vals, cnts):
            p = mp.mpf(int(v)) ** 2 / mp.mpf(Nn) ** 2
            s += int(c) * p * mp.log(1 / p, 2)
        return s
    H_core = Hsum(W0, Nc)
    H_aux = sum(Hsum(W, Nc) for W in Wg)
    H = H_core + H_aux
    R = H / (mp.mpf(I_tot.numerator) / I_tot.denominator - 1)
    print("H_core =", mp.nstr(H_core, 25), " H_aux =", mp.nstr(H_aux, 25))
    print("H =", mp.nstr(H, 30), " R = H/(I-1) =", mp.nstr(R, 30))
    # singletons
    print("core singleton numerators W0({i}):", [int(W0[1 << i]) for i in range(m)])
    print("core weight sum W0^2/N^2 =", Fraction(int((W0 * W0).sum()), Nc * Nc))
    print("number of -1 cells in c0:", int((c0 == -1).sum()), " +1 cells:", int((c0 == 1).sum()), " holes:", int((c0 == 0).sum()))
    np.save(BASE + "/F2-new-gates/logs/numaro_core_c0.npy", c0.astype(np.int8))
    json.dump(dict(hosts=[list(map(int, h)) for h in hosts], I=str(I_tot), I_core=str(I_core), I_aux=str(I_aux),
                   H=mp.nstr(H, 40), H_core=mp.nstr(H_core, 40), H_aux=mp.nstr(H_aux, 40), R=mp.nstr(R, 40),
                   pairs=info), open(BASE + "/F2-new-gates/logs/numaro_decomposition.json", "w", encoding="utf-8"), indent=1, default=int)


if __name__ == "__main__":
    main()
