"""Is I(s*) an artefact of the histogram bin width? Decisive: vary the bin count.

I(s*) was read as -log(P[bin])/K. A BIN probability carries the width: P[bin] ~ e^(-K I) * Delta, so
    measured = I(s*) - log(Delta)/K,
and with 400 bins over a range ~2.7 that bias is about 0.185 at K = 26 - the size of the effect itself.
If real, halving the bin count must SHIFT the reading by log(2)/K and leave the density estimate
I_density = -log(P/Delta)/K unchanged. Same samples, three bin counts.
"""
import numpy as np, math

NS = 1_000_000
rng = np.random.default_rng(777)
print(f"{'K':>4} {'bins':>6} {'s*':>9} {'-logP/K':>10} {'-log(P/D)/K':>13} {'shift vs 200':>13}")
for K in (18, 26):
    th = 1/3 + rng.random(NS) / 3.0
    s = np.zeros(NS)
    for m in range(K + 1):
        s += np.log(np.maximum(1.0 + np.cos(2*np.pi*np.mod(th * 1.5**m, 1.0)), 1e-300))
    s /= (K + 1)
    base = None
    for nb in (200, 400, 800):
        h, e = np.histogram(s, bins=nb, range=(s.min(), s.max()))
        mid = 0.5*(e[:-1] + e[1:]); D = e[1] - e[0]
        P = h / NS
        j = int((P * np.exp((K+1) * mid)).argmax())
        raw = -math.log(max(P[j], 1e-300)) / (K+1)
        dens = -math.log(max(P[j]/D, 1e-300)) / (K+1)
        if base is None: base = raw
        print(f"{K:>4} {nb:>6} {mid[j]:>9.4f} {raw:>10.4f} {dens:>13.4f} {raw-base:>13.4f}")
    print(f"     predicted shift for 400 and 800 bins: {math.log(2)/(K+1):.4f}, {math.log(4)/(K+1):.4f}")
