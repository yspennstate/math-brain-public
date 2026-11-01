"""Pivotal sets, 2-faces and the price of an unpredictable coordinate (NOTES section 5d), by brute force (n <= 20).

For Boolean f (truth table T, index bit j set <=> x_j = -1) and coordinates i != j:
  A_i      = {x : f(x) != f(x^i)}, the pivotal set of i, P(A_i) = eps_i
  E_ij     = the {i,j}-face through x has an odd number of -1 values (AND-like face)
  Par_ij   = the {i,j}-face through x is a parity face (f(x) = f(x^ij) != f(x^i) = f(x^j))
  s(x)     = #{i : x in A_i}, the sensitivity at x
  I(1_A)   = sum_j P(1_A(x) != 1_A(x^j)), the total influence of the indicator of A
Checked exactly, for every coordinate or pair:
  (P1) 1_{A_i}(x) xor 1_{A_i}(x^j) = 1_{E_ij}(x) = 1_{A_j}(x) xor 1_{A_j}(x^i),  P(E_ij) = 4 P(E_ij, A_i, A_j)
  (P1') P(A_i and A_j) = P(E_ij)/4 + P(Par_ij)
  (P4) M_i := sum_{S contains i} (|S| - 1) fhat(S)^2 = I(1_{A_i})/4 + sum_{j != i} P(Par_ij); summed: E[s^2] = E[|S|^2]
  (P2) Harper: I(1_{A_i}) >= 2 eps_i log2(1/eps_i), hence h2(eps_i) <= eps_i log2(e) + I(1_{A_i})/2
  (P3) for any set C of coordinates: sum_{t in C} h2(eps_t) <= log2(e) sum_C eps_t + (1/2) sum_C I(1_{A_t})
                                                           <= log2(e) sum_C eps_t + 2 E[s_C(x) (s(x) - 1)]
Also B_i = H(S_i | S - i) exactly, and u_i = B_i / h2(eps_i) (u_i near 1: S - i says almost nothing about S_i).
Usage: python -B pivotal_faces.py OUTJSON
"""
import sys, os, json, math
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import general_witness as gw  # noqa: E402  (constructors and walsh only)

LOG2E = 1.0 / math.log(2)


def h2(x):
    if x <= 0 or x >= 1:
        return 0.0
    return -(x * math.log2(x) + (1 - x) * math.log2(1 - x))


def analyse(T, name, unpred=0.9):
    N = len(T)
    n = N.bit_length() - 1
    idx = np.arange(N, dtype=np.int64)
    fh = gw.walsh(T)
    p = fh * fh
    pc = gw.popcount(idx)
    I_spec = float((pc * p).sum())
    S2_spec = float((pc * pc * p).sum())
    pp = p[p > 1e-300]
    H = float(-(pp * np.log2(pp)).sum())
    A = np.zeros((n, N), dtype=bool)
    for i in range(n):
        A[i] = T != T[idx ^ (1 << i)]
    eps = A.mean(1)
    s = A.sum(0).astype(np.int64)
    Es2 = float((s * s).mean())
    I_sens = float(s.mean())
    PE = np.zeros((n, n))
    PPar = np.zeros((n, n))
    PAA = np.zeros((n, n))
    err_p1 = 0.0
    err_p1b = 0.0
    for i in range(n):
        Ti = T[idx ^ (1 << i)]
        for j in range(i + 1, n):
            Tj = T[idx ^ (1 << j)]
            Tij = T[idx ^ (1 << i) ^ (1 << j)]
            prod = T.astype(np.int64) * Ti * Tj * Tij
            E = prod == -1
            Par = (T == Tij) & (Ti == Tj) & (T != Ti)
            a = (A[i] != A[i][idx ^ (1 << j)])
            b = (A[j] != A[j][idx ^ (1 << i)])
            err_p1 = max(err_p1, float(np.count_nonzero(a != E)), float(np.count_nonzero(b != E)))
            pe = E.mean()
            pe4 = 4 * (E & A[i] & A[j]).mean()
            paa = (A[i] & A[j]).mean()
            ppar = Par.mean()
            err_p1b = max(err_p1b, abs(pe - pe4), abs(paa - (pe / 4 + ppar)))
            PE[i, j] = PE[j, i] = pe
            PPar[i, j] = PPar[j, i] = ppar
            PAA[i, j] = PAA[j, i] = paa
    IA = PE.sum(1)                                   # I(1_{A_i}) = sum_j P(E_ij), by (P1)
    M = np.array([float(((pc - 1) * p)[(idx >> i) & 1 == 1].sum()) for i in range(n)])
    err_p4 = float(np.max(np.abs(M - (IA / 4 + PPar.sum(1)))))
    B = np.zeros(n)
    for i in range(n):
        lo = idx[(idx >> i) & 1 == 0]
        B[i] = float(gw.phi_vec(p[lo], p[lo | (1 << i)]).sum())
    h = np.array([h2(e) for e in eps])
    harper = np.array([IA[i] / (2 * eps[i] * math.log2(1 / eps[i])) if 0 < eps[i] < 1 else float("nan") for i in range(n)])
    p2_slack = float(np.min(eps * LOG2E + IA / 2 - h))
    u = np.array([B[i] / h[i] if h[i] > 1e-15 else float("nan") for i in range(n)])
    C = [i for i in range(n) if not np.isnan(u[i]) and u[i] >= unpred]
    sC = A[C].sum(0).astype(np.int64) if C else np.zeros(N, dtype=np.int64)
    bound1 = LOG2E * float(eps[C].sum()) + 0.5 * float(IA[C].sum())
    bound2 = LOG2E * float(eps[C].sum()) + 2.0 * float((sC * (s - 1)).mean())
    O2 = float(np.triu(PE, 1).sum())
    O2_id = 2 * float((s * (s - 1)).mean()) - 4 * float(np.triu(PPar, 1).sum())
    I = float(eps.sum())
    k = int(np.nanargmax(np.where(np.isnan(u), -1, u))) if n else 0
    row = dict(name=name, n=n, I=I, H=H, B=float(B.sum()), B_over_I=float(B.sum() / I), sum_h2_over_I=float(h.sum() / I),
               O2_over_I=O2 / I, Es2_over_I=Es2 / I,
               err=dict(I_sens_vs_spec=abs(I_sens - I_spec), I_eps_vs_spec=abs(I - I_spec), Es2_vs_S2=abs(Es2 - S2_spec),
                        P1_points=err_p1, P1_probs=err_p1b, P4=err_p4, O2_identity=abs(O2 - O2_id)),
               harper_min=float(np.nanmin(harper)) if np.any(~np.isnan(harper)) else None, P2_min_slack=p2_slack,
               unpred_set=C, unpred_B_over_I=float(B[C].sum() / I), unpred_h2_over_I=float(h[C].sum() / I),
               P3_bound1_over_I=bound1 / I, P3_bound2_over_I=bound2 / I,
               most_unpred=dict(i=k, u=float(u[k]), eps=float(eps[k]), B_over_eps=float(B[k] / eps[k]) if eps[k] > 0 else None,
                                h2_over_eps=float(h[k] / eps[k]) if eps[k] > 0 else None, harper=float(harper[k]),
                                IA_over_eps=float(IA[k] / eps[k]) if eps[k] > 0 else None))
    return row


def sel_random(m, logeps, seed):
    """F(y, t) = g(y) (-1)^{t 1_A(y)}: g bent on m bits, A a uniformly random set of 2^(m - logeps) points, t = bit m"""
    rng = np.random.default_rng(seed)
    g = gw.bent_pm(m)
    A = rng.choice(1 << m, 1 << (m - logeps), replace=False)
    F = np.concatenate([g, g]).astype(np.int8)
    F[(1 << m) + A] = -F[(1 << m) + A]
    return F


def sel_cube(m, k):
    """the same with A = {y : y_0 = ... = y_{k-1} = 0}, a subcube of codimension k (k = m is X009)"""
    g = gw.bent_pm(m)
    F = np.concatenate([g, g]).astype(np.int8)
    A = np.arange(1 << m)[(np.arange(1 << m) & ((1 << k) - 1)) == 0]
    F[(1 << m) + A] = -F[(1 << m) + A]
    return F


def sel_many(m, N, logeps, seed):
    """F(y, t) = g(y) (-1)^{<t, a(y)>}: N selector bits t_k (bits m..m+N-1), each with an independent random set A_k of
    2^(m - logeps) points, a(y) = (1_{A_k}(y))_k"""
    rng = np.random.default_rng(seed)
    g = gw.bent_pm(m)
    sets = [set(rng.choice(1 << m, 1 << (m - logeps), replace=False).tolist()) for _ in range(N)]
    idx = np.arange(1 << (m + N), dtype=np.int64)
    y = idx & ((1 << m) - 1)
    par = np.zeros(len(idx), dtype=np.int64)
    for k in range(N):
        mem = np.zeros(1 << m, dtype=np.int64)
        mem[list(sets[k])] = 1
        par ^= ((idx >> (m + k)) & 1) & mem[y]
    return (g[y] * (1 - 2 * par)).astype(np.int8)


def main():
    out = sys.argv[1]
    fams = [("tribes 3x3", lambda: gw.tribes(3, 3)), ("tribes 4x3", lambda: gw.tribes(4, 3)), ("tribes 3x5", lambda: gw.tribes(3, 5)),
            ("majority 9", lambda: gw.majority(9)), ("majority 13", lambda: gw.majority(13)),
            ("ball 12 r3", lambda: gw.ball(12, 3)), ("x0*bent m4", lambda: gw.x0bent(4)),
            ("andor d3", lambda: gw.andor(3)), ("andor d4", lambda: gw.andor(4)), ("OR4 of MAJ3", lambda: gw.or_of_maj3(4)),
            ("MAJ3 of AND4", lambda: gw.maj3_of_and(4)), ("address 3", lambda: gw.address(3)), ("address 4", lambda: gw.address(4)),
            ("X002 m7", lambda: gw.x002(7)), ("X003 k4 r8", lambda: gw.x003(4, 8)),
            ("X009 m6", lambda: gw.x009(6)), ("X009 m10", lambda: gw.x009(10)), ("X009 m14", lambda: gw.x009(14)),
            ("sel cube m12 k4", lambda: sel_cube(12, 4)), ("sel cube m12 k8", lambda: sel_cube(12, 8)),
            ("sel rand m12 eps2^-4", lambda: sel_random(12, 4, 1)), ("sel rand m12 eps2^-8", lambda: sel_random(12, 8, 2)),
            ("sel rand m14 eps2^-6", lambda: sel_random(14, 6, 3)),
            ("sel many m6 N8 eps2^-2", lambda: sel_many(6, 8, 2, 4)), ("sel many m8 N8 eps2^-3", lambda: sel_many(8, 8, 3, 5)),
            ("sel many m8 N12 eps2^-4", lambda: sel_many(8, 12, 4, 6)),
            ("random dnf n12 s1", lambda: gw.random_dnf(12, 6, 3, 1)), ("random table n10 s1", lambda: gw.random_table(10, 1))]
    rows = []
    for name, mk in fams:
        T = mk()
        r = analyse(T, name)
        rows.append(r)
        mu = r["most_unpred"]
        e = r["err"]
        print(f"{name:24s} n={r['n']:2d} B/I={r['B_over_I']:.4f} H/I={r['H']/r['I']:.4f} sumh2/I={r['sum_h2_over_I']:.4f} "
              f"O2/I={r['O2_over_I']:.4f} harper_min={r['harper_min']:.4f} P2slack={r['P2_min_slack']:.2e} "
              f"maxerr={max(e.values()):.1e} | unpred {len(r['unpred_set'])}: B/I={r['unpred_B_over_I']:.4f} "
              f"P3={r['P3_bound1_over_I']:.4f}/{r['P3_bound2_over_I']:.4f} | top u={mu['u']:.4f} eps={mu['eps']:.3g} "
              f"harper={mu['harper']:.4f}", flush=True)
    with open(out, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(dict(rows=rows), fh, indent=1)
    print("wrote", out, len(rows), "functions")


if __name__ == "__main__":
    main()
