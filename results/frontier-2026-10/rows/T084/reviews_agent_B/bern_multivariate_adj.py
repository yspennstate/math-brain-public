"""Adjacent pairs only, multivariate monomial-wise Bernstein positivity (bern_multivariate.run) on more graphs, 9-10 edges."""
import json, itertools, random
from bern_multivariate import run
G = [("K33", 6, [(i, j) for i in range(3) for j in range(3, 6)]),
     ("wheel5", 6, [(0, i) for i in range(1, 6)] + [(i, i % 5 + 1) for i in range(1, 6)]),
     ("K5-e", 5, list(itertools.combinations(range(5), 2))[1:]),
     ("prism3", 6, [(0, 1), (1, 2), (2, 0), (3, 4), (4, 5), (5, 3), (0, 3), (1, 4), (2, 5)]),
     ("theta+", 5, [(0, 1), (1, 2), (2, 3), (3, 0), (0, 4), (4, 2), (1, 3), (1, 4)])]
rng = random.Random(5)
for _ in range(4):
    E = sorted(rng.sample(list(itertools.combinations(range(6), 2)), 9)); G.append(("rand6_9", 6, E))
for name, n, E in G:
    pairs = [(e, f) for e, f in itertools.combinations(range(len(E)), 2) if set(E[e]) & set(E[f])]
    tot = neg = 0; ex = None
    for e, f in pairs[:6]:
        r = run(n, E, e, f)
        if r is None: continue
        tot += 1
        if r["negative"]: neg += 1; ex = ex or (E[e], E[f], r["example"])
    print(json.dumps({"graph": name, "adjacent_pairs_tested": tot, "monomialwise_negative": neg, "example": ex}), flush=True)
