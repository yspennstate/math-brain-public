# Adversarial hill-climb for the biased isoperimetric ratios r1, r2 (60-digit arithmetic).
import random, sys, math
from isoper2 import ratios, ltf, randmono, randfun
rng = random.Random(int(sys.argv[1]))
key = sys.argv[2]            # r1 or r2
rounds = int(sys.argv[3]); nmax = int(sys.argv[4])
best_overall = -1e9
for rd in range(rounds):
    n = rng.randint(2, nmax)
    kind = rng.choice(['ltf', 'ltf', 'mono', 'rand'])
    f = ltf(n, rng) if kind == 'ltf' else (randmono(n, rng) if kind == 'mono' else randfun(n, rng))
    if len(set(f)) < 2: continue
    lg = [rng.uniform(-18, 18) for _ in range(n)]      # logit of q (natural log)
    def qof(lg): return [1 / (1 + math.exp(-t)) for t in lg]
    cur = ratios(f, qof(lg)).get(key, -1e9)
    for step in range(60):
        lg2 = [t + rng.gauss(0, 2.0) if rng.random() < 0.5 else t for t in lg]
        lg2 = [max(-25, min(25, t)) for t in lg2]
        v = ratios(f, qof(lg2)).get(key, -1e9)
        if v > cur: cur, lg = v, lg2
    if cur > best_overall:
        best_overall = cur
        print('round', rd, 'new best', key, round(cur, 5), kind, n, [round(t, 2) for t in lg], f, flush=True)
print('DONE best', key, best_overall)
