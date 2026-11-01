"""Scale profile of the block ratio on towers.

For f and the nested restrictions f_m (rate delta^m), the average block ratio at scale m is
    R_m = E D_delta(f_m) / ((1-delta) E I(f_m)) = [(1-delta^{m+1}) kappa_{delta^{m+1}}(f) - (1-delta^m) kappa_{delta^m}(f)] / ((1-delta) delta^m),
and H(f)/I(f) = sum_m (1-delta) delta^m R_m.  Also the average entropy/influence ratio of the theta-restrictions,
    c(theta) = E H(f_theta) / E I(f_theta) = (H/I - (1-theta) kappa_theta) / theta.
Input: the json logs of tower.py small and tower_numaro.py (last depth used as the tower limit).
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
LOG = os.path.join(HERE, "..", "logs")


def profile(kap_of, HI, delta, mmax):
    out = []
    for m in range(mmax):
        a, b = delta ** m, delta ** (m + 1)
        if a not in kap_of or b not in kap_of:
            break
        Ka = kap_of[a] if m > 0 else kap_of[a]
        R = ((1 - b) * kap_of[b] - (1 - a) * Ka) / ((1 - delta) * a)
        out.append(R)
    return out


lines = []
small = json.load(open(os.path.join(LOG, "tower_small.json")))
for name, HI in (("maj3", 4.0), ("seed4", 6.0)):
    kap = {float(k.split("_")[1]): v[-1]["kappa"] for k, v in small.items() if k.startswith(name)}
    kap[1.0] = 0.0
    lines.append(f"{name}: tower-limit H/I = {HI}")
    for th in sorted(kap):
        if th < 1.0:
            lines.append(f"   theta={th:<8} kappa={kap[th]:.5f}   c(theta)=E H/E I of theta-restrictions = {(HI - (1 - th) * kap[th]) / th:.4f}")
    R = profile({**kap, 1.0: 0.0}, HI, 0.5, 8)
    lines.append("   R_m (delta=1/2): " + "  ".join(f"{r:.4f}" for r in R))
nfile = [f for f in os.listdir(LOG) if f.startswith("tower_numaro_") and f.endswith(".json")]
for nf in sorted(nfile):
    d = json.load(open(os.path.join(LOG, nf)))
    Hg, Ig = d["H_g"], d["I_g"]
    kap = {float(k): v[-1]["kappa"] for k, v in d["rows"].items()}
    se = {float(k): v[-1].get("kappa_se", 0.0) for k, v in d["rows"].items()}
    depth = max(len(v) for v in d["rows"].values())
    HIk = Hg * (Ig ** depth - 1) / ((Ig - 1) * Ig ** depth)
    HIinf = Hg / (Ig - 1)
    lines.append(f"numaro tower ({nf}), depth {depth}: H/I(G_depth) = {HIk:.5f}, limit {HIinf:.5f}")
    for th in sorted(kap):
        lines.append(f"   theta={th:<8} kappa={kap[th]:.5f} (se {se[th]:.4f})   c(theta) = {(HIk - (1 - th) * kap[th]) / th:.4f}")
    R = profile(kap, HIk, 0.5, 6)
    lines.append("   R_m (delta=1/2): " + "  ".join(f"{r:.4f}" for r in R))
txt = "\n".join(lines)
print(txt)
open(os.path.join(LOG, "scale_profile.log"), "w").write(txt + "\n")
