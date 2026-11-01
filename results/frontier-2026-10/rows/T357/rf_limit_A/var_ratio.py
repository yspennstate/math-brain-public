"""T357 sign lemma, the reduction. With Y = sigma(x + tau Z) and m = E Y, f_W = E[Y (1 - Y)] = m (1 - m) - Var Y, so
Lam'(x) = f_W/(m (1 - m)) = 1 - r(x), r(x) = Var Y/(m (1 - m)) in [0, 1]. Lam convex on x > 0 iff r decreasing there; the weaker
star condition Lam(x)/x increasing iff r(x) <= (1/x) int_0^x r. This checks r'(x) < 0 on (0, 40] directly (Var and m by
trapezoid in z on [-40, 40], step 1e-3). Y is computed as 1 - sigma = exp(-logaddexp(0, t)), which is exact in the right tail; Var
and m (1 - m) are unchanged by Y -> 1 - Y. Run 1 (var_ratio_run1.txt) used sigma itself and lost r to cancellation past x 35; run 2
is the record. Also checks the identity against a central-difference Lam' at x 0.5, 2, 5."""
import numpy as np
z = np.arange(-40, 40, 1e-3); w = np.exp(-z ** 2 / 2); w /= w.sum()
def r_of(x, tau):
    Y = np.exp(-np.logaddexp(0, x[:, None] + tau * z[None, :]))   # 1 - sigma, exact in the right tail; Var and m(1-m) are symmetric
    m = Y @ w; v = (Y * Y) @ w - m ** 2
    v2 = ((Y - m[:, None]) ** 2) @ w            # two-pass variance, to check cancellation
    return v2 / (m * (1 - m)), m, v, v2
def lam(x, tau):
    t = x[:, None] + tau * z[None, :]
    lh = np.log(np.exp(-np.logaddexp(0, -t)) @ w); l1h = np.log(np.exp(-np.logaddexp(0, t)) @ w)
    return lh - l1h
for tau in [0.02, 0.1, 0.5, 1, 2, 3, 4, 6, 8, 12]:
    x = np.linspace(0, 40, 4001)
    r = np.concatenate([r_of(x[i:i + 250], tau)[0] for i in range(0, len(x), 250)])
    dr = np.diff(r)
    xs = np.array([0.5, 2.0, 5.0]); h = 1e-4
    lp = (lam(xs + h, tau) - lam(xs - h, tau)) / (2 * h)
    rs = r_of(xs, tau)[0]
    print(f"tau {tau:5}: r(0) {r[0]:.5f} r(5) {r[500]:.3e} r(40) {r[-1]:.3e}  max diff r {dr.max():+.3e} at x {x[1 + int(np.argmax(dr))]:.2f}"
          f"  |Lam' - (1 - r)| at 0.5/2/5: {np.abs(lp - (1 - rs)).max():.1e}", flush=True)
