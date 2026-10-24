# Exhaustive calibration of good-coordinate / erasure constants for all Boolean f on n<=NMAX inputs.
# Float64 screening with an explicit error budget; every comparison inside TOL is re-decided exactly
# from integer coefficient vectors over {1, log2 3, log2 5, ...} (log2 of distinct primes are Q-independent
# together with 1), evaluated at 300 bits when nonzero.
import sys, json, math, time
import numpy as np
import mpmath
mpmath.mp.prec = 300
NMAX = int(sys.argv[1]); OUT = sys.argv[2]
A = 2.0 / math.log(2.0)          # 2/ln2
TOL = 1e-9                        # near-tie band (float error budget is below 1e-11, see REPORT)
PRIMES = [p for p in range(3, 4**NMAX + 2) if all(p % q for q in range(2, int(p**0.5) + 1))]


def vp(k, p):
    e = 0
    while k % p == 0:
        k //= p; e += 1
    return e


def phivec(k):  # k log2 k as (const, {p: coef}) integer data
    if k <= 1:
        return 0, {}
    d = {}
    c = k * vp(k, 2)
    for p in PRIMES:
        if p > k:
            break
        e = vp(k, p)
        if e:
            d[p] = k * e
    return c, d


class V:  # integer linear form const + sum coef_p log2 p
    __slots__ = ("c", "d")

    def __init__(s, c=0, d=None):
        s.c = c; s.d = dict(d or {})

    def add(s, o, w=1):
        s.c += w * o.c
        for p, v in o.d.items():
            s.d[p] = s.d.get(p, 0) + w * v
        return s

    def addphi(s, k, w=1):
        c, d = phivec(int(k)); s.c += w * c
        for p, v in d.items():
            s.d[p] = s.d.get(p, 0) + w * v
        return s

    def sign(s):
        d = {p: v for p, v in s.d.items() if v}
        if s.c == 0 and not d:
            return 0
        val = mpmath.mpf(s.c) + mpmath.fsum(mpmath.mpf(v) * mpmath.log(p, 2) for p, v in d.items())
        bound = (abs(s.c) + sum(abs(v) for v in d.values()) + 1) * mpmath.mpf(2) ** -280
        if abs(val) <= bound:
            raise RuntimeError("undecided sign")
        return 1 if val > 0 else -1

    def text(s, den):
        parts = [str(s.c)] + ["%+d*log2(%d)" % (v, p) for p, v in sorted(s.d.items()) if v]
        return "(" + " ".join(parts) + ")/%d" % den


def popc(x):
    return bin(int(x)).count("1")


def run_n(n):
    N = 1 << n; N2 = N * N; M2 = (N // 2) ** 2
    S = np.arange(N); pc = np.array([popc(s) for s in S])
    Mx = np.array([[(-1) ** popc(s & x) for x in S] for s in S], dtype=np.int64)
    T = np.arange(1 << N, dtype=np.int64)
    F = 1 - 2 * ((T[:, None] >> S[None, :]) & 1)            # f(x) = 1-2*bit_x(t)
    W = F @ Mx.T                                            # Walsh sums, integer
    c = W * W
    phi = np.array([0.0] + [float(mpmath.mpf(k) * mpmath.log(k, 2)) for k in range(1, N2 + 1)])
    H = 2 * n - phi[c].sum(1) / N2
    I = (c * pc).sum(1) / N2
    nc = I > 0
    shape = (len(T), n)
    Inf = np.zeros(shape); B = np.zeros(shape); Dl = np.zeros(shape)
    Hp = np.zeros(shape); Hm = np.zeros(shape); Ip = np.zeros(shape); Im = np.zeros(shape)
    for i in range(n):
        bit = 1 << i; lo = S[(S & bit) == 0]; hi = lo | bit
        a = c[:, lo]; b = c[:, hi]
        Inf[:, i] = b.sum(1) / N2
        B[:, i] = (phi[a + b] - phi[a] - phi[b]).sum(1) / N2
        wp = (W[:, lo] + W[:, hi]) // 2; wm = (W[:, lo] - W[:, hi]) // 2
        cp, cm = wp * wp, wm * wm
        pcl = np.array([popc(t) for t in lo])
        Hp[:, i] = 2 * (n - 1) - phi[cp].sum(1) / M2
        Hm[:, i] = 2 * (n - 1) - phi[cm].sum(1) / M2
        Ip[:, i] = (cp * pcl).sum(1) / M2; Im[:, i] = (cm * pcl).sum(1) / M2
        Dl[:, i] = H - (Hp[:, i] + Hm[:, i]) / 2
    JS = Dl - B
    rel = Inf > 0
    Bt = B.sum(1); DTC = H - Bt
    out = {"n": n, "functions": int(len(T)), "nonconstant": int(nc.sum())}
    Isafe = np.where(nc, I, 1.0)
    r = np.where(nc, H / Isafe, 0.0)

    def exactvecs(t):
        w = W[t]; cc = c[t]
        vH = V(N2 * 2 * n)
        for k in cc:
            vH.addphi(k, -1)
        res = {"H": vH, "I": int((cc * pc).sum()), "Inf": [], "B": [], "D": [], "Hpm": [], "Ipm": []}
        for i in range(n):
            bit = 1 << i; lo = S[(S & bit) == 0]; hi = lo | bit
            pcl = np.array([popc(t2) for t2 in lo])
            vB = V()
            for x, y in zip(cc[lo], cc[hi]):
                vB.addphi(x + y).addphi(x, -1).addphi(y, -1)
            hs = []; is_ = []
            for sg in (1, -1):
                wq = (w[lo] + sg * w[hi]) // 2; cq = wq * wq
                vh = V(M2 * 2 * (n - 1))
                for k in cq:
                    vh.addphi(k, -1)
                hs.append(vh); is_.append(int((cq * pcl).sum()))
            vHbar = V().add(hs[0], 2).add(hs[1], 2)          # = N2*(H_+ + H_-)/2
            vD = V().add(vH).add(vHbar, -1)                   # = N2*Delta_i
            res["Inf"].append(int(cc[hi].sum())); res["B"].append(vB); res["D"].append(vD)
            res["Hpm"].append(hs); res["Ipm"].append(is_)
        return res

    ratioB = np.where(rel, B / np.where(rel, Inf, 1), np.inf)
    ratioD = np.where(rel, Dl / np.where(rel, Inf, 1), np.inf)
    minB = np.where(nc, ratioB.min(1), -np.inf); minD = np.where(nc, ratioD.min(1), -np.inf)
    infmax = Inf.max(1)
    atmax = rel & (Inf >= infmax[:, None] - 1e-15)
    ratio_at_max = np.where(nc, np.where(atmax, ratioB, np.inf).min(1), -np.inf)
    Hpos = H > 1e-12
    stats = {}
    for name, x in [("max_H_over_I", np.where(nc, r, -1)),
                    ("max_B_over_I", np.where(nc, Bt / Isafe, -1)),
                    ("max_DTC_over_I", np.where(nc, DTC / Isafe, -1)),
                    ("max_B_over_H", np.where(Hpos, Bt / np.where(Hpos, H, 1), -1)),
                    ("min_B_over_H_among_H_pos", np.where(Hpos, -Bt / np.where(Hpos, H, 1), -9)),
                    ("G_star_max_f_min_i_Bi_over_Infi", minB),
                    ("D_star_max_f_min_i_Deltai_over_Infi", minD),
                    ("max_f_Bi_over_Infi_at_max_influence_coord", ratio_at_max)]:
        t = int(np.argmax(x)); v = float(x[t])
        stats[name] = {"value": v, "argmax_truth_table_int": t, "count_within_1e-9": int((x >= v - 1e-9).sum())}
    stats["min_B_over_H_among_H_pos"]["value"] *= -1
    t = stats["max_H_over_I"]["argmax_truth_table_int"]; ev = exactvecs(t)
    stats["max_H_over_I"]["exact"] = {"H": ev["H"].text(N2), "I": "%d/%d" % (ev["I"], N2)}
    out["stats"] = stats

    def h2(x):
        xs = np.clip(x, 1e-300, 1 - 1e-16)
        v = -xs * np.log2(xs) - (1 - xs) * np.log2(1 - xs)
        return np.where((x > 0) & (x < 1), v, 0.0)
    chk = {}
    chk["min_(h2(Inf_i)-B_i)"] = float((h2(Inf) - B)[nc].min())
    chk["min_JS_i"] = float(JS[nc].min())
    mn = np.minimum(Inf, 1 - Inf)
    q = np.where(mn > 0, JS / np.where(mn > 0, mn, 1), 0.0)
    chk["max_JS_i_over_min(Inf,1-Inf)"] = float(q.max()); chk["2/ln2"] = A
    chk["max_|JS_i|_where_min(Inf,1-Inf)=0"] = float(np.abs(np.where(mn > 0, 0, JS)).max())
    chk["min_DTC"] = float(DTC.min())
    chk["min_(Inf_i*log2(e/Inf_i)-h2(Inf_i))"] = float(np.where(rel, Inf * np.log2(math.e / np.where(rel, Inf, 1)) - h2(Inf), 0).min())
    out["checks"] = chk

    mrel = rel.sum(1)
    margin = Dl * I[:, None] - H[:, None] * Inf                 # Delta_i*I - H*Inf_i
    near = rel & (np.abs(margin) <= TOL) & nc[:, None]
    exact_calls = 0
    rlm_float = nc & (mrel >= 2) & np.all(~rel | (margin > TOL) | near, axis=1)
    rlm = []
    for t in np.nonzero(rlm_float)[0]:
        ok = True
        if near[t].any():
            ev = exactvecs(int(t)); exact_calls += 1
            for i in np.nonzero(near[t])[0]:
                v = V().add(ev["D"][i], ev["I"]).add(ev["H"], -ev["Inf"][i])
                if v.sign() <= 0:
                    ok = False; break
        if ok:
            rlm.append(int(t))
    rlm = np.array(rlm, dtype=np.int64)
    childmax = np.zeros(len(T))
    for i in range(n):
        for Hx, Ix in ((Hp[:, i], Ip[:, i]), (Hm[:, i], Im[:, i])):
            rr = np.where(Ix > 0, Hx / np.where(Ix > 0, Ix, 1), 0.0)
            childmax = np.where(rel[:, i], np.maximum(childmax, rr), childmax)
    srm_m = r - childmax
    srm_float = nc & (mrel >= 2) & (srm_m > -TOL)
    srm = []
    for t in np.nonzero(srm_float)[0]:
        if srm_m[t] > TOL:
            srm.append(int(t)); continue
        ev = exactvecs(int(t)); exact_calls += 1; ok = True
        for i in range(n):
            if ev["Inf"][i] == 0:
                continue
            for s in (0, 1):
                Ic = ev["Ipm"][i][s]
                if Ic == 0:
                    continue
                v = V().add(ev["H"], Ic).add(ev["Hpm"][i][s], -ev["I"])   # (N2 H)(M2 I_c) - (M2 H_c)(N2 I), common denominator N2*M2
                if v.sign() <= 0:
                    ok = False
        if ok:
            srm.append(int(t))
    srm = np.array(srm, dtype=np.int64)

    def lemma_margins(idx, Cstar):
        if len(idx) == 0:
            return {"count": 0}
        rr = r[idx]; II = I[idx]; m = mrel[idx]
        d = {"count": int(len(idx)),
             "min_(aI-DTC)/I": float(((A * II - DTC[idx]) / II).min()),
             "min_over_f_min_i_(B_i-(r-a)Inf_i)": float(np.where(rel[idx], B[idx] - (rr[:, None] - A) * Inf[idx], np.inf).min(1).min()),
             "min_(e^3*2^-r - max Inf_i)": float((math.e ** 3 * 2.0 ** (-rr) - infmax[idx]).min()),
             "max_r": float(rr.max()), "max_DTC_over_I": float((DTC[idx] / II).max()),
             "min_B_over_H": float((Bt[idx] / H[idx]).min())}
        if Cstar is not None:
            cs = Cstar[idx]
            d["min_over_f_min_i_(Delta_i-C*Inf_i-(r-C*)I)"] = float(np.where(rel[idx], Dl[idx] - cs[:, None] * Inf[idx] - (rr - cs)[:, None] * II[:, None], np.inf).min(1).min())
            d["min_((a-(m-1)(r-C*))I-DTC)"] = float(((A - (m - 1) * (rr - cs)) * II - DTC[idx]).min())
            d["max_(m-1)(r-C*)"] = float(((m - 1) * (rr - cs)).max())
        return d
    out["RLM_every_relevant_i_Delta_gt_r_Inf"] = lemma_margins(rlm, None)
    out["SRM_r_gt_every_restriction_ratio"] = lemma_margins(srm, childmax)
    out["SRM_subset_of_RLM"] = bool(np.isin(srm, rlm).all()) if len(srm) else True
    if len(srm):
        k = int(srm[np.argmax(r[srm])])
        out["SRM_example_max_r"] = {"truth_table_int": k, "r": float(r[k]), "childmax": float(childmax[k]),
                                    "relevant": int(mrel[k]), "influences": [float(x) for x in Inf[k]],
                                    "B_over_H": float(Bt[k] / H[k]), "DTC_over_I": float(DTC[k] / I[k])}
    out["exact_sign_calls"] = exact_calls
    out["near_tie_coordinates_screened"] = int(near.sum())
    out["SRM_near_ties_screened"] = int((srm_float & (srm_m <= TOL)).sum())
    return out


res = []
t0 = time.time()
for n in range(1, NMAX + 1):
    t1 = time.time(); o = run_n(n); o["seconds"] = round(time.time() - t1, 2); res.append(o)
    print(json.dumps({"n": n, "sec": o["seconds"], "maxHI": o["stats"]["max_H_over_I"]["value"],
                      "Gstar": o["stats"]["G_star_max_f_min_i_Bi_over_Infi"]["value"],
                      "RLM": o["RLM_every_relevant_i_Delta_gt_r_Inf"]["count"],
                      "SRM": o["SRM_r_gt_every_restriction_ratio"]["count"], "exact_calls": o["exact_sign_calls"]}), flush=True)
with open(OUT, "w", encoding="utf-8") as fh:
    json.dump({"spec": "claude-B01-exact-v1", "TOL": TOL, "results": res, "total_seconds": round(time.time() - t0, 2)}, fh, indent=1)
