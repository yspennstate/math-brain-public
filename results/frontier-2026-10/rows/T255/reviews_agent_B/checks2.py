"""T255 audit checks, part 2: uniformity of Lemma A(ii) in Phi_S and in degenerate shapes; the m = 2 mean-token mode."""
import json, random, sympy as sp, mpmath as mp
from gen_paper import Model
from checks import rand_pd, corner_V, corner_funcs  # noqa (re-runs part 1's prints; cheap enough)

random.seed(29)
mpf = mp.mpf
OUT = {}
for m in (3, 4):
    M = Model(m); F = corner_funcs(M)
    for g2s in ("0.5", "1"):
        g2 = mpf(g2s); muS = g2 / m ** 2 * (g2 - m * (m - 2) / mpf(m - 1))
        a = mpf("1e12"); rows = {}
        for phi in ("1e-1", "1e-2", "1e-3"):
            gap = 0; qvmax = 0
            for shape in range(6):
                if shape < 3:
                    X0 = rand_pd(m - 1)
                else:                                   # nearly rank one, or nearly rank m-2
                    v = mp.matrix([random.gauss(0, 1) for _ in range(m - 1)])
                    X0 = v * v.T + mp.eye(m - 1) * mpf(10) ** (-6 * (shape - 2))
                tr = sum(X0[i, i] for i in range(m - 1))
                Vx = corner_V(m, a, [0] * (m - 1), mpf(phi) * a / tr, X0)
                _, d, q = M.gen(F["logPhiS"], Vx, g2, mpf(1))
                gap = max(gap, abs(d / M.W2(Vx) - muS)); qvmax = max(qvmax, q / M.W2(Vx))
            rows[phi] = [float(gap), float(qvmax)]
        OUT[f"m{m}_g2_{g2s}_PhiS_gap_and_qv"] = rows
        print(m, g2s, rows, flush=True)

# m = 2: S = 1^T V 1 drift (g2 w^2 / (4 tau0^2)) S claimed; QV O((1+w) S)^2
M = Model(2); V = M.Vs
Sc = M.compile(V[0, 0] + V[1, 1] + 2 * V[0, 1])
worst = 0; qv_ratio = 0
for _ in range(30):
    Vn = rand_pd(2, random.choice([0.1, 1, 10]))
    g2 = mpf(random.choice(["0.3", "0.5", "1"])); tau0 = mpf(random.choice(["0.5", "1", "2"]))
    S, d, q = M.gen(Sc, Vn, g2, tau0)
    w = (Vn[0, 0] + Vn[1, 1] - 2 * Vn[0, 1]) / 2
    worst = max(worst, abs(d - g2 * w ** 2 / (4 * tau0 ** 2) * S) / abs(d))
    qv_ratio = max(qv_ratio, q / ((1 + w) * S) ** 2)
OUT["m2_S_drift_max_rel"] = float(worst); OUT["m2_S_qv_over_((1+w)S)^2_max"] = float(qv_ratio)
print(OUT, flush=True)
json.dump(OUT, open("checks2.json", "w"), indent=1)
