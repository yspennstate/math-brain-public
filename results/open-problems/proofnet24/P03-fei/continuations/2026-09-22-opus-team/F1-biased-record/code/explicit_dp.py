"""Interpolation-free dynamic programme over explicit functions near truth probability 1/2.

Every pool member is an actual composition of g, AND, OR, NOT on fresh variables with exact (p, I, H) from the
composition identity (explicit.py); the pool keeps, per bin of t = p - 1/2, the member of least slack s = C I - H.
Moves per round: A (all core inputs <- F), B (core 0 <- F), Ba (aux 9 <- F), AND(F, K_m) and OR(F, L_m) with
K_m = OR of m fresh variables (Pr = 1 - 2^-m), L_m = AND of m fresh variables (Pr = 2^-m).  After every round the
exactly balanced P(F) = g(aux 9 <- F, aux 10 <- NOT F) is evaluated for every member; s(P(F)) < C would be a genuine
witness H > C (I - 1).  Usage: python explicit_dp.py C rounds tmax binw
"""
import sys, time, math
import numpy as np
try:
    import psutil
    _p = psutil.Process(); _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); _p.cpu_affinity([2, 3, 14, 15])
except Exception:
    pass
from explicit import gate_g, AND, OR, NOT, VAR, P, CREC
from compressed import Compressed

C = float(sys.argv[1]); rounds = int(sys.argv[2]); tmax = float(sys.argv[3]); binw = float(sys.argv[4])
cB = Compressed([0]); cBa = Compressed([9])


def h2v(V):
    V = np.clip(V, 1e-300, 1.0)
    out = np.zeros_like(V); m = V < 1
    out[m] = -V[m] * np.log2(V[m]) - (1 - V[m]) * np.log2(1 - V[m])
    return out


def single(cm, F):
    """g with one biased input (compressed class set cm) fed by the pool members F (arrays p, I, H)."""
    p, I, H = F
    e = cm.evaluate(p[:, None])
    V = 4 * p * (1 - p)
    w = e["It"][:, 0] / V
    return e["pout"], w * I + e["Irest"], e["Ht"] + w * (H - h2v(V))


pool = {}   # bin -> (s, p, I, H, recipe)


def offer(p, I, H, rec):
    t = p - 0.5
    if abs(t) > tmax:
        return False
    b = int(math.floor(t / binw))
    s = C * I - H
    cur = pool.get(b)
    if cur is None or s < cur[0] - 1e-15:
        pool[b] = (s, p, I, H, rec)
        return True
    return False


# seeds: read-once formulas of small size, then B and Ba of them
ro = {"x": VAR}
names = list(ro)
for _ in range(3):
    items = list(ro.items())
    for n1, f1 in items:
        for n2, f2 in items:
            for op, fn in (("AND", AND), ("OR", OR)):
                f = fn(f1, f2); nm = "%s(%s,%s)" % (op, n1, n2)
                key = round(f[0], 12)
                if len(nm) < 60:
                    ro[nm] = f
    # keep one representative per measure (least slack)
    best = {}
    for nm, f in ro.items():
        k = round(f[0], 12)
        if k not in best or C * f[1] - f[2] < C * best[k][1][1] - best[k][1][2]:
            best[k] = (nm, f)
    ro = {nm: f for nm, f in best.values()}
print("read-once seeds: %d distinct measures" % len(ro), flush=True)
arr = np.array([f for f in ro.values()]); recs = list(ro.keys())
for cm, lab in ((cB, "B"), (cBa, "Ba")):
    po, I, H = single(cm, (arr[:, 0], arr[:, 1], arr[:, 2]))
    for k in range(len(po)):
        offer(po[k], I[k], H[k], "%s[%s]" % (lab, recs[k]))
offer(0.5, 1.0, 0.0, "x")
Km = [(m, OR_m) for m, OR_m in []]
shiftK = []
f = VAR
for m in range(2, 16):
    f = OR(f, VAR) if m > 1 else f
    shiftK.append(("ORv%d" % m, f))                 # Pr = 1 - 2^-m
shiftL = [("ANDv%d" % m, NOT(g)) for m, (nm, g) in zip(range(2, 16), shiftK)]
t0 = time.time()
for rnd in range(rounds):
    items = list(pool.values())
    F = (np.array([it[1] for it in items]), np.array([it[2] for it in items]), np.array([it[3] for it in items]))
    new = 0
    for cm, lab in ((cB, "B"), (cBa, "Ba")):
        po, I, H = single(cm, F)
        for k in range(len(po)):
            new += offer(po[k], I[k], H[k], "%s[%d]" % (lab, rnd))
    for it in items:
        if abs(it[1] - 0.5) <= tmax / 2.2:
            q = gate_g([(it[1], it[2], it[3])] * 9 + [VAR] * 9)
            new += offer(q[0], q[1], q[2], "A[%d]" % rnd)
        for nm, K in shiftK[:6]:
            q = AND((it[1], it[2], it[3]), K); new += offer(q[0], q[1], q[2], "AND-%s[%d]" % (nm, rnd))
            q = OR((it[1], it[2], it[3]), NOT(K)); new += offer(q[0], q[1], q[2], "OR-%s[%d]" % (nm, rnd))
    # exactly balanced candidates
    bestP = None
    for it in pool.values():
        q = P((it[1], it[2], it[3]))
        sP = C * q[1] - q[2]
        if bestP is None or sP < bestP[0]:
            bestP = (sP, it[1], q[1], q[2])
    sC = sorted(pool.items())
    near = [(b, v[0] - C) for b, v in sC if abs(b * binw) < 0.003]
    print("round %2d: pool %d, new %d, best balanced P(F): s-C = %+.4e (F at p=%.6f, H/(I-1) - C = %+.3e); min over |t|<0.003 of s-C = %+.4e  (%.0f s)" % (
        rnd, len(pool), new, bestP[0] - C, bestP[1], bestP[3] / (bestP[2] - 1) - C, min(x[1] for x in near) if near else float('nan'), time.time() - t0), flush=True)
    if new == 0:
        break
