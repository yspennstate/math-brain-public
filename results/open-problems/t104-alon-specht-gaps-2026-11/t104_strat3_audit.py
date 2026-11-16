"""Independent audit of Codex STRAT3 (T104 stratum claim).
(A) n = 5, D = 3: symbolic check of C(g), of 7+16g-kP, the square completion behind m4 <= p + (3+5p) m3^2/4,
    and a random check of that moment bound and of B >= 5 over unit zero-sum v and g in (0, 2/3] with
    p <= (2+g)/(20g).
(B) equitable 1,a,b: symbolic check of (13), (14), the q=3 two-singleton identity; random equitable instances
    with block sizes 1,a,b checking T >= E_a s_a + E_b s_b - K t (12), t <= h_b s_a, t <= h_a s_b (10), T > 0.
(C) the exact 1,2,2 example: spectrum, X1, X2, X3, 2S5 in rationals.
usage: python t104_strat3_audit.py trials seed
"""
import sys
import numpy as np
import sympy as sp

TR, SEED = int(sys.argv[1]), int(sys.argv[2])
rng = np.random.default_rng(SEED)

# ---------------- (A) symbolic
g, p, h, m3, m4, dl, n, a, b, lam = sp.symbols('g p h m3 m4 delta n a b lam', positive=True)
k = 200 * g - 70; P = (2 + g) / (20 * g)
print("A1 C(g) diff:", sp.simplify(120 * g - k * (3 + 5 * P) / 4 - 5 * (14 + 51 * g - 68 * g**2) / (8 * g)))
print("A2 7+16g-kP diff:", sp.simplify(7 + 16 * g - k * P - (5 + (3 * g - 2) * (4 * g - 7) / (2 * g))))
print("A3 square completion diff:", sp.expand(dl * h * m3 - (h - m3)**2 - (-(h - (1 + dl / 2) * m3)**2 + dl * (1 + dl / 4) * m3**2)))
print("A4 1+delta/4 at delta=5p-1 minus (3+5p)/4:", sp.simplify((1 + (5 * p - 1) / 4) - (3 + 5 * p) / 4))
print("A5 min of 14+51g-68g^2 on [7/20,2/3]:", min(sp.Rational(14) + 51 * x - 68 * x**2 for x in (sp.Rational(7, 20), sp.Rational(2, 3))))

worst_mom = np.inf; worstB = np.inf; kept = 0
for _ in range(TR):
    v = rng.standard_normal(5) * rng.uniform(0.2, 3, 5)
    v -= v.mean(); v /= np.linalg.norm(v)
    pp = max(-v[i] * v[j] for i in range(5) for j in range(i + 1, 5))
    M3, M4 = (v**3).sum(), (v**4).sum()
    worst_mom = min(worst_mom, pp + (3 + 5 * pp) * M3**2 / 4 - M4)
    gmax = min(2 / 3, 2 / (20 * pp - 1)) if pp > 0.05 else 2 / 3
    for gg in (gmax, rng.uniform(0, gmax), 0.35, min(gmax, 35 / 76 + 1e-9)):
        if gg <= 0 or gg > gmax:
            continue
        B = 7 + 16 * gg + (70 - 200 * gg) * M4 + 120 * gg * M3**2
        worstB = min(worstB, B); kept += 1
print("A6 min [p+(3+5p)m3^2/4 - m4] over %d v: %.3e" % (TR, worst_mom))
print("A7 min B over %d feasible (v,g): %.6f (claim >= 5)" % (kept, worstB))

# ---------------- (B) symbolic, n = 1+a+b
nn = 1 + a + b; c = 2 * nn / (nn - 2)
Aa = 2 - c * (1 / a - 1 / nn); Ab = 2 - c * (1 / b - 1 / nn)
ha = lam * a / nn; hb = lam * b / nn
K = 4 * ((nn - 1) / (nn - 2) - 1 / a - 1 / b)
da = 2 * lam * (b - 1) * ((nn - 1) * a - nn) / (nn * a * (nn - 2))
db = 2 * lam * (a - 1) * ((nn - 1) * b - nn) / (nn * b * (nn - 2))
print("B1 (13a) diff:", sp.simplify(da / hb + db / ha - K + 2 * (nn - 3) / (a * b * (nn - 2))))
print("B2 (13b) diff:", sp.simplify(Aa / b + Ab / a - 2 * (nn**2 - 4 * nn + 1) / (a * b * (nn - 2))))
betamin = lam / (nn * (nn - 2))
print("B3 (14) diff:", sp.simplify(da / hb + db / ha - K + betamin * (Aa / hb + Ab / ha) - 2 * (nn - 5) / (a * b * (nn - 2)**2)))
a2 = n - 2; c2 = 2 * n / (n - 2); A0 = 2 - c2 * (1 / a2 - 1 / n)
print("B4 two-singleton identity diff:", sp.simplify(2 * lam - 4 * lam / n * (1 + 1 / a2) - A0 * lam * a2 / n))


# ---------------- (B) numeric
def lap(W):
    return np.diag(W.sum(1)) - W


def sinkhorn(M, r, cc, it=4000):
    for _ in range(it):
        M *= (r / M.sum(1))[:, None]; M *= (cc / M.sum(0))[None, :]
    return M


def build(sizes):
    N = sum(sizes); q = len(sizes); L0 = 1.0
    W = np.zeros((N, N)); off = np.cumsum([0] + sizes)
    for x in range(q):
        for y in range(x + 1, q):
            A_, B_ = sizes[x], sizes[y]
            M = rng.random((A_, B_)) ** rng.uniform(1, 6) * (rng.random((A_, B_)) < rng.uniform(0.4, 1.0)) + 1e-9
            M = sinkhorn(M, np.full(A_, L0 * B_ / N), np.full(B_, L0 * A_ / N))
            W[off[x]:off[x + 1], off[y]:off[y + 1]] = M
    W = W + W.T
    for x in range(q):
        A_ = sizes[x]
        if A_ >= 2:
            Bm = rng.random((A_, A_)) * (rng.random((A_, A_)) < rng.uniform(0.3, 1.0)); Bm = np.triu(Bm, 1); Bm = Bm + Bm.T
            W[off[x]:off[x + 1], off[x]:off[x + 1]] = Bm * rng.uniform(0.05, 1.5)
    lab = np.repeat(np.arange(q), sizes)
    Y = np.column_stack([np.ones(N)] + [(lab == x).astype(float) for x in range(q)])
    Qm = np.linalg.qr(Y)[0][:, :q]; R = np.eye(N) - Qm @ Qm.T
    for _ in range(80):
        if np.linalg.eigvalsh(R @ lap(W) @ R).max() < L0 * (1 - 1e-6):
            return W / W[np.triu_indices(N, 1)].sum(), lab
        for x in range(q):
            W[off[x]:off[x + 1], off[x]:off[x + 1]] *= 0.8
    return None, None


def terms(W, tol=1e-8):
    N = W.shape[0]; L = lap(W)
    ev, U = np.linalg.eigh(L); lm = ev[-1]; top = np.where(ev > lm - tol)[0]; D = len(top)
    Pi = U[:, top] @ U[:, top].T
    G = lm * (np.eye(N) - np.ones((N, N)) / N) - L
    cc = 2 * N / (N - 2); beta = (1 - lm) / (N - 2)
    X1 = D * (lm * np.trace(G) - np.trace(G @ G)); X2 = cc * np.trace(G @ (Pi * G))
    X3 = beta * (D * np.trace(G) - cc * float(np.diag(Pi) @ np.diag(G)))
    S5 = 0.0
    for i in range(N):
        for j in range(i + 1, N):
            if W[i, j] > 0:
                S5 += W[i, j] * (Pi[i, i] + Pi[j, j] - 2 * Pi[i, j]) * (G[i, i] + G[j, j] - 2 * G[i, j])
    return D, lm, G, X1, X2, X3, 2 * S5


worst12 = np.inf; worst10 = np.inf; minT = np.inf; minm = np.inf; cnt = 0
for _ in range(TR):
    A_, B_ = int(rng.integers(2, 7)), int(rng.integers(2, 7))
    W, lab = build([1, A_, B_])
    if W is None:
        continue
    D, lm, G, X1, X2, X3, Y2 = terms(W)
    if D != 2:
        continue
    cnt += 1; N = 1 + A_ + B_
    T = X1 + X2 + X3 - Y2
    Ga = G[1:1 + A_, 1:1 + A_]; Gb = G[1 + A_:, 1 + A_:]; Bx = G[1:1 + A_, 1 + A_:]
    sa, sb, t = np.trace(Ga), np.trace(Gb), (Bx**2).sum()
    cc = 2 * N / (N - 2); beta = (1 - lm) / (N - 2)
    Aa_ = 2 - cc * (1 / A_ - 1 / N); Ab_ = 2 - cc * (1 / B_ - 1 / N)
    da_ = 2 * lm * (B_ - 1) * ((N - 1) * A_ - N) / (N * A_ * (N - 2))
    db_ = 2 * lm * (A_ - 1) * ((N - 1) * B_ - N) / (N * B_ * (N - 2))
    K_ = 4 * ((N - 1) / (N - 2) - 1 / A_ - 1 / B_)
    rhs = (da_ + beta * Aa_) * sa + (db_ + beta * Ab_) * sb - K_ * t
    worst12 = min(worst12, T - rhs)
    worst10 = min(worst10, lm * B_ / N * sa - t, lm * A_ / N * sb - t)
    minT = min(minT, T); minm = min(minm, X1 + X2 - Y2)
print("B5 1,a,b instances kept %d: min T-(12)rhs %.3e  min (10) slack %.3e  min T %.3e  min X1+X2-2S5 %.3e"
      % (cnt, worst12, worst10, minT, minm))

# ---------------- (C) exact example
R = sp.Rational
Wc = sp.zeros(5, 5)
for (i, j, w) in [(0, 1, R(1, 8)), (0, 2, R(1, 8)), (0, 3, R(1, 8)), (0, 4, R(1, 8)), (1, 3, R(49, 200)), (2, 4, R(49, 200)),
                  (1, 4, R(1, 200)), (2, 3, R(1, 200))]:
    Wc[i, j] = Wc[j, i] = w
Lc = sp.diag(*[sum(Wc.row(i)) for i in range(5)]) - Wc
print("C1 total weight:", sum(Wc[i, j] for i in range(5) for j in range(i + 1, 5)))
print("C2 spectrum:", sorted(Lc.eigenvals().items()))
lm = R(5, 8)
Y = [sp.Matrix([1 if i == 0 else 0 for i in range(5)]) - sp.ones(5, 1) / 5,
     sp.Matrix([1 if i in (1, 2) else 0 for i in range(5)]) - sp.ones(5, 1) * R(2, 5)]
Bq = sp.Matrix.hstack(*Y); Pic = Bq * (Bq.T * Bq).inv() * Bq.T
print("C3 L Pi = lam Pi:", sp.simplify(Lc * Pic - lm * Pic) == sp.zeros(5, 5))
Gc = lm * (sp.eye(5) - sp.ones(5, 5) / 5) - Lc
cc = R(10, 3); beta = (1 - lm) / 3; D = 2
X1 = D * (lm * Gc.trace() - (Gc * Gc).trace())
X2 = cc * (Gc * Pic.multiply_elementwise(Gc)).trace()
X3 = beta * (D * Gc.trace() - cc * sum(Pic[i, i] * Gc[i, i] for i in range(5)))
S5 = sum(Wc[i, j] * (Pic[i, i] + Pic[j, j] - 2 * Pic[i, j]) * (Gc[i, i] + Gc[j, j] - 2 * Gc[i, j])
         for i in range(5) for j in range(i + 1, 5))
print("C4 X1 X2 X3 2S5:", sp.nsimplify(X1), sp.nsimplify(X2), sp.nsimplify(X3), sp.nsimplify(2 * S5))
print("C5 X1+X2-2S5 =", sp.simplify(X1 + X2 - 2 * S5), "  T =", sp.simplify(X1 + X2 + X3 - 2 * S5))
