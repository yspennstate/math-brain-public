"""Value iteration over a rich gate set by column generation.

Round 0: the AND/OR/NOT/XOR iteration (plus any initial families) to convergence at C.
Round t: the policy check (policy.check_gate, multi-start) of every gate of the set against the current V; every end
point with D < -thr becomes a family (the gate, its biased inputs, the most output-sensitive biased input as solver,
the other biased inputs at the end point and at scaled/perturbed copies of it, all output nodes); iterate again,
warm-started from the current V (an upper bound of the new fixed point).  Stop when no gate finds D < -thr or when
V(1/2) < C or min V < 0 (the constant C is beaten by the gate set).

usage: colgen.py C SET tag [rounds] [thr] [init]
  SET  as in run_policy.py;  init: 'g10' adds F1's ten families of g with one or two biased inputs
"""
import os, sys, json, time, math
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import vicore as V
import policy as PO
import run_policy as RP

TEAM = os.path.join(HERE, "..", "..")


def families_from(name, tab, k, P, grid, D=None, maxfree=10, window=0.1, maxpts=4):
    """families built from end points P (rows) of the policy search for one gate (the maxpts most negative distinct
    ones); output nodes within `window` of the end point's p_out (and of its mirror)"""
    fams = []
    buf = np.empty(1 << k)
    if D is not None:
        order = np.argsort(D)
        P = P[order]
    keep = []
    for p in P:
        if len(keep) >= maxpts:
            break
        if all(np.max(np.abs(p - q)) > 1e-3 for q in keep):
            keep.append(p)
    for row, p in enumerate(keep):
        po = 0.5 * (1.0 - V.gmean(tab, k, p, buf))
        r_index = np.flatnonzero((np.abs(grid.rs - po) < window) | (np.abs(grid.rs - (1.0 - po)) < window))
        dev = np.abs(p - 0.5)
        Kidx = [i for i in range(k) if dev[i] > 1e-7]
        # sensitivity of the output mean to each input: E(p_i = 1) - E(p_i = 0)
        sens = np.zeros(k)
        for i in range(k):
            q = p.copy(); q[i] = 0.0; e0 = V.gmean(tab, k, q, buf)
            q[i] = 1.0; e1 = V.gmean(tab, k, q, buf)
            sens[i] = abs(e1 - e0)
        if not Kidx:
            Kidx = [int(np.argmax(sens))]
        Kidx = sorted(Kidx, key=lambda i: -sens[i])[:maxfree + 1]
        js = 0                                  # the most sensitive biased input solves
        m = len(Kidx)
        base = p[Kidx]
        cfgs = [base.copy()]
        for lam in (0.5, 0.75, 0.9, 1.1, 1.25, 1.5):
            c = 0.5 + lam * (base - 0.5)
            if np.all((c > 1e-9) & (c < 1 - 1e-9)):
                cfgs.append(c)
        u = PO.U_of(base)
        for q in range(1, m):
            for du in (-0.25, 0.25, -0.05, 0.05):
                uu = u.copy(); uu[q] += du
                cfgs.append(PO.P_of(uu))
        FP = np.array(cfgs)
        fam = V.Family("%s#%d" % (name, row), tab, Kidx, js, None, grid, FP=FP, r_index=r_index)
        fams.append(fam)
    return fams


def run(C, gates, grid, tag, rounds=6, thr=1e-6, init_fams=(), nstart=16, log=print, G0=None, iters=2500):
    fams = list(init_fams)
    t0 = time.time()
    res = V.iterate(grid, C, families=fams, G0=G0, verbose=False, iters=iters)
    log("[%s] round 0: %s after %d sweeps, V(1/2)-C %+.3e, min V %.3e (%.0f s)" % (tag, res["reason"], res["it"],
        res["G"][0] * 0.5 - C, float((res["G"] * grid.ps).min()), time.time() - t0))
    hist = []
    for rd in range(1, rounds + 1):
        if res["reason"] != "converged":
            break
        G = res["G"]
        newf = []
        worst = []
        for name, tab in gates:
            k = int(round(np.log2(len(tab))))
            r = PO.check_gate(tab, k, grid, G, nstart=nstart)
            bad = r["D_all"] < -thr
            worst.append((r["D"], name, r["pout"]))
            if bad.any():
                newf.extend(families_from(name, tab, k, r["P_all"][bad], grid, D=r["D_all"][bad]))
        worst.sort()
        log("[%s] round %d: %d new families from %d gates; worst D: %s (%.0f s)" % (tag, rd, len(newf), len(gates),
            "; ".join("%s %.3e @%.5f" % (b, a, c) for a, b, c in worst[:4]), time.time() - t0))
        hist.append(dict(round=rd, nfam=len(newf), worst=[(float(a), b, float(c)) for a, b, c in worst[:10]]))
        if not newf:
            break
        fams.extend(newf)
        res = V.iterate(grid, C, families=fams, G0=res["G"], verbose=False, iters=iters)
        Gm = res["G"]
        log("[%s]   iterate: %s after %d sweeps, V(1/2)-C %+.3e, min V %.3e, max drop vs previous %.3e (%.0f s)" % (
            tag, res["reason"], res["it"], Gm[0] * 0.5 - C, float((Gm * grid.ps).min()),
            float(np.max((G - Gm) * grid.ps)), time.time() - t0))
    return res, fams, hist


if __name__ == "__main__":
    V.lowprio(4)
    C = float(sys.argv[1])
    spec = sys.argv[2]
    tag = sys.argv[3]
    rounds = int(sys.argv[4]) if len(sys.argv) > 4 else 6
    thr = float(sys.argv[5]) if len(sys.argv) > 5 else 1e-6
    init = sys.argv[6] if len(sys.argv) > 6 else ""
    grid = V.Grid()
    gates = RP.gate_list(spec)
    res, fams, hist = run(C, gates, grid, tag, rounds=rounds, thr=thr)
    out = os.path.join(HERE, "..", "logs", "colgen_%s.npz" % tag)
    np.savez(out, xs=grid.xs, G=res["G"], C=C, M=grid.M, K=grid.K)
    print("C = %.15f  set %s: %s  (families %d)" % (C, spec, res["reason"], len(fams)))
    for p in (0.5, 0.4995, 0.499, 0.495, 0.49, 0.485, 0.48, 0.45, 0.4, 0.25):
        print("  V(%.4f) - C = %+.6e" % (p, float(grid.V(res["G"], p)[0]) - C))
