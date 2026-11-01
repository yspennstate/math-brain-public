"""Standalone interval certificate for the erasure and restriction-step constants of the amplification
tower of Numaro's g, depths 1..4 (G_1 = g on 18 variables, G_2 on 324, G_3 on 5832, G_4 on 104976).

Certified quantities (lower and upper bounds):
  B(G_k)/I(G_k),   min_w B_w(G_k)/Inf_w(G_k),   rho_0(G_k) = min_w Delta_w(G_k)/Inf_w(G_k).
Inputs: the truth table inputs/numaro18_pm1_table.npy (SHA-256 printed).  Its Fourier coefficients are
integers / 2^17; they, their squares and the level-1 values 57/256, 1/256 are exact float64 numbers;
products that may need more than 53 bits (c^2 times a spectral weight) are enclosed outward.  Mathematics used (proved in the report): the balanced composition laws
  B_w(G_k)     = Inf_j(g) B_w(G_{k-1}) + Xi_j(c^2),                    Xi_j(c^2) = sum_{T not ni j} E(p_T, c^2 p_{T+j}),
  Delta_w(G_k) = Inf_j(g) [Delta_w(G_{k-1}) + h2(c^2)] + H(g) - (Ht(j,+c)+Ht(j,-c))/2,
  Inf_w(G_k)   = Inf_j(g) Inf_w(G_{k-1}),   c = Inf_w(G_{k-1}) = level-1 coefficient (g monotone, balanced).
Arithmetic: every elementary operation is rounded outward by one ulp (numpy.nextafter); numpy log2/log1p
are assumed accurate to 8 ulp (the assumption of continuations/2026-09-21-readonce-certificate) and padded
accordingly; every sum is padded by (N u) sum|x| with u = 2^-53.  For |t| < 1e-6 the function
F(t) = [(1+t)^2 ln(1+t) + (1-t)^2 ln(1-t)]/ln 2 is enclosed by [(3t^2 - t^4/5)/ln 2, 3t^2/ln 2] (all
Taylor coefficients after t^2 are negative: -2/(k(k-1)(k-2)) for even k >= 4).
"""
import sys, os, hashlib, json
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
U = 2.0 ** -53
INF = np.inf


def dn(x): return np.nextafter(x, -INF)
def up(x): return np.nextafter(x, INF)


def iv(x):
    x = np.asarray(x, float); return (x.copy(), x.copy())


def add(a, b): return (dn(a[0] + b[0]), up(a[1] + b[1]))
def sub(a, b): return (dn(a[0] - b[1]), up(a[1] - b[0]))
def neg(a): return (-a[1], -a[0])


def mul(a, b):
    c = [a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1]]
    return (dn(np.minimum.reduce(c)), up(np.maximum.reduce(c)))


def div_pos(a, b):
    """a / b with b > 0 elementwise."""
    assert np.all(b[0] > 0)
    c = [a[0] / b[0], a[0] / b[1], a[1] / b[0], a[1] / b[1]]
    return (dn(np.minimum.reduce(c)), up(np.maximum.reduce(c)))


def pad8(v):
    s = 8 * np.spacing(np.abs(v)) + 1e-300
    return (v - s, v + s)


def log2_iv(a):
    assert np.all(a[0] > 0)
    lo = pad8(np.log2(a[0]))[0]; hi = pad8(np.log2(a[1]))[1]
    return (dn(lo), up(hi))


def log1p_iv(a):
    assert np.all(a[0] > -1)
    lo = pad8(np.log1p(a[0]))[0]; hi = pad8(np.log1p(a[1]))[1]
    return (dn(lo), up(hi))


INVLN2 = (dn(1 / np.log(2.0)) - 4 * np.spacing(1 / np.log(2.0)), up(1 / np.log(2.0)) + 4 * np.spacing(1 / np.log(2.0)))
INVLN2 = (np.float64(INVLN2[0]), np.float64(INVLN2[1]))


def scal(a, s):
    """multiply interval array by scalar interval s=(lo,hi)."""
    return mul(a, (np.full_like(a[0], s[0]), np.full_like(a[1], s[1])))


def isum(a):
    N = a[0].size
    lo = np.sum(a[0]); hi = np.sum(a[1])
    padlo = (N + 1) * U * np.sum(np.abs(a[0])) * 1.01 + 1e-300
    padhi = (N + 1) * U * np.sum(np.abs(a[1])) * 1.01 + 1e-300
    return (float(dn(lo - padlo)), float(up(hi + padhi)))


def phi_exact(x):
    """-x log2 x for exact nonnegative x (array), interval."""
    x = np.asarray(x, float)
    pos = x > 0
    lo = np.zeros_like(x); hi = np.zeros_like(x)
    L = log2_iv(iv(x[pos]))
    r = mul(neg(L), iv(x[pos]))
    lo[pos], hi[pos] = r
    return (lo, hi)


def phi_iv(a):
    """-x log2 x for interval x with lo > 0."""
    return mul(neg(log2_iv(a)), a)


def s_(x): return (float(x[0]), float(x[1]))


def ssum(*xs):
    lo = 0.0; hi = 0.0
    for x in xs:
        lo = float(dn(lo + x[0])); hi = float(up(hi + x[1]))
    return (lo, hi)


def smul(a, b):
    c = [a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1]]
    return (float(dn(min(c))), float(up(max(c))))


def sdiv(a, b):
    assert b[0] > 0
    c = [a[0] / b[0], a[0] / b[1], a[1] / b[0], a[1] / b[1]]
    return (float(dn(min(c))), float(up(max(c))))


def main():
    path = os.path.join(HERE, "..", "..", "inputs", "numaro18_pm1_table.npy")
    raw = open(path, "rb").read()
    print("input sha256", hashlib.sha256(raw).hexdigest())
    g = np.load(path).astype(np.int64)
    canon = hashlib.sha256(",".join(map(str, g.tolist())).encode()).hexdigest()
    assert canon == "f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839", "not the published Numaro table"
    print("published truth-table SHA-256 matched:", canon)
    n = 18; N = 1 << n
    # exact Walsh transform in integers
    a = g.copy()
    h = 1
    while h < N:
        a = a.reshape(-1, 2, h)
        x = a[:, 0, :].copy(); y = a[:, 1, :].copy()
        a[:, 0, :] = x + y; a[:, 1, :] = x - y
        a = a.reshape(N); h *= 2
    assert np.all(a % 2 == 0)
    K = a // 2                    # fhat = K / 2^17 exactly
    assert K[0] == 0, "balanced"
    fh = K.astype(float) / 2.0 ** 17
    p = fh * fh                   # exact (K^2 < 2^53)
    S = np.arange(N)
    lows = [S[((S >> j) & 1) == 0] for j in range(n)]
    Inf = np.array([p[S[((S >> j) & 1) == 1]].sum() for j in range(n)])   # exact dyadic sums
    lvl1 = np.array([fh[1 << j] for j in range(n)])
    assert np.all(np.abs(lvl1) == Inf), "monotone: Inf_j = |ghat({j})| exactly"
    core = [j for j in range(n) if Inf[j] == 57 / 256]
    aux = [j for j in range(n) if Inf[j] == 1 / 256]
    assert len(core) == 9 and len(aux) == 9
    Ig = Inf.sum(); assert Ig == 261 / 128
    # H(g)
    Hg = isum(phi_exact(p))
    # per-coordinate B_j(g), JS_j(g) (exact arguments)
    Bj, Dj = [], []
    for j in range(n):
        u = fh[lows[j]]; v = fh[lows[j] | (1 << j)]
        uu, vv = u * u, v * v; m = uu + vv                   # exact
        p1 = (u + v) ** 2; p0 = (u - v) ** 2                 # exact (u, v in 2^-17 Z)
        Bt = sub(add(phi_exact(uu), phi_exact(vv)), phi_exact(m))
        JSt = sub(phi_exact(m), scal(add(phi_exact(p0), phi_exact(p1)), (0.5, 0.5)))
        B = isum(Bt); JS = isum(JSt)
        Bj.append(B); Dj.append(ssum(B, JS))

    def Xi(j, c2):
        """sum_T E(p_T, c2 p_{T+j}) with E(x,y) = [x log1p(y/x) + y log1p(x/y)]/ln 2 ; c2 exact."""
        lo = lows[j]
        x = p[lo]; pj = p[lo | (1 << j)]
        m = (x > 0) & (pj > 0)
        X = iv(x[m])
        Y = (dn(c2 * pj[m]), up(c2 * pj[m]))              # c2*p may need > 53 bits: enclose outward
        t1 = mul(X, log1p_iv(div_pos(Y, X)))
        t2 = mul(Y, log1p_iv(div_pos(X, Y)))
        return smul(isum(add(t1, t2)), INVLN2)

    def h2_exact(x):
        """binary entropy of exact x in (0,1/2]."""
        X = iv(np.array([x]))
        t1 = mul(neg(log2_iv(X)), X)
        t2 = scal(mul(neg(iv(np.array([1 - x]))), log1p_iv(neg(X))), INVLN2)
        r = add(t1, t2)
        return (float(r[0][0]), float(r[1][0]))

    def gate_increment(j, c):
        """H(g) - (Ht(j,+c)+Ht(j,-c))/2 ; c exact."""
        lo = lows[j]
        A = fh[lo]; Bv = fh[lo | (1 << j)]
        c2 = c * c
        parts = []
        nz = (A != 0) & (Bv != 0)
        a = A[nz]; b = Bv[nz]
        a2 = iv(a * a)
        t = div_pos(iv(c * b), iv(np.abs(a)))              # t = c b / |a| (sign irrelevant: F even)
        t = (np.minimum(np.abs(t[0]), np.abs(t[1])) * (np.sign(t[0]) == np.sign(t[1])), np.maximum(np.abs(t[0]), np.abs(t[1])))
        small = t[1] < 1e-6
        assert np.all(t[1] < 0.5), "need |t| < 1/2"
        F = (np.empty_like(t[0]), np.empty_like(t[0]))
        ts = (t[0][small], t[1][small])
        t2s = mul(ts, ts); t4s = mul(t2s, t2s)
        Flo = scal(sub(scal(t2s, (3.0, 3.0)), scal(t4s, (0.2, 0.2))), INVLN2)[0]
        Fhi = scal(scal(t2s, (3.0, 3.0)), INVLN2)[1]
        F[0][small] = Flo; F[1][small] = Fhi
        tl = (t[0][~small], t[1][~small])
        one = iv(np.ones_like(tl[0]))
        s1 = mul(mul(add(one, tl), add(one, tl)), log1p_iv(tl))
        s2 = mul(mul(sub(one, tl), sub(one, tl)), log1p_iv(neg(tl)))
        Fl = scal(add(s1, s2), INVLN2)
        F[0][~small] = Fl[0]; F[1][~small] = Fl[1]
        tsq = mul(t, t)
        term = mul(a2, sub(F, mul(tsq, neg(log2_iv(a2)))))
        parts.append(isum(term))
        # a = 0, b != 0 : -phi(c^2 b^2)
        z = (A == 0) & (Bv != 0)
        if z.any():
            b2z = Bv[z] ** 2
            q = neg(phi_iv((dn(c2 * b2z), up(c2 * b2z)))); parts.append(isum(q))
        # a != 0, b = 0 contributes 0 ; all b != 0: c^2 b^2 log2(1/b^2) + (1-c^2) b^2 log1p(-c^2)/ln 2
        bz = Bv != 0
        b2 = Bv[bz] ** 2
        r1 = scal(mul(iv(b2), neg(log2_iv(iv(b2)))), (c2, c2))
        l1 = log1p_iv(iv(np.array([-c2])))
        coef = smul(smul((float(dn(1 - c2)), float(up(1 - c2))), (float(l1[0][0]), float(l1[1][0]))), INVLN2)
        r2 = scal(iv(b2), coef)
        parts.append(isum(add(r1, r2)))
        return ssum(*parts)

    # self-tests of the enclosures
    import math
    for xx in (0.25, 57 / 256 * 57 / 256, 1 / 256 ** 2, 1e-12):
        tv = -xx * math.log2(xx) - (1 - xx) * math.log2(1 - xx) if xx > 1e-9 else -xx * math.log2(xx) + xx / math.log(2)
        e = h2_exact(xx)
        assert e[0] <= tv * (1 + 1e-12) and tv * (1 - 1e-12) <= e[1], ("h2 enclosure", xx, e, tv)
    print("self-test h2 enclosure ok", flush=True)
    res = {}
    KMAX = int(os.environ.get("CERT_DEPTH", "4"))
    # depth 1
    ratioB1 = {j: sdiv(Bj[j], (Inf[j], Inf[j])) for j in range(n)}
    ratioD1 = {j: sdiv(Dj[j], (Inf[j], Inf[j])) for j in range(n)}
    Bsum1 = ssum(*Bj)
    res[1] = dict(B_over_I=sdiv(Bsum1, (Ig, Ig)), exist_B=(min(r[0] for r in ratioB1.values()), min(r[1] for r in ratioB1.values())),
                  rho0=(min(r[0] for r in ratioD1.values()), min(r[1] for r in ratioD1.values())))
    cls = {j: (1, 0) if j in core else (0, 1) for j in range(n)}
    # dynamic programme over tail types (a core, b auxiliary positions): minima and B sums (intervals)
    bestB, bestD, Bsum, cnt = {}, {}, {}, {}
    for j in range(n):
        k0 = cls[j]
        for d, r in ((bestB, ratioB1[j]), (bestD, ratioD1[j])):
            old = d.get(k0, (INF, INF)); d[k0] = (min(old[0], r[0]), min(old[1], r[1]))
        Bsum[k0] = ssum(Bsum.get(k0, (0.0, 0.0)), Bj[j]); cnt[k0] = cnt.get(k0, 0) + 1
    incB, incD = {}, {}
    Iprev = Ig
    for depth in range(2, KMAX + 1):
        nB, nD, nS, nc = {}, {}, {}, {}
        for key in bestB:
            a_, b_ = key
            c = (57 / 256) ** a_ * (1 / 256) ** b_          # exact: numerator 57^a_ < 2^53
            for j in range(n):
                if (j, key) not in incB:
                    ic = (float(dn(Inf[j] * c)), float(up(Inf[j] * c)))
                    xi = Xi(j, c * c)
                    incB[(j, key)] = (sdiv(xi, ic), xi)
                    gi = gate_increment(j, c)
                    num = ssum(smul((Inf[j], Inf[j]), h2_exact(c * c)), gi)
                    incD[(j, key)] = sdiv(num, ic)
                nk = (a_ + cls[j][0], b_ + cls[j][1])
                rb = ssum(bestB[key], incB[(j, key)][0]); rd = ssum(bestD[key], incD[(j, key)])
                old = nB.get(nk, (INF, INF)); nB[nk] = (min(old[0], rb[0]), min(old[1], rb[1]))
                old = nD.get(nk, (INF, INF)); nD[nk] = (min(old[0], rd[0]), min(old[1], rd[1]))
                # B over leaves: every leaf of type key sits in outer block j
                add_ = ssum(smul((Inf[j], Inf[j]), Bsum[key]), smul((float(cnt[key]), float(cnt[key])), incB[(j, key)][1]))
                nS[nk] = ssum(nS.get(nk, (0.0, 0.0)), add_)
                nc[nk] = nc.get(nk, 0) + cnt[key]
        print("depth", depth, "increments done", flush=True)
        bestB, bestD, Bsum, cnt = nB, nD, nS, nc
        Ik = Ig ** depth                                      # exact (261/128)^k for k <= 4
        Btot = ssum(*Bsum.values())
        res[depth] = dict(B_over_I=sdiv(Btot, (float(dn(Ik)), float(up(Ik)))),
                          exist_B=(min(v[0] for v in bestB.values()), min(v[1] for v in bestB.values())),
                          rho0=(min(v[0] for v in bestD.values()), min(v[1] for v in bestD.values())))
    for k in range(1, KMAX + 1):
        print(f"depth {k} (n = {18**k}):  B/I in [{res[k]['B_over_I'][0]:.9f}, {res[k]['B_over_I'][1]:.9f}]"
              f"   min_w B_w/Inf_w in [{res[k]['exist_B'][0]:.9f}, {res[k]['exist_B'][1]:.9f}]"
              f"   rho_0 in [{res[k]['rho0'][0]:.9f}, {res[k]['rho0'][1]:.9f}]")
    print("H(g) in", Hg)
    ref = {2: (3.967379182484557, 3.9165518995751234, 6.329015279480451), 3: (4.407413713929042, 4.367640897268202, 6.8901123137005555),
           4: (4.538834676723036, 4.504878857394826, 7.051852835007349)}
    for k, (b, e, r) in ref.items():
        if k > KMAX: continue
        for name, val in (("B_over_I", b), ("exist_B", e), ("rho0", r)):
            lo, hi = res[k][name]
            print(f"  depth {k} {name}: float value {val:.12f} inside certified interval: {lo - 1e-9 <= val <= hi + 1e-9}")
    json.dump({str(k): v for k, v in res.items()}, open(os.path.join(HERE, "..", "logs", "certify_tower.json"), "w"), indent=1)


if __name__ == "__main__":
    try:
        import psutil
        pp = psutil.Process(); pp.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
        pp.cpu_affinity([c for c in (2, 3, 14, 15) if c < psutil.cpu_count()])
    except Exception:
        pass
    main()
