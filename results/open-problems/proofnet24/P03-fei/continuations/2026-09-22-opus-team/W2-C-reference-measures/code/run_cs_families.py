"""Optimal count-splitting tree (CSopt) on the hard families (n <= 14) and adversarial search at n = 6..8."""
import sys, time, json
import numpy as np
import wlib as W, csdp

W.set_polite()
rng = np.random.default_rng(17)


def numaro_restriction(k_aux):
    """Numaro's g with core coordinates 0..8 free, auxiliary 9..9+k_aux-1 free, the other auxiliaries set to +1 (false)."""
    g = W.load_numaro()
    n = 9 + k_aux
    N = 1 << n
    x = np.arange(N, dtype=np.int64)
    # bits of the remaining auxiliaries (positions 9+k_aux .. 17) are 0 (= coordinate value +1 = false)
    return g[x].astype(np.int8), n


def fams():
    L = []
    for n in (5, 9, 13):
        L.append((f"maj{n}", W.fam_majority(n), n))
    for (w, s) in ((2, 5), (3, 4), (4, 3)):
        L.append((f"tribes w{w} s{s}", W.fam_tribes(w, s), w * s))
    L.append(("recmaj d2", W.fam_recmaj(2), 9))
    g = W.fam_recmaj(2)
    for trial in range(3):
        perm = rng.permutation(9)
        L.append((f"mux(recmaj, recmaj o pi#{trial})", W.fam_mux(g, W.fam_recmaj(2, perm=perm), 9), 10))
    # 2 address bits choosing among 4 scrambled copies (n = 11)
    copies = [W.fam_recmaj(2, perm=rng.permutation(9)) for _ in range(4)]
    N = 1 << 11
    x = np.arange(N)
    a = x & 3
    y = x >> 2
    tt = np.array([copies[a[i]][y[i]] for i in range(N)], dtype=np.int8)
    L.append(("addr2 over 4 scrambled recmaj", tt, 11))
    for m2 in (2, 3, 4, 5, 6):
        L.append((f"bent+flip m={2*m2}", W.fam_bent_flip(m2), 2 * m2 + 1))
    L.append(("addressing k3", W.fam_addressing(3), 11))
    for n in (9, 13):
        L.append((f"maj{n}+flip(F4 6.1)", W.fam_maj_flip(n), n + 1))
    L.append(("alt chain n12", W.fam_chain(['&' if j % 2 == 0 else '|' for j in range(11)]), 12))
    for n in (10, 12, 14):
        L.append((f"LTF gauss n{n}", W.fam_ltf(rng.normal(size=n), 0.3), n))
        L.append((f"LTF power -1/2 n{n}", W.fam_ltf(np.arange(1, n + 1) ** -0.5, 0.0), n))
    for k in (0, 1, 3, 5):
        tt, n = numaro_restriction(k)
        L.append((f"numaro core+{k}aux", tt, n))
    return L


def main():
    out = open("../logs/run_cs_families.log", "w")
    rows = []
    for name, tt, n in fams():
        t0 = time.time()
        p = W.spectrum(tt)
        H = W.H_of(p); I = W.I_of(p, n)
        cs, tree = csdp.cs_opt(p, n)
        hit, _ = W.tree_markov_H(p, n)
        r = {"name": name, "n": n, "H": H, "I": I, "H/I": H / I, "CSopt": cs, "CSopt/I": cs / I,
             "(CSopt-H)/I": (cs - H) / I, "CSopt-H": cs - H, "HITopt/I": hit / I, "tree": str(tree), "secs": time.time() - t0}
        rows.append(r)
        s = (f"{name:34s} n={n:2d} H/I={H/I:.4f} CSopt/I={cs/I:.4f} (CSopt-H)/I={(cs-H)/I:.4f} CSopt-H={cs-H:.4f}b "
             f"HITopt/I={hit/I:.4f} [{r['secs']:.1f}s]")
        print(s, flush=True); print(s, file=out, flush=True)
        if "numaro" in name or "mux" in name or "addr2" in name:
            print("    tree:", tree, file=out, flush=True)
    json.dump(rows, open("../logs/run_cs_families.json", "w"), indent=1)


if __name__ == "__main__":
    main()
