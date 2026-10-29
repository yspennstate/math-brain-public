"""Cross term X (bern_cross_term.cross) for ADJACENT pairs on random 6-vertex graphs, every g not in {e,f}, equal and random weights."""
import itertools, json, random
from fractions import Fraction
from bern_cross_term import cross
rng = random.Random(8); vals = [Fraction(1, 100), Fraction(1), Fraction(100)]
allE = list(itertools.combinations(range(6), 2)); tot = bad = 0; ex = None
for G in range(8):
    E = sorted(rng.sample(allE, rng.randint(8, 11)))
    adj = [(e, f) for e, f in itertools.combinations(range(len(E)), 2) if set(E[e]) & set(E[f])]
    e, f = rng.choice(adj)
    for g in range(len(E)):
        if g in (e, f): continue
        for t in range(3):
            lam = [Fraction(1)] * len(E) if t == 0 else [rng.choice(vals) for _ in E]
            b = cross(6, E, lam, e, f, g)
            if b is None: continue
            tot += 1
            if min(b) < 0: bad += 1; ex = ex or {"E": E, "e": E[e], "f": E[f], "g": E[g], "eq": t == 0, "j": b.index(min(b)), "val": float(min(b))}
print(json.dumps({"n": 6, "graphs": 8, "checks": tot, "X_negative": bad, "example": ex}))
