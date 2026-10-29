"""Weighted Bernstein positivity (bcoefs from bern_weighted_numeric) with extreme weights 10^-4..10^4 per edge, on random
connected-ish graphs with 6-7 vertices, random edge pairs (adjacent and disjoint), native degree."""
import itertools, json, random, sys
from fractions import Fraction
from bern_weighted_numeric import bcoefs
rng = random.Random(int(sys.argv[1]))
vals = [Fraction(1, 10 ** 4), Fraction(1, 100), Fraction(1), Fraction(100), Fraction(10 ** 4)]
for n, mlo, mhi, G, T in ((6, 8, 12, 10, 12), (7, 10, 13, 6, 8)):
    allE = list(itertools.combinations(range(n), 2)); tot = bad = 0; ex = None
    for g in range(G):
        E = sorted(rng.sample(allE, rng.randint(mlo, mhi)))
        pairs = list(itertools.combinations(range(len(E)), 2)); rng.shuffle(pairs)
        for e, f in pairs[:4]:
            for t in range(T):
                lam = [rng.choice(vals) for _ in E]
                try: b = bcoefs(n, E, e, f, lam, 0)
                except ValueError: continue  # N identically zero (pair in different components etc.)
                tot += 1
                if min(b) < 0:
                    bad += 1; ex = ex or {"E": E, "e": E[e], "f": E[f], "lam": [str(x) for x in lam], "j": b.index(min(b))}
    print(json.dumps({"n": n, "graphs": G, "checks": tot, "negative": bad, "example": ex}), flush=True)
