import sys, json
from fractions import Fraction as F
R = r"~/AppData/Local/Temp/claude/727c9a8b9fa813fe/agent-66b6-4575-b3c4-a8807fd17369/scratchpad/zen8/toeplitz-hankel-section-profiles"
sys.path.insert(0, R + "/engine")
from tk_core import canonical, is_parity_mixing
def reduced(pm):
    n = len(pm); return all(pm[i] != (i + 1) % n for i in range(n))
def pm_of(word):
    pos = {}
    for i, ch in enumerate(word): pos.setdefault(ch, []).append(i)
    pm = [None] * len(word)
    for a, b in pos.values(): pm[a], pm[b] = b, a
    return tuple(pm)
def load(path):
    d = json.load(open(path))
    print(path.split("/")[-1], {k: d[k] for k in d if k != "orbits"} if isinstance(d, dict) else type(d))
    orb = d["orbits"] if isinstance(d, dict) and "orbits" in d else d
    return orb
for n, path in ((10, f"{R}/data/volumes_H10.json"), (12, f"{R}/data/volumes_H12.json"), (14, f"{R}/data/volumes_H14.json"), (16, f"{R}/verify/H16_direct_volumes.json")):
    orb = load(path)
    if isinstance(orb, dict):
        items = [(tuple(json.loads(k)), v) for k, v in orb.items()]
    else:
        print("list sample", orb[:1]); continue
    sample = items[0]
    def V(v): return F(v["volume"]) if isinstance(v, dict) else F(v)
    def S(v): return v.get("size", None) if isinstance(v, dict) else None
    red = [(k, v) for k, v in items if reduced(k) and is_parity_mixing(k)]
    vols = [V(v) for k, v in red]
    mx = max(vols)
    print(f"n={n}: reduced pm orbits {len(red)} labelled {sum(S(v) or 0 for k,v in red)} distinct {len(set(vols))} max {mx} at", [k for k, v in red if V(v) == mx])
    for w in ("abcabcdefdef", "abcabcgdefdefg", "abcabcghdefdefhg", "abcdeabcde", "abcdefgabcdefg"):
        if len(w) == n:
            print("   ", w, "canon", canonical(pm_of(w)))
