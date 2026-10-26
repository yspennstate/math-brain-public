"""Which reduced cores lie OUTSIDE the grammar class, and what do they look
like?  Their structure names the operation the calculus is missing."""
import json, os, sys
from fractions import Fraction as Fr
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "verify"))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
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

def word_of(pm):
    lab, nxt, out = {}, 0, []
    for i in range(len(pm)):
        c = min(i, pm[i])
        if c not in lab:
            lab[c] = chr(97+nxt); nxt += 1
        out.append(lab[c])
    return "".join(out)

res = json.load(open(os.path.join(HERE, "rerun_moments_results.json"), encoding="utf-8"))
for r in (5, 6):
    po = res[f"reduced_T{r}"]["per_orbit"]
    g = gram(r)
    outside = {}
    for key, (v, s) in po.items():
        fv = Fr(v)
        if fv not in g:
            outside.setdefault(fv, []).append(key)
    print(f"=== r={r}: {len(outside)} volumes outside the grammar ===")
    for v in sorted(outside, reverse=True):
        k = outside[v][0]
        pm = tuple(int(x) for x in k.split("-"))
        print(f"   {v} = {float(v):.5f}   e.g. {word_of(pm)}  "
              f"({len(outside[v])} orbit(s))")
