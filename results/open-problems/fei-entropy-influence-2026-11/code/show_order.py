"""Print the optimal reveal ordering of the filtration witness (FLOW 12(d)) for named functions of filt_big.py,
with the stage profile: revealed coordinate (decoded), A_k, B_k, Phi(A_k, B_k), the running products
A_{>=k} B_{<=k} / Inf^2, and the two conditional quantities of 12(e):
    resid_g = E Var(g | F_{k}) / Inf   (how much of g is still undetermined after stage k, in units of Inf),
    know_h  = E (E[h | F_k])^2 / Inf^2 (how much is known about pivotality; 1 = nothing, 1/Inf = everything).

usage: python show_order.py NAME[,NAME...]     (coordinate 0)
"""
import sys
import itertools
import numpy as np
from local_cs import wht, phi
from filt_cs import zeta, best_order
from filt_big import catalogue


def decode(name, n):
    if name.startswith("K") and name[1].isdigit() and "_" in name and not name.startswith("K_"):
        v = int(name[1])
        edges = list(itertools.combinations(range(v), 2))
        if len(edges) == n:
            return ["%d%d" % e for e in edges]
    for pre in ("PM_K", "NOISO_K", "C4_K"):
        if name.startswith(pre):
            l, r = int(name[len(pre)]), int(name[len(pre) + 1])
            return ["%d%s" % (a, "abcdefgh"[b]) for a in range(l) for b in range(r)]
    return [str(j) for j in range(n)]


def show(name, n, make):
    f = make()
    mu = wht(f, n) ** 2
    idx = np.arange(1 << n)
    i = 0
    lo = idx[(idx >> i) & 1 == 0]
    p, q = mu[lo], mu[lo | (1 << i)]
    m = n - 1
    inf = float(q.sum())
    val, order, M = best_order(p, q, m)
    a, b = zeta(p, m), zeta(q, m)
    names = decode(name, n)
    others = [names[j] for j in range(n) if j != i]
    print("%s n=%d  coordinate %s  Inf=%.5f  E/Inf=%.4f  F=%.4f  M(best order)=%.3f"
          % (name, n, names[i], inf, float(phi(p, q).sum()) / inf, val / inf, M))
    print("  k coord        A_k        B_k/Inf   Phi/Inf   resid_g/Inf  know_h   A>=k*B<=k/Inf^2")
    R = 0
    tot_a = float(a[-1])
    A0, B0 = float(a[0]), float(b[0])
    print("  0 (mean)   %.6f   %.6f   %.4f   %9.4f   %7.3f" % (A0, B0 / inf, float(phi(A0, B0)) / inf,
                                                               (tot_a - A0) / inf, B0 / inf ** 2))
    for k, j in enumerate(order, 1):
        Rn = R | (1 << j)
        Ak = float(a[Rn] - a[R])
        Bk = float(b[Rn] - b[R])
        prod = (tot_a - float(a[R])) * float(b[Rn]) / inf ** 2
        print(" %2d %-6s   %.6f   %.6f   %.4f   %9.4f   %7.3f   %.3f"
              % (k, others[j], Ak, Bk / inf, float(phi(Ak, Bk)) / inf, (tot_a - float(a[Rn])) / inf,
                 float(b[Rn]) / inf ** 2, prod))
        R = Rn
    print()


def main():
    cat, _ = catalogue()
    for name in sys.argv[1].split(","):
        n, make, _ = cat[name]
        show(name, n, make)


if __name__ == "__main__":
    main()
