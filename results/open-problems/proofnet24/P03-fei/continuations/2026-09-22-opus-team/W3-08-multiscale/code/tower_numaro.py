"""kappa_theta(G_k) on the self-compositions of Numaro's g, for several restriction rates theta.

Level 1 is exact (the exact profile E H(g_{J,x}) from families.py numaro).  The law L_1 of the restricted
mean of g is exact (restr_mean_hist).  Levels k >= 2 use Monte Carlo: nu_1..nu_18 iid from L_{k-1}
(exact for k = 2, a population sample afterwards), Xi_k = H(g) - E Htilde_g(nu) + I(g) E h2(nu^2).

usage: python tower_numaro.py NPOP DEPTH theta1,theta2,...
"""
import sys, os, json, time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from mslib import polite, fwht, entropy_bits, influences, restr_mean_hist, size_weights
from tower import law_from_hist, mc_level_tilted, h2sq

polite()
npop = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
depth = int(sys.argv[2]) if len(sys.argv) > 2 else 10
thetas = [float(t) for t in sys.argv[3].split(",")] if len(sys.argv) > 3 else [0.5]

g = np.load(os.path.join(HERE, "..", "..", "inputs", "numaro18_pm1_table.npy")).astype(np.int64)
n = 18
ghat = fwht(g)
Hg = entropy_bits(ghat * ghat)
inf = influences(ghat, n)
Ig = inf.sum()
print(f"H(g) = {Hg:.15f}  I(g) = {Ig:.15f}", flush=True)

prof = np.load(os.path.join(HERE, "..", "logs", "numaro18_profile.npz"))
cEH = prof["cEH"]
hist_path = os.path.join(HERE, "..", "logs", "numaro18_meanhist.npy")
if os.path.exists(hist_path):
    Hc = np.load(hist_path)
else:
    t0 = time.time()
    Hc = restr_mean_hist(g, n)
    np.save(hist_path, Hc)
    print(f"restricted-mean histogram computed in {time.time() - t0:.0f}s", flush=True)

out = {}
rng = np.random.default_rng(12345)
for theta in thetas:
    t0 = time.time()
    w = size_weights(n, theta)
    EH1 = float((w * cEH).sum())
    Xi1 = Hg - EH1                      # = D_theta(g), exact
    vals, probs = law_from_hist(Hc, n, theta)
    Enu2 = float((probs * vals ** 2).sum())
    kap = Xi1 / ((1 - theta) * Ig)
    rows = [{"k": 1, "Xi": Xi1, "se": 0.0, "kappa": kap, "Enu2_child": None}]
    print(f"theta={theta}: k=1 Xi={Xi1:.6f} kappa={kap:.6f}  (L_1: {len(vals)} atoms, E nu^2 = {Enu2:.6f})", flush=True)
    pop = rng.choice(vals, size=npop, p=probs / probs.sum())
    var_kap = 0.0
    for k in range(2, depth + 1):
        Ht, Eh2_pop, newpop = mc_level_tilted(ghat, inf, pop, npop, 1000 * k + int(theta * 1e6), 0.0)
        if k == 2:
            Eh2 = float(sum(p * h2sq(v) for v, p in zip(vals, probs)))   # exact for L_1
        else:
            Eh2 = Eh2_pop
        Xi = Hg - Ht.mean() + Ig * Eh2
        se = Ht.std() / np.sqrt(npop)
        kap += Xi / ((1 - theta) * Ig ** k)
        var_kap += (se / ((1 - theta) * Ig ** k)) ** 2
        rows.append({"k": k, "Xi": float(Xi), "se": float(se), "kappa": float(kap), "kappa_se": float(np.sqrt(var_kap)),
                     "Enu2_child": float(np.mean(pop ** 2))})
        print(f"theta={theta}: k={k:2d} Xi={Xi:.6f} (se {se:.4f})  kappa={kap:.6f} (se {np.sqrt(var_kap):.4f})  "
              f"E nu^2 of children={np.mean(pop ** 2):.5f}  [{time.time() - t0:.0f}s]", flush=True)
        pop = newpop
    out[str(theta)] = rows
    with open(os.path.join(HERE, "..", "logs", f"tower_numaro_{npop}.json"), "w") as fo:
        json.dump({"H_g": Hg, "I_g": Ig, "rows": out}, fo, indent=1)
