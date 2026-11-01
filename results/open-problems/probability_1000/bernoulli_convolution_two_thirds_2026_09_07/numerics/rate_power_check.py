"""Does the sampling actually SEE the mass that carries the octave integral?

The dominating-rate measurement is only meaningful if the Monte Carlo estimate of
    G_K = int_(1/3)^(2/3) prod_(m<=K) (1 + cos 2 pi theta (3/2)^m) d theta
reproduces the value known from quadrature (about 0.0149-0.0164 for K in the 20s). If the sample falls
short, it is missing exactly the rare alignments in question and the reported s* is biased low.
Direct comparison, same sampler, plus the fraction of the estimate contributed by the top 0.1 pct of
samples - if a handful of draws carry the integral, the estimate is unreliable however well it matches.
"""
import numpy as np

NS = 2_000_000
rng = np.random.default_rng(4242)
known = {12: 0.028177, 16: 0.019597, 20: 0.014885, 24: 0.016369}
print(f"{'K':>4} {'MC estimate':>13} {'quadrature':>12} {'MC/quad':>9} {'top 0.1% share':>15} {'max single draw':>16}")
for K in (12, 16, 20, 24):
    th = 1/3 + rng.random(NS) / 3.0
    lg = np.zeros(NS)
    for m in range(K + 1):
        lg += np.log(np.maximum(1.0 + np.cos(2*np.pi*np.mod(th * 1.5**m, 1.0)), 1e-300))
    w = np.exp(lg)
    est = w.mean() / 3.0                      # window width 1/3
    srt = np.sort(w)
    top = srt[int(NS*0.999):].sum() / srt.sum()
    mx = srt[-1] / srt.sum()
    print(f"{K:>4} {est:>13.6f} {known[K]:>12.6f} {est/known[K]:>9.3f} {top:>15.3f} {mx:>16.3e}")
print()
print("MC/quad near 1 means the sampler sees the carrying mass; well below 1 means it does not,")
print("and a top-0.1% share near 1 means the estimate rests on a few draws and should not be trusted.")
