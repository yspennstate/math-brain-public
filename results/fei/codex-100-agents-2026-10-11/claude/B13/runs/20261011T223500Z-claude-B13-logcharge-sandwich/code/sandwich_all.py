# claude-B13-sandwich-v1: exhaustive n<=4 check of the restriction-tree log-charge identities,
# the sandwich H-(3/ln2)I <= E sum lambda <= H on complete trees, and the n<=4 constants
#   C_n = max H/I,  K_n = max_g min_i D_i/d_i,  KL_n = max_g min_i lambda_i/d_i.
# Spectral probabilities are exact dyadics; logs come from a table of log2(integer) values
# computed with mpmath (40 digits) and rounded to float64.
import json, math, sys, time
import numpy as np
import mpmath

mpmath.mp.dps = 40
OUT = sys.argv[1]
LN2 = math.log(2.0)
MAXINT = 2 * 16 * 16 + 4
LOG2 = np.array([0.0] + [float(mpmath.log(k, 2)) for k in range(1, MAXINT + 1)])


def fwht(v):
    v = v.astype(np.int64).copy()
    B, N = v.shape
    h = 1
    while h < N:
        v = v.reshape(B, N // (2 * h), 2, h)
        a = v[:, :, 0, :].copy()
        b = v[:, :, 1, :].copy()
        v[:, :, 0, :] = a + b
        v[:, :, 1, :] = a - b
        v = v.reshape(B, N)
        h *= 2
    return v


def ent_from_ints(c, den):
    """Entropy (bits) of law c^2/den summed over last axis; c integer array, sum c^2 = den."""
    c = np.abs(c)
    return math.log2(den) - (2.0 / den) * (c * c * LOG2[c]).sum(axis=-1)


def ent_from_squares(s, den):
    """Entropy of law s/den, s nonnegative integers."""
    return math.log2(den) - (1.0 / den) * (s * LOG2[s]).sum(axis=-1)


def all_functions(m):
    N = 1 << m
    T = np.arange(1 << N, dtype=np.int64)
    bits = (T[:, None] >> np.arange(N)[None, :]) & 1
    return T, 1 - 2 * bits


def analyze(m):
    N = 1 << m
    T, f = all_functions(m)
    W = fwht(f)  # W[S] = sum_x f(x) chi_S(x)
    den = N * N
    H = ent_from_ints(W, den)
    S = np.arange(N)
    pop = np.array([bin(s).count("1") for s in S])
    I = (W * W * pop[None, :]).sum(axis=1) / den
    res = dict(T=T, W=W, H=H, I=I)
    per = []
    for j in range(m):
        T0 = np.array([s for s in S if not (s >> j) & 1])
        T1 = T0 | (1 << j)
        a = W[:, T0]
        b = W[:, T1]
        d = (b * b).sum(axis=1) / den
        cp = (a + b) // 2  # child x_j=+1 (bit 0) Walsh on m-1 vars
        cm = (a - b) // 2
        assert np.all((a + b) % 2 == 0)
        dc = (N // 2) ** 2
        Hp = ent_from_ints(cp, dc)
        Hm = ent_from_ints(cm, dc)
        D = H - 0.5 * (Hp + Hm)
        s = a * a + b * b
        Hq = ent_from_squares(s, den)
        Bv = H - Hq  # exact identity H(p) = H(q) + B
        # direct B = sum_T q h2(theta)
        with np.errstate(divide="ignore", invalid="ignore"):
            qf = s / den
            th = np.where(s > 0, (b * b) / np.maximum(s, 1), 0.0)
            h2 = np.where((th > 0) & (th < 1), -th * np.log2(np.where(th > 0, th, 1)) - (1 - th) * np.log2(np.where(th < 1, 1 - th, 1)), 0.0)
        Bdir = (qf * h2).sum(axis=1)
        J = Hq - 0.5 * (Hp + Hm)
        bb = b * b
        lam = (bb * (LOG2[s] - LOG2[np.abs(b)] * 2) ).sum(axis=1) / den  # terms with b=0 vanish (bb=0)
        # second formula: sum_{S contains j} p(S) log2(1+p(S\j)/p(S))  (same terms, written via ratio)
        with np.errstate(divide="ignore", invalid="ignore"):
            lam2 = np.where(bb > 0, (bb / den) * np.log2(1.0 + (a * a) / np.where(bb > 0, bb, 1)), 0.0).sum(axis=1)
        # KL form: d log2(1/d) - d KL(nu||q)
        with np.errstate(divide="ignore", invalid="ignore"):
            nu = np.where(d[:, None] > 0, (bb / den) / np.where(d[:, None] > 0, d[:, None], 1), 0.0)
            kl = np.where(nu > 0, nu * np.log2(np.where(nu > 0, nu, 1) / np.where(s > 0, s / den, 1)), 0.0).sum(axis=1)
            lam3 = np.where(d > 0, d * np.log2(np.where(d > 0, 1 / np.where(d > 0, d, 1), 1)) - d * kl, 0.0)
        # children indices
        posp = [x for x in range(N) if not (x >> j) & 1]
        posm = [x for x in range(N) if (x >> j) & 1]
        bits = (T[:, None] >> np.arange(N)[None, :]) & 1
        w = (1 << np.arange(N // 2))
        chp = (bits[:, posp] * w).sum(axis=1)
        chm = (bits[:, posm] * w).sum(axis=1)
        per.append(dict(d=d, D=D, B=Bv, Bdir=Bdir, J=J, lam=lam, lam2=lam2, lam3=lam3, chp=chp, chm=chm))
    res["per"] = per
    return res


def main():
    t0 = time.time()
    tabs = {}
    report = {"checks": {}, "constants": {}, "trees": {}, "potential": {}}
    for m in range(0, 5):
        if m == 0:
            tabs[0] = dict(H=np.zeros(2), I=np.zeros(2), per=[])
            continue
        r = analyze(m)
        tabs[m] = r
        H, I = r["H"], r["I"]
        mx = {"D=B+J": 0.0, "B identity vs direct": 0.0, "lam formulas": 0.0, "lam KL form": 0.0,
              "D<=lam+3d/ln2 violation": 0.0, "lam<=B violation": 0.0, "J<=2d/ln2 violation": 0.0,
              "B<=lam+d/ln2 violation": 0.0, "D>=0 violation": 0.0}
        for q in r["per"]:
            mx["D=B+J"] = max(mx["D=B+J"], float(np.max(np.abs(q["D"] - q["B"] - q["J"]))))
            mx["B identity vs direct"] = max(mx["B identity vs direct"], float(np.max(np.abs(q["B"] - q["Bdir"]))))
            mx["lam formulas"] = max(mx["lam formulas"], float(np.max(np.abs(q["lam"] - q["lam2"]))))
            mx["lam KL form"] = max(mx["lam KL form"], float(np.max(np.abs(q["lam"] - q["lam3"]))))
            mx["D<=lam+3d/ln2 violation"] = max(mx["D<=lam+3d/ln2 violation"], float(np.max(q["D"] - q["lam"] - 3 * q["d"] / LN2)))
            mx["lam<=B violation"] = max(mx["lam<=B violation"], float(np.max(q["lam"] - q["B"])))
            mx["J<=2d/ln2 violation"] = max(mx["J<=2d/ln2 violation"], float(np.max(q["J"] - 2 * q["d"] / LN2)))
            mx["B<=lam+d/ln2 violation"] = max(mx["B<=lam+d/ln2 violation"], float(np.max(q["B"] - q["lam"] - q["d"] / LN2)))
            mx["D>=0 violation"] = max(mx["D>=0 violation"], float(np.max(-q["D"])))
        report["checks"][f"n={m}"] = mx
        # constants
        nz = I > 1e-12
        ratio = np.where(nz, H / np.where(nz, I, 1), -1)
        Dd = np.stack([np.where(q["d"] > 0, q["D"] / np.where(q["d"] > 0, q["d"], 1), np.inf) for q in r["per"]], axis=1)
        Ld = np.stack([np.where(q["d"] > 0, q["lam"] / np.where(q["d"] > 0, q["d"], 1), np.inf) for q in r["per"]], axis=1)
        minD = np.where(nz, Dd.min(axis=1), -1)
        minL = np.where(nz, Ld.min(axis=1), -1)
        # pointwise relations
        Bsum = sum(q["B"] for q in r["per"])
        gap_pw = np.where(nz, minD - ratio, -1e9)
        argC, argK, argL = int(np.argmax(ratio)), int(np.argmax(minD)), int(np.argmax(minL))
        report["constants"][f"n={m}"] = {
            "C_n=max H/I": float(ratio.max()), "argmax_truth_table": argC,
            "K_n=max_g min_i D_i/d_i": float(minD.max()), "argmax_K": argK,
            "H/I at argmax_K": float(ratio[argK]),
            "KL_n=max_g min_i lambda_i/d_i": float(minL.max()), "argmax_KL": argL,
            "max_g (min_i D_i/d_i - H/I)": float(gap_pw.max()), "argmax_gap": int(np.argmax(gap_pw)),
            "pointwise bound min_i D_i/d_i <= H/I + 2/ln2 violation": float(np.max(np.where(nz, minD - ratio - 2 / LN2, -1e9))),
            "pointwise bound min_i lam_i/d_i <= B/I violation": float(np.max(np.where(nz, minL - Bsum / np.where(nz, I, 1), -1e9))),
            "count functions with min_i D_i/d_i > H/I": int(np.sum(nz & (minD > ratio + 1e-9))),
            "nonconstant functions": int(np.sum(nz)),
        }
        tabs[m]["ratio"] = ratio
        tabs[m]["minD"] = minD
        tabs[m]["minL"] = minL
        tabs[m]["Dd"] = Dd
    # complete-tree DP for rules
    rules = ["minInf", "maxInf", "greedyD", "greedyL", "lex"]
    C4 = report["constants"]["n=4"]["C_n=max H/I"]
    Cs = {"C4": C4, "4": 4.0, "6.5218": 6.5218, "8": 8.0}
    for rule in rules:
        Lam, SD, Sd, Q = {0: np.zeros(2)}, {0: np.zeros(2)}, {0: np.zeros(2)}, {c: {0: np.zeros(2)} for c in Cs}
        for m in range(1, 5):
            r = tabs[m]
            nfun = len(r["H"])
            dmat = np.stack([q["d"] for q in r["per"]], axis=1)
            rel = dmat > 0
            if rule == "minInf":
                key = np.where(rel, dmat, np.inf)
                ch = key.argmin(axis=1)
            elif rule == "maxInf":
                key = np.where(rel, -dmat, np.inf)
                ch = key.argmin(axis=1)
            elif rule == "greedyD":
                ch = np.where(rel, r["Dd"], np.inf).argmin(axis=1)
            elif rule == "greedyL":
                Ld = np.stack([np.where(q["d"] > 0, q["lam"] / np.where(q["d"] > 0, q["d"], 1), np.inf) for q in r["per"]], axis=1)
                ch = np.where(rel, Ld, np.inf).argmin(axis=1)
            else:
                ch = np.where(rel, np.arange(m)[None, :], m + 1).argmin(axis=1)
            nonconst = rel.any(axis=1)
            idx = np.arange(nfun)
            lam = np.stack([q["lam"] for q in r["per"]], axis=1)[idx, ch]
            D = np.stack([q["D"] for q in r["per"]], axis=1)[idx, ch]
            d = dmat[idx, ch]
            cp = np.stack([q["chp"] for q in r["per"]], axis=1)[idx, ch]
            cm = np.stack([q["chm"] for q in r["per"]], axis=1)[idx, ch]
            Lam[m] = np.where(nonconst, lam + 0.5 * (Lam[m - 1][cp] + Lam[m - 1][cm]), 0.0)
            SD[m] = np.where(nonconst, D + 0.5 * (SD[m - 1][cp] + SD[m - 1][cm]), 0.0)
            Sd[m] = np.where(nonconst, d + 0.5 * (Sd[m - 1][cp] + Sd[m - 1][cm]), 0.0)
            for c, Cv in Cs.items():
                Q[c][m] = np.where(nonconst, np.maximum(0.0, D - Cv * d + 0.5 * (Q[c][m - 1][cp] + Q[c][m - 1][cm])), 0.0)
        out = {}
        for m in range(1, 5):
            H, I = tabs[m]["H"], tabs[m]["I"]
            nz = I > 1e-12
            out[f"n={m}"] = {
                "max |E sum D - H| (telescope)": float(np.max(np.abs(SD[m] - H))),
                "max |E sum d - I| (telescope)": float(np.max(np.abs(Sd[m] - I))),
                "upper sandwich violation max(E sum lam - H)": float(np.max(Lam[m] - H)),
                "lower sandwich violation max(H - 3I/ln2 - E sum lam)": float(np.max(H - 3 * I / LN2 - Lam[m])),
                "max (H - E sum lam)/I": float(np.max(np.where(nz, (H - Lam[m]) / np.where(nz, I, 1), -1))),
                "min (H - E sum lam)/I": float(np.min(np.where(nz, (H - Lam[m]) / np.where(nz, I, 1), 99))),
                "Qstar_root/I max": {c: float(np.max(np.where(nz, Q[c][m] / np.where(nz, I, 1), 0))) for c in Cs},
                "Qstar_root/I argmax": {c: int(np.argmax(np.where(nz, Q[c][m] / np.where(nz, I, 1), 0))) for c in Cs},
            }
        report["trees"][rule] = out
        tabs[f"Lam_{rule}"] = Lam
    # spread of E sum lambda across rules (tree dependence), n=4
    r4 = tabs[4]
    nz = r4["I"] > 1e-12
    L = np.stack([tabs[f"Lam_{ru}"][4] for ru in rules], axis=1)
    spread = (L.max(axis=1) - L.min(axis=1))
    report["trees"]["n=4 max over g of (max_rule - min_rule) E sum lam / I"] = float(np.max(np.where(nz, spread / np.where(nz, r4["I"], 1), 0)))
    report["runtime_seconds"] = time.time() - t0
    # save maximizer truth tables for interval certification
    json.dump(report, open(OUT + "/sandwich_all_results.json", "w"), indent=1)
    np.save(OUT + "/n4_ratio.npy", tabs[4]["ratio"])
    np.save(OUT + "/n4_minD.npy", tabs[4]["minD"])
    np.save(OUT + "/n4_minL.npy", tabs[4]["minL"])
    print(json.dumps(report, indent=1))


if __name__ == "__main__":
    main()
