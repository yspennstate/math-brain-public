"""floating-point estimate of the margin c a candidate needs: min over (p,q) of Phi/((1-p)(1-q)) for c = 0, on random
points plus dense scans of the tight lines (q = 2^-k, the near-1/2 strips on both sides).  usage: scan_cmin.py <npz>"""
import numpy as np, math, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import fei_cert_vi as V
src = sys.argv[1]
d = np.load(src); xs, G = d["xs"], d["G"]; K = float(xs[-1]); bstar = 8 - 4 / math.log(2); sig_t = (G[-1] - bstar) / K
def Ghat(x):
    x = np.asarray(x, float); inside = x <= K
    return np.where(inside, np.interp(np.minimum(x, K), xs, G), G[-1] + (x - K) * sig_t)
def Gam(z):
    z = np.asarray(z, float); s = np.minimum(z, 1 - z); return s * Ghat(np.log2(1 / s))
def R(p, q):
    E = V.E_fun(p, q, np.log2(1 / p), np.log2(1 / q))
    return (Gam(p) / p + Gam(q) / q - Gam(p * q) / (p * q) - E) / ((1 - p) * (1 - q))
rng = np.random.default_rng(11); worst = []
for trial in range(8):
    N = 2_000_000; x = rng.uniform(1, K + 1, N); y = rng.uniform(1, K + 1, N); p = 2.0 ** -x; q = 2.0 ** -y
    side = rng.integers(0, 4, N); p = np.where(side & 1, 1 - p, p); q = np.where(side & 2, 1 - q, q)
    r = R(p, q); j = np.argsort(r)[:3]; worst += [(float(r[i]), float(p[i]), float(q[i])) for i in j]
worst.sort(); print("random (16M points): worst Phi/((1-p)(1-q)) = %+.4e at p=%.6g q=%.6g" % worst[0])
res = [worst[0][0]]
xg = np.linspace(1, K + 0.5, 20001)
for k in range(1, 8):
    p = 2.0 ** -xg; q = np.full_like(p, 2.0 ** -k); r = R(p, q); res.append(r.min())
    print("  line q=2^-%d: min %+.4e at p=%.5g" % (k, r.min(), p[np.argmin(r)]))
# near-1/2 strips: p in (0.5 - 0.02, 0.5), v = 1-q in (2^-14, 2^-1) and the mirror
P = 0.5 - np.linspace(1e-7, 0.02, 3000); Vv = 2.0 ** -np.linspace(1, 14, 1500)
PP, VV = np.meshgrid(P, Vv, indexing="ij"); r = R(PP.ravel(), 1 - VV.ravel()); res.append(r.min()); print("  strip p->1/2-, q->1: min %+.4e" % r.min())
r = R(1 - VV.ravel(), PP.ravel()); res.append(r.min()); print("  strip p->1, q->1/2-: min %+.4e" % r.min())
r = R(PP.ravel(), VV.ravel()); res.append(r.min()); print("  p->1/2-, q small: min %+.4e" % r.min())
r = R(1 - PP.ravel(), VV.ravel()); res.append(r.min()); print("  p->1/2+, q small: min %+.4e" % r.min())
# the corner p, q -> 1/2
xg2 = np.linspace(1, 3, 1500); X2, Y2 = np.meshgrid(xg2, xg2); P2 = 2.0 ** -X2.ravel(); Q2 = 2.0 ** -Y2.ravel()
for a in (P2, 1 - P2):
    for b in (Q2, 1 - Q2):
        r = R(a, b); res.append(r.min())
print("estimated c_min (needed margin, before interval widths) = %.4e   -> C_cert >= C0 + %.3e" % (-min(res), -min(res) / 4))
