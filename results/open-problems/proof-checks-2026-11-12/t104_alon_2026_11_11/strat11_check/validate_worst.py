"""Exact recheck of the triage's worst sampled points: evaluate the N=6 numerator in rationals at the stored points."""
import sys, json, os
from fractions import Fraction as F
src = os.path.abspath(sys.argv[1]); d = json.load(open(sys.argv[2], encoding="utf-8"))
sys.path.insert(0, src); os.chdir(src)
from cover_face import polynomials
P = polynomials()[0]
fe = sorted([r for r in d if r['nfeas']], key=lambda r: r['minrel'])
pick = fe[:8] + fe[len(fe)//2:len(fe)//2+2]
for r in pick:
    x = [F(v).limit_denominator(10**12) for v in r['pt']]
    val = sum(F(c) * eval_mon(x, e) if False else F(c) * __import__('math').prod([x[i]**e[i] for i in range(6)]) for e, c in P.items())
    print(r['node'], "float %.4e exact %.4e" % (r['minv'], float(val)), "agree" if abs(float(val) - r['minv']) <= 1e-6 * abs(float(val)) + 1e-9 else "DIFFER")
