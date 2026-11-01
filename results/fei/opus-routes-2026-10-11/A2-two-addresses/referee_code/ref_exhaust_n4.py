"""Exhaustive check of the two-address class K2 for n <= 4 (every Boolean function, every address pair).

For each n in {2,3,4}: enumerate all 2^(2^n) Boolean functions, decide K2 membership exactly
(for |C| = n - 2 <= 2 a law on two bits is product iff a00 a11 = a01 a10), and for every member:
  * decide exactly the signs of H - c* I and H - 4 I (c* = 16/3 - (3/2) log2 3);
  * run the exact row analysis (Lemmas 1-6, the identity of Lemma 3(c), e_T <= ebar_T row by row);
  * decide exactly the sign of Phi = sum_T w_T ebar_T and of Phi - (H - c* I).
Also: max H/I over K2 and over all functions; equality cases of H = c* I."""
import sys, json, time
from fractions import Fraction
import numpy as np
from refk2 import walsh_int, LogLin, H_minus_cI_exact, H_float, I_exact
from ref_rows import analyse_row

t0 = time.time()
results = {}
for n in (2, 3, 4):
    N = 1 << n
    nf = 1 << N
    F = np.array([[1 - 2 * ((k >> x) & 1) for x in range(N)] for k in range(nf)], dtype=np.int64)
    W = walsh_int(F)
    pairs = [(a, b) for a in range(n) for b in range(a + 1, n)]
    member = np.zeros(nf, dtype=bool)
    pair_of = {}
    for (a1, a2) in pairs:
        C = [i for i in range(n) if i not in (a1, a2)]
        m = len(C)
        ok = np.ones(nf, dtype=bool)
        if m == 2:
            c1, c2 = C
            for t in range(4):
                T = ((t & 1) << a1) | (((t >> 1) & 1) << a2)
                a00 = W[:, T] ** 2
                a01 = W[:, T | (1 << c1)] ** 2
                a10 = W[:, T | (1 << c2)] ** 2
                a11 = W[:, T | (1 << c1) | (1 << c2)] ** 2
                ok &= (a00 * a11 == a01 * a10)
        # m <= 1: every law is product
        for k in np.nonzero(ok & ~member)[0]:
            pair_of[int(k)] = (a1, a2)
        member |= ok
    idx = np.nonzero(member)[0]
    n_member = len(idx)
    worst_c = None
    n_eq = 0
    eq_examples = []
    bad_c = []
    bad_4 = []
    bad_chain = []
    maxratio = 0.0
    argmax = None
    for k in idx:
        k = int(k)
        Wk = W[k]
        if np.count_nonzero(Wk[1:]) == 0:  # constant function: I = 0, skip ratio
            continue
        Q, Itot = H_minus_cI_exact(Wk, n)
        s = Q.sign()
        if s > 0:
            bad_c.append(k)
        if s == 0:
            n_eq += 1
            if len(eq_examples) < 5:
                eq_examples.append(k)
        Q4, _ = H_minus_cI_exact(Wk, n, c_rational=4, c_is_cstar=False)
        if Q4.sign() > 0:
            bad_4.append(k)
        r = H_float(Wk, n) / float(Itot)
        if r > maxratio:
            maxratio, argmax = r, k
        # exact chain H - cI <= Phi <= 0 with the address pair that certified membership
        if n >= 3:
            a1, a2 = pair_of[k]
            C = [i for i in range(n) if i not in (a1, a2)]
            m = len(C)
            Phi = LogLin()
            HcI = LogLin()
            for t in range(4):
                T = ((t & 1) << a1) | (((t >> 1) & 1) << a2)
                V = []
                for u in range(1 << m):
                    U = sum(((u >> j) & 1) << C[j] for j in range(m))
                    V.append(int(Wk[T | U]))
                res = analyse_row(V, m, n, bin(t).count("1"))
                assert res is not False
                if res is None:
                    continue
                Phi.add(res["web"])
                HcI.add(res["we"])
                # row-wise e_T <= ebar_T
                d = LogLin().add(res["web"]).add(res["we"], -1)
                if d.sign() < 0:
                    bad_chain.append((k, "row e>ebar"))
            diff = LogLin().add(HcI).add(Q, -1).clean()
            if diff.q0 != 0 or diff.ql:
                bad_chain.append((k, "sum w e != H - cI"))
            if Phi.sign() > 0:
                bad_chain.append((k, "Phi>0"))
    # max H/I over all functions (for comparison)
    maxall = 0.0
    for k in range(nf):
        if np.count_nonzero(W[k][1:]) == 0:
            continue
        p = (W[k].astype(np.float64) / N) ** 2
        I = float(sum(p[S] * bin(S).count("1") for S in range(N)))
        nz = p > 0
        Hh = float(-(p[nz] * np.log2(p[nz])).sum())
        maxall = max(maxall, Hh / I)
    results[n] = dict(functions=nf, K2_members=n_member, H_gt_cstar_I=len(bad_c), H_gt_4I=len(bad_4),
                      equality_cases=n_eq, equality_examples=eq_examples, chain_failures=bad_chain[:10],
                      n_chain_failures=len(bad_chain), max_ratio_K2=maxratio, argmax=argmax, max_ratio_all=maxall)
    print(n, results[n], f"{time.time()-t0:.1f}s", flush=True)

json.dump(results, open(sys.argv[1] if len(sys.argv) > 1 else "ref_exhaust_n4.json", "w", encoding="utf-8"), indent=1, default=str)
