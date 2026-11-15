"""Per-orbit check of paper 7's T10 volumes: Monte Carlo over EVERY member pairing of each dihedral orbit
(so the dihedral reduction is tested too) against the exact orbit volume in data/volumes_T10.json."""
import json, numpy as np, time
from fractions import Fraction
from p8_moment_mc import pairings, vol
D = "~/AppData/Local/Temp/claude/727c9a8b9fa813fe/agent-66b6-4575-b3c4-a8807fd17369/scratchpad/zen8/crossing-cores-toeplitz-hankel/data/volumes_T10.json"
def canon(inv):
    n = len(inv); best = None
    for r in range(n):
        for refl in (False, True):
            f = (lambda i: (-i + r) % n) if refl else (lambda i: (i + r) % n)
            g = [0] * n
            for i in range(n): g[f(i)] = f(inv[i])
            t = tuple(g)
            if best is None or t < best: best = t
    return best
if __name__ == "__main__":
    d = json.load(open(D)); orb = d["orbits"]
    print("json moment_exact", d["moment_exact"], "sum size*vol",
          sum(Fraction(v["volume"]) * v["size"] for v in orb.values()), "sizes", sum(v["size"] for v in orb.values()))
    keymap = {canon(json.loads(k)): k for k in orb}
    acc = {k: [0.0, 0.0, 0] for k in orb}
    rng = np.random.default_rng(777); t0 = time.time(); miss = 0
    for pr in pairings(list(range(1, 11))):
        inv = [0] * 10
        for a, b in pr: inv[a - 1] = b - 1; inv[b - 1] = a - 1
        k = keymap.get(canon(inv))
        if k is None: miss += 1; continue
        q, s = vol(pr, 10, "T", 1_000_000, rng); acc[k][0] += q; acc[k][1] += s * s; acc[k][2] += 1
    print("pairings not in any orbit:", miss, f"({time.time()-t0:.0f} s)")
    tot = var = 0.0; rows = []
    for k, v in orb.items():
        ex = float(Fraction(v["volume"])) * v["size"]; mc, vv, c = acc[k]
        z = (mc - ex) / max(vv ** 0.5, 1e-12); tot += mc; var += vv
        rows.append((abs(z), z, k, v["volume"], v["size"], c, mc, ex))
        if c != v["size"]: print("SIZE MISMATCH", k, c, v["size"])
    rows.sort(reverse=True)
    for r in rows[:8]: print(f"z={r[1]:+.2f} orbit {r[2]} vol {r[3]} size {r[4]} counted {r[5]} mc {r[6]:.4f} exact {r[7]:.4f}")
    print(f"total MC {tot:.4f} +- {var**0.5:.4f}; chi2 = {sum(r[1]**2 for r in rows):.1f} over {len(rows)} orbits")
