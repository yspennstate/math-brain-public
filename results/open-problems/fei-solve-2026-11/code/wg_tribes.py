"""General weights g(Inf) = log2(1/Inf)^-b: sum g(Inf_i) E_i <= C sum g(Inf_i) Inf_i on f_k with
Ben-Or-Linial tribes (width w, s = round(2^w ln 2) terms) substituted for each y_j.
Large-w limit in log space: p -> 1/2, leaf influence P_j * 2^-(w-1) * (1-2^-w)^(s-1) -> P_j * 2^-w,
leaf count w*s -> w 2^w ln2, so the leaves' weighted total is sum_j w ln2 P_j g(P_j 2^-w).
Tribes no-go needs w g(2^-w) -> 0, i.e. b > 1; b = 1 is Talagrand's weight."""
import math, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wa_tribes import biased_E_inf_x


def g(log2_inv_t, b):
    return log2_inv_t ** (-b)


for k in (5, 9):
    B = biased_E_inf_x(k, 0.5)
    Ex, Ix = B[0]
    for lw in (8, 12, 16, 20, 30, 40):
        w = 2.0 ** lw
        out = [f"k={k} w=2^{lw} r_x={Ex/Ix:.4f}"]
        for b in (0.5, 1.0, 1.5, 2.0):
            gx = g(-math.log2(Ix), b)
            leaves = sum(w * math.log(2) * B[1 + j][1] * g(w - math.log2(B[1 + j][1]), b) for j in range(k))
            out.append(f"b={b}:{gx*Ex/(gx*Ix+leaves):.4f}")
        print("  ".join(out))
        sys.stdout.flush()
