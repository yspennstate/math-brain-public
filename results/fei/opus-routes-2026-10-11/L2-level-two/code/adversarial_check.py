"""Adversarial pass for route L2: a second, independent code path (nothing imported from check_levels.py).

For each function: spectrum by a freshly written Walsh-Hadamard transform, then for every coordinate i and every
U not containing i the edge term phi(p(U), p(U+i)), accumulated per level |U|.  Checked against the theorems:
  Lemma 1      B^(i)_j <= phi(a_{j,i}, d_{j,i}) <= psi(d_{j,i})
  Lemma 2      d_0 <= eps^2, d_1 <= 2 eps^2 ln(2/eps), d_j <= min over q of eps^(2-2/q)(q-1)^j (closed-form q*)
  Theorem 3    B_{k-1} <= b_k I with the certified b_k (data/certify_constants.json)
  Theorem 5    sum_i sum_{j <= c ln(1/eps_i)} B^(i)_j <= C(c) I with the certified C(c)
  identities   B_i = h2(eps_i) - I(S_i; S\\i),  B <= H (chain rule),  sum_j phi(a_j, d_j) = H(S_i | |S\\i|)
Then a hill-climb over truth tables (n = 8) that tries to push B_{k-1}/I and Loc_c/I up towards the constants.
Usage: python adversarial_check.py OUTJSON
"""
import os, sys, json, math, time
os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np

try:
    import ctypes
    from ctypes import wintypes
    _k = ctypes.WinDLL("kernel32", use_last_error=True)
    _k.GetCurrentProcess.restype = wintypes.HANDLE
    _k.SetPriorityClass.argtypes = [wintypes.HANDLE, wintypes.DWORD]
    _k.SetPriorityClass.restype = wintypes.BOOL
    _k.SetPriorityClass(_k.GetCurrentProcess(), 0x4000)
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
CERT = json.load(open(os.path.join(HERE, "..", "data", "certify_constants.json"), encoding="utf-8"))


def spectrum(tt):
    """tt: array of +-1 of length 2^n indexed by x in {0,1}^n (bit k of the index = coordinate k, 1 means -1)."""
    a = np.asarray(tt, dtype=np.float64).copy()
    N = a.size
    h = 1
    while h < N:
        for s in range(0, N, 2 * h):
            x = a[s:s + h].copy()
            y = a[s + h:s + 2 * h].copy()
            a[s:s + h] = x + y
            a[s + h:s + 2 * h] = x - y
        h *= 2
    return (a / N) ** 2


def xlog(x):
    x = np.asarray(x, dtype=float)
    out = np.zeros_like(x)
    m = x > 0
    out[m] = x[m] * np.log2(x[m])
    return out


def phi(x, y):
    return xlog(x + y) - xlog(x) - xlog(y)


def h2(e):
    return -(xlog(np.array([e]))[0] + xlog(np.array([1 - e]))[0])


def analyse(tt):
    p = spectrum(tt)
    N = p.size
    n = N.bit_length() - 1
    idx = np.arange(N)
    pc = np.array([bin(s).count("1") for s in range(N)])
    eps = np.array([p[(idx >> i) & 1 == 1].sum() for i in range(n)])
    I = float((pc * p).sum())
    H = float(-xlog(p).sum())
    B = np.zeros((n, n))
    a = np.zeros((n, n))
    d = np.zeros((n, n))
    for i in range(n):
        U = idx[(idx >> i) & 1 == 0]
        V = U | (1 << i)
        ph = phi(p[U], p[V])
        lv = pc[U]
        for j in range(n):
            m = lv == j
            B[i, j] = ph[m].sum()
            a[i, j] = p[U][m].sum()
            d[i, j] = p[V][m].sum()
    return dict(n=n, p=p, eps=eps, I=I, H=H, B=B, a=a, d=d)


def bonami_ratio(L, j):
    if j == 0:
        return math.exp(-L)
    if L < 2 * j:
        return 1.0
    x = ((L - j) + math.sqrt(L * (L - 2 * j))) / j
    return min(1.0, math.exp(-L * (x - 1) / (x + 1) + j * math.log(x)))


def check(R, tol=1e-10):
    n, eps, B, a, d, I = R["n"], R["eps"], R["B"], R["a"], R["d"], R["I"]
    v = dict(lemma1=0, lemma2=0, thm3=0, thm5=0, ident=0)
    worst = dict(lemma1=0.0, d1=0.0, thm3={}, thm5={})
    for i in range(n):
        e = eps[i]
        if e <= 1e-15:
            continue
        L = math.log(1 / e)
        for j in range(n):
            ph_ad = float(phi(np.array([a[i, j]]), np.array([d[i, j]]))[0])
            ps = d[i, j] * math.log2(math.e / d[i, j]) if d[i, j] > 0 else 0.0
            if B[i, j] > ph_ad + tol or ph_ad > ps + tol:
                v["lemma1"] += 1
            if ps > 1e-12:
                worst["lemma1"] = max(worst["lemma1"], B[i, j] / ps)
            bound = e * bonami_ratio(L, j)
            if j == 0:
                bound = min(bound, e * e)
            if j == 1:
                bound = min(bound, 2 * e * e * math.log(2 / e))
                worst["d1"] = max(worst["d1"], d[i, j] / (2 * e * e * math.log(2 / e)))
            if d[i, j] > bound * (1 + 1e-9) + tol:
                v["lemma2"] += 1
        # identities: sum_j phi(a_j, d_j) = H(S_i | |S\i|) >= B_i, and B_i = h2(eps_i) - I(S_i; S\i) >= 0
        Hc = float(phi(a[i], d[i]).sum())
        if B[i].sum() > Hc + tol or abs(a[i].sum() + d[i].sum() - 1) > 1e-9:
            v["ident"] += 1
    if B.sum() > R["H"] + 1e-9:
        v["ident"] += 1
    if I > 1e-12:
        for k in range(1, min(n, 10) + 1):
            key = "b2" if k == 2 else f"b{k}"
            if k == 1:
                bk = 2 / (math.sqrt(math.e) * math.log(2))
            else:
                bk = CERT[key]["certified_upper_bound"]
            r = B[:, k - 1].sum() / I
            worst["thm3"][k] = r
            if r > bk + 1e-9:
                v["thm3"] += 1
        for c in ("0.2", "0.3", "0.4", "0.45"):
            cf = float(c)
            tot = 0.0
            for i in range(n):
                if eps[i] <= 1e-15:
                    continue
                J = math.floor(cf * math.log(1 / eps[i]) + 1e-12)
                tot += B[i, :J + 1].sum()
            r = tot / I
            worst["thm5"][c] = r
            if r > CERT[f"C({c})"]["certified_upper_bound"] + 1e-9:
                v["thm5"] += 1
    return v, worst


def tt_from(fn, n):
    return np.array([fn([(x >> k) & 1 for k in range(n)]) for x in range(1 << n)], dtype=np.int8)


def tribes(w, s):
    return tt_from(lambda b: -1 if any(all(b[t * w + u] for u in range(w)) for t in range(s)) else 1, w * s)


def majority(n):
    return tt_from(lambda b: -1 if sum(b) > n // 2 else 1, n)


def threshold(n, t):
    return tt_from(lambda b: -1 if sum(b) >= t else 1, n)


def bent_x0(m):
    n = 2 * m + 1
    return tt_from(lambda b: (1 - 2 * (sum(b[1 + k] * b[1 + m + k] for k in range(m)) % 2)) * (1 - 2 * b[0]), n)


def address(k):
    n = k + (1 << k)
    return tt_from(lambda b: 1 - 2 * b[k + sum(b[t] << t for t in range(k))], n)


def hamming_ball(n, r):
    return tt_from(lambda b: -1 if sum(b) <= r else 1, n)


def random_dt(n, depth, rng):
    def build(dd, used):
        if dd == 0 or rng.random() < 0.15:
            return int(rng.choice([-1, 1]))
        var = int(rng.choice([v for v in range(n) if v not in used]))
        return (var, build(dd - 1, used | {var}), build(dd - 1, used | {var}))

    tree = build(depth, frozenset())

    def ev(t, b):
        while isinstance(t, tuple):
            t = t[2] if b[t[0]] else t[1]
        return t
    return tt_from(lambda b: ev(tree, b), n)


def objective(tt, kind):
    R = analyse(tt)
    if R["I"] < 1e-12:
        return 0.0
    B, eps, I = R["B"], R["eps"], R["I"]
    if kind[0] == "level":
        return B[:, kind[1]].sum() / I
    cf = kind[1]
    tot = 0.0
    for i in range(R["n"]):
        if eps[i] > 1e-15:
            tot += B[i, :math.floor(cf * math.log(1 / eps[i]) + 1e-12) + 1].sum()
    return tot / I


def hill_climb(kind, n, rng, starts=6, steps=1500):
    best_all = (0.0, None)
    for _ in range(starts):
        dens = rng.choice([0.5, 0.2, 0.05])
        tt = np.where(rng.random(1 << n) < dens, -1, 1).astype(np.int8)
        cur = objective(tt, kind)
        for _ in range(steps):
            k = int(rng.integers(0, 1 << n))
            tt[k] = -tt[k]
            v = objective(tt, kind)
            if v >= cur:
                cur = v
            else:
                tt[k] = -tt[k]
        if cur > best_all[0]:
            best_all = (cur, "".join("1" if x < 0 else "0" for x in tt))
    return best_all


def main():
    out = dict(started=time.strftime("%Y-%m-%d %H:%M:%S"))
    rng = np.random.default_rng(20261012)
    fams = []
    for (w, s) in ((2, 3), (3, 3), (2, 5), (3, 4), (4, 3), (2, 6)):
        fams.append((f"tribes({w},{s})", tribes(w, s)))
    for n in (5, 7, 9, 11):
        fams.append((f"maj{n}", majority(n)))
    for n in (8, 11):
        for t in (1, 2, n // 3, n // 2):
            fams.append((f"thr{n},{t}", threshold(n, t)))
    for m in (2, 3, 4, 5):
        fams.append((f"bent{2 * m}*x0", bent_x0(m)))
    for k in (2, 3):
        fams.append((f"address{k}", address(k)))
    for (n, r) in ((11, 1), (11, 2), (12, 3)):
        fams.append((f"ball{n},{r}", hamming_ball(n, r)))
    for t in range(40):
        fams.append((f"dt12_{t}", random_dt(12, 6, rng)))
    for t in range(40):
        fams.append((f"rand10_{t}", np.where(rng.random(1024) < rng.choice([0.5, 0.1, 0.02]), -1, 1).astype(np.int8)))
    tot = dict(lemma1=0, lemma2=0, thm3=0, thm5=0, ident=0)
    worst_l1 = (0.0, None)
    worst_d1 = (0.0, None)
    worst3 = {}
    worst5 = {}
    tribes_rows = []
    for name, tt in fams:
        R = analyse(tt)
        v, w = check(R)
        for k2 in tot:
            tot[k2] += v[k2]
        if w["lemma1"] > worst_l1[0]:
            worst_l1 = (w["lemma1"], name)
        if w["d1"] > worst_d1[0]:
            worst_d1 = (w["d1"], name)
        for k, r in w["thm3"].items():
            if r > worst3.get(k, (0, None))[0]:
                worst3[k] = (r, name)
        for c, r in w["thm5"].items():
            if r > worst5.get(c, (0, None))[0]:
                worst5[c] = (r, name)
        if name.startswith("tribes"):
            Hc = sum(float(phi(R["a"][i], R["d"][i]).sum()) for i in range(R["n"]))
            h2s = sum(h2(e) for e in R["eps"])
            tribes_rows.append(dict(name=name, n=R["n"], I=R["I"], eps=float(R["eps"][0]), B_over_I=float(R["B"].sum() / R["I"]),
                                    H_over_I=R["H"] / R["I"], Hcond_level_sum_over_I=Hc / R["I"], h2_sum_over_I=h2s / R["I"]))
    out.update(functions=len(fams), violations=tot, lemma1_max_ratio=worst_l1, d1_over_entropy_bound_max=worst_d1,
               thm3_max_ratio={str(k): v for k, v in sorted(worst3.items())},
               thm5_max_ratio=worst5, tribes=tribes_rows)
    print("functions", len(fams), "violations", tot, flush=True)
    print("Lemma 1 max B/psi", worst_l1, " d1/(2eps^2 ln(2/eps)) max", worst_d1, flush=True)
    print("Thm 3 max B_{k-1}/I", {k: round(v[0], 4) for k, v in sorted(worst3.items())}, flush=True)
    print("Thm 5 max Loc/I", {c: round(v[0], 4) for c, v in worst5.items()}, flush=True)
    for r in tribes_rows:
        print(" ", r["name"], "Hcond/I", round(r["Hcond_level_sum_over_I"], 6), "h2/I", round(r["h2_sum_over_I"], 6), "B/I", round(r["B_over_I"], 4))
    hc = {}
    for kind in (("level", 0), ("level", 1), ("level", 2), ("loc", 0.3), ("loc", 0.4)):
        val, tts = hill_climb(kind, 8, rng)
        hc[f"{kind[0]}_{kind[1]}"] = dict(best=val, tt=tts)
        print("hill-climb", kind, round(val, 5), flush=True)
    out["hill_climb_n8"] = hc
    out["finished"] = time.strftime("%Y-%m-%d %H:%M:%S")
    json.dump(out, open(sys.argv[1], "w", encoding="utf-8"), indent=1)


if __name__ == "__main__":
    main()
