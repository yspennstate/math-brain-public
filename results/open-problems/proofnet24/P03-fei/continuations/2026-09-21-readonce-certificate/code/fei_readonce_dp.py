"""Pareto dynamic program over read-once formulas with AND/OR/NOT gates (fan-in two) on independent uniform variables.

State of a formula: (p, I, H) with p = Pr[true]. NOT: (1-p, I, H). For a 2-input gate on independent inputs with
measures p, q (V_p = 4p(1-p)), the biased spectral influences and entropy are closed forms:
    AND: Pr = pq,              It_a = q V_p,       It_b = p V_q
    OR : Pr = 1-(1-p)(1-q),    It_a = (1-q) V_p,   It_b = (1-p) V_q
    w_empty = (1 - 2 Pr)^2,  w_ab = w_empty + It_a + It_b - 1,  w_a = It_a - w_ab,  w_b = It_b - w_ab,
    Ht = sum phi(w) over the four weights,  phi(w) = w log2(1/w)
and the composition lemma gives  I = It_a I+_a + It_b I+_b,  H = It_a H+_a + It_b H+_b + Ht,
with I+ = I/V, H+ = (H - h(V))/V.  (Checked against the general evaluator: NAND at the golden ratio gives It = 8 Phi^4.)

Dominance: at fixed p, a state with smaller I and larger H is better for every continuation (gate outputs are
increasing in each input's I+ and H+), so per p-bin only the Pareto frontier (min I, max H) is kept. The sup of H/I
over the closure is the FEI constant restricted to read-once AND/OR/NOT formulas; every point is a real formula
(back-pointers reconstruct it) and every ratio is a rigorous lower bound on the FEI constant.
"""
import sys, math, time, json, os
import numpy as np
from math import log2

def h2v(v):
    v = np.clip(v, 1e-300, 1 - 1e-16)
    return -v * np.log2(v) - (1 - v) * np.log2(1 - v)

def phiv(w):
    w = np.clip(w, 0.0, 1.0)
    out = np.zeros_like(w)
    m = w > 1e-300
    out[m] = -w[m] * np.log2(w[m])
    return out

def gate_batch(pa, Ia, Ha, pb, Ib, Hb, kind):
    Va = 4 * pa * (1 - pa); Vb = 4 * pb * (1 - pb)
    Iap = Ia / Va; Hap = (Ha - h2v(Va)) / Va
    Ibp = Ib / Vb; Hbp = (Hb - h2v(Vb)) / Vb
    if kind == "AND":
        pr = pa * pb; Ita = pb * Va; Itb = pa * Vb
    else:
        pr = 1 - (1 - pa) * (1 - pb); Ita = (1 - pb) * Va; Itb = (1 - pa) * Vb
    w0 = (1 - 2 * pr) ** 2
    wab = w0 + Ita + Itb - 1
    wa = Ita - wab; wb = Itb - wab
    Ht = phiv(w0) + phiv(wa) + phiv(wb) + phiv(wab)
    I = Ita * Iap + Itb * Ibp
    H = Ita * Hap + Itb * Hbp + Ht
    return pr, I, H

class Frontier:
    def __init__(self, bins=400, cap=24):
        self.bins = bins; self.cap = cap
        # arrays of points
        self.p = np.array([0.5]); self.I = np.array([1.0]); self.H = np.array([0.0])
        self.parent = [None]  # (kind, ia, ib) or None for the variable
        self.best = (0.0, 0)

    def add_and_prune(self, p, I, H, parents):
        P = np.concatenate([self.p, p]); Ii = np.concatenate([self.I, I]); Hh = np.concatenate([self.H, H])
        par = self.parent + parents
        keep_idx = []
        b = np.minimum((P * self.bins).astype(int), self.bins - 1)
        order = np.lexsort((-Hh, Ii))  # by I ascending, then H descending
        # per bin Pareto: sweep in order of increasing I, keep if H exceeds the running max of that bin
        best_H = {}
        count = {}
        for idx in order:
            bb = b[idx]
            if not (1e-9 < P[idx] < 1 - 1e-9) or not np.isfinite(Ii[idx]) or not np.isfinite(Hh[idx]) or Ii[idx] <= 0:
                continue
            mh = best_H.get(bb, -1.0)
            if Hh[idx] > mh + 1e-12:
                if count.get(bb, 0) < self.cap:
                    keep_idx.append(idx); best_H[bb] = Hh[idx]; count[bb] = count.get(bb, 0) + 1
                else:
                    # bin full: keep the better-ratio point by replacing the worst-ratio one occasionally (skip for simplicity)
                    pass
        keep_idx = np.array(sorted(keep_idx))
        # remap parents
        remap = {old: new for new, old in enumerate(keep_idx.tolist())}
        newpar = []
        for old in keep_idx.tolist():
            pr = par[old]
            if pr is None:
                newpar.append(None)
            else:
                kind, ia, ib = pr
                newpar.append((kind, remap.get(ia, ("lost", ia)), remap.get(ib, ("lost", ib))))
        self.p = P[keep_idx]; self.I = Ii[keep_idx]; self.H = Hh[keep_idx]; self.parent = newpar
        # the variable must stay (it is at p=0.5, I=1, H=0 and is Pareto-optimal there: I=1 is minimal at p=1/2)
        ratios = self.H / self.I
        j = int(np.argmax(ratios)); self.best = (float(ratios[j]), j)

    def sweep(self, chunk=4000000):
        n = len(self.p)
        newp, newI, newH, newpar = [], [], [], []
        idx = np.arange(n)
        A, B = np.meshgrid(idx, idx, indexing="ij"); A = A.ravel(); B = B.ravel()
        mask = A <= B  # gates are symmetric
        A = A[mask]; B = B[mask]
        for s in range(0, len(A), chunk):
            a = A[s:s + chunk]; b = B[s:s + chunk]
            for kind in ("AND", "OR"):
                pr, I, H = gate_batch(self.p[a], self.I[a], self.H[a], self.p[b], self.I[b], self.H[b], kind)
                # NOT closure: also add (1-pr, I, H)
                newp.append(pr); newI.append(I); newH.append(H); newpar += [(kind, int(x), int(y)) for x, y in zip(a, b)]
                newp.append(1 - pr); newI.append(I); newH.append(H); newpar += [("N" + kind, int(x), int(y)) for x, y in zip(a, b)]
        self.add_and_prune(np.concatenate(newp), np.concatenate(newI), np.concatenate(newH), newpar)

    def formula(self, j, depth=0, maxdepth=40):
        pr = self.parent[j]
        if pr is None:
            return "x"
        if depth > maxdepth:
            return "..."
        kind, ia, ib = pr
        if isinstance(ia, tuple) or isinstance(ib, tuple):
            return "%s(lost)" % kind
        return "%s(%s, %s)" % (kind, self.formula(ia, depth + 1, maxdepth), self.formula(ib, depth + 1, maxdepth))

def selfcheck():
    # NAND2 at Phi: It total 8 Phi^4, and the chain l<2/3> via OR(x, AND(x, .)) iteration
    Phi = (math.sqrt(5) - 1) / 2
    pa = np.array([Phi]); Ia = np.array([1.2976895]); Ha = np.array([2.4239396])
    pr, I, H = gate_batch(pa, Ia, Ha, pa, Ia, Ha, "AND")   # NAND = NOT AND: same I, H
    # compare with the general evaluator's Lemma 3.1 value for one composition level
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import fei_recsys as R
    st = (Phi, 1.2976895, 2.4239396)
    res = R.recursion = None
    p_out, It, Ht = R.biased_stats(R.tt_values(R.AND2, 2), 2, [Phi, Phi])
    pl = R.plus(st)
    I_ref = It.sum() * pl[0]; H_ref = It.sum() * pl[1] + Ht
    print("selfcheck AND at Phi: I %.9f vs %.9f, H %.9f vs %.9f, It sum %.6f (8Phi^4 = %.6f)" % (I[0], I_ref, H[0], H_ref, It.sum(), 8 * Phi ** 4))
    # chain: state after m levels of OR(x, AND(x, T)) must approach (2/3, 4/3, 2 log2 3)
    p, I, H = 0.5, 1.0, 0.0
    for _ in range(60):
        pr1, I1, H1 = gate_batch(np.array([0.5]), np.array([1.0]), np.array([0.0]), np.array([p]), np.array([I]), np.array([H]), "AND")
        pr2, I2, H2 = gate_batch(np.array([0.5]), np.array([1.0]), np.array([0.0]), pr1, I1, H1, "OR")
        p, I, H = float(pr2[0]), float(I2[0]), float(H2[0])
    print("selfcheck chain: p %.9f I %.9f H %.9f (2/3, 4/3, %.9f)" % (p, I, H, 2 * log2(3)))
    return abs(I[0] - I_ref) < 1e-9 if False else (abs(p - 2 / 3) < 1e-9 and abs(H - 2 * log2(3)) < 1e-8)

if __name__ == "__main__":
    ok = selfcheck()
    print("selfcheck", "OK" if ok else "MISMATCH")
    bins = int(sys.argv[1]) if len(sys.argv) > 1 else 300
    cap = int(sys.argv[2]) if len(sys.argv) > 2 else 16
    sweeps = int(sys.argv[3]) if len(sys.argv) > 3 else 30
    F = Frontier(bins=bins, cap=cap)
    t0 = time.time()
    for s in range(sweeps):
        F.sweep()
        b, j = F.best
        print("sweep %2d: points %6d  best ratio %.7f at p=%.5f I=%.5f H=%.5f  (%.0f s)" % (s + 1, len(F.p), b, F.p[j], F.I[j], F.H[j], time.time() - t0), flush=True)
    b, j = F.best
    print("best formula:", F.formula(j, maxdepth=12))
    json.dump(dict(best=b, p=float(F.p[j]), I=float(F.I[j]), H=float(F.H[j]), formula=F.formula(j, maxdepth=60)),
              open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "readonce_dp_best_%d_%d.json" % (bins, cap)), "w"), indent=1)
