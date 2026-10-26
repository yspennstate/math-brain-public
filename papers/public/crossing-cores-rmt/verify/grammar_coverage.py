"""How thin is the grammar class?  Compare its distinct volumes against
the true distinct volumes among ALL reduced Toeplitz cores at r = 5,6,7,
which are known exactly from the reduced-core sweeps."""
import json, os, sys
from fractions import Fraction as Fr
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "verify"))
from grammar_max import pmul, pint01, cycle_poly, profiles
HERE = os.path.dirname(os.path.abspath(__file__))

memo = {}
def gram(r):
    out = set()
    if r >= 2: out.add(cycle_poly(r))
    for a in range(2, r-1):
        b = r-a
        if b < 2: continue
        for pa in profiles(a, memo):
            for pb in profiles(b, memo):
                out.add(tuple(pmul(list(pa), list(pb))))
    return {pint01(list(p)) for p in out}

res = json.load(open(os.path.join(HERE, "rerun_moments_results.json"), encoding="utf-8"))
print(" r   all reduced cores            grammar class        max captured?")
for r in (5, 6, 7):
    po = res[f"reduced_T{r}"]["per_orbit"]
    allv = {Fr(v) for v, s in po.values()}
    g = gram(r)
    amax, gmax = max(allv), max(g)
    print(f" {r}   {len(po):5d} orbits, {len(allv):3d} volumes   "
          f"{len(g):3d} volumes        max {amax} vs {gmax}  "
          f"{'YES' if amax == gmax else 'NO'}")
    print(f"      grammar volumes present in the true spectrum: "
          f"{len(g & allv)}/{len(g)}")
