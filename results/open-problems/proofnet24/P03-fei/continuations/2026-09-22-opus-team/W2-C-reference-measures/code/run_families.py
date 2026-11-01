"""Family survey: H, I and reference-measure costs (bits) for the hard families.

  Tbin : optimal binary tree-Markov (hierarchical) reference, exact subset DP
  LW   : optimal level-wise product reference (conditional Bernoulli per level) = lower envelope of F5-type refs
  F5   : F5's rank-weighted reference, coordinates ordered by influence, best a on a grid
"""
import sys, time, json
import numpy as np
import wlib as W

W.set_polite()
rng = np.random.default_rng(7)


def f5_best(p, n):
    inf = W.influences(p, n)
    order = list(np.argsort(-inf, kind="stable"))
    best = None
    for a in (1.1, 1.25, 1.5, 1.75, 2.0, 2.5, 3.0, 4.0):
        c = W.f5_rank_cost(p, n, order, a)
        if best is None or c < best[0]:
            best = (c, a)
    return best


def survey(name, tt, n, do_lw=True, do_tree=True):
    t0 = time.time()
    p = W.spectrum(tt)
    H = W.H_of(p); I = W.I_of(p, n)
    row = {"name": name, "n": n, "H": H, "I": I, "H/I": H / I}
    if do_tree:
        Tb, tree = W.tree_markov_H(p, n)
        row.update({"Tbin": Tb, "Tbin/I": Tb / I, "(Tbin-H)/I": (Tb - H) / I, "tree": str(tree)})
    if do_lw:
        L = W.levelwise_product_cost(p, n)
        row.update({"LW": L, "LW/I": L / I})
        c5, a5 = f5_best(p, n)
        row.update({"F5": c5, "F5/I": c5 / I, "F5_a": a5})
    row["secs"] = time.time() - t0
    return row


def fmt(r):
    s = f"{r['name']:28s} n={r['n']:2d} H/I={r['H/I']:.4f}"
    if "Tbin" in r:
        s += f"  Tbin/I={r['Tbin/I']:.4f} (Tbin-H)/I={r['(Tbin-H)/I']:.4f}"
    if "LW" in r:
        s += f"  LW/I={r['LW/I']:.4f}  F5/I={r['F5/I']:.4f}(a={r['F5_a']})"
    s += f"  [{r['secs']:.1f}s]"
    return s


def main():
    rows = []
    fams = []
    for n in (5, 7, 9, 11, 13, 15, 17):
        fams.append((f"maj{n}", W.fam_majority(n), n))
    for n in (4, 8, 12, 16):
        fams.append((f"AND{n}", W.fam_and(n), n))
    for (w, s) in ((2, 3), (2, 5), (2, 8), (3, 3), (3, 4), (3, 5), (4, 3), (4, 4)):
        fams.append((f"tribes w{w} s{s}", W.fam_tribes(w, s), w * s))
    fams.append(("recmaj d2", W.fam_recmaj(2), 9))
    for m2 in (2, 3, 4, 5, 6, 7):
        fams.append((f"bent m={2*m2}", W.fam_bent(m2), 2 * m2))
        fams.append((f"bent+flip m={2*m2}", W.fam_bent_flip(m2), 2 * m2 + 1))
    for k in (2, 3):
        fams.append((f"addressing k{k}", W.fam_addressing(k), k + (1 << k)))
    for n in (5, 9, 13, 17):
        fams.append((f"maj{n}+flip(F4 6.1)", W.fam_maj_flip(n), n + 1))
    # AND/OR chains (lexicographic LTFs, H/I -> 4)
    for n in (8, 12, 16):
        ops = ['&' if j % 2 == 0 else '|' for j in range(n - 1)]
        fams.append((f"alt chain n{n}", W.fam_chain(ops), n))
    # random LTFs with gaussian weights
    for n in (10, 14):
        w = rng.normal(size=n)
        fams.append((f"LTF gauss n{n}", W.fam_ltf(w, 0.3), n))
    # mux of recmaj and a scrambled recmaj (the same 9 variables)
    g = W.fam_recmaj(2)
    perm = rng.permutation(9)
    gp = W.fam_recmaj(2, perm=perm)
    fams.append(("mux(recmaj, recmaj o pi)", W.fam_mux(g, gp, 9), 10))
    fams.append(("recmaj o pi", gp, 9))
    for name, tt, n in fams:
        r = survey(name, tt, n, do_lw=(n <= 17))
        rows.append(r)
        print(fmt(r), flush=True)
    # Numaro's g (n=18): DP is 3^18/2 splits
    g18 = W.load_numaro()
    r = survey("numaro g18", g18, 18, do_lw=True)
    rows.append(r)
    print(fmt(r), flush=True)
    print("tree(g18) =", r["tree"])
    with open("../logs/run_families.json", "w") as fh:
        json.dump(rows, fh, indent=1)


if __name__ == "__main__":
    main()
