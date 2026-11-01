"""Simulated annealing over recursive read-once systems (fei_recsys), maximizing the converged limit ratio.
usage: python -u fei_recanneal.py <tag> <seed> [r] [kmax] [minutes]
Moves: flip a truth-table bit, rewire a slot (fresh / prev copy of any symbol / cur copy of itself), change a
symbol's arity between 2 and 3. Non-converged or degenerate systems score -inf. Records every improvement to
recanneal_<tag>.jsonl and keeps recanneal_<tag>_TOP.txt current. Stop with STOP_<tag>. BelowNormal priority.
"""
import sys, os, json, time, math, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fei_recsys as R
try:
    import psutil
    psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass

tag = sys.argv[1]; seed = int(sys.argv[2]); r = int(sys.argv[3]) if len(sys.argv) > 3 else 2
kmax = int(sys.argv[4]) if len(sys.argv) > 4 else 3; minutes = float(sys.argv[5]) if len(sys.argv) > 5 else 600
HERE = os.path.dirname(os.path.abspath(__file__))
rng = random.Random(seed)
out = open(os.path.join(HERE, f"recanneal_{tag}.jsonl"), "a", encoding="utf-8")
topf = os.path.join(HERE, f"recanneal_{tag}_TOP.txt"); stopf = os.path.join(HERE, f"STOP_{tag}")
RECORD = 6.4547837

def slot_options(j):
    opts = [("x",)]
    for i in range(r):
        opts.append(("T", i, "prev"))
    opts.append(("T", j, "cur"))
    return opts

def random_system():
    sysm = []
    for j in range(r):
        k = rng.choice([2, 3]) if kmax >= 3 else 2
        tt = rng.randrange(1 << (1 << k))
        wiring = [rng.choice(slot_options(j)) for _ in range(k)]
        sysm.append((tt, k, wiring))
    return sysm

def score(sysm):
    if not all(R.nondegenerate(tt, k) for tt, k, w in sysm):
        return -1e9, None
    if not any(w[0] == "T" for tt, k, wiring in sysm for w in wiring):
        return -1e9, None
    try:
        res = R.evaluate(sysm, levels=140, inner=70, tol=1e-10)
    except Exception:
        return -1e9, None
    if not res.get("ok") or res.get("note"):
        return -1e9, None
    vals = [x for x in res["ratio"] if math.isfinite(x)]
    if not vals:
        return -1e9, None
    b = max(vals)
    if b > 50:
        return -1e9, None
    return b, res

def mutate(sysm):
    sysm = [(tt, k, list(w)) for tt, k, w in sysm]
    j = rng.randrange(r); tt, k, w = sysm[j]
    mv = rng.random()
    if mv < 0.5:
        tt ^= 1 << rng.randrange(1 << k)
    elif mv < 0.9:
        w[rng.randrange(k)] = rng.choice(slot_options(j))
    else:
        k2 = 3 if k == 2 else 2
        if k2 <= kmax:
            k = k2; tt = rng.randrange(1 << (1 << k)); w = [rng.choice(slot_options(j)) for _ in range(k)]
    sysm[j] = (tt, k, w)
    return sysm

def dump_top(top, n, t0, best_ever):
    with open(topf, "w", encoding="utf-8") as f:
        f.write("tag %s r=%d kmax=%d evaluated %d elapsed %.0f s best_ever %.7f (record to beat %.7f)\n" % (tag, r, kmax, n, time.time() - t0, best_ever, RECORD))
        for b, s in top:
            f.write("%.7f  %s\n" % (b, s))

t0 = time.time(); n = 0; top = []; best_ever = -1
while time.time() - t0 < minutes * 60 and not os.path.exists(stopf):
    cur = random_system(); cs, _ = score(cur); n += 1
    tries = 0
    while cs < -1e8 and tries < 50:
        cur = random_system(); cs, _ = score(cur); n += 1; tries += 1
    if cs < -1e8:
        continue
    best_local = (cs, cur)
    T0 = 0.05; steps = 400
    for it in range(steps):
        if os.path.exists(stopf):
            break
        T = T0 * (1 - it / steps) + 1e-3
        cand = mutate(cur); s, res = score(cand); n += 1
        if s > -1e8 and (s >= cs or rng.random() < math.exp((s - cs) / T)):
            cur, cs = cand, s
            if s > best_local[0]:
                best_local = (s, cand)
                if s > best_ever:
                    best_ever = s
                    out.write(json.dumps(dict(best=s, system=[(tt, k, [list(x) for x in w]) for tt, k, w in cand], ratio=res["ratio"], levels=res.get("levels"), t=time.time() - t0)) + "\n"); out.flush()
        if n % 500 == 0:
            dump_top(top, n, t0, best_ever)
    top.append((best_local[0], [(tt, k, [list(x) for x in w]) for tt, k, w in best_local[1]]))
    top.sort(key=lambda t: -t[0]); top = top[:25]
    dump_top(top, n, t0, best_ever)
dump_top(top, n, t0, best_ever)
print("done", n, "evaluations, best_ever %.7f" % best_ever)
