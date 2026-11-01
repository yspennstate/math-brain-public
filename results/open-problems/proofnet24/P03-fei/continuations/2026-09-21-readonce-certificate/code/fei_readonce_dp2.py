"""Pareto dynamic program over read-once AND/OR/NOT formulas, version 2 (see fei_readonce_dp.py for the formulas).
Changes: vectorized per-bin Pareto pruning with even thinning along the frontier, edge bins (p outside [pmin, 1-pmin])
excluded from the frontier, persistent node table for exact reconstruction, exact re-evaluation of the best formula.
usage: python -u fei_readonce_dp2.py <bins> <cap> <sweeps> <pmin> <tag>
"""
import sys, math, time, json, os
import numpy as np
from math import log2
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fei_readonce_dp import gate_batch, h2v
try:
    import psutil
    psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass

class DP:
    def __init__(self, bins, cap, pmin):
        self.bins, self.cap, self.pmin = bins, cap, pmin
        self.nodes = [None]              # node 0 = variable
        self.p = np.array([0.5]); self.I = np.array([1.0]); self.H = np.array([0.0]); self.nid = np.array([0])
        self.best = (0.0, 0)

    def prune(self, P, I, H, A, B, kinds):
        """P,I,H arrays of candidates; A,B parent node ids; kinds int codes. Returns kept arrays + new node ids."""
        good = (P > self.pmin) & (P < 1 - self.pmin) & np.isfinite(I) & np.isfinite(H) & (I > 1e-12) & (H >= -1e-9)
        P, I, H, A, B, kinds = P[good], I[good], H[good], A[good], B[good], kinds[good]
        b = np.minimum((P * self.bins).astype(np.int64), self.bins - 1)
        order = np.lexsort((-H, I, b))          # by bin, then I ascending, then H descending
        P, I, H, A, B, kinds, b = P[order], I[order], H[order], A[order], B[order], kinds[order], b[order]
        # per-bin running max of H (segmented cummax): offsets grow with bin and dominate H (H < 200 here)
        off = b.astype(float) * 1000.0
        cm = np.maximum.accumulate(H + off) - off
        # a point is on the frontier if its H strictly exceeds the running max BEFORE it
        prev = np.concatenate([[-np.inf], cm[:-1]])
        newbin = np.concatenate([[True], b[1:] != b[:-1]])
        keep = (H > prev + 1e-12) | newbin
        P, I, H, A, B, kinds, b = P[keep], I[keep], H[keep], A[keep], B[keep], kinds[keep], b[keep]
        # thin each bin evenly to at most cap points
        if len(P):
            starts = np.concatenate([[0], np.flatnonzero(b[1:] != b[:-1]) + 1, [len(P)]])
            sel = []
            for s, e in zip(starts[:-1], starts[1:]):
                n = e - s
                if n <= self.cap:
                    sel.extend(range(s, e))
                else:
                    sel.extend((s + np.round(np.linspace(0, n - 1, self.cap))).astype(int).tolist())
            sel = np.array(sel)
            P, I, H, A, B, kinds = P[sel], I[sel], H[sel], A[sel], B[sel], kinds[sel]
        return P, I, H, A, B, kinds

    def sweep(self, chunk=3000000):
        n = len(self.p)
        idx = np.arange(n)
        A, B = np.triu_indices(n)
        cand = []
        for s in range(0, len(A), chunk):
            a = A[s:s + chunk]; bb = B[s:s + chunk]
            for code, kind in ((0, "AND"), (1, "OR")):
                pr, I, H = gate_batch(self.p[a], self.I[a], self.H[a], self.p[bb], self.I[bb], self.H[bb], kind)
                cand.append((pr, I, H, self.nid[a], self.nid[bb], np.full(len(a), code)))
                cand.append((1 - pr, I, H, self.nid[a], self.nid[bb], np.full(len(a), code + 2)))   # NOT of the gate
        # include the current frontier itself (so nothing is lost between sweeps) with kinds -1
        cand.append((self.p, self.I, self.H, self.nid, self.nid, np.full(n, -1)))
        P = np.concatenate([c[0] for c in cand]); I = np.concatenate([c[1] for c in cand]); H = np.concatenate([c[2] for c in cand])
        Aa = np.concatenate([c[3] for c in cand]); Bb = np.concatenate([c[4] for c in cand]); K = np.concatenate([c[5] for c in cand])
        P, I, H, Aa, Bb, K = self.prune(P, I, H, Aa, Bb, K)
        # assign node ids: existing points (K == -1) keep their id (stored in Aa); new points get new nodes
        nid = np.empty(len(P), dtype=np.int64)
        for i in range(len(P)):
            if K[i] == -1:
                nid[i] = Aa[i]
            else:
                self.nodes.append((int(K[i]), int(Aa[i]), int(Bb[i])))
                nid[i] = len(self.nodes) - 1
        self.p, self.I, self.H, self.nid = P, I, H, nid
        r = self.H / self.I
        j = int(np.argmax(r)); self.best = (float(r[j]), j)

    def formula(self, node, depth=0, maxdepth=14):
        if node == 0:
            return "x"
        if depth > maxdepth:
            return "…"
        code, a, b = self.nodes[node]
        name = ["AND", "OR", "NAND", "NOR"][code]
        return "%s(%s, %s)" % (name, self.formula(a, depth + 1, maxdepth), self.formula(b, depth + 1, maxdepth))

    def exact_state(self, node, memo=None):
        """re-evaluate a node's (p, I, H) exactly from the tree (no binning involved)"""
        if memo is None:
            memo = {}
        if node in memo:
            return memo[node]
        if node == 0:
            st = (0.5, 1.0, 0.0)
        else:
            code, a, b = self.nodes[node]
            pa, Ia, Ha = self.exact_state(a, memo); pb, Ib, Hb = self.exact_state(b, memo)
            pr, I, H = gate_batch(np.array([pa]), np.array([Ia]), np.array([Ha]), np.array([pb]), np.array([Ib]), np.array([Hb]), "AND" if code % 2 == 0 else "OR")
            st = (float(pr[0]) if code < 2 else 1 - float(pr[0]), float(I[0]), float(H[0]))
        memo[node] = st
        return st

    def size(self, node, memo=None):
        if memo is None:
            memo = {}
        if node in memo:
            return memo[node]
        if node == 0:
            return 1
        code, a, b = self.nodes[node]
        v = self.size(a, memo) + self.size(b, memo); memo[node] = v
        return v

if __name__ == "__main__":
    bins = int(sys.argv[1]); cap = int(sys.argv[2]); sweeps = int(sys.argv[3]); pmin = float(sys.argv[4]); tag = sys.argv[5]
    here = os.path.dirname(os.path.abspath(__file__))
    log = open(os.path.join(here, f"readonce_dp2_{tag}.log"), "a", encoding="utf-8")
    D = DP(bins, cap, pmin); t0 = time.time(); best_ever = 0.0
    for s in range(sweeps):
        if os.path.exists(os.path.join(here, f"STOP_{tag}")):
            break
        D.sweep()
        b, j = D.best
        line = "sweep %2d: points %6d  best ratio %.7f at p=%.5f I=%.5f H=%.5f  nodes %d  (%.0f s)" % (s + 1, len(D.p), b, D.p[j], D.I[j], D.H[j], len(D.nodes), time.time() - t0)
        print(line, flush=True); log.write(line + "\n"); log.flush()
        if b > best_ever + 1e-9:
            best_ever = b
            node = int(D.nid[j]); ex = D.exact_state(node)
            rec = dict(sweep=s + 1, ratio=b, exact=dict(p=ex[0], I=ex[1], H=ex[2], ratio=ex[2] / ex[1]), size=D.size(node), formula=D.formula(node, maxdepth=4))
            import pickle
            pickle.dump(dict(nodes=D.nodes, node=node, p=D.p, I=D.I, H=D.H, nid=D.nid), open(os.path.join(here, f"readonce_dp2_{tag}_state.pkl"), "wb"))
            log.write("  RECORD " + json.dumps(rec) + "\n"); log.flush()
            json.dump(rec, open(os.path.join(here, f"readonce_dp2_{tag}_best.json"), "w"), indent=1)
    print("done", flush=True)
