"""A randomised attempt to break Hasebe and Ueda's Conjecture 3.5: mu box+ nu unimodal for symmetric
unimodal mu, nu.  By Khinchin the test family is mixtures of uniform laws on symmetric intervals, and
mixtures with widely separated scales are the hardest cases, so the scales are drawn log-uniformly.
"""
import numpy as np, sys
from free_subord import G_mix, density, modes

rng = np.random.default_rng(int(sys.argv[2]) if len(sys.argv) > 2 else 0)
trials = int(sys.argv[1]) if len(sys.argv) > 1 else 200
bad = 0
worst = None
for k in range(trials):
    out = []
    for _ in range(2):
        m = int(rng.integers(1, 5))
        a = np.sort(np.exp(rng.uniform(np.log(0.005), np.log(3.0), m)))
        w = rng.dirichlet(np.ones(m) * rng.choice([0.3, 1.0]))
        out.append((list(w), list(a)))
    (w1, a1), (w2, a2) = out
    span = (max(a1) + max(a2)) * 1.25 + 0.3
    xs = np.linspace(-span, span, 3001)
    f = density(G_mix(w1, a1), G_mix(w2, a2), xs, eps=3e-6, iters=3000)
    m = modes(xs, f, tol=1e-10)
    if m > 1:
        bad += 1
        print(f"  NOT UNIMODAL: mu weights {np.round(w1,3)} scales {np.round(a1,4)}; "
              f"nu weights {np.round(w2,3)} scales {np.round(a2,4)}; modes {m}", flush=True)
        if worst is None: worst = (w1, a1, w2, a2)
    if (k + 1) % 25 == 0:
        print(f"  {k+1} pairs tested, {bad} not unimodal", flush=True)
print(f"\n{trials} random symmetric-unimodal pairs tested; {bad} gave a non-unimodal free convolution")
