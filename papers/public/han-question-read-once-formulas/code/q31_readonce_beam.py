# T021: sup of D_k/I_k over read-once formulas = sup over sequences P_l in (0,1) of the general recursion (q31_readonce_general.py).
# Beam search over P sequences; bins on (c0, log I) keep diversity.
import mpmath as mp, math
from q31_readonce_general import stepP
mp.mp.dps = 60
grid = sorted(set([mp.mpf(j) / 40 for j in range(1, 40)] + [1 - mp.mpf(10) ** (-e / 2) for e in range(3, 9)]))
beam = [((mp.mpf(0), mp.mpf(1), mp.mpf(0)), ())]
best = (mp.mpf(0), ())
for L in range(1, 61):
    nxt = {}
    for st, seq in beam:
        for P in grid:
            s2 = stepP(st, P)
            if s2[1] < mp.mpf("1e-40"): continue
            r = s2[2] / s2[1]
            key = (round(float(s2[0]) * 20), round(math.log(float(s2[1])) * 2))
            if key not in nxt or r > nxt[key][0]: nxt[key] = (r, s2, seq + (float(P),))
            if r > best[0]: best = (r, seq + (float(P),))
    items = sorted(nxt.values(), key=lambda t: -t[0])[:300]
    beam = [(s, q) for _, s, q in items]
    if L % 10 == 0 or L < 4: print("L=%d best r so far %s  beam top %s" % (L, mp.nstr(best[0], 10), mp.nstr(items[0][0], 10)), flush=True)
print("best D_k/I_k = %s nats; pi^2/2 = %s" % (mp.nstr(best[0], 12), mp.nstr(mp.pi ** 2 / 2, 12)))
print("best P sequence (first 30):", [round(p, 4) for p in best[1][:30]], "len", len(best[1]))
