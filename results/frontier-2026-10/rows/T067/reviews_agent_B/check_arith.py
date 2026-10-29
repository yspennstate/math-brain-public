"""Exact arithmetic of the T067 band compositions (agent B second audit)."""
from fractions import Fraction as F
import re, glob, json, os
out = {}
curve = {"BAND74": (74, 76, F(5, 43), F(531277441825, 4947802324992), F(1805, 16641)),
         "BAND77": (77, 79, F(31, 272), F(177412024601, 1649267441664), F(290405, 2663424))}
for k, (a, D, eta, x, rad) in curve.items():
    out[k] = {"eta2>=1/a": eta * eta >= F(1, a), "eta<1": eta < 1,
              "radius=5(1-eta)^2/36": F(5, 36) * (1 - eta) ** 2 == rad, "x<radius": x < rad, "gap": str(rad - x)}
cut = F(179, 1500)
for k, (a, D, eta, x, gap) in {"BAND80": (80, 83, F(35, 313), F(2075411390651, 19791209299968), F(35792448226481, 2473901162496000)),
                              "BAND84": (84, 88, F(37, 339), F(2346313218091, 19791209299968), F(1929719796481, 2473901162496000)),
                              "BAND89": (89, 90, F(529999, 5000000), F(581906566811, 4947802324992), F(1066397163089, 618475290624000))}.items():
    out[k] = {"eta2>=1/a": eta * eta >= F(1, a), "x<179/1500": x < cut, "stated gap exact": cut - x == gap}
out["BAND77 77eta^2-1"] = str(77 * F(31, 272) ** 2 - 1)
# ALL-REGULAR partition from the band texts' own headers
P = r"(local file)"
rows = []
for f in glob.glob(os.path.join(P, "T067-BAND*-001_v1.md")):
    if "UPPER" in f or "COMPARISON" in f:
        continue
    t = open(f, encoding="utf-8").read()
    m = re.search(r"degrees? ?(\d+)\s*(?:\.\.|and)\s*(\d+)", t) or re.search(r"degrees? ?(\d+)\b", t)
    lo = int(m.group(1)); hi = int(m.group(2)) if m.lastindex == 2 else lo
    rows.append((lo, hi, os.path.basename(f)))
rows.sort()
cover = [d for lo, hi, _ in rows if hi <= 79 for d in range(lo, hi + 1)]
out["band headers"] = [(lo, hi, n) for lo, hi, n in rows]
out["bands 7..79 disjoint and complete"] = sorted(cover) == list(range(7, 80))
print(json.dumps(out, indent=1, default=str))
json.dump(out, open("check_arith.json", "w"), indent=1, default=str)
