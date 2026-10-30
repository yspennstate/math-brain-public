"""T228 T3 step 1 numbers (agent H): h(p)=E xi^p on (0,alpha), the root alpha, and the
small-ball law of xi used for E log- xi < oo. xi^2 = (1-cX)^2 + c^2 X Y, X~chi2_b, Y~chi2_{d-1}."""
import numpy as np
rng = np.random.default_rng(20261022)
N = 4_000_000
for d, b, eta in [(3, 2, 0.9), (5, 4, 1.0), (2, 1, 0.8)]:
    c = eta / b
    X = rng.chisquare(b, N); Y = rng.chisquare(d - 1, N)
    xi = np.sqrt((1 - c * X) ** 2 + c * c * X * Y)
    lx = np.log(xi)
    gam = lx.mean()
    h = lambda p: np.exp(np.log(np.mean(np.exp(p * lx))))
    ps = np.linspace(0.05, 3.0, 60)
    hs = np.array([np.mean(np.exp(p * lx)) for p in ps])
    lo, hi = 1e-3, 3.0
    for _ in range(50):
        mid = (lo + hi) / 2
        (lo, hi) = (mid, hi) if np.mean(np.exp(mid * lx)) < 1 else (lo, mid)
    alpha = (lo + hi) / 2
    below = ps[ps < alpha - 0.02]
    ok = np.all(hs[ps < alpha - 0.02] < 1)
    t = np.array([1e-2, 3e-3, 1e-3])
    small = [np.mean(xi < s) for s in t]
    print(f"d={d} b={b} eta={eta}: gamma=E log xi={gam:.4f}  alpha={alpha:.4f}  h(p)<1 on (0,alpha): {ok}  "
          f"E xi^2={np.mean(xi**2):.4f} (formula {1-2*eta+eta**2*(b+d+1)/b:.4f})  P(xi<t)/t^d at t=1e-2,3e-3,1e-3: "
          + ", ".join(f"{s/tt**d:.3g}" for s, tt in zip(small, t)))
