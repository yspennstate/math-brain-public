"""Independent numerical check of P5 ("A filtration bound for the erasure entropies of Boolean functions").
Written by an agent without reading p5/code. Conditional expectations, W and V are computed by averaging on the
cube (no Fourier sums), and compared with the Fourier-side quantities of the paper."""
import itertools
import numpy as np

rng = np.random.default_rng(5)


def wht(f):
    a = f.astype(float).copy(); h = 1
    while h < len(a):
        a = a.reshape(-1, 2 * h); x = a[:, :h].copy(); y = a[:, h:].copy()
        a[:, :h] = x + y; a[:, h:] = x - y; a = a.reshape(-1); h *= 2
    return a / len(a)


def eta(x):
    x = np.asarray(x, float); out = np.zeros_like(x); m = x > 0
    out[m] = -x[m] * np.log2(x[m]); return out


def Phi(a, b):
    return eta(a) + eta(b) - eta(np.asarray(a, float) + np.asarray(b, float))


def h2(t):
    return float(eta(t) + eta(1 - t))


def avg_out(u, n, coords):
    """average u over the listed coordinates (resample them)."""
    u = u.copy()
    for j in coords:
        idx = np.arange(1 << n); u = 0.5 * (u + u[idx ^ (1 << j)])
    return u


class Coord:
    def __init__(self, f, n, i):
        self.n, self.i = n, i; N = 1 << n; c = wht(f); mu = c * c
        idx = np.arange(N); self.Ts = idx[(idx >> i & 1) == 0]
        self.p = mu[self.Ts]; self.q = mu[self.Ts | 1 << i]
        self.others = [j for j in range(n) if j != i]
        self.delta = self.q.sum(); self.E = Phi(self.p, self.q).sum()
        x0 = idx & ~(1 << i); x1 = idx | 1 << i
        self.g = 0.5 * (f[x0] + f[x1]); self.h = 0.5 * (f[x0] - f[x1])  # bit 0 means x_i = +1
        self.mu = mu

    def AB(self, order):
        pos = {j: k + 1 for k, j in enumerate(order)}; lab = np.zeros(len(self.Ts), int)
        for j in order:
            lab = np.where(self.Ts >> j & 1, np.maximum(lab, pos[j]), lab)
        m = len(order)
        A = np.bincount(lab, self.p, m + 1); B = np.bincount(lab, self.q, m + 1)
        return A, B, lab

    def L(self, order):
        A, B, _ = self.AB(order); return Phi(A, B).sum()

    def L_window(self, order, r):
        pos = {j: k + 1 for k, j in enumerate(order)}; atoms = {}
        for t, P, Q in zip(self.Ts, self.p, self.q):
            ps = sorted((pos[j] for j in order if t >> j & 1), reverse=True)[:r]
            key = tuple(ps); a = atoms.setdefault(key, [0.0, 0.0]); a[0] += P; a[1] += Q
        v = np.array(list(atoms.values())); return Phi(v[:, 0], v[:, 1]).sum()

    def best(self):
        n, i = self.n, self.i; N = 1 << n
        pa = np.zeros(N); pb = np.zeros(N); pa[self.Ts] = self.p; pb[self.Ts] = self.q
        for j in range(n):  # zeta transform: a(R) = sum_{T subset R} p(T)
            idx = np.arange(N); sel = (idx >> j & 1) == 1
            pa[sel] += pa[idx[sel] ^ (1 << j)]; pb[sel] += pb[idx[sel] ^ (1 << j)]
        beta = np.full(N, np.inf); beta[0] = float(Phi(pa[0], pb[0]))
        for R in range(1, N):
            if R >> i & 1:
                continue
            best = np.inf
            for j in self.others:
                if R >> j & 1:
                    S = R ^ (1 << j)
                    v = beta[S] + float(Phi(pa[R] - pa[S], pb[R] - pb[S]))
                    best = min(best, v)
            beta[R] = best
        return beta[(N - 1) ^ (1 << i)]


def lemma2_bound(A, B):
    d = B.sum(); m = len(A) - 1
    M = max(A[K:].sum() * B[:K + 1].sum() for K in range(m + 1)) / d ** 2
    return (1 / np.log(2) + 4 + 2 * np.log2(1 + 2 * M)) * d, M


worst = {}


def rec(k, v):
    worst.setdefault(k, []).append(v)


fs = []
for n in range(3, 8):
    for bias in (0.5, 0.2, 0.05):
        for _ in range(4):
            f = np.where(rng.random(1 << n) < bias, -1.0, 1.0)
            if abs(f.mean()) < 1:
                fs.append((n, f))
for n, f in fs:
    for i in range(n):
        C = Coord(f, n, i)
        if C.delta < 1e-12:
            continue
        orders = list(itertools.permutations(C.others)) if n <= 6 else [list(rng.permutation(C.others)) for _ in range(40)]
        Ls = []
        for o in orders:
            o = list(o); A, B, _ = C.AB(o); L = Phi(A, B).sum(); Ls.append(L)
            rec("E - L (<=0)", C.E - L); rec("L - h2(Inf) (<=0)", L - h2(C.delta))
            bd, M = lemma2_bound(A, B); rec("L - lemma2 bound (<=0)", L - bd)
            # Theorem 3 identities by resampling on the cube
            m = len(o)
            for k in range(1, m + 1):
                Rk = o[k:]; Rk1 = o[k - 1:]
                W = np.mean(C.h * avg_out(C.h, n, Rk)); V = np.mean(C.g ** 2) - np.mean(C.g * avg_out(C.g, n, Rk1))
                rec("|W(R_k) - sum_{l<=k} B|", abs(W - B[:k + 1].sum())); rec("|V(R_k-1) - sum_{l>=k} A|", abs(V - A[k:].sum()))
            # Theorem 3 constant: with M3 = max(max_k W V / delta^2, 1)
            M3 = max(max(B[:k + 1].sum() * A[k:].sum() for k in range(1, m + 1)) / C.delta ** 2, 1.0)
            rec("L - thm3 bound (<=0)", L - (1 / np.log(2) + 4 + 2 * np.log2(1 + 2 * M3)) * C.delta)
            rec("K=0 product / delta^2 (<=1)", A.sum() * B[0] / C.delta ** 2)
            if o is not orders[0] and len(Ls) > 3:
                continue
            # martingale form by averaging on the cube
            Gp = avg_out(C.g, n, o); Hp = avg_out(C.h, n, o)
            rec("|A0-(Eg)^2|+|B0-(Eh)^2|", abs(A[0] - Gp[0] ** 2) + abs(B[0] - Hp[0] ** 2))
            for k in range(1, m + 1):
                Gk = avg_out(C.g, n, o[k:]); Hk = avg_out(C.h, n, o[k:])
                rec("martingale |A_k - E dG^2|+|B_k - E dH^2|", abs(A[k] - np.mean((Gk - Gp) ** 2)) + abs(B[k] - np.mean((Hk - Hp) ** 2)))
                Gp, Hp = Gk, Hk
            # windows
            Lw = [C.L_window(o, r) for r in range(1, m + 1)]
            rec("|L_window(1) - L|", abs(Lw[0] - L)); rec("|L_window(m) - E|", abs(Lw[-1] - C.E))
            rec("window increments (<=0)", max(Lw[r] - Lw[r - 1] for r in range(1, m)) if m > 1 else 0.0)
            rec("E - L_window(r) (<=0)", max(C.E - x for x in Lw))
        dp = C.best()
        if n <= 6:
            rec("|DP - min over all orders|", abs(dp - min(Ls)))
        else:
            rec("DP - min over sampled orders (<=0)", dp - min(Ls))
        rec("E - DP (<=0)", C.E - dp)

# Proposition 5: composition
for _ in range(60):
    b = int(rng.integers(2, 4)); z = int(rng.integers(1, 4)); n = b + z
    g = np.where(rng.random(1 << b) < rng.choice([0.5, 0.2]), -1.0, 1.0)
    F = np.where(rng.random(1 << (1 + z)) < 0.5, -1.0, 1.0)  # F index: bit 0 = u, bits 1.. = z
    if abs(g.mean()) == 1:
        continue
    f = np.zeros(1 << n)
    for x in range(1 << n):
        xb = x & ((1 << b) - 1); xz = x >> b; u = g[xb]; ubit = 0 if u > 0 else 1
        f[x] = F[ubit | (xz << 1)]
    F0 = np.array([(F[0 | t << 1] + F[1 | t << 1]) / 2 for t in range(1 << z)])
    F1 = np.array([(F[0 | t << 1] - F[1 | t << 1]) / 2 for t in range(1 << z)])
    c0, c1 = wht(F0), wht(F1); gh = wht(g)
    for i in range(b):
        Cf = Coord(f, n, i); Cg = Coord(g, b, i)
        if Cg.delta < 1e-12:
            continue
        nF1 = (c1 ** 2).sum()
        rhs = nF1 * (Cg.E - float(Phi(gh[0] ** 2, gh[1 << i] ** 2))) + Phi((c0 + gh[0] * c1) ** 2, gh[1 << i] ** 2 * c1 ** 2).sum()
        rec("composition |E_i(f) - formula|", abs(Cf.E - rhs)); rec("composition |Inf_i(f) - Inf_i(g)||F1||^2|", abs(Cf.delta - Cg.delta * nF1))

# Proposition 6: private AND (i = coordinate 0, B = 1..k, v = the rest)
for _ in range(80):
    k = int(rng.integers(0, 4)); nv = int(rng.integers(1, 4)); n = 1 + k + nv
    A0 = np.where(rng.random(1 << nv) < 0.5, -1.0, 1.0); A1 = np.where(rng.random(1 << nv) < rng.choice([0.5, 0.1]), -A0, A0)
    if np.all(A1 == A0):
        continue
    f = np.zeros(1 << n)
    for x in range(1 << n):
        a = (x & ((1 << (k + 1)) - 1)) == 0; v = x >> (k + 1); f[x] = A1[v] if a else A0[v]
    C = Coord(f, n, 0); vco = list(range(k + 1, n)); bco = list(range(1, k + 1))
    order = list(rng.permutation(vco)) + list(rng.permutation(bco)) if k else list(rng.permutation(vco))
    L = C.L(order); d = C.delta; rho = np.mean(A1 != A0)
    lo = 2 * (1 - 2.0 ** -k); hi = lo + 2.0 ** -k * np.log2(np.e * 2 ** k / d)
    rec("private: |delta - 2^-k Pr[c!=0]|", abs(d - 2.0 ** -k * rho))
    rec("private: lo - E/d, E/d - L/d, L/d - hi (<=0)", max(lo - C.E / d, C.E / d - L / d, L / d - hi))
    rec("private: hi - abstract form 2+2^-k(2k+1+log 1/rho) (<=0)", hi - (2 + 2.0 ** -k * (2 * k + 1 + np.log2(1 / rho))))
    rec("private: hi - tighter 2+2^-k(2k+log 1/rho) (<=0)", hi - (2 + 2.0 ** -k * (2 * k + np.log2(1 / rho))))

for k_, v in worst.items():
    print(f"{k_:62s} max {max(v): .3e}  (n={len(v)})")


def table_entry(f, n, symmetric=False):
    best_L = np.inf; best_E = np.inf
    for i in range(n):
        C = Coord(f, n, i)
        if C.delta < 1e-12:
            continue
        best_E = min(best_E, C.E / C.delta)
        best_L = min(best_L, (C.L(C.others) if symmetric else C.best()) / C.delta)
        if symmetric:
            break
    return best_L, best_E


def AND(n):
    return np.array([-1.0 if x == (1 << n) - 1 else 1.0 for x in range(1 << n)])


def MAJ(n):
    return np.array([-1.0 if bin(x).count("1") > n // 2 else 1.0 for x in range(1 << n)])


def TRIBES(w, s):
    n = w * s; out = np.ones(1 << n)
    for x in range(1 << n):
        if any(((x >> (w * t)) & ((1 << w) - 1)) == (1 << w) - 1 for t in range(s)):
            out[x] = -1.0
    return out, n


print("\ntable (F = min_i,pi L/Inf ; min_i E/Inf):")
for n in (6, 8, 10):
    print(f"  AND_{n:<3d} %.4f  %.4f" % table_entry(AND(n), n), "  Prop 6 upper bound k=n-1: %.5f" % (2 + 2.0 ** -(n - 1) * (2 * (n - 1) + np.log2(np.e) - 2)))
for n in (3, 5, 7, 9, 11):
    print(f"  MAJ_{n:<3d} %.4f  %.4f" % table_entry(MAJ(n), n, symmetric=True))
for w, s in ((2, 3), (2, 4), (2, 5), (3, 3)):
    f, n = TRIBES(w, s); print(f"  TRIBES_{w}x{s}  %.4f  %.4f" % table_entry(f, n))

print("\ntribes order claim (other tribes first, mates last; i = coordinate 0): M and L/Inf")
for w, s in ((2, 3), (2, 4), (2, 5), (3, 3), (4, 2), (3, 4)):
    f, n = TRIBES(w, s); C = Coord(f, n, 0)
    order = list(range(w, n)) + list(range(1, w)); A, B, _ = C.AB(order)
    M = max(B[:k + 1].sum() * A[k:].sum() for k in range(1, n)) / C.delta ** 2
    print(f"  TRIBES_{w}x{s}: M = {M:.4f}, L/Inf = {Phi(A, B).sum() / C.delta:.4f}, thm3 bound/Inf = {1/np.log(2)+4+2*np.log2(1+2*max(M,1)):.3f}")

print("\nbent point (y = all bits clear, i = last coordinate):")
for k in (2, 4, 6, 8):
    n = k + 1; f = np.zeros(1 << n)
    for x in range(1 << n):
        y = x & ((1 << k) - 1); xi = x >> k
        if y == 0:
            f[x] = 1.0 if xi == 0 else -1.0
        else:
            ip = sum((y >> (2 * t) & 1) & (y >> (2 * t + 1) & 1) for t in range(k // 2)) % 2
            f[x] = -1.0 if ip else 1.0
    C = Coord(f, n, k); Fy = min(Coord(f, n, j).best() / Coord(f, n, j).delta for j in range(k))
    print(f"  k={k}: new E/Inf {C.E / C.delta:.3f}, new min L/Inf {C.best() / C.delta:.3f}, min over y coords of min L/Inf {Fy:.3f}")
