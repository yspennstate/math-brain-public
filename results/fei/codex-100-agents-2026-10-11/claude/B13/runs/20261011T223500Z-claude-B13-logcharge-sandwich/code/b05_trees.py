# claude-B13-sandwich-v1, part 2: the B05 sparse bent point-defect family F_k.
# Coordinates: 0 = selector y, 1..k = data x, k+1..3k = control z. F = G (y=0) or H (y=1),
# G = 1 + A(z)(b(x)-1), H = 1 + A(z)(b'(x)-1), A = 1{z=0}, b quadratic bent, b' = b flipped at x=0.
# Root per-coordinate ledger for k=4,6; complete-tree ledgers for k=4 under several rules.
import json, math, sys, time
import numpy as np

OUT = sys.argv[1]
LN2 = math.log(2.0)


def fwht1(v):
    v = v.astype(np.int64).copy()
    N = v.shape[0]
    h = 1
    while h < N:
        v = v.reshape(N // (2 * h), 2, h)
        a = v[:, 0, :].copy(); b = v[:, 1, :].copy()
        v[:, 0, :] = a + b; v[:, 1, :] = a - b
        v = v.reshape(N)
        h *= 2
    return v


def xlog(p):
    p = np.asarray(p, dtype=float)
    out = np.zeros_like(p)
    m = p > 0
    out[m] = -p[m] * np.log2(p[m])
    return out


def build(k):
    m = 3 * k + 1
    N = 1 << m
    idx = np.arange(N, dtype=np.int64)
    y = idx & 1
    x = (idx >> 1) & ((1 << k) - 1)
    z = idx >> (k + 1)
    xb = [(x >> i) & 1 for i in range(k)]
    q = np.zeros(N, dtype=np.int64)
    for i in range(0, k, 2):
        q ^= xb[i] & xb[i + 1]
    b = 1 - 2 * q
    bp = b.copy()
    bp[x == 0] *= -1
    f = np.where(z != 0, 1, np.where(y == 0, b, bp))
    return f.astype(np.int64), m


def ledger(f, m):
    """Per-coordinate quantities of a +-1 truth table on m variables."""
    N = 1 << m
    W = fwht1(f)
    den = float(N) * N
    p = (W.astype(float) ** 2) / den
    H = float(xlog(p).sum())
    pop = np.array([bin(s).count("1") for s in range(N)]) if N <= 4096 else np.unpackbits(np.arange(N, dtype=np.uint32).view(np.uint8)).reshape(N, 32).sum(1)
    I = float((p * pop).sum())
    per = []
    S = np.arange(N)
    for j in range(m):
        T0 = S[((S >> j) & 1) == 0]
        T1 = T0 | (1 << j)
        a = W[T0].astype(float) / N
        bb = W[T1].astype(float) / N
        d = float((bb * bb).sum())
        if d <= 0:
            per.append(None)
            continue
        Hp = float(xlog((a + bb) ** 2).sum())
        Hm = float(xlog((a - bb) ** 2).sum())
        D = H - 0.5 * (Hp + Hm)
        qv = a * a + bb * bb
        Hq = float(xlog(qv).sum())
        B = H - Hq
        J = Hq - 0.5 * (Hp + Hm)
        msk = bb * bb > 0
        lam = float((bb[msk] ** 2 * np.log2(qv[msk] / bb[msk] ** 2)).sum())
        per.append(dict(d=d, D=D, B=B, J=J, lam=lam))
    return H, I, per


def restrict(f, m, j, val):
    """Restrict coordinate j to bit val; returns truth table on m-1 vars."""
    N = 1 << m
    idx = np.arange(N)
    sel = idx[((idx >> j) & 1) == val]
    return f[sel]


def tree(f0, labels0, rule, Cs, k):
    memo = {}
    stats = {"nodes": 0, "max_local_ratio": 0.0}

    def rec(f, labels):
        key = (labels, f.tobytes())
        if key in memo:
            return memo[key]
        m = len(labels)
        if m == 0 or np.all(f == f[0]):
            res = dict(Lam=0.0, SD=0.0, Sd=0.0, Q={c: 0.0 for c in Cs}, Pos={c: 0.0 for c in Cs}, maxr=0.0)
            memo[key] = res
            return res
        stats["nodes"] += 1
        H, I, per = ledger(f, m)
        rel = [j for j in range(m) if per[j] is not None]
        if rule in ("selector_first", "control_first", "control_selector", "data_first"):
            order = {"selector_first": ["y", "z", "x"], "control_first": ["z", "x", "y"],
                     "control_selector": ["z", "y", "x"], "data_first": ["x", "y", "z"]}[rule]
            def grp(l):
                return "y" if l == 0 else ("x" if l <= k else "z")
            rel.sort(key=lambda j: (order.index(grp(labels[j])), labels[j]))
            j = rel[0]
        elif rule == "greedyD":
            j = min(rel, key=lambda j: (per[j]["D"] / per[j]["d"], labels[j]))
        elif rule == "minInf":
            j = min(rel, key=lambda j: (per[j]["d"], labels[j]))
        elif rule == "maxInf":
            j = min(rel, key=lambda j: (-per[j]["d"], labels[j]))
        else:
            raise ValueError(rule)
        q = per[j]
        nl = labels[:j] + labels[j + 1:]
        c0 = rec(restrict(f, m, j, 0), nl)
        c1 = rec(restrict(f, m, j, 1), nl)
        r = q["D"] / q["d"]
        res = dict(
            Lam=q["lam"] + 0.5 * (c0["Lam"] + c1["Lam"]),
            SD=q["D"] + 0.5 * (c0["SD"] + c1["SD"]),
            Sd=q["d"] + 0.5 * (c0["Sd"] + c1["Sd"]),
            Q={c: max(0.0, q["D"] - Cv * q["d"] + 0.5 * (c0["Q"][c] + c1["Q"][c])) for c, Cv in Cs.items()},
            Pos={c: max(0.0, q["D"] - Cv * q["d"]) + 0.5 * (c0["Pos"][c] + c1["Pos"][c]) for c, Cv in Cs.items()},
            maxr=max(r, c0["maxr"], c1["maxr"]),
            root_choice=labels[j], root_ratio=r,
        )
        memo[key] = res
        return res

    return rec(f0, labels0), stats


def main():
    t0 = time.time()
    rep = {"root": {}, "trees": {}}
    for k in (4, 6):
        f, m = build(k)
        H, I, per = ledger(f, m)
        def grp(l):
            return "y" if l == 0 else ("x" if l <= k else "z")
        byg = {}
        for j, q in enumerate(per):
            g = grp(j)
            if q is None:
                continue
            byg.setdefault(g, []).append((q["D"] / q["d"], q["lam"] / q["d"], q["B"] / q["d"], q["J"] / q["d"], q["d"]))
        rep["root"][f"k={k}"] = {
            "m": m, "H": H, "I": I, "H/I": H / I,
            "selector y": {"D/d": byg["y"][0][0], "lam/d": byg["y"][0][1], "B/d": byg["y"][0][2], "J/d": byg["y"][0][3], "d": byg["y"][0][4], "k+log2e": k + 1 / LN2},
            "data x (max D/d, min D/d)": [max(v[0] for v in byg["x"]), min(v[0] for v in byg["x"])],
            "control z (max D/d, min D/d)": [max(v[0] for v in byg["z"]), min(v[0] for v in byg["z"])],
            "min_i D_i/d_i": min(min(v[0] for v in L) for L in byg.values()),
            "argmin group": min(byg, key=lambda g: min(v[0] for v in byg[g])),
            "sum_i lam_i / I": sum(q["lam"] for q in per if q) / I,
            "sum_i B_i / I": sum(q["B"] for q in per if q) / I,
        }
        print(json.dumps(rep["root"][f"k={k}"]), flush=True)
    k = 4
    f, m = build(k)
    H, I, _ = ledger(f, m)
    Cs = {"4": 4.0, "6.5218": 6.5218, "8": 8.0}
    for rule in ("selector_first", "control_first", "control_selector", "data_first", "greedyD", "minInf", "maxInf"):
        res, st = tree(f, tuple(range(m)), rule, Cs, k)
        rep["trees"][rule] = {
            "root_choice_label": res.get("root_choice"), "root_D/d": res.get("root_ratio"),
            "E sum D - H": res["SD"] - H, "E sum d - I": res["Sd"] - I,
            "(H - E sum lam)/I": (H - res["Lam"]) / I, "sandwich_ok": bool(H - 3 * I / LN2 - 1e-12 <= res["Lam"] <= H + 1e-12),
            "max local D/d on reached nodes": res["maxr"],
            "Qstar_root/I": {c: res["Q"][c] / I for c in Cs},
            "E sum (D - C d)^+ / I": {c: res["Pos"][c] / I for c in Cs},
            "internal nodes (memo distinct)": st["nodes"],
        }
        print(rule, json.dumps(rep["trees"][rule]), flush=True)
    rep["k=4 H"] = H
    rep["k=4 I"] = I
    rep["runtime_seconds"] = time.time() - t0
    json.dump(rep, open(OUT + "/b05_trees_results.json", "w"), indent=1)


if __name__ == "__main__":
    main()
