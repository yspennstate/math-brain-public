"""Lemma 1'' (superadditivity of phi): B^(i)_j <= phi(a_{j,i}, d_{j,i}) <= d log2(e (a+d)/d) <= d log2(e/d),
a_{j,i} = sum_{|U| = j, i notin U} p(U).  Also checks sum_j phi(a_{j,i}, d_{j,i}) = H(S_i | |S minus i|) >= B_i.
Usage: python check_lemma1pp.py OUTJSON
"""
import os, sys, json, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import check_levels as CL


def phi(a, b):
    return CL.eta(a) + CL.eta(b) - CL.eta(a + b)


def run(tt):
    R = CL.analyse(tt)
    p, n = R["p"], R["n"]
    pc, idx0 = CL.tables(n)
    worst = [0.0, 0.0, 0.0]
    viol = [0, 0, 0]
    for i in range(n):
        z0 = idx0[i]
        z1 = z0 | (1 << i)
        A, Bv = p[:, z0], p[:, z1]
        ph = phi(A, Bv)
        lev = pc[z0]
        tot_level = np.zeros(p.shape[0])
        for j in range(n):
            s = lev == j
            Bij = ph[:, s].sum(1)
            a = A[:, s].sum(1)
            d = Bv[:, s].sum(1)
            agg = phi(a, d)
            with np.errstate(divide="ignore", invalid="ignore"):
                mid = np.where(d > 0, d * np.log2(math.e * (a + d) / np.where(d > 0, d, 1)), 0)
                top = np.where(d > 0, d * np.log2(math.e / np.where(d > 0, d, 1)), 0)
            for q, (lo, hi) in enumerate(((Bij, agg), (agg, mid), (mid, top))):
                viol[q] += int(np.sum(lo > hi + 1e-10))
                with np.errstate(divide="ignore", invalid="ignore"):
                    r = np.where(hi > 1e-14, lo / np.where(hi > 1e-14, hi, 1), 0)
                worst[q] = max(worst[q], float(r.max()))
            tot_level += agg
        # sum_j phi(a_j, d_j) >= B_i  (conditioning on the level only)
        viol[0] += int(np.sum(R["Bi"][:, i] > tot_level + 1e-10))
    return p.shape[0], viol, worst


def main():
    rng = np.random.default_rng(11)
    batches = [CL.all_functions(n) for n in (2, 3, 4)]
    for n in (5, 6, 7, 8, 9):
        batches.append((1 - 2 * rng.integers(0, 2, (150, 1 << n))).astype(np.int8))
        batches.append(CL.random_dt(n, 5, rng, 50))
        batches.append(CL.random_dnf(n, 2, 3, rng, 50))
        batches.append(CL.random_ltf(n, rng, 50))
        batches.append(np.where(rng.random((150, 1 << n)) < 0.08, -1, 1).astype(np.int8))
    for m in (2, 4, 6, 8):
        batches.append(CL.fam_bent_times_x0(m))
    for n in (9, 11):
        for t in range(n // 2 + 1):
            batches.append(CL.fam_threshold(n, t))
    for (w, s) in ((2, 3), (3, 2), (2, 4), (3, 3), (4, 2)):
        batches.append(CL.fam_tribes(w, s))
    total = 0
    V = [0, 0, 0]
    Wst = [0.0, 0.0, 0.0]
    for bt in batches:
        c, v, w = run(bt)
        total += c
        V = [x + y for x, y in zip(V, v)]
        Wst = [max(x, y) for x, y in zip(Wst, w)]
    out = dict(functions=total, violations={"B_ij<=phi(a,d) and B_i<=sum_j phi": V[0], "phi(a,d)<=d log(e(a+d)/d)": V[1],
                                             "d log(e(a+d)/d)<=d log(e/d)": V[2]},
               max_ratio={"B_ij/phi(a,d)": Wst[0], "phi/mid": Wst[1], "mid/top": Wst[2]})
    json.dump(out, open(sys.argv[1], "w", encoding="utf-8"), indent=1)
    print(json.dumps(out))


if __name__ == "__main__":
    main()
