import json
from fractions import Fraction as F
from math import comb
exec(open("check_hank.py").read().split("def load")[0])
from tk_core import dihedral_images
def cat(k): return comb(2 * k, k) // (k + 1)
def kappa(kind, n):
    if n == 16 and kind == "H":
        d = json.load(open(f"{R}/verify/kappa8_volumes_H.json"))
        items = [(tuple(int(x) for x in k.split("-")), F(v)) for k, v in d.items()]
        return sum(v * len(set(map(tuple, dihedral_images(k)))) for k, v in items if reduced(k))
    d = json.load(open(f"{R}/data/volumes_{kind}{n}.json"))
    return sum(F(v["volume"]) * v["size"] for k, v in d["orbits"].items() if reduced(json.loads(k)))
known = {"T": {8: F(908, 15), 10: F(415), 12: F(23840, 7), 14: F(325719, 10)},
         "H": {8: F(281, 15), 10: F(2717, 36), 12: F(1052, 3), 14: F(1331087, 720), 16: F(9179819, 840)}}
for kind in ("T", "H"):
    kap = {r: kappa(kind, 2 * r) for r in range(2, 9 if kind == "H" else 8)}
    for n in sorted(known[kind]):
        k = n // 2
        m = cat(k) + sum(comb(2 * k, k - r) * kap[r] for r in range(2, k + 1))
        print(kind, 2 * k, m, m == known[kind][n])
