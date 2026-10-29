"""T255 audit checks (agent B), against the paper's Theorem 4.2 coefficients (gen_paper.py)."""
import json, random, sympy as sp, mpmath as mp
from gen_paper import Model

random.seed(17)
mpf = mp.mpf
OUT = {}


def rand_pd(m, scale=1.0):
    A = mp.matrix(m, m)
    for i in range(m):
        for j in range(m):
            A[i, j] = mpf(random.gauss(0, 1))
    return (A * A.T + mp.eye(m) * mpf("0.1")) * scale


def rel(a, b):
    return abs(a - b) / max(abs(b), mpf("1e-50"))


# C1 + C2 + C3 ------------------------------------------------------------------------------
def noise_rep_cov(M, V, g2, tau0):
    """Covariance of the upper entries of L dGamma L^T, section 1 of M2_EXACT.md."""
    m = M.m
    L = mp.cholesky(V)
    Pm = mp.eye(m) - mp.ones(m, m) / m
    K = L.T * Pm * L
    c = g2 * (2 - g2); k = g2 / (m * tau0)
    dirs = []
    E = lambda i, j: mp.matrix([[1 if (a, b) == (i, j) else 0 for b in range(m)] for a in range(m)])
    for i in range(m):
        for j in range(i, m):
            S = E(i, j) * mp.sqrt(2) if i == j else E(i, j) + E(j, i)
            dirs.append(L * (mp.sqrt(c) * S) * L.T)
    for i in range(m):
        for j in range(m):
            dirs.append(L * (k * (E(i, j) * K + K * E(j, i))) * L.T)
    P = len(M.pairs)
    C = mp.matrix(P, P)
    for G in dirs:
        v = [G[a, b] for (a, b) in M.pairs]
        for x in range(P):
            for y in range(P):
                C[x, y] += v[x] * v[y]
    return C


def b_simplified(M, V, g2, tau0):
    m = M.m
    Pm = mp.eye(m) - mp.ones(m, m) / m
    W = Pm * V * Pm
    W2 = sum(W[i, j] ** 2 for i in range(m) for j in range(m))
    v = mp.matrix([V[i, i] for i in range(m)])
    trW = sum(W[i, i] for i in range(m))
    D = mp.matrix([W[i, i] - trW / m for i in range(m)])
    VD = V * D
    B = g2 / tau0 ** 2 * (V * W2 / m ** 2 + (v * VD.T + VD * v.T) / (2 * m))
    return [B[a, b] for (a, b) in M.pairs]


# C5-C8: the corner a e1 e1^T
def corner_funcs(M):
    V = M.Vs; m = M.m
    a = V[0, 0]
    vp = sp.Matrix([V[0, i] for i in range(1, m)])
    X = sp.Matrix(m - 1, m - 1, lambda i, j: V[i + 1, j + 1]) - vp * vp.T / a
    return {"loga": M.compile(sp.log(a)), "logPhiS": M.compile(sp.log(X.trace() / a)),
            "w2": M.compile((vp.T * vp)[0, 0] / a ** 2)}


def corner_V(m, a, w, eps, X0):
    u = mp.matrix([1] + list(w))
    V = a * u * u.T
    for i in range(m - 1):
        for j in range(m - 1):
            V[i + 1, j + 1] += eps * X0[i, j]
    return V


if __name__ == "__main__":
    res = {"noise_rep_vs_paper_Sigma_max_rel": [], "b_simplified_vs_paper_max_rel": []}
    for m in (2, 3, 4):
        M = Model(m)
        for _ in range(6):
            V = rand_pd(m, random.choice([0.3, 1, 5]))
            g2 = mpf(random.choice(["0.2", "0.5", "0.9", "1"])); tau0 = mpf(random.choice(["0.7", "1", "2"]))
            b, Sig = M.coeffs(V, g2, tau0)
            C = noise_rep_cov(M, V, g2, tau0)
            mx = max(abs(Sig[i, j]) for i in range(len(M.pairs)) for j in range(len(M.pairs)))
            res["noise_rep_vs_paper_Sigma_max_rel"].append(float(max(abs(C[i, j] - Sig[i, j]) for i in range(len(M.pairs))
                                                                    for j in range(len(M.pairs))) / mx))
            bs = b_simplified(M, V, g2, tau0)
            res["b_simplified_vs_paper_max_rel"].append(float(max(abs(x - y) for x, y in zip(bs, b)) / max(abs(y) for y in b)))
    OUT["C2_C3"] = {k: max(v) for k, v in res.items()}
    print("C2/C3", OUT["C2_C3"], flush=True)

    # C1: m = 2 autonomous w
    M2 = Model(2); Vs = M2.Vs
    w_expr = (Vs[0, 0] + Vs[1, 1] - 2 * Vs[0, 1]) / 2
    wc = M2.compile(w_expr)
    worst = [0, 0]
    for _ in range(40):
        V = rand_pd(2, random.choice([0.1, 1, 10]))
        g2 = mpf(random.choice(["0.2", "0.5", "0.9", "1"])); tau0 = mpf(random.choice(["0.5", "1", "3"]))
        w, dr, qv = M2.gen(wc, V, g2, tau0)
        c = g2 * (2 - g2)
        worst[0] = max(worst[0], float(rel(dr, g2 / (4 * tau0 ** 2) * w ** 3)))
        worst[1] = max(worst[1], float(rel(qv, 2 * c * w ** 2 + g2 ** 2 * w ** 4 / tau0 ** 2)))
    OUT["C1_m2_w"] = {"drift_max_rel": worst[0], "qv_max_rel": worst[1]}
    print("C1", OUT["C1_m2_w"], flush=True)

    # C1b: the m = 2 scale-density exponent and threshold, symbolically
    y, c_, k2, kap, g = sp.symbols("y c k2 kappa g", positive=True)
    expo = sp.simplify((g / 4) / (g ** 2))        # kappa / (4k^2) with kappa = g/(4 tau^2), 4k^2 = g^2/tau^2
    OUT["C1b_scale_exponent_kappa_over_4k2"] = str(expo)

    # C4: log det near singular
    for m in (3, 4):
        M = Model(m)
        ldc = M.compile(sp.log(M.Vs.det()))
        rows = []
        for e in (mpf("1e-4"), mpf("1e-12"), mpf("1e-30")):
            Q, _ = mp.qr(rand_pd(m))
            lam = mp.diag([e] + [mpf(1 + i) for i in range(m - 1)])
            V = Q * lam * Q.T
            _, dr, qv = M.gen(ldc, V, mpf("0.7"), mpf(1))
            rows.append([float(e), float(dr), float(qv)])
        OUT[f"C4_logdet_m{m}"] = rows
        print("C4", m, rows, flush=True)


    for m in (3, 4, 5, 6):
        M = Model(m); F = corner_funcs(M)
        out = {}
        for g2s in ("0.5", "1"):
            g2 = mpf(g2s); tau0 = mpf(1)
            Pe1 = (m - 1) / mpf(m)
            f = g2 / tau0 ** 2 * (Pe1 ** 2 / m ** 2 + ((m - 1) * (m - 2) / mpf(m) ** 2) / m)
            B = 2 * g2 * Pe1 / (m * tau0)
            alpha = (f - B ** 2 / 2) * m ** 2 / (m - 1) ** 2
            muS = g2 / m ** 2 * (g2 - m * (m - 2) / mpf(m - 1))
            kappa = g2 * (m - 2) / (2 * m * (m - 1))
            a = mpf("1e12")
            # alpha: exact rank one, w = 0
            V = corner_V(m, a, [0] * (m - 1), mpf(0), mp.zeros(m - 1, m - 1))
            _, dr, qv = M.gen(F["loga"], V, g2, tau0)
            W2 = M.W2(V)
            # mu_S: several shapes, eps -> 0, w = 0
            mus = []
            for _ in range(5):
                X0 = rand_pd(m - 1)
                for eps in (mpf("1e-6"),):
                    Vx = corner_V(m, a, [0] * (m - 1), eps, X0)
                    _, d2, q2 = M.gen(F["logPhiS"], Vx, g2, tau0)
                    mus.append([float(d2 / M.W2(Vx)), float(q2 / M.W2(Vx))])
            # regularity in w
            wreg = []
            for wn in (mpf("1e-1"), mpf("1e-2"), mpf("1e-3")):
                gap = 0
                for _ in range(4):
                    wv = [mpf(random.gauss(0, 1)) for _ in range(m - 1)]
                    nn = mp.sqrt(sum(x * x for x in wv)); wv = [wn * x / nn for x in wv]
                    Vx = corner_V(m, a, wv, mpf("1e-8") * a, rand_pd(m - 1)) if False else corner_V(m, a, wv, mpf("1e-6"), rand_pd(m - 1))
                    _, d2, _ = M.gen(F["logPhiS"], Vx, g2, tau0)
                    gap = max(gap, abs(d2 / M.W2(Vx) - muS))
                wreg.append(float(gap))
            # kappa: X = 0 exactly, small tilt
            kap = []
            for wn in (mpf("1e-3"), mpf("1e-5")):
                wv = [mpf(random.gauss(0, 1)) for _ in range(m - 1)]
                nn = mp.sqrt(sum(x * x for x in wv)); wv = [wn * x / nn for x in wv]
                Vx = corner_V(m, a, wv, mpf(0), mp.zeros(m - 1, m - 1))
                w2, d3, q3 = M.gen(F["w2"], Vx, g2, tau0)
                kap.append([float(d3 / M.W2(Vx) / w2), float(q3)])
            # the c-noise at moderate a: does it change the sign of mu_S?
            Vm = corner_V(m, mpf(50), [0] * (m - 1), mpf("1e-6"), rand_pd(m - 1))
            _, d4, _ = M.gen(F["logPhiS"], Vm, g2, tau0)
            out[g2s] = {"alpha_claim": float(alpha), "alpha_mine": float(dr / W2), "loga_qv_per_u": float(qv / W2),
                        "two_f_over_B2_claim": float((m * m - m - 1) / (2 * g2 * (m - 1))), "two_f_over_B2_mine": float(2 * f / B ** 2),
                        "muS_claim": float(muS), "muS_mine_shapes[drift,qv]": mus, "w_regularity_gap_at_1e-1_1e-2_1e-3": wreg,
                        "minus2kappa_claim": float(-2 * kappa), "w2_drift_over_w2_[1e-3,1e-5]": kap,
                        "logPhiS_drift_per_u_at_a50": float(d4 / M.W2(Vm))}
        OUT[f"corner_m{m}"] = out
        print("corner", m, json.dumps(out), flush=True)

    json.dump(OUT, open("checks.json", "w"), indent=1)
