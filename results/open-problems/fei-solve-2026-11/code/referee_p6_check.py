"""Independent check of P6 ('Erasure entropies of sparse linear DNFs'), written from the paper's statements only.

For each linear DNF and each coordinate i in d >= 1 terms it computes, by exact Walsh-Hadamard transforms:
  E_i, Inf_i = delta, A = E N, the sums in Lemmas A, h, N and the bound of Theorem lin for every k in 1..L.
Convention: chi_S(x) = (-1)^{sum_{j in S} x_j}, f = 1 - 2F, fhat(S) = E[f chi_S].
Also: the AND formula of the introduction, the star table, and the m x m rows-and-columns ratios.
"""
import itertools, math, random, sys
import numpy as np

LOG2E = 1.0 / math.log(2)


def wht(v):
    a = np.asarray(v, dtype=float).copy()
    n = a.size
    h = 1
    while h < n:
        a = a.reshape(-1, 2, h)
        a = np.stack([a[:, 0] + a[:, 1], a[:, 0] - a[:, 1]], axis=1).reshape(-1)
        h *= 2
    return a / n


def eta(x):
    x = np.asarray(x, dtype=float)
    out = np.zeros_like(x)
    m = x > 0
    out[m] = -x[m] * np.log2(x[m])
    return out


def Phi(a, b):
    return eta(a) + eta(b) - eta(a + b)


def popcount(arr):
    arr = arr.astype(np.uint64)
    c = np.zeros(arr.shape, dtype=np.int64)
    while arr.any():
        c += (arr & np.uint64(1)).astype(np.int64)
        arr = arr >> np.uint64(1)
    return c


def term_values(terms, n):
    x = np.arange(1 << n, dtype=np.int64)
    vals = []
    for t in terms:
        m = sum(1 << j for j in t)
        vals.append((x & m) == m)
    return vals


def analyse(terms, n, coords=None, ks=None):
    terms = [tuple(sorted(t)) for t in terms]
    w = len(terms[0]); L = w - 1; a = 2.0 ** -L
    assert all(len(t) == w for t in terms)
    for s, u in itertools.combinations(terms, 2):
        assert len(set(s) & set(u)) <= 1, "not linear"
    D = max(sum(j in t for t in terms) for j in range(n))
    tv = term_values(terms, n)
    F = np.zeros(1 << n, dtype=bool)
    for v in tv:
        F |= v
    f = 1.0 - 2.0 * F
    fh = wht(f)
    wt = fh ** 2
    S = np.arange(1 << n, dtype=np.int64)
    rows = []
    for i in (coords if coords is not None else range(n)):
        through = [t for t in terms if i in t]
        d = len(through)
        if d == 0:
            continue
        lo = S[(S >> i) & 1 == 0]
        p, q = wt[lo], wt[lo | (1 << i)]
        E = float(Phi(p, q).sum()); delta = float(q.sum())
        bg = np.zeros(1 << n, dtype=bool)
        for t, v in zip(terms, tv):
            if i not in t:
                bg |= v
        Nf = (~bg).astype(float)
        A = float(Nf.mean())
        Nh = wht(Nf)[lo]
        # pivotal indicator h = N * OR_s A_s; A_s = all mates of t_s equal 1
        mates = [[j for j in t if j != i] for t in through]
        anyA = np.zeros(1 << n, dtype=bool)
        for ms in mates:
            m = sum(1 << j for j in ms)
            anyA |= (S & m) == m
        hfun = Nf * anyA
        hh = wht(hfun)[lo]
        # sanity: hhat equals fhat(T + i) and hhat(empty) = delta
        assert np.allclose(hh, fh[lo | (1 << i)], atol=1e-12), "hhat != fhat(T+i)"
        assert abs(hh[0] - delta) < 1e-12
        # g-hat = 2 Nhat - hhat off the empty set
        assert np.allclose(fh[lo][1:], 2 * Nh[1:] - hh[1:], atol=1e-12)
        theta = 1 - L * (D - 1) * a - (d - 1) * a / 2
        lemA_lo, lemA_hi = d * a * theta * A, d * a * A
        cnt = np.stack([popcount(lo & sum(1 << j for j in ms)) for ms in mates])  # mates of each t_s in T
        mx = cnt.max(axis=0)
        for k in (ks if ks is not None else range(1, L + 1)):
            inO = mx >= k
            off_h = float((hh[~inO] ** 2).sum())
            on_N = float((Nh[inO] ** 2).sum())
            gam = a * sum(math.comb(L, j) for j in range(k))
            eps = min(1.0, d * gam)
            ok_h = off_h <= eps * delta + 1e-15
            if k * (D - 1) * a < 2:
                alpha = math.comb(L, k) * 2.0 ** (math.comb(k, 2) - 2 * k) * ((D - 1) * a) ** k / (1 - k * (D - 1) * a / 2)
                ok_N = on_N <= d * alpha * A + 1e-15
            else:
                alpha, ok_N = None, None
            thm = None
            if theta > 0 and alpha is not None and d * a <= 0.25:
                kap = alpha / (a * theta)
                da = d * a
                thm = 2 * eps + 8 * LOG2E * math.sqrt(kap) + eps * math.log2(math.e * (3 + 8 / (eps * da * theta))) \
                    + da * math.log2(math.e * (1 + da ** -2))
            # Proposition 2 itself, with the measured eps' = off_h/delta and kappa' = on_N/delta
            ep, kp = max(off_h / delta, 1e-300), on_N / delta
            varN = A - A * A
            pl = 2 - 2 * ep - 8 * LOG2E * math.sqrt(kp)
            pu = 2 + 8 * LOG2E * math.sqrt(kp) + ep * math.log2(math.e * (3 + 8 * varN / (ep * delta))) \
                + delta * math.log2(math.e * (1 + delta ** -2))
            rows.append(dict(i=i, d=d, k=k, E=E, delta=delta, ratio=E / delta, A=A, D=D, L=L,
                             lemA=(lemA_lo <= delta + 1e-15 and delta <= lemA_hi + 1e-15),
                             lemh=ok_h, lemN=ok_N, thm=thm,
                             thm_ok=(None if thm is None else abs(E / delta - 2) <= thm + 1e-12),
                             prop=(pl - 1e-12 <= E / delta <= pu + 1e-12) if ep <= 1 else None))
    return rows


def star(D, w):
    n = 1 + D * (w - 1)
    terms, nxt = [], 1
    for _ in range(D):
        terms.append([0] + list(range(nxt, nxt + w - 1))); nxt += w - 1
    return terms, n


def grid(m):
    rows = [[r * m + c for c in range(m)] for r in range(m)]
    cols = [[r * m + c for r in range(m)] for c in range(m)]
    return rows + cols, m * m


def random_linear(n, w, D, nterms, rng):
    terms = []
    deg = [0] * n
    tries = 0
    while len(terms) < nterms and tries < 20000:
        tries += 1
        t = rng.sample(range(n), w)
        if any(deg[j] >= D for j in t):
            continue
        if any(len(set(t) & set(u)) > 1 for u in terms):
            continue
        terms.append(t)
        for j in t:
            deg[j] += 1
    return terms


def main():
    # 1. AND of k+1 variables: formula vs exact, and the 2^-k (2k+2) claim
    print("AND formula: E/Inf = 2(1-2^-k) + 2^k Phi((1-2^-k)^2, 4^-k)")
    for k in range(1, 12):
        n = k + 1
        r = analyse([list(range(n))], n, coords=[0], ks=[1])[0]
        form = 2 * (1 - 2.0 ** -k) + 2 ** k * float(Phi(np.array([(1 - 2.0 ** -k) ** 2]), np.array([4.0 ** -k]))[0])
        print("  k=%2d exact %.10f formula %.10f |r-2|=%.3e  bound 2^-k(2k+2)=%.3e %s"
              % (k, r["ratio"], form, abs(r["ratio"] - 2), 2.0 ** -k * (2 * k + 2),
                 "ok" if abs(r["ratio"] - 2) <= 2.0 ** -k * (2 * k + 2) else "FAIL"))
    # 2. star table
    print("\nstar table (centre i=0, other i=1)")
    for D, w in [(2, 4), (2, 6), (2, 8), (2, 10), (3, 5), (3, 7), (4, 5)]:
        terms, n = star(D, w)
        rc = analyse(terms, n, coords=[0], ks=[1])[0]
        ro = analyse(terms, n, coords=[1], ks=[1])[0]
        print("  D=%d w=%2d n=%2d Inf_c=%.4f E/Inf_c=%.3f Inf_o=%.4f E/Inf_o=%.3f"
              % (D, w, n, rc["delta"], rc["ratio"], ro["delta"], ro["ratio"]))
    # 3. rows and columns
    print("\nrows and columns of an m x m array")
    for m in (3, 4):
        terms, n = grid(m)
        rs = analyse(terms, n, coords=[0], ks=[1])
        print("  m=%d ratio %.4f (coordinate 0, d=%d)" % (m, rs[0]["ratio"], rs[0]["d"]))
    # 4. all lemmas, theorem and proposition on a family
    print("\nlemma / theorem / proposition checks")
    rng = random.Random(51)
    fams = [("star D=%d w=%d" % (D, w),) + star(D, w) for D, w in [(2, 4), (2, 6), (3, 5), (4, 5), (2, 8)]]
    fams += [("grid m=%d" % m,) + grid(m) for m in (3, 4)]
    for j in range(14):
        n = rng.choice([14, 15, 16, 17])
        w = rng.choice([4, 5]); D = rng.choice([2, 3, 4])
        t = random_linear(n, w, D, rng.randint(4, 8), rng)
        if t:
            fams.append(("rand n=%d w=%d D<=%d #t=%d" % (n, w, D, len(t)), t, n))
    tot = dict(pairs=0, lemA=0, lemh=0, lemN=0, lemN_na=0, thm=0, thm_na=0, prop=0, maxfrac=0.0)
    for name, terms, n in fams:
        rows = analyse(terms, n)
        bad = [r for r in rows if not (r["lemA"] and r["lemh"] and r["lemN"] in (True, None)
                                         and r["thm_ok"] in (True, None) and r["prop"] in (True, None))]
        for r in rows:
            tot["pairs"] += 1
            tot["lemA"] += r["lemA"]; tot["lemh"] += r["lemh"]
            if r["lemN"] is None: tot["lemN_na"] += 1
            else: tot["lemN"] += r["lemN"]
            if r["thm"] is None: tot["thm_na"] += 1
            else:
                tot["thm"] += r["thm_ok"]
                tot["maxfrac"] = max(tot["maxfrac"], abs(r["ratio"] - 2) / r["thm"])
            tot["prop"] += bool(r["prop"])
        rr = sorted({round(r["ratio"], 4) for r in rows})
        print("  %-28s pairs %3d  ratios %.3f..%.3f  failures %d" % (name, len(rows), rr[0], rr[-1], len(bad)))
        for r in bad[:3]:
            print("     FAIL", r)
    print("\ntotals:", tot)
    # 5. derivative claim in the proof of Theorem lin: d/dx x log2(e[1+x^-2]) > 0 on (0, 1/4]
    xs = np.linspace(1e-6, 0.25, 200001)
    der = np.log2(1 + xs ** -2) + LOG2E * (1 - 2 / (1 + xs ** 2))
    second = LOG2E * (1 - 2 / (1 + xs ** 2))
    print("\nTheorem lin derivative: min over (0,1/4] = %.4f (paper's lower bound log2 17 - log2e*15/17 = %.4f)"
          % (der.min(), math.log2(17) - LOG2E * 15 / 17))
    print("  second piece log2e(1-2/(1+x^2)): min %.4f (at x->0), max %.4f (at x=1/4)" % (second.min(), second.max()))


if __name__ == "__main__":
    main()
