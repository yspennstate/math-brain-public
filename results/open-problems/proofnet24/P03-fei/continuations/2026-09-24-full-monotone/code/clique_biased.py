"""The vertex-coding bound for the k-clique property of G(n, p), any 0 < p <= 1/2.

Fourier analysis is with respect to mu_p: phi_e = (x_e - p)/sigma, sigma^2 = p(1 - p), F = 1 - 2f,
P(T) = Fhat(T)^2, H = sum P log2(1/P) (= Ent_p of Keller-Mossel-Schlank in base 2), and the spectral influence
I_s = sum |T| P(T) = 4 p (1 - p) I_p with I_p = sum_e Pr_p[e pivotal] (their total influence).

Every quantity is an explicit upper or lower bound from the paper, with p in place of 1/2 (the proofs are the same):
  H <= A' + E log2 C(n, v) + I_s log2(e E C(v,2)/I_s)                                   (Proposition 2.1)
  Pr[S touches u] <= min(eps, 4 min(1, lambda k/n) Pr_p[G - u clique-free])             (Lemma 3.1)
  E C(v,2) <= I_s + (1/2) sum_{u != w} 8 (E[ab] + E[c]) Pr_p[G - {u,w} clique-free]     (Lemma 3.2)
  Janson with p-biased Delta; Harris lower bounds; Bonferroni and second moment for Pr[e pivotal].
Printed: B(n,k,p) >= H/I_s, the limit value log2(1/p)/(1-p) + log2(e(1 + 2(1+lambda)/(1-p))), and B in the
Keller-Mossel-Schlank normalisation, H/(p log2(1/p) I_p) <= 4 (1-p) B/log2(1/p).
With --exact: exact H/I_s for n <= 7 under mu_p, and the three lemmas and the bound checked there.
"""
import sys
import functools
import itertools
import mpmath as mp

print = functools.partial(print, flush=True)
mp.mp.dps = 60


def C(a, b):
    if b < 0 or a < 0 or b > a:
        return mp.mpf(0)
    return mp.binomial(a, b)


def log2(x):
    return mp.log(x) / mp.log(2)


def h2(x):
    x = mp.mpf(x)
    if x <= 0 or x >= 1:
        return mp.mpf(0)
    return -x * log2(x) - (1 - x) * log2(1 - x)


class BiasedClique:
    def __init__(self, n, k, p):
        self.n, self.k = n, k
        self.p = mp.mpf(p)
        self.m = k * (k - 1) // 2
        self.pk = self.p ** self.m                  # probability that a given k-clique is present
        self.lam = C(n, k) * self.pk
        self._cf = {}

    def mu_delta(self, n1):
        k, p, pk, m = self.k, self.p, self.pk, self.m
        mu = C(n1, k) * pk
        s = mp.mpf(0)
        for j in range(2, k):
            s += C(k, j) * C(n1 - k, k - j) * p ** (m - j * (j - 1) // 2)
        return mu, mu * s                          # Delta = sum over ordered pairs sharing an edge

    def cf_up(self, n1):
        if n1 in self._cf:
            return self._cf[n1]
        if n1 < self.k:
            self._cf[n1] = mp.mpf(1)
            return self._cf[n1]
        mu, D = self.mu_delta(n1)
        b = min(mp.mpf(1), mp.exp(-mu + D / 2))
        if D >= mu and D > 0:
            b = min(b, mp.exp(-mu * mu / (2 * D)))
        self._cf[n1] = b
        return b

    def eps_up(self):
        q_up = self.cf_up(self.n)
        one_minus_q_lo = -mp.expm1(C(self.n, self.k) * mp.log1p(-self.pk))
        return min(mp.mpf(1), 4 * q_up, 4 * one_minus_q_lo)

    def piv_sum_bounds(self):
        """lower and upper bounds for sum_e Pr_p[e pivotal] (= I_p)."""
        n, k, m, p, pk = self.n, self.k, self.m, self.p, self.pk
        N = C(n, 2)
        mu_e = C(n - 2, k - 2) * p ** (m - 1)
        lg = mp.mpf(0)
        for j in range(0, k):
            cj = C(k, j) * C(n - k, k - j)
            if j >= 2:
                cj -= C(k - 2, j - 2) * C(n - k, k - j)
            if cj <= 0:
                continue
            lg += cj * mp.log1p(-p ** (m - j * (j - 1) // 2))
        EX_lo = mu_e * mp.exp(lg)
        s = mp.mpf(0)
        for j in range(2, k):
            s += C(k - 2, j - 2) * C(n - k, k - j) * p ** (m - j * (j - 1) // 2)
        P2 = mu_e * s
        mu_me = (C(n, k) - C(n - 2, k - 2)) * pk
        _, D_full = self.mu_delta(n)
        PD = min(mp.mpf(1), mp.exp(-mu_me + D_full / 2))
        if D_full >= mu_me and D_full > 0:
            PD = min(PD, mp.exp(-mu_me * mu_me / (2 * D_full)))
        bonf = EX_lo - P2 / 2 * PD
        smom = EX_lo * EX_lo / (EX_lo + P2 * PD)
        piv_lo = max(bonf, smom)
        piv_up = min(mu_e * PD, mp.mpf(1))
        return N * piv_lo, N * piv_up

    def mixed(self):
        n, k, p, pk, m = self.n, self.k, self.p, self.pk, self.m
        s = mp.mpf(0)
        for j in range(0, k):
            s += C(k - 1, j) * C(n - k - 1, k - 1 - j) * p ** (-(j * (j - 1) // 2))
        EAB = C(n - 2, k - 1) * s * pk * pk
        EC = C(n - 2, k - 2) * pk
        return 8 * n * (n - 1) * (EAB + EC) * self.cf_up(n - 2)

    def bound(self):
        n, k, p = self.n, self.k, self.p
        eps = self.eps_up()
        piv_lo, piv_up = self.piv_sum_bounds()
        if piv_lo <= 0:
            return None
        s2 = 4 * p * (1 - p)
        I_lo, I_up = s2 * piv_lo, s2 * piv_up
        R = self.mixed()
        x = min(eps, I_up)
        A = h2(min(eps, mp.mpf('0.5'))) + x * log2(mp.e * I_up / x)
        Ev = n * min(eps, 4 * min(mp.mpf(1), self.lam * k / n) * self.cf_up(n - 1))
        c = min(Ev, n * eps)
        V = c * log2(mp.e * n * eps / c) if c > 0 else mp.mpf(0)
        x1 = min(eps, Ev)
        Ap = A + (x1 * log2(mp.e * Ev / x1) if x1 > 0 else mp.mpf(0))
        jensen = log2(mp.e * (1 + R / (2 * I_lo)))
        B = Ap / I_lo + V / I_lo + jensen
        lim = log2(1 / p) / (1 - p) + log2(mp.e * (1 + 2 * (1 + self.lam) / (1 - p)))
        kms = 4 * (1 - p) * B / log2(1 / p)
        return dict(B=B, lim=lim, kms=kms, Ap=Ap / I_lo, V=V / I_lo, jensen=jensen, pair=R / (2 * I_lo),
                    ratio=I_lo / I_up, lam=self.lam)


def exact(n, k, p):
    """exact spectral entropy and the lemmas under mu_p, n <= 7."""
    import numpy as np
    E = list(itertools.combinations(range(n), 2)); idx = {e: i for i, e in enumerate(E)}; N = len(E)
    X = np.arange(1 << N, dtype=np.int64)
    pc = np.zeros(1 << N, dtype=np.int64)
    t = X.copy()
    while t.any():
        pc += t & 1
        t >>= 1
    mu = p ** pc * (1 - p) ** (N - pc)
    masks = [sum(1 << idx[e] for e in itertools.combinations(c, 2)) for c in itertools.combinations(range(n), k)]
    f = np.zeros(1 << N, dtype=bool)
    for mk in masks:
        f |= (X & mk) == mk
    A = np.where(f, -1.0, 1.0)
    sig = (p * (1 - p)) ** 0.5
    h = 1
    while h < A.size:
        A = A.reshape(-1, 2, h)
        a, b = A[:, 0, :].copy(), A[:, 1, :].copy()
        A[:, 0, :] = (1 - p) * a + p * b
        A[:, 1, :] = sig * (b - a)
        A = A.reshape(-1)
        h *= 2
    P = A ** 2
    tot = P.sum()
    nz = P > 1e-300
    H = float(-(P[nz] * np.log2(P[nz])).sum()); Is = float((P * pc).sum()); eps = 1 - float(P[0])
    vmask = [sum(1 << idx[e] for e in E if u in e) for u in range(n)]
    touch = np.stack([(X & vmask[u]) != 0 for u in range(n)], axis=1)
    v = touch.sum(axis=1)
    Ev = float((P * v).sum()); EC2 = float((P * v * (v - 1) / 2).sum())
    Vt = float((P * np.array([np.log2(float(C(n, int(t)))) for t in v])).sum())
    hh = 0 if eps <= 0 or eps >= 1 else -eps * np.log2(eps) - (1 - eps) * np.log2(1 - eps)
    prop = hh + eps * np.log2(np.e * Ev / eps) + eps * np.log2(np.e * Is / eps) + Vt + Is * np.log2(np.e * EC2 / Is)
    # Lemma 3.1 at every vertex, Lemma 3.2 at every pair (under mu_p, Harris included)
    w1 = 0.0
    for u in range(n):
        lhs = float(P[touch[:, u]].sum())
        pt = np.zeros(1 << N, dtype=bool); pa = np.zeros(1 << N, dtype=bool)
        for mk in masks:
            pr = (X & mk) == mk
            if mk & vmask[u]:
                pt |= pr
            else:
                pa |= pr
        rhs = 4 * float(mu[pt].sum()) * (1 - float(mu[pa].sum()))
        w1 = max(w1, lhs / rhs if rhs > 0 else (0.0 if lhs < 1e-15 else float('inf')))
    w2 = 0.0
    for u, w in itertools.combinations(range(n), 2):
        lhs = float(P[touch[:, u] & touch[:, w]].sum())
        inS = (X & (1 << idx[(u, w)])) != 0
        qa = np.zeros(1 << N, dtype=bool); qb = np.zeros(1 << N, dtype=bool)
        qc = np.zeros(1 << N, dtype=bool); q0 = np.zeros(1 << N, dtype=bool)
        for mk in masks:
            pr = (X & mk) == mk
            tu, tw = bool(mk & vmask[u]), bool(mk & vmask[w])
            if tu and tw:
                qc |= pr
            elif tu:
                qa |= pr
            elif tw:
                qb |= pr
            else:
                q0 |= pr
        rhs = float(P[inS].sum()) + 8 * (float(mu[qa & qb].sum()) + float(mu[qc].sum())) * (1 - float(mu[q0].sum()))
        w2 = max(w2, lhs / rhs if rhs > 0 else (0.0 if lhs < 1e-15 else float('inf')))
    return dict(H=H, Is=Is, tot=tot, prop=prop, w1=w1, w2=w2)


def main():
    if '--exact' in sys.argv:
        nmax = 7 if '--n7' in sys.argv else 6
        for n in range(4, nmax + 1):
            for k in range(3, n + 1):
                for p in (0.5, 0.3, 0.1, 0.03):
                    if 4 * p ** (k * (k - 1) // 2) < 1e-9:
                        print(f"n={n} k={k} p={p}: skipped, Pr[S nonempty] is below double-precision resolution")
                        continue
                    ex = exact(n, k, p)
                    b = BiasedClique(n, k, p).bound()
                    B = float(b['B']) if b else float('nan')
                    ok = (abs(ex['tot'] - 1) < 1e-9 and ex['H'] <= ex['prop'] + 1e-9 and ex['prop'] <= B * ex['Is'] + 1e-9
                          and ex['w1'] <= 1 + 1e-9 and ex['w2'] <= 1 + 1e-9)
                    print(f"n={n} k={k} p={p}: H/I_s={ex['H'] / ex['Is']:.4f}  Prop2.1/I_s={ex['prop'] / ex['Is']:.4f}  "
                          f"B={B:.3f}  Lemma3.1 max ratio {ex['w1']:.3f}  Lemma3.2 max ratio {ex['w2']:.3f}  "
                          f"KMS ratio H/(p log2(1/p) I_p)={float(ex['H'] * 4 * (1 - p) / (ex['Is'] * float(mp.log(1 / p, 2)))):.3f}  "
                          f"{'ok' if ok else 'FAIL'}")
        return
    for p in [mp.mpf(1) / 2, mp.mpf(1) / 4, mp.mpf(1) / 16, mp.mpf(1) / 256, mp.mpf(2) ** -16]:
        print(f"--- p = {mp.nstr(p, 6)}")
        for e in (12, 16, 20, 24, 32, 40):
            n = 2 ** e
            rows = []
            for k in range(3, 400):
                c = BiasedClique(n, k, p)
                lam = c.lam
                if lam < mp.mpf(2) ** -12:
                    break
                if lam <= 16:
                    rows.append(c)
            for c in rows:
                b = c.bound()
                if b is None:
                    print(f"n=2^{e:<2d} k={c.k:3d} lambda={mp.nstr(c.lam, 4):>10}: pivotal lower bound not positive")
                    continue
                print(f"n=2^{e:<2d} k={c.k:3d} lambda={mp.nstr(c.lam, 4):>10}: B={mp.nstr(b['B'], 5):>8}  limit {mp.nstr(b['lim'], 5):>7}  "
                      f"KMS form {mp.nstr(b['kms'], 4):>6}  [A'/I {mp.nstr(b['Ap'], 3)}, V/I {mp.nstr(b['V'], 4)}, "
                      f"jensen {mp.nstr(b['jensen'], 4)}, I_lo/I_up {mp.nstr(b['ratio'], 4)}]")


if __name__ == "__main__":
    main()
