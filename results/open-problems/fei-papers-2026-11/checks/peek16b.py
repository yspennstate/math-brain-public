import json
exec(open("check_hank.py").read().split("def load")[0])
from tk_core import dihedral_images
for name in ("kappa8_volumes_H.json", "kappa8_orbits_H.json"):
    d = json.load(open(f"{R}/verify/{name}"))
    print(name, type(d).__name__, len(d), (list(d.items())[:2] if isinstance(d, dict) else d[:2]))
d = json.load(open(f"{R}/verify/kappa8_volumes_H.json"))
def key(k):
    return tuple(int(x) for x in k.replace("[","").replace("]","").replace(" ","").replace("-",",").split(",") if x != "")
items = [(key(k), F(v if not isinstance(v, dict) else v["volume"])) for k, v in d.items()]
red = [(k, v) for k, v in items if reduced(k) and is_parity_mixing(k)]
print("entries", len(items), "reduced pm", len(red))
if red:
    lab = sum(len(set(map(tuple, dihedral_images(k)))) for k, v in red)
    vs = [v for k, v in red]; mx = max(vs)
    print("labelled", lab, "distinct", len(set(vs)), "max", mx, "at", [k for k, v in red if v == mx], "eta2", canonical(pm_of("abcabcghdefdefhg")))
