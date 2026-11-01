"""All edge pairs of random graphs (n vertices, m edges in [mlo, mhi]) - Bernstein positivity count, one enumeration per edge e."""
import sys, random, json, itertools
from bern_named import run
rng = random.Random(int(sys.argv[1])); n, mlo, mhi, G = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
for g in range(G):
    m = rng.randint(mlo, mhi); edges = sorted(rng.sample(list(itertools.combinations(range(n), 2)), m))
    neg = pairs = 0
    for e in range(m):
        r = run(n, edges, e); pairs += len(r); neg += sum(1 for x in r if x)
    print(json.dumps({"n": n, "m": m, "edges": edges, "ordered_pairs": pairs, "bernstein_negative": neg}), flush=True)
