"""Second path for NOTES section 5d (pivotal faces), independent of pivotal_faces.analyse where it matters.

(1) Negative controls: the identity checks of pivotal_faces.py must fail when a term is dropped.
(2) Selector bit of F(y, t) = g(y) (-1)^{t 1_A(y)} (g bent on m bits): B_t from the closed form
    p(U + t) = (g 1_A)^(U)^2, p(U) = (ghat(U) - (g 1_A)^(U))^2 (m-bit transforms only), I(1_{A_t}) by counting the edges of A in
    the m-cube, E[s - 1 | A_t] from the truth table; compared with pivotal_faces.analyse for m <= 14 and extended to m = 20.
(3) AND_n: E[s - 1 | A_t] = (1/2) log2(1/eps_t) exactly (the bound of section 5d is attained).
(4) P(A_i and A_j) = P(i, j in S) from the truth table against the Fourier weights, and the summed form
    E[s_C (s - 1)] = E[|S cap C| (|S| - 1)] for C = the even coordinates.
Usage: python -B audit_pivotal_faces.py
"""
import sys, os, math
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import general_witness as gw   # noqa: E402
import pivotal_faces as pf     # noqa: E402


def controls():
    print("(1) negative controls (each should be clearly nonzero)")
    for name, T in (("x0*bent m4", gw.x0bent(4)), ("majority 9", gw.majority(9)), ("tribes 3x3", gw.tribes(3, 3))):
        N = len(T)
        n = N.bit_length() - 1
        idx = np.arange(N, dtype=np.int64)
        p = gw.walsh(T) ** 2
        pc = gw.popcount(idx)
        A = np.array([T != T[idx ^ (1 << i)] for i in range(n)])
        e_drop_par = 0.0
        e_factor2 = 0.0
        for i in range(n):
            IA = 0.0
            par = 0.0
            for j in range(n):
                if j == i:
                    continue
                Ti, Tj, Tij = T[idx ^ (1 << i)], T[idx ^ (1 << j)], T[idx ^ (1 << i) ^ (1 << j)]
                E = (T.astype(np.int64) * Ti * Tj * Tij) == -1
                IA += E.mean()
                par += ((T == Tij) & (Ti == Tj) & (T != Ti)).mean()
                e_factor2 = max(e_factor2, abs(E.mean() - 2 * (E & A[i] & A[j]).mean()))
            M = float(((pc - 1) * p)[(idx >> i) & 1 == 1].sum())
            e_drop_par = max(e_drop_par, abs(M - IA / 4))
        print(f"  {name:12s} max|M_i - I(1_A)/4| = {e_drop_par:.4f}   max|P(E) - 2 P(E,A_i,A_j)| = {e_factor2:.4f}")


def ghat_pair(m, A):
    g = gw.bent_pm(m)
    ind = np.zeros(1 << m)
    ind[A] = 1.0
    return gw.walsh(g), gw.walsh(g * ind), g, ind


def selector_closed(m, A):
    G, H, g, ind = ghat_pair(m, A)
    pUt = H * H
    pU = (G - H) ** 2
    Bt = float(gw.phi_vec(pU, pUt).sum())
    eps = float(ind.mean())
    y = np.arange(1 << m)
    edges = 0
    for j in range(m):
        edges += int(np.count_nonzero(ind != ind[y ^ (1 << j)]))
    IA = edges / (1 << m)          # sum_j P(1_A(y) != 1_A(y^j)), each boundary edge seen from both ends
    # sensitivity on A_t: at (y, t) with y in A, t is pivotal; y_j is pivotal iff F(y, t) != F(y^j, t)
    s_minus1 = np.zeros(1 << m)
    for t in (0, 1):
        F = g * np.where((ind > 0) & (t == 1), -1, 1)
        for j in range(m):
            s_minus1 += (F != F[y ^ (1 << j)]) * ind
    Es1 = float(s_minus1.sum() / (2 * ind.sum()))
    return Bt, eps, IA, Es1


def selector_rows():
    print("(2) selector bit t of F = g(y) (-1)^{t 1_A(y)}, closed form vs brute force")
    print("   m  set        eps_t      B_t/eps   h2/eps    u_t     harper   E[s-1|A_t]  (1/2)log2(1/eps)  brute-force B_t diff")
    rng_seeds = {}
    cases = [(10, "cube", 10), (12, "cube", 8), (12, "cube", 12), (14, "cube", 7), (14, "cube", 14),
             (10, "rand", 5), (12, "rand", 6), (12, "rand", 8), (14, "rand", 7), (16, "rand", 8), (18, "rand", 9), (20, "rand", 10),
             (12, "rand", 4), (16, "rand", 4), (20, "rand", 4)]
    for m, kind, k in cases:
        if kind == "cube":
            A = np.arange(1 << m)[(np.arange(1 << m) & ((1 << k) - 1)) == 0]
            T = pf.sel_cube(m, k) if m <= 14 else None
        else:
            seed = 100 + m * 7 + k
            rng = np.random.default_rng(seed)
            A = rng.choice(1 << m, 1 << (m - k), replace=False)
            T = None
            if m <= 14:
                T = np.concatenate([gw.bent_pm(m), gw.bent_pm(m)]).astype(np.int8)
                T[(1 << m) + A] = -T[(1 << m) + A]
        Bt, eps, IA, Es1 = selector_closed(m, A)
        h = pf.h2(eps)
        diff = ""
        if T is not None:
            idx = np.arange(len(T), dtype=np.int64)
            p = gw.walsh(T) ** 2
            lo = idx[(idx >> m) & 1 == 0]
            Bt_bf = float(gw.phi_vec(p[lo], p[lo | (1 << m)]).sum())
            diff = f"{abs(Bt - Bt_bf):.1e}"
        harper = IA / (2 * eps * math.log2(1 / eps))
        print(f"  {m:2d}  {kind} {k:2d}   {eps:.3e}  {Bt/eps:8.4f}  {h/eps:8.4f}  {Bt/h:.4f}  {harper:7.4f}  {Es1:9.4f}  {0.5*math.log2(1/eps):9.4f}  {diff}")


def spectral_pairs():
    """(4) P(A_i and A_j) = ||D_i D_j f||^2 = P(i, j in S), so E[s_C (s - 1)] = E[|S cap C| (|S| - 1)] for any C.
    The left sides from the truth table, the right sides from the Fourier weights only."""
    print("(4) P(A_i and A_j) against P(i, j in S); E[s_C (s - 1)] against E[|S cap C| (|S| - 1)]")
    for name, T in (("x0*bent m4", gw.x0bent(4)), ("majority 9", gw.majority(9)), ("tribes 3x3", gw.tribes(3, 3)),
                    ("andor d3", gw.andor(3)), ("address 3", gw.address(3)), ("X009 m6", gw.x009(6)),
                    ("sel many m6 N8", pf.sel_many(6, 8, 2, 4)), ("random table n10", gw.random_table(10, 1))):
        N = len(T)
        n = N.bit_length() - 1
        idx = np.arange(N, dtype=np.int64)
        p = gw.walsh(T) ** 2
        pc = gw.popcount(idx)
        A = np.array([T != T[idx ^ (1 << i)] for i in range(n)])
        s = A.sum(0).astype(np.int64)
        err = 0.0
        for i in range(n):
            for j in range(i + 1, n):
                both = ((idx >> i) & 1 == 1) & ((idx >> j) & 1 == 1)
                err = max(err, abs(float((A[i] & A[j]).mean()) - float(p[both].sum())))
        C = list(range(0, n, 2))
        sC = A[C].sum(0).astype(np.int64)
        lhs = float((sC * (s - 1)).mean())
        inC = np.zeros(N, dtype=np.int64)
        for t in C:
            inC += (idx >> t) & 1
        rhs = float((inC * (pc - 1) * p).sum())
        print(f"  {name:18s} n={n:2d} max_ij |P(A_i,A_j) - P(i,j in S)| = {err:.1e}   E[s_C(s-1)] = {lhs:.6f}  "
              f"E[|S cap C|(|S|-1)] = {rhs:.6f}  diff {abs(lhs - rhs):.1e}")


def and_rows():
    print("(3) AND_n: E[s - 1 | A_t] against (1/2) log2(1/eps_t)")
    for n in (4, 8, 12, 16):
        T = gw.table(n, lambda b: np.all(b, axis=1))
        N = len(T)
        idx = np.arange(N, dtype=np.int64)
        A = np.array([T != T[idx ^ (1 << i)] for i in range(n)])
        s = A.sum(0)
        eps = A[0].mean()
        Es1 = float((s - 1)[A[0]].mean())
        print(f"  n={n:2d} eps_t={eps:.3e}  E[s-1|A_t]={Es1:.4f}  (1/2)log2(1/eps_t)={0.5*math.log2(1/eps):.4f}")


if __name__ == "__main__":
    controls()
    selector_rows()
    and_rows()
    spectral_pairs()
    print("done")
