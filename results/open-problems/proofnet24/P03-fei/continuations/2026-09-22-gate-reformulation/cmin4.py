"""c_min for a candidate potential: the largest margin any point of the square demands.

need(p,q) = -Phi(p,q) / ((1-p)(1-q)),  Phi = G(p)+G(q)-G(pq)-E(p,q),  because adding c p(1-p) to Gamma raises
Phi by exactly c (1-p)(1-q).  A plain grid is a lottery here - the dips sit at grid nodes in one coordinate and
at awkward reals in the other (the c = 0.003 run died at (2^-4, 2/3)) - so this sweeps the shapes that dip and
then runs a multi-start local refinement from the worst hundreds of points found.
usage: cmin4.py <npz> [dense] [nodestep] [starts]"""
import numpy as np, math, sys, time, json, heapq
import fei_cert_vi as V, gam

def make_need(npz):
    Gm = gam.Gam(npz, 0.0)
    def need(p, q):
        E = V.E_fun(p, q, np.log2(1 / p), np.log2(1 / q))
        return -(Gm(p) / p + Gm(q) / q - Gm(p * q) / (p * q) - E) / ((1 - p) * (1 - q))
    return need, Gm

def topk(need, P, Q, k=40, chunk=2_000_000):
    out = []
    for i in range(0, len(P), chunk):
        p = np.clip(P[i:i + chunk], 1e-300, 1 - 1e-16); q = np.clip(Q[i:i + chunk], 1e-300, 1 - 1e-16)
        r = need(p, q); r = np.where(np.isfinite(r), r, -1e9)
        m = min(k, len(r))
        idx = np.argpartition(-r, m - 1)[:m]
        out += [(float(r[j]), float(p[j]), float(q[j])) for j in idx]
    out.sort(reverse=True)
    return out[:k]

def refine(need, p0, q0):
    p, q = p0, q0
    cur = float(need(np.array([p]), np.array([q]))[0]); step = 0.125
    while step > 1e-11:
        moved = False
        for dp, dq in ((step, 0), (-step, 0), (0, step), (0, -step), (step, step), (-step, -step), (step, -step), (-step, step)):
            pp = min(max(p * (2.0 ** -dp), 1e-300), 1 - 1e-16)
            qq = min(max(q * (2.0 ** -dq), 1e-300), 1 - 1e-16)
            v = float(need(np.array([pp]), np.array([qq]))[0])
            if np.isfinite(v) and v > cur:
                cur, p, q, moved = v, pp, qq, True
        if not moved:
            step *= 0.5
    return cur, p, q

if __name__ == "__main__":
    npz = sys.argv[1]
    dense = int(sys.argv[2]) if len(sys.argv) > 2 else 30000
    nstep = int(sys.argv[3]) if len(sys.argv) > 3 else 4
    starts = int(sys.argv[4]) if len(sys.argv) > 4 else 200
    need, Gm = make_need(npz)
    xs = np.asarray(np.load(npz)["xs"], float)
    nodes = 2.0 ** -xs
    both = np.unique(np.concatenate([nodes, 1 - nodes])); both = both[(both > 0) & (both < 1)]
    sub = both[::nstep]
    qd = np.unique(np.concatenate([np.linspace(1e-7, 1 - 1e-7, dense),
                                   2.0 ** -np.linspace(1.0, 40.0, dense), 1 - 2.0 ** -np.linspace(1.0, 40.0, dense)]))
    lad = [0.5]
    for _ in range(45): lad.append(1.0 / (1.0 + lad[-1]))
    lad = np.unique(np.concatenate([np.array(lad), 1 - np.array(lad)])); lad = lad[(lad > 0) & (lad < 1)]
    pool = []; t0 = time.time()
    def fam(name, P, Q, k=60):
        got = topk(need, P, Q, k)
        pool.extend(got)
        print("  %-18s best %+.6e at p=%.12g q=%.12g   (%.0f s)" % ((name,) + got[0] + (time.time() - t0,)), flush=True)
    for i in range(0, len(sub), 32):
        a = sub[i:i + 32]
        pool.extend(topk(need, np.repeat(a, len(qd)), np.tile(qd, len(a)), 12))
    pool.sort(reverse=True)
    print("  %-18s best %+.6e at p=%.12g q=%.12g   (%.0f s)" % (("subnode x dense",) + pool[0] + (time.time() - t0,)), flush=True)
    fam("ladder x dense", np.repeat(lad, len(qd)), np.tile(qd, len(lad)))
    fam("subnode x subnode", np.repeat(sub, len(sub)), np.tile(sub, len(sub)))
    rng = np.random.default_rng(5)
    N = 3_000_000
    for _ in range(3):
        x = rng.uniform(1, 41, N); y = rng.uniform(1, 41, N)
        p = 2.0 ** -x; q = 2.0 ** -y; s = rng.integers(0, 4, N)
        fam("random 3M", np.where(s & 1, 1 - p, p), np.where(s & 2, 1 - q, q), 30)
    pool.sort(reverse=True)
    seen = set(); best = (-1e9, 0, 0); n = 0
    for v, p, q in pool:
        key = (round(math.log2(max(p, 1e-300)), 3), round(math.log2(max(q, 1e-300)), 3))
        if key in seen:
            continue
        seen.add(key); n += 1
        r = refine(need, p, q)
        if r[0] > best[0]: best = r
        if n >= starts:
            break
    print("  refined from %d distinct starts: best %+.6e at p=%.12g q=%.12g" % ((n,) + best), flush=True)
    cmin = max(best[0], pool[0][0])
    print("C_MIN %s : c >= %.7e   ->  certified constant C0 + c/4 >= %.7f   (C0 = %.7f)  (%.0f s)"
          % (npz, cmin, Gm.cap + cmin / 4, Gm.cap, time.time() - t0))
    json.dump({"npz": npz, "cmin": cmin, "best": list(best), "pool_top": pool[:20]},
              open("cmin4_%s.json" % npz.replace(".npz", ""), "w"))
