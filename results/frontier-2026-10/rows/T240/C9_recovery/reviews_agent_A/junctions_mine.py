import json, sys
from fractions import Fraction as F
P = [("bfull14", 0, 199), ("brst10", 200, 599), ("flow599", 600, 887), ("plain888g8", 888, None)]
L = {n: [json.loads(l) for l in open(n + ".jsonl", encoding="utf-8")] for n, _, _ in P}
maxR, last = 0.0, None
for n, k0, k1 in P:
    rows = [r for r in L[n][1:] if "k" in r]
    ks = [int(r["k"]) for r in rows]
    if k1 is None: k1 = ks[-1]
    sel = [r for r in rows if k0 <= int(r["k"]) <= k1]
    assert [int(r["k"]) for r in sel] == list(range(k0, k1 + 1)), n
    fails = sum(1 for r in sel if r.get("fail"))
    mR = max(max(map(float, r["R"])) for r in sel)
    maxR = max(maxR, mR)
    hdr = L[n][0]; vin = [float(F(x)) for x in hdr["v_in"]]
    prev = "" if last is None else "prev-row float v %s" % ["%.3e" % x for x in last]
    print(n, "rows", k0, k1, "n", len(sel), "fails", fails, "max R %.3e" % mR, "t_end", sel[-1]["t"], "| v_in", ["%.3e" % x for x in vin], "blocks_in", hdr["blocks_in"], prev)
    last = list(map(float, sel[-1]["v"])); tail = [r for r in L[n][1:] if "k" not in r]
    if tail: print("   tail keys", [list(r.keys())[:4] for r in tail][:3])
print("overall max R %.4e  last |v| %s" % (maxR, ["%.4e" % x for x in last]))
