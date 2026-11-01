"""Background search over recursive read-once systems (see fei_recsys.py). Writes JSONL rows and a running TOP file.
usage: python -u fei_recsearch_run.py <tag> <mode>   modes: r1k2, r1k3, r2k2, r1k4sample
Runs at BelowNormal priority. Stop early by creating STOP_<tag> in this folder.
"""
import sys, os, json, time, math, itertools, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fei_recsys as R
try:
    import psutil
    psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass

tag, mode = sys.argv[1], sys.argv[2]
HERE = os.path.dirname(os.path.abspath(__file__))
out = open(os.path.join(HERE, f"recsearch_{tag}.jsonl"), "a", encoding="utf-8")
topf = os.path.join(HERE, f"recsearch_{tag}_TOP.txt")
stopf = os.path.join(HERE, f"STOP_{tag}")
import fei_chain, fei_comp_search
STARTS = [("var", R.FRESH), ("l23", R.L23), ("l58", fei_chain.chain_state(fei_comp_search.lex_pattern(5 / 8)))]
top = []
n = 0; t0 = time.time()

def record(system, sname, res):
    global top
    r = res["ratio"]; best = max(x for x in r if math.isfinite(x)) if any(math.isfinite(x) for x in r) else float("nan")
    row = dict(system=[(tt, k, list(map(list, w))) for tt, k, w in system], start=sname, ratio=r, best=best,
               levels=res.get("levels"), note=res.get("note", ""), states=[list(map(float, s)) for s in res["states"]])
    out.write(json.dumps(row) + "\n")
    if math.isfinite(best) and best < 50 and not res.get("note"):
        top.append((best, row)); top.sort(key=lambda t: -t[0]); top = top[:30]

def flush_top():
    with open(topf, "w", encoding="utf-8") as f:
        f.write("mode %s  evaluated %d  elapsed %.0f s\n" % (mode, n, time.time() - t0))
        for b, row in top:
            f.write("%.7f  start=%s levels=%s  system=%s\n" % (b, row["start"], row["levels"], row["system"]))

def evaluate_all(systems_iter):
    global n
    for system in systems_iter:
        for sname, st in STARTS:
            if os.path.exists(stopf):
                flush_top(); return
            res = R.evaluate(system, starts=[st] * len(system), levels=160, inner=80, tol=1e-10)
            n += 1
            if res.get("ok"):
                record(system, sname, res)
            if n % 200 == 0:
                out.flush(); flush_top()
    out.flush(); flush_top()

def gates(k):
    return [tt for tt in range(1 << (1 << k)) if R.nondegenerate(tt, k)]

if mode == "r1k2":
    evaluate_all([(tt, 2, list(w))] for tt in gates(2) for w in R.all_wirings(2, 1) if any(x[0] == "T" for x in w))
elif mode == "r1k3":
    evaluate_all([(tt, 3, list(w))] for tt in gates(3) for w in R.all_wirings(3, 1) if any(x[0] == "T" for x in w))
elif mode == "r2k2":
    g2 = gates(2)
    def gen():
        for ta in g2:
            for tb in g2:
                for wa in R.all_wirings(2, 2):
                    if not any(x[0] == "T" for x in wa):
                        continue
                    for wb in R.all_wirings(2, 2):
                        if not any(x[0] == "T" for x in wb):
                            continue
                        yield [(ta, 2, list(wa)), (tb, 2, list(wb))]
    evaluate_all(gen())
elif mode == "r1k4sample":
    rng = random.Random(7)
    g4 = gates(4)
    ws = [w for w in R.all_wirings(4, 1) if any(x[0] == "T" for x in w)]
    def gen():
        while True:
            yield [(rng.choice(g4), 4, list(rng.choice(ws)))]
    evaluate_all(gen())
print("done", mode, n, "evaluations in %.0f s" % (time.time() - t0))
flush_top()
