"""Constants b_k in  B_{k-1} <= b_k I  (route L2, per-level theorem).

For a coordinate i and level k >= 1 let d = W_{k-1}(D_i f) (level-(k-1) Fourier weight of the derivative,
equivalently sum of p(T) over |T| = k, T containing i).  Lemma 1: B^(i)_{k-1} <= d log2(e/d).
With r = d/eps_i <= rho_k(eps_i), d log2(e/d) = eps [r log2(e/r) + r log2(1/eps)], increasing in r, so
b_k = sup_eps [rho log2(e/rho) + rho log2(1/eps)] with rho = rho_k(eps).
rho_1(eps) = eps                                  (|fhat(i)| <= Inf_i)
rho_k(eps) = min(1, inf_{q>=2} eps^(1-2/q) (q-1)^(k-1))   (Bonami, k >= 2)
rho_2^H(eps) = min(1, 2 eps ln(2/eps))            (level-1 inequality for {0,+-1} derivatives, A096)
The q-infimum is taken over a grid (any q gives a valid upper bound on rho), the eps-supremum over a fine
log grid; the grid sup is a lower estimate of the true sup, so a margin is added when constants are stated.
"""
import numpy as np, math, json, sys

LOG2E = 1 / math.log(2)


def G(eps, rho):
    rho = np.minimum(rho, 1.0)
    return rho * np.log2(math.e / rho) + rho * np.log2(1 / eps)


def rho_hc(eps, k, qs):
    L = np.log(1 / eps)[:, None]
    lr = -L * (1 - 2 / qs[None, :]) + (k - 1) * np.log(qs[None, :] - 1)
    return np.minimum(1.0, np.exp(lr.min(1)))


def sup_refined(k, qs, rho_fn):
    """coarse ln-grid then two local refinements around the argmax."""
    ln = np.linspace(0, 700, 7001)
    best = None
    for width, num in ((None, None), (0.2, 4001), (0.002, 4001)):
        if width is not None:
            c = best[1]
            ln = np.linspace(max(0.0, c - width), c + width, num)
        e = np.exp(-ln)
        g = G(e, rho_fn(e))
        j = int(g.argmax())
        best = (float(g[j]), float(ln[j]))
    return best


def main():
    qs = np.concatenate([2 + np.exp(np.linspace(-12, 0, 1500)), np.linspace(3, 200, 1500)])
    out = {}
    out["b1"], _ = sup_refined(1, qs, lambda e: e)
    out["b1_exact"] = 2 / (math.sqrt(math.e) * math.log(2))
    out["b2_hoeffding"], lnH = sup_refined(2, qs, lambda e: np.minimum(1.0, 2 * e * np.log(2 / e)))
    out["b2_hoeffding_at_eps"] = math.exp(-lnH)
    rows = []
    for k in range(2, 41):
        bk, lk = sup_refined(k, qs, lambda e, k=k: rho_hc(e, k, qs))
        rows.append(dict(k=k, b_k=bk, at_ln_inv_eps=lk, analytic_bound=2 * k * LOG2E, ratio_to_k=bk / k))
    out["b_hc"] = rows
    b2 = min(out["b2_hoeffding"], rows[0]["b_k"])
    out["sum_b_upto_D"] = {str(D): out["b1_exact"] + b2 + sum(r["b_k"] for r in rows[1:D - 1]) for D in (2, 3, 5, 10, 20, 40)}
    path = sys.argv[1]
    json.dump(out, open(path, "w"), indent=1)
    print("b1 grid", round(out["b1"], 6), "exact", round(out["b1_exact"], 6))
    print("b2 Hoeffding", round(out["b2_hoeffding"], 5), "at eps", round(out["b2_hoeffding_at_eps"], 5))
    for r in rows[:6] + rows[8::10]:
        print(f"  k={r['k']:2d}  b_k={r['b_k']:.4f}  b_k/k={r['ratio_to_k']:.4f}  at ln(1/eps)={r['at_ln_inv_eps']:.3f}  analytic 2k log2e={r['analytic_bound']:.3f}")
    print("sum b_1..b_D", json.dumps({k: round(v, 3) for k, v in out["sum_b_upto_D"].items()}))


if __name__ == "__main__":
    main()
