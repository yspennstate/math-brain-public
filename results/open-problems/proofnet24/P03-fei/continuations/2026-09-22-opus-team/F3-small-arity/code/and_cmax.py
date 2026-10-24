"""max over (p,q) of the AND margin c_AND = -Phi/((1-p)(1-q)) for a stored potential (Pr = probability of true).
Same families as gate-reformulation/cmin4.py (node x dense, Hod ladder x dense, node x node, random), then multi-start
local refinement.  usage: and_cmax.py <npz> [dense] [nodestep] [starts] [tag]"""
import sys, os, math, time, json
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "2026-09-21-readonce-certificate", "code"))
import fgate as F
F.lowprio()
import fei_cert_vi as V

npz = sys.argv[1]
dense = int(sys.argv[2]) if len(sys.argv) > 2 else 10000
nstep = int(sys.argv[3]) if len(sys.argv) > 3 else 2
starts = int(sys.argv[4]) if len(sys.argv) > 4 else 150
tag = sys.argv[5] if len(sys.argv) > 5 else os.path.basename(npz).replace(".npz", "")
pot = F.Pot(npz, 0.0)

def need(p, q):
    E = V.E_fun(p, q, np.log2(1 / p), np.log2(1 / q))
    return -(pot(p) / p + pot(q) / q - pot(p * q) / (p * q) - E) / ((1 - p) * (1 - q))

def topk(P, Q, k=40, chunk=1_000_000):
    out = []
    for i in range(0, len(P), chunk):
        p = np.clip(P[i:i + chunk], 1e-300, 1 - 1e-16); q = np.clip(Q[i:i + chunk], 1e-300, 1 - 1e-16)
        r = need(p, q); r = np.where(np.isfinite(r), r, -1e9)
        m = min(k, len(r)); idx = np.argpartition(-r, m - 1)[:m]
        out += [(float(r[j]), float(p[j]), float(q[j])) for j in idx]
    out.sort(reverse=True)
    return out[:k]

def refine(p, q):
    cur = float(need(np.array([p]), np.array([q]))[0]); step = 0.125
    while step > 1e-12:
        moved = False
        for dp, dq in ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)):
            for side in (0, 1):
                pp = p * 2.0 ** (-dp * step) if side == 0 else 1 - (1 - p) * 2.0 ** (-dp * step)
                qq = q * 2.0 ** (-dq * step) if side == 0 else 1 - (1 - q) * 2.0 ** (-dq * step)
                pp = min(max(pp, 1e-300), 1 - 1e-16); qq = min(max(qq, 1e-300), 1 - 1e-16)
                v = float(need(np.array([pp]), np.array([qq]))[0])
                if np.isfinite(v) and v > cur:
                    cur, p, q, moved = v, pp, qq, True
        if not moved:
            step *= 0.5
    return cur, p, q

t0 = time.time()
xs = pot.xs
nodes = 2.0 ** -xs
both = np.unique(np.concatenate([nodes, 1 - nodes])); both = both[(both > 0) & (both < 1)]
sub = both[::nstep]
qd = np.unique(np.concatenate([np.linspace(1e-7, 1 - 1e-7, dense), 2.0 ** -np.linspace(1.0, 40.0, dense),
                               1 - 2.0 ** -np.linspace(1.0, 40.0, dense)]))
lad = [0.5]
for _ in range(45):
    lad.append(1.0 / (1.0 + lad[-1]))
lad = np.unique(np.concatenate([np.array(lad), 1 - np.array(lad)])); lad = lad[(lad > 0) & (lad < 1)]
pool = []
for i in range(0, len(sub), 16):
    a = sub[i:i + 16]
    pool.extend(topk(np.repeat(a, len(qd)), np.tile(qd, len(a)), 12))
pool.sort(reverse=True)
print("node x dense       best %+.9e at p=%.12g q=%.12g  (%.0f s)" % (pool[0] + (time.time() - t0,)), flush=True)
got = topk(np.repeat(lad, len(qd)), np.tile(qd, len(lad)), 60); pool += got
print("ladder x dense     best %+.9e at p=%.12g q=%.12g  (%.0f s)" % (got[0] + (time.time() - t0,)), flush=True)
got = topk(np.repeat(sub, len(sub)), np.tile(sub, len(sub)), 60); pool += got
print("node x node        best %+.9e at p=%.12g q=%.12g  (%.0f s)" % (got[0] + (time.time() - t0,)), flush=True)
rng = np.random.default_rng(5)
for _ in range(2):
    N = 3_000_000
    x = rng.uniform(0, 41, N); y = rng.uniform(0, 41, N)
    p = 2.0 ** -(x + 1); q = 2.0 ** -(y + 1); s = rng.integers(0, 4, N)
    got = topk(np.where(s & 1, 1 - p, p), np.where(s & 2, 1 - q, q), 30); pool += got
    print("random 3M          best %+.9e at p=%.12g q=%.12g  (%.0f s)" % (got[0] + (time.time() - t0,)), flush=True)
pool.sort(reverse=True)
seen = set(); best = (-1e9, 0, 0); n = 0
for v, p, q in pool:
    key = (round(math.log2(max(p, 1e-300)), 3), round(math.log2(max(q, 1e-300)), 3))
    if key in seen:
        continue
    seen.add(key); n += 1
    r = refine(p, q)
    if r[0] > best[0]:
        best = r
    if n >= starts:
        break
cmax = max(best[0], pool[0][0])
print("refined from %d starts: best %+.10e at p=%.15g q=%.15g" % ((n,) + best))
print("C_AND_MAX %s : %.10e  -> constant C0 + c/4 = %.8f  (%.0f s)" % (npz, cmax, pot.C0 + cmax / 4, time.time() - t0))
json.dump({"npz": npz, "cmax": cmax, "best": list(best), "pool_top": pool[:30]},
          open(os.path.join(HERE, "..", "logs", "and_cmax_%s.json" % tag), "w"), indent=1)
