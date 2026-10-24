# Use identity (A) to compute the L2 sum efficiently and see how it is distributed.
#   sum_{k>=1} |hat_mu(k)|^2 = sum_{gcd(m,6)=1} sum_{s>=0} (s+1) |hat_mu(2^s m)|^2
# Compare the two sides on a truncation and see which (m, s) carry the mass.
import numpy as np, math
def hat_mu(xi, terms=4000):
    xi = np.asarray(xi, dtype=np.float64); out = np.ones(xi.shape, dtype=np.complex128); a = xi/3.0
    for _ in range(terms):
        out *= (1 + np.exp(-2j*np.pi*a))/2; a *= 2.0/3.0
        if np.max(np.abs(a)) < 1e-16: break
    return out
X = 1 << 20
tot_direct = 0.0; step = 1 << 15
for lo in range(1, X, step):
    kk = np.arange(lo, min(lo+step, X), dtype=np.float64)
    tot_direct += float(np.sum(np.abs(hat_mu(kk))**2))
print(f"direct  sum_{{1<=k<{X}}} |hat_mu(k)|^2 = {tot_direct:.6f}")
# lattice side, restricted to the same range: for each m coprime to 6, s with 2^s m < X, weight = #{(a,b): a+b=s, 2^a 3^b m < X}
tot_lat = 0.0; contrib = {}
ms = [m for m in range(1, X) if math.gcd(m, 6) == 1]
mv = np.array(ms, dtype=np.float64)
for s in range(0, 21):
    val = np.abs(hat_mu((2.0**s)*mv))**2
    w = np.zeros(len(ms))
    for i, m in enumerate(ms):
        c = 0
        for a in range(s+1):
            b = s - a
            if (2**a)*(3**b)*m < X: c += 1
        w[i] = c
    part = float(np.sum(w*val)); tot_lat += part
    if part > 1e-6: contrib[s] = part
print(f"lattice sum with exact in-range multiplicities   = {tot_lat:.6f}")
print("mass by s (only s with > 1e-6):", {k: round(v, 6) for k, v in contrib.items()})
print(f"top: s=0 carries {contrib.get(0,0)/tot_lat*100:.1f} pct")
