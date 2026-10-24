"""Read-once formulas: the conditional entropy B_i in closed form, the level statistic, and fixed-height witnesses.

Spectral sample of a read-once formula (composition with independent inputs): at a gate v with child means mu_j, the
mu-biased law P_v(J) = gtilde_v(J)^2 picks the set J of active children (normalized by 1 - P_v(empty) below the root); each
active child recurses into its own normalized sample.  For a leaf i with ancestors v_0 (root), ..., v_{d-1} and path
children c_t = v_{t+1}: alpha_t = Pr(v_t active), rho_{>t} = prod_{t<t'<d} P_{t'}({c_{t'}}).  Lemma R: with tau the deepest
path node whose subtree meets S - i and A the set of its off-path children that meet S,
  B_i = H(S_i | S - i) = H(S_i | tau, A) = phi(mu^2, fhat(i)^2) + sum_t alpha_t sum_{A != empty} phi(P_t(A), P_t(A + c_t) rho_{>t}).
The height-s witness W = S cap (sub(v_s) - i) sees tau and A only when tau >= s:
  H(S_i | W) = sum_{t >= s} alpha_t sum_A phi(...) + phi(Z_s, y_s),  Z_s = Pr(S cap sub(v_s) = empty), y_s = Pr(S cap sub(v_s) = {i}).
The level statistic H(S_i | |S - i|) comes from generating functions along the path.  Small trees are checked against a
brute-force Walsh transform of the truth table.  Usage: python readonce_witness.py OUTJSON
"""
import sys, json, math, itertools
import numpy as np

LOG2 = math.log(2)


def phi(x, y):
    if x <= 0 or y <= 0:
        return 0.0
    return (x * math.log1p(y / x) + y * math.log1p(x / y)) / LOG2


def AND(k):  # -1 = true
    g = lambda ys: -1 if all(y == -1 for y in ys) else 1
    g.kind = "AND"
    return g


def OR(k):
    g = lambda ys: -1 if any(y == -1 for y in ys) else 1
    g.kind = "OR"
    return g


def and_or_law(kind, qs, qbs):
    """Closed form for AND/OR with independent children, q_j = Pr(child true), qb_j = Pr(child false), both carried
    accurately.  AND: gtilde(J)^2 = 4 q^2 prod_{j in J} qb_j / q_j; OR: 4 qb^2 prod_{j in J} q_j / qb_j (J nonempty);
    gtilde(empty)^2 = (qb - q)^2 and the nonempty masks sum to 4 q qb."""
    k = len(qs)
    if kind == "AND":
        q = math.prod(qs)
        qb = 1 - q if q < 0.5 else -math.expm1(sum(math.log1p(-x) for x in qbs))
        base, r = 4 * q * q, [qbs[j] / qs[j] for j in range(k)]
    else:
        qb = math.prod(qbs)
        q = 1 - qb if qb < 0.5 else -math.expm1(sum(math.log1p(-x) for x in qs))
        base, r = 4 * qb * qb, [qs[j] / qbs[j] for j in range(k)]
    law = {0: (qb - q) ** 2}
    for mask in range(1, 1 << k):
        P = base
        for j in range(k):
            if mask >> j & 1:
                P *= r[j]
        law[mask] = P
    return q, qb, law


def gate_law(g, k, mus):
    """mu-biased spectral law of g: {+-1}^k -> {+-1} with independent inputs of means mus. Returns (mean, {mask: P})."""
    sig = [math.sqrt(max(1 - m * m, 0.0)) for m in mus]
    coef = {}
    mean = 0.0
    for ys in itertools.product((1, -1), repeat=k):
        pr = 1.0
        for y, m in zip(ys, mus):
            pr *= (1 + y * m) / 2
        gv = g(ys)
        mean += pr * gv
        for mask in range(1 << k):
            v = gv * pr
            for j in range(k):
                if mask >> j & 1:
                    v *= (ys[j] - mus[j]) / sig[j]
            coef[mask] = coef.get(mask, 0.0) + v
    return mean, {m: c * c for m, c in coef.items()}


class Node:
    def __init__(self, gate=None, children=(), var=None):
        self.gate, self.children, self.var = gate, list(children), var


def build_alt(depth, fan, top="AND", start=0):
    """Alternating AND/OR tree, fan-in fan[h] at height h (list indexed from the leaves)."""
    if depth == 0:
        return Node(var=start), start + 1
    kids, nxt = [], start
    for _ in range(fan[depth - 1]):
        c, nxt = build_alt(depth - 1, fan, "OR" if top == "AND" else "AND", nxt)
        kids.append(c)
    k = len(kids)
    return Node(gate=(AND(k) if top == "AND" else OR(k)), children=kids), nxt


def build_shared(depth, fan, top="AND", plain=False):
    """Same tree as build_alt with every node's children one shared object (valid for symmetric trees only).
    plain=True hides the gate kind, so annotate uses the generic 2^k expansion instead of the closed form."""
    v = Node(var=0)
    typ = top if depth % 2 == 0 else ("OR" if top == "AND" else "AND")  # type at height 1
    for h in range(1, depth + 1):
        t_h = top if (depth - h) % 2 == 0 else ("OR" if top == "AND" else "AND")
        k = fan[h - 1]
        g = AND(k) if t_h == "AND" else OR(k)
        if plain:
            g = (lambda gg: (lambda ys: gg(ys)))(g)
        v = Node(gate=g, children=[v] * k)
    return v


def mp_path(depth, fan, top):
    """Path laws of the symmetric tree from the generic expansion g~(J) = E g(y) prod (y_j - mu_j)/sigma_j in mpmath
    (80 digits); returned as float objects with the attributes leaf_quantities reads (Plaw, norm)."""
    import mpmath as mpm
    from types import SimpleNamespace
    mpm.mp.dps = 80
    mean, levels = mpm.mpf(0), []
    for h in range(1, depth + 1):
        t_h = top if (depth - h) % 2 == 0 else ("OR" if top == "AND" else "AND")
        k = fan[h - 1]
        g = AND(k) if t_h == "AND" else OR(k)
        sig = mpm.sqrt(1 - mean * mean)
        coef, mnew = {}, mpm.mpf(0)
        for ys in itertools.product((1, -1), repeat=k):
            pr = mpm.mpf(1)
            for y in ys:
                pr *= (1 + y * mean) / 2
            gv = g(ys)
            mnew += pr * gv
            for mask in range(1 << k):
                v = gv * pr
                for j in range(k):
                    if mask >> j & 1:
                        v *= (ys[j] - mean) / sig
                coef[mask] = coef.get(mask, 0) + v
        law = {m: c * c for m, c in coef.items()}
        levels.append(SimpleNamespace(Plaw={m: float(P) for m, P in law.items()}, norm=float(1 - law[0])))
        mean = mnew
    return [(lv, 0) for lv in reversed(levels)]


def annotate(v, want_Q=True):
    """mean, normalized law, count generating function Q (given active), subtree entropy (bits) given active.
    Shared subtrees (symmetric trees) are annotated once."""
    if hasattr(v, "mean"):
        return
    if v.var is not None:
        v.mean, v.q, v.qb, v.Q, v.Hs, v.leaves = 0.0, 0.5, 0.5, np.array([0.0, 1.0]), 0.0, [v.var]
        return
    for c in v.children:
        annotate(c, want_Q)
    k = len(v.children)
    kind = getattr(v.gate, "kind", None)
    if kind in ("AND", "OR"):
        v.q, v.qb, v.Plaw = and_or_law(kind, [c.q for c in v.children], [c.qb for c in v.children])
        v.mean, v.norm = v.qb - v.q, 4 * v.q * v.qb
    else:
        v.mean, v.Plaw = gate_law(v.gate, k, [c.mean for c in v.children])
        v.q, v.qb = (1 - v.mean) / 2, (1 + v.mean) / 2
        v.norm = 1 - v.Plaw.get(0, 0.0)
    v.leaves = [x for c in v.children for x in c.leaves] if want_Q else []
    Q = np.zeros(1)
    Hs = 0.0
    for mask, P in v.Plaw.items():
        if mask == 0 or P <= 0:
            continue
        Pn = P / v.norm
        poly = np.array([1.0])
        for j in range(k):
            if mask >> j & 1:
                if want_Q:
                    poly = np.convolve(poly, v.children[j].Q)
                Hs += Pn * v.children[j].Hs
        if len(poly) > len(Q):
            Q = np.pad(Q, (0, len(poly) - len(Q)))
        Q[:len(poly)] += Pn * poly
        Hs += -Pn * math.log2(Pn)
    v.Q, v.Hs = Q, Hs


def root_entropy(r):
    """H(f) in bits: root law unnormalized (includes S = empty)."""
    H = 0.0
    for mask, P in r.Plaw.items():
        if P <= 0:
            continue
        if mask == 0:  # P = mean^2 = 1 - norm; written so that a near-constant root keeps its (1 - P) log e
            H += -(1 - r.norm) * math.log1p(-r.norm) / LOG2
            continue
        H += -P * math.log2(P)
        for j in range(len(r.children)):
            if mask >> j & 1:
                H += P * r.children[j].Hs
    return H


def path_to(r, i):
    path, v = [], r
    while v.var is None:
        for j, c in enumerate(v.children):
            if i in c.leaves:
                path.append((v, j))
                v = c
                break
    return path


def leaf_quantities(r, i, path=None, want_lev=True):
    if path is None:
        path = path_to(r, i)
    d = len(path)
    law = []  # per depth: dict mask -> probability given the node active (root: unnormalized)
    for t, (v, j) in enumerate(path):
        law.append({m: (P if t == 0 else P / v.norm) for m, P in v.Plaw.items() if t == 0 or m != 0})
    single = [law[t].get(1 << path[t][1], 0.0) for t in range(d)]
    sel = [sum(P for m, P in law[t].items() if m >> path[t][1] & 1) for t in range(d)]
    alpha = [1.0]
    for t in range(d):
        alpha.append(alpha[-1] * sel[t])
    eps = alpha[d]
    rho_gt = [1.0] * (d + 1)
    for t in range(d - 1, -1, -1):
        rho_gt[t] = rho_gt[t + 1] * (single[t + 1] if t + 1 < d else 1.0)  # rho_{>t} = prod_{t<t'<d} single[t']
    mu2 = law[0].get(0, 0.0)
    fi2 = math.prod(single)
    term = []
    for t, (v, j) in enumerate(path):
        c = 1 << j
        s = 0.0
        for m, P in law[t].items():
            if m & c or m == 0:
                continue
            s += phi(P, law[t].get(m | c, 0.0) * rho_gt[t])
        term.append(alpha[t] * s)
    B = phi(mu2, fi2) + sum(term)
    wit = {}
    for s_ in range(d):  # witness at the path node v_s (s_ = 0: root, gives B)
        y = alpha[s_] * math.prod(single[s_:])
        Z = mu2 if s_ == 0 else 1 - alpha[s_]
        wit[d - s_] = sum(term[s_:]) + phi(Z, y)  # keyed by height above the leaf
    if not want_lev:
        return dict(depth=d, eps=eps, B=B, Hlev=None, wit=wit, fi2=fi2, mu2=mu2)
    # level statistic: X(z) = E z^{|S-i|} 1{i in S}, Y(z) = E z^{|S-i|} 1{i notin S}
    X, Y = np.array([1.0]), np.array([0.0])
    for t in range(d - 1, -1, -1):
        v, j = path[t]
        k = len(v.children)
        nX, nY = np.zeros(1), np.zeros(1)
        for m, P in law[t].items():
            if P <= 0:
                continue
            poly = np.array([1.0])
            for jj in range(k):
                if jj != j and m >> jj & 1:
                    poly = np.convolve(poly, v.children[jj].Q)
            if m >> j & 1:
                ax, ay = P * np.convolve(poly, X), P * np.convolve(poly, Y)
            else:
                ax, ay = np.zeros(1), P * poly
            L = max(len(nX), len(ax), len(nY), len(ay))
            nX, nY, ax, ay = [np.pad(a, (0, L - len(a))) for a in (nX, nY, ax, ay)]
            nX, nY = nX + ax, nY + ay
        X, Y = nX, nY
    L = max(len(X), len(Y))
    X, Y = np.pad(X, (0, L - len(X))), np.pad(Y, (0, L - len(Y)))
    Hlev = sum(phi(float(a), float(b)) for a, b in zip(Y, X))
    return dict(depth=d, eps=eps, B=B, Hlev=Hlev, wit=wit, mass_X=float(X.sum()), mass_Y=float(Y.sum()), fi2=fi2, mu2=mu2)


def truth_table(r, n):
    def ev(v, x):
        if v.var is not None:
            return x[v.var]
        return v.gate(tuple(ev(c, x) for c in v.children))
    T = np.empty(1 << n)
    for idx in range(1 << n):
        x = [(-1 if idx >> b & 1 else 1) for b in range(n)]
        T[idx] = ev(r, x)
    return T


def walsh(T):
    a = T.astype(float).copy()
    h = 1
    while h < len(a):
        for s in range(0, len(a), 2 * h):
            u, w = a[s:s + h].copy(), a[s + h:s + 2 * h].copy()
            a[s:s + h], a[s + h:s + 2 * h] = u + w, u - w
        h *= 2
    return a / len(a)


def brute(r, n):
    p = walsh(truth_table(r, n)) ** 2
    idx = np.arange(1 << n)
    pc = np.array([bin(s).count("1") for s in range(1 << n)])
    out = {}
    for i in range(n):
        lo = idx[(idx >> i & 1) == 0]
        B = sum(phi(p[u], p[u | (1 << i)]) for u in lo)
        Hl = 0.0
        for m in range(n):
            sel = lo[pc[lo] == m]
            Hl += phi(float(p[sel].sum()), float(p[sel | (1 << i)].sum()))
        wit = {}
        for v, j in path_to(r, i):
            mask = sum(1 << x for x in v.leaves if x != i)
            Wv = idx & mask
            h = 0.0
            for wv in np.unique(Wv[lo]):
                s0 = lo[Wv[lo] == wv]
                h += phi(float(p[s0].sum()), float(p[s0 | (1 << i)].sum()))
            wit[v] = h
        out[i] = dict(B=B, Hlev=Hl, eps=float(p[(idx >> i & 1) == 1].sum()), wit=wit)
    H = -sum(x * math.log2(x) for x in p if x > 1e-300)
    return out, H


def main():
    res = dict(check=[], families={})
    # brute-force checks on small trees (all leaves)
    small = [("and2_or2_d2", [2, 2], "AND", 2), ("and2_or2_d3", [2, 2, 2], "AND", 3), ("or2_and2_d3", [2, 2, 2], "OR", 3),
             ("and2_or2_d4", [2, 2, 2, 2], "AND", 4), ("and3_or2_d2", [3, 2], "OR", 2), ("tribes_3x3", [3, 3], "OR", 2),
             ("mix_2_3_2", [2, 3, 2], "AND", 3)]
    for name, fan, top, d in small:
        r, n = build_alt(d, fan, top)
        annotate(r)
        bf, Hb = brute(r, n)
        worst = 0.0
        for i in range(n):
            q = leaf_quantities(r, i)
            b = bf[i]
            worst = max(worst, abs(q["B"] - b["B"]), abs(q["Hlev"] - b["Hlev"]), abs(q["eps"] - b["eps"]))
            for (v, j), h in zip(path_to(r, i), sorted(q["wit"].items(), key=lambda kv: -kv[0])):
                worst = max(worst, abs(h[1] - b["wit"][v]))
        Hc = root_entropy(r)
        res["check"].append(dict(name=name, n=n, max_abs_diff=worst, H_formula=Hc, H_brute=Hb))
        print(f"check {name:14s} n={n:3d}  max|formula - brute| = {worst:.2e}   H {Hc:.10f} vs {Hb:.10f}", flush=True)
    # families (symmetric trees: one leaf stands for all); shared trees agree with build_alt on small depths (checked)
    fams = [("AND/OR fan-in 2, AND on top", lambda d: ([2] * d, "AND")),
            ("AND/OR fan-in 2, OR on top", lambda d: ([2] * d, "OR")),
            ("AND2/OR3 (OR gates fan-in 3), OR on top", lambda d: ([3 if (d - hp) % 2 == 0 else 2 for hp in range(1, d + 1)], "OR"))]
    for fname, mk in fams:
        rows = []
        for d in range(1, 41):
            fan, top = mk(d)
            n = math.prod(fan)
            want_lev = n <= 70000
            r = build_shared(d, fan, top)
            annotate(r, want_Q=want_lev)
            path, v = [], r
            while v.var is None:
                path.append((v, 0))
                v = v.children[0]
            if min(min(u.q, u.qb) for u, _ in path) < 1e-200:  # the next depths underflow
                print(f"{fname[:24]:24s} stop at d={d}: a gate is constant to 1e-200", flush=True)
                break
            q = leaf_quantities(r, 0, path=path, want_lev=want_lev)
            if d <= 14:  # closed-form float laws against the generic 2^k expansion in 80-digit arithmetic (second path)
                path3 = mp_path(d, fan, top)
                q3 = leaf_quantities(None, 0, path=path3, want_lev=False)
                dB = abs(q3["B"] - q["B"]) / q["eps"]
                dW = max(abs(q3["wit"][h] - q["wit"][h]) / q["eps"] for h in q["wit"])
                res.setdefault("second_path", []).append(dict(family=fname, depth=d, max_rel_diff_B=dB, max_rel_diff_wit=dW,
                                                              rel_diff_eps=abs(q3["eps"] - q["eps"]) / q["eps"]))
                assert dB < 1e-8 and dW < 1e-8, (fname, d, dB, dW)
            if d <= 4:  # shared tree against the explicit tree
                r2, _ = build_alt(d, fan, top)
                annotate(r2)
                q2 = leaf_quantities(r2, 0)
                assert abs(q2["B"] - q["B"]) < 1e-12 and abs(q2["eps"] - q["eps"]) < 1e-15, (fname, d)
            if not q["eps"] > 1e-250:
                print(f"{fname[:24]:24s} stop at d={d}: eps below 1e-250", flush=True)
                break
            I = n * q["eps"]
            H = root_entropy(r)
            row = dict(depth=d, n=n, eps=q["eps"], H_over_I=H / I, B_over_I=n * q["B"] / I,
                       Hlev_over_I=(n * q["Hlev"] / I if q["Hlev"] is not None else None),
                       log2_inv_eps=math.log2(1 / q["eps"]),
                       witness_over_I={h: n * w / I for h, w in sorted(q["wit"].items())})
            rows.append(row)
            ws = " ".join(f"{h}:{row['witness_over_I'][h]:.3f}" for h in sorted(row["witness_over_I"])[:5])
            hl = "%.4f" % row["Hlev_over_I"] if row["Hlev_over_I"] is not None else "   -  "
            print(f"{fname[:24]:24s} d={d:2d} log2(1/eps)={row['log2_inv_eps']:6.2f}  H/I={row['H_over_I']:.4f}  "
                  f"B/I={row['B_over_I']:.4f}  Hlev/I={hl}  witness h:cost/I {ws}", flush=True)
        res["families"][fname] = rows
    json.dump(res, open(sys.argv[1], "w", encoding="utf-8"), indent=1)


if __name__ == "__main__":
    main()
