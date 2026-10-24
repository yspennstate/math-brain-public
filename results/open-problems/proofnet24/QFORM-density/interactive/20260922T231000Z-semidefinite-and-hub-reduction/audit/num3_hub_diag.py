try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
import numpy as np
np.random.seed(3)
# Pure hub with small diagonal: Q = a X_h^2 + 2 (L + beta) X_h, X_h uniform[-1/2,1/2], L = <w,X'> (|w| = 1, spread)
N = 2_000_000
nprime = 60
w = np.ones(nprime) / np.sqrt(nprime)
L = np.zeros(N)
for j in range(nprime):
    L += w[j] * (np.random.rand(N) - 0.5)
def dens_hub(a, beta, s):
    t = L + beta
    disc = t**2 + a * s
    ok = disc > 0
    r = np.sqrt(np.where(ok, disc, 0.0))
    tot = np.zeros(N)
    for sg in (1.0, -1.0):
        x = (-t + sg * r) / a
        valid = ok & (np.abs(x) <= 0.5) & (r > 0)
        tot += np.where(valid, 1.0 / (2 * np.where(r > 0, r, 1.0)), 0.0)
    return tot.mean()
print("Pure hub a X_h^2 + 2(L+beta)X_h: density near the singular value s = 0 (exact conditional formula)", flush=True)
for a in [0.2, 0.05, 0.01]:
    for beta in [0.0, 0.1]:
        vals = [dens_hub(a, beta, sg * 10.0**-k) for k in range(1, 8) for sg in (1,)]
        vneg = [dens_hub(a, beta, -10.0**-k) for k in range(1, 8)]
        print(f"  a={a:5.2f} beta={beta:3.1f}  p(+10^-k), k=1..7: " + " ".join(f"{v:6.3f}" for v in vals), flush=True)
        print(f"  {'':17s}  p(-10^-k), k=1..7: " + " ".join(f"{v:6.3f}" for v in vneg), flush=True)
print("  (log singularity: increments per decade roughly constant; square-root singularity: ratio sqrt(10) per decade)", flush=True)
# Rank-one witness: A = (1/a)(a,w)(a,w)^T, Q = (a X_h + L)^2 / a  -> P(|Q|<=u) ~ sqrt(u)
Xh = np.random.rand(N) - 0.5
for a in [0.05]:
    Z = a * Xh + L
    Q = Z**2 / a
    print(f"Rank-one witness a={a}: P(|Q|<=u)/(u(1+log(1/u))) for u = 10^-k:", flush=True)
    print("   " + " ".join(f"{np.mean(np.abs(Q) <= 10.0**-k) / (10.0**-k * (1 + k*np.log(10))):8.2f}" for k in range(2, 7)), flush=True)
