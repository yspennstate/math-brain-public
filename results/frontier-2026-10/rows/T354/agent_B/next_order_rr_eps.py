# T354 next-order term under random reshuffling, momentum and eps > 0 (agent B, 20 Oct 2026 04:2x). Candidate.
# With s = sqrt(B2), r = s/(s + eps), p2 = s(eps + 3s)/(4(eps + s)^2) (psi''(1) for psi(y) = (s + eps)/(s sqrt(y) + eps), as in
# next_order_eps.py), K = K_rr(n, beta1, beta2), H as in next_order_rr_mom.py and x0 = r d K B3/(2 B2):
#   x*/x0 = 1 + d (r K - p2 T H/(r K B2 B3)) + O(d^2).
# Derivation: the eps remainder lemma (remainder_rr_eps.py) gives 0 = x + p1 d K C/V + (p2/2) Q + O(d^3) with p1 = -r/2 and the
# same Q = (d/B2)^2 T H as at eps = 0 (Q does not see eps; r and p2 move with V = x^2 + B2 only at O(x^2)). Under iid sampling
# the S = Var(b^2) terms come from E[(y-1)^2] = O(d) over the long lag window; under reshuffling that is O(d^2) (each earlier
# epoch sums Z to zero), so they drop out, as at eps = 0. eps = 0 gives r = 1, p2 = 3/4 and next_order_rr_mom.py.
# Exact roots: audit_A/rr_exact_mom_eps.py (erfcx Laplace kernel, no Taylor step). Argv: beta1:beta2:eps ...
import numpy as np, sys, runpy, math
from kfactor import K_rr
n = 10; b = np.array([9.0] + [-1.0] * 9); B2 = np.mean(b ** 2); B3 = np.mean(b ** 3); Z = b * b - B2; T = np.mean(b * Z * Z)
P = np.arange(n); h = 1 - 3 * P / (n - 1) + 2 * P * (P - 1) / ((n - 1) * (n - 2)); s = math.sqrt(B2)
for arg in sys.argv[1:]:
    b1, b2, eps = (float(v) for v in arg.split(":")); d = 1 - b2
    H = np.mean((1 - b1 ** (P + 1)) * h); K = K_rr(n, b1, b2); r = s / (s + eps); p2 = s * (eps + 3 * s) / (4 * (eps + s) ** 2)
    cp = r * K - p2 * T * H / (r * K * B2 * B3)
    sv = sys.argv; sys.argv = ["rr_exact_mom_eps.py", str(b1), str(b2), str(eps)]
    xs = runpy.run_path("../audit_A/rr_exact_mom_eps.py", run_name="rr")["xs"]; sys.argv = sv
    x0 = r * d * K * B3 / (2 * B2); ce = (xs / x0 - 1) / d
    print("beta1 %s beta2 %s eps %s r %.5f p2 %.5f K %.6f exact x*/x0 %.9f (x*/x0-1)/d %.5f predicted %.5f gap/d %.3f"
          % (b1, b2, eps, r, p2, K, xs / x0, ce, cp, (ce - cp) / d), flush=True)
