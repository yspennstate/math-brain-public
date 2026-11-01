"""The margin a candidate potential needs: c_min = max over (p,q) of -Phi/((1-p)(1-q)).

scan_cmin.py misses the dip at (2^-4, 2/3) that the c = 0.003 run failed on, because q = 2/3 lies on no line
q = 2^-k.  This sweeps the shapes that dip: every grid node against a dense q, the Hod ladder q_{j+1} = 1/(1+q_j)
against a dense p, a subsampled node x node lattice, random pairs, and a local refinement from the worst of each.
usage: cmin3.py <npz> [dense] [nodestep]"""
import numpy as np, math, sys, time, json
import fei_cert_vi as V, gam

def make_need(npz):
    Gm = gam.Gam(npz, 0.0)
    def need(p, q):
        E = V.E_fun(p, q, np.log2(1 / p), np.log2(1 / q))
        return -(Gm(p) / p + Gm(q) / q - Gm(p * q) / (p * q) - E) / ((1 - p) * (1 - q))
    return need, Gm

def sweep(need, P, Q, chunk=1_500_000):
    best = (-1e9, 0.0, 0.0)
    for i in range(0, len(P), chunk):
        p = np.clip(P[i:i + chunk], 1e-300, 1 - 1e-16); q = np.clip(Q[i:i + chunk], 1e-300, 1 - 1e-16)
        r = need(p, q)
        r = np.where(np.isfinite(r), r, -1e9)
        j = int(np.argmax(r))
        if r[j] > best[0]:
            best = (float(r[j]), float(p[j]), float(q[j]))
    return best

def refine(need, p0, q0, rounds=80):
    p, q = p0, q0
    cur = float(need(np.array([p]), np.array([q]))[0]); step = 0.25
    while step > 1e-10 and rounds > 0:
        rounds -= 1; moved = False
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
    npz = sys.argv[1]; dense = int(sys.argv[2]) if len(sys.argv) > 2 else 40000
    nstep = int(sys.argv[3]) if len(sys.argv) > 3 else 8
    need, Gm = make_need(npz)
    d = np.load(npz); xs = np.asarray(d["xs"], float)
    nodes = 2.0 ** -xs
    both = np.unique(np.concatenate([nodes, 1 - nodes])); both = both[(both > 0) & (both < 1)]
    sub = both[::nstep]
    qd = np.unique(np.concatenate([np.linspace(1e-7, 1 - 1e-7, dense),
                                   2.0 ** -np.linspace(1.0, 40.0, dense), 1 - 2.0 ** -np.linspace(1.0, 40.0, dense)]))
    lad = [0.5]
    for _ in range(45): lad.append(1.0 / (1.0 + lad[-1]))
    lad = np.unique(np.concatenate([np.array(lad), 1 - np.array(lad)])); lad = lad[(lad > 0) & (lad < 1)]
    res = []; t0 = time.time()
    def fam(name, P, Q):
        b = sweep(need, P, Q); res.append((name, b))
        print("  %-18s need = %+.6e at p=%.12g q=%.12g   (%.0f s)" % ((name,) + b + (time.time() - t0,)), flush=True)
    b = (-1e9, 0, 0)
    for i in range(0, len(both), 16):
        a = both[i:i + 16]
        x = sweep(need, np.repeat(a, len(qd)), np.tile(qd, len(a)))
        if x[0] > b[0]: b = x
    res.append(("node x dense", b)); print("  %-18s need = %+.6e at p=%.12g q=%.12g   (%.0f s)" % (("node x dense",) + b + (time.time() - t0,)), flush=True)
    fam("ladder x dense", np.repeat(lad, len(qd)), np.tile(qd, len(lad)))
    fam("subnode x subnode", np.repeat(sub, len(sub)), np.tile(sub, len(sub)))
    rng = np.random.default_rng(5)
    b = (-1e9, 0, 0)
    for _ in range(4):
        N = 3_000_000
        x = rng.uniform(1, 41, N); y = rng.uniform(1, 41, N)
        p = 2.0 ** -x; q = 2.0 ** -y; s = rng.integers(0, 4, N)
        x2 = sweep(need, np.where(s & 1, 1 - p, p), np.where(s & 2, 1 - q, q))
        if x2[0] > b[0]: b = x2
    res.append(("random 12M", b)); print("  %-18s need = %+.6e at p=%.12g q=%.12g   (%.0f s)" % (("random 12M",) + b + (time.time() - t0,)), flush=True)
    ref = sorted((refine(need, p, q) + (nm,) for nm, (v, p, q) in res), reverse=True)
    print("  refined worst      need = %+.6e at p=%.12g q=%.12g   (from %s)" % ref[0], flush=True)
    cmin = max(max(r[1][0] for r in res), ref[0][0])
    print("C_MIN %s : c >= %.6e  ->  certified constant C0 + c/4 >= %.7f   (C0 = %.7f)  (%.0f s)"
          % (npz, cmin, Gm.cap + cmin / 4, Gm.cap, time.time() - t0))
    json.dump({"npz": npz, "cmin": cmin, "families": [[n, list(b)] for n, b in res],
               "refined": [list(r) for r in ref]}, open("cmin3_%s.json" % npz.replace(".npz", ""), "w"))
