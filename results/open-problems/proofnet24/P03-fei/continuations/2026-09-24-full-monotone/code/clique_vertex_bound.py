"""Rigorous upper bound on H/I for the k-clique property of G(n, 1/2), from the vertex-coding inequality.

Every quantity below is an explicit upper (or lower) bound proved in REPORT.md section 4:
  H <= A + log2(3) T + I log2(e (1 + R/(2 I))),
  A = h(eps) + eps log2(e I / eps),                 eps = 1 - Fhat(0)^2 = 4 q (1 - q), q = Pr[no k-clique]
  T = sum over internal nodes N of a balanced binary tree on [n] of Pr[S touches N]
      <= min(eps, 4 min(1, lambda - mu_{-N}) Pr[G - N has no k-clique])            (Parseval + Harris)
  R = sum over ordered pairs u != w of Pr[S meets E_u - uw and E_w - uw]
      <= 8 n (n-1) (E[g_A g_B] + E[g_AB]) Pr[G - {u, w} has no k-clique]         (Parseval + Harris)
  I >= C(n,2) Pr[e pivotal], Pr[e pivotal] >= max(Bonferroni, second moment) with Harris/Janson factors.
Pr[no k-clique in an n'-vertex G(n',1/2)] <= min(1, exp(-mu + Delta/2), exp(-mu^2/(2 Delta)) if Delta >= mu) (Janson).

Printed per (n, k): lambda, the bound B(n,k) >= H/I, its pieces, the ratio I_lo/I_up, and the asymptotic value
2 log2 3 + log2(e (5 + 4 lambda)). With --exact the bound is compared with the exact H/I for n <= 6.
"""
import sys
import functools
import mpmath as mp

print = functools.partial(print, flush=True)
mp.mp.dps = 60
LOG2E = 1 / mp.log(2)


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


class Clique:
    def __init__(self, n, k):
        self.n, self.k = n, k
        self.m = k * (k - 1) // 2
        self.p = mp.mpf(2) ** (-self.m)
        self.lam = C(n, k) * self.p
        self._cf = {}

    def mu_delta(self, n1):
        """expected number of k-cliques in G(n1, 1/2) and Janson's Delta (ordered pairs sharing an edge)."""
        k, p = self.k, self.p
        mu = C(n1, k) * p
        s = mp.mpf(0)
        for j in range(2, k):
            s += C(k, j) * C(n1 - k, k - j) * mp.mpf(2) ** (j * (j - 1) // 2)
        return mu, C(n1, k) * s * p * p

    def cf_up(self, n1):
        """upper bound on Pr[G(n1, 1/2) has no k-clique]."""
        if n1 in self._cf:
            return self._cf[n1]
        if n1 < self.k:
            self._cf[n1] = mp.mpf(1)
            return mp.mpf(1)
        mu, D = self.mu_delta(n1)
        b = min(mp.mpf(1), mp.exp(-mu + D / 2))
        if D >= mu and D > 0:
            b = min(b, mp.exp(-mu * mu / (2 * D)))
        self._cf[n1] = b
        return b

    def cf_lo(self, n1):
        """Harris lower bound prod (1 - p) over the cliques."""
        return mp.exp(C(n1, self.k) * mp.log1p(-self.p))

    def eps_up(self):
        n = self.n
        q_up = self.cf_up(n)
        one_minus_q_lo = -mp.expm1(C(n, self.k) * mp.log1p(-self.p))   # 1 - q_lo without cancellation
        return min(mp.mpf(1), 4 * q_up, 4 * one_minus_q_lo)

    def node_sizes(self):
        """{level: {size: count}} for internal nodes (size >= 2) of the balanced split tree, root excluded."""
        levels = []
        cur = {self.n: 1}
        while True:
            nxt = {}
            for s, c in cur.items():
                if s < 2:
                    continue
                a, b = s // 2, s - s // 2
                for t in (a, b):
                    nxt[t] = nxt.get(t, 0) + c
            nxt = {s: c for s, c in nxt.items() if s >= 2}
            if not nxt:
                break
            levels.append(nxt)
            cur = nxt
        return levels

    def tree_sum(self, eps_up):
        n, lam = self.n, self.lam
        T = eps_up          # the root is touched iff S is nonempty
        per_level = []
        for lev in self.node_sizes():
            tot = mp.mpf(0)
            for w, cnt in lev.items():
                mu_out = C(n - w, self.k) * self.p
                touch = min(mp.mpf(1), lam - mu_out)
                b = min(eps_up, 4 * touch * self.cf_up(n - w))
                tot += cnt * b
            per_level.append(tot)
            T += tot
        return T, per_level

    def infl_bounds(self):
        n, k, m, p = self.n, self.k, self.m, self.p
        N = C(n, 2)
        mu_e = C(n - 2, k - 2) * mp.mpf(2) ** (-(m - 1))
        # Harris lower bound on Pr[D | A_K]: D = no k-clique avoiding e in G - e, A_K = K - e present
        lg = mp.mpf(0)
        for j in range(0, k):
            cj = C(k, j) * C(n - k, k - j)
            if j >= 2:
                cj -= C(k - 2, j - 2) * C(n - k, k - j)
            if cj <= 0:
                continue
            e_sh = j * (j - 1) // 2
            lg += cj * mp.log1p(-mp.mpf(2) ** (-(m - e_sh)))
        EX_lo = mu_e * mp.exp(lg)
        # pairs of cliques through e
        s = mp.mpf(0)
        for j in range(2, k):
            s += C(k - 2, j - 2) * C(n - k, k - j) * mp.mpf(2) ** (-(m - j * (j - 1) // 2))
        P2 = mu_e * s
        # Pr[D] upper bound: cliques avoiding e
        mu_me = (C(n, k) - C(n - 2, k - 2)) * p
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
        n, k, p = self.n, self.k, self.p
        s = mp.mpf(0)
        for j in range(0, k):
            s += C(k - 1, j) * C(n - k - 1, k - 1 - j) * mp.mpf(2) ** (j * (j - 1) // 2)
        EAB = C(n - 2, k - 1) * s * p * p
        EC = C(n - 2, k - 2) * p
        return 8 * n * (n - 1) * (EAB + EC) * self.cf_up(n - 2), EAB, EC

    def bound(self):
        eps = self.eps_up()
        T, per_level = self.tree_sum(eps)
        I_lo, I_up = self.infl_bounds()
        R, EAB, EC = self.mixed()
        if I_lo <= 0:
            return None
        # A = h(eps) + eps log2(e I/eps); x -> x log2(e I/x) increases in I, and in x for x <= I, and eps <= I
        x = min(eps, I_up)
        A = h2(min(eps, mp.mpf('0.5'))) + x * log2(mp.e * I_up / x)
        tree_term = mp.log(3, 2) * T / I_lo
        jensen = log2(mp.e * (1 + R / (2 * I_lo)))
        B_tree = A / I_lo + tree_term + jensen
        # direct coding of V(S): H(V(S)) <= H(v) + E log2 C(n, v).  E v = sum_u Pr[S touches u], and
        # Pr[S touches u] <= min(eps, 4 (lambda k/n) Pr[G - u clique-free])  (Lemma 3.1 at W = {u}).
        n, k = self.n, self.k
        Ev = n * min(eps, 4 * min(mp.mpf(1), self.lam * k / n) * self.cf_up(n - 1))
        # E log2 C(n, v) <= E v log2(e n/v) <= eps phi(E v/eps), phi(y) = y log2(e n/y) concave (v >= 2 when S is
        # nonempty); maximising over the unknowns eps <= eps_up and E v <= Ev gives c log2(e n eps_up/c), c = min(Ev, n eps_up)
        c = min(Ev, n * eps)
        V = c * log2(mp.e * n * eps / c) if c > 0 else mp.mpf(0)
        # H(v) <= h(eps) + eps log2(e E[v | S nonempty]); x -> x log2(e c/x) increases for x <= c, and E v >= 2 eps
        x1 = min(eps, Ev)
        Ap = A + (x1 * log2(mp.e * Ev / x1) if x1 > 0 else mp.mpf(0))
        B_direct = Ap / I_lo + V / I_lo + jensen
        B = min(B_tree, B_direct)
        return dict(B=B, B_tree=B_tree, B_direct=B_direct, A=A / I_lo, Ap=Ap / I_lo, V_over_I=V / I_lo,
                    tree=tree_term, T_over_I=T / I_lo, jensen=jensen, R_over_2I=R / (2 * I_lo),
                    I_lo=I_lo, I_up=I_up, eps=eps, lam=self.lam)


def exact_ratio(n, k):
    import itertools
    import numpy as np
    E = list(itertools.combinations(range(n), 2)); idx = {e: i for i, e in enumerate(E)}; N = len(E)
    x = np.arange(1 << N)
    f = np.zeros(1 << N, dtype=bool)
    for c in itertools.combinations(range(n), k):
        mk = sum(1 << idx[e] for e in itertools.combinations(c, 2))
        f |= (x & mk) == mk
    a = np.where(f, -1.0, 1.0); h = 1
    while h < a.size:
        a = a.reshape(-1, 2 * h); u = a[:, :h].copy(); v = a[:, h:].copy()
        a[:, :h] = u + v; a[:, h:] = u - v; a = a.reshape(-1); h *= 2
    P = (a / a.size) ** 2
    size = np.array([bin(t).count('1') for t in x])
    nz = P > 0
    H = float(-(P[nz] * np.log2(P[nz])).sum()); I = float((P * size).sum())
    return H / I


def main():
    if '--exact' in sys.argv:
        for n, k in [(4, 3), (5, 3), (5, 4), (6, 3), (6, 4), (6, 5)]:
            b = Clique(n, k).bound()
            r = exact_ratio(n, k)
            print(f"n={n} k={k}: exact H/I = {r:.4f};  bound = {mp.nstr(b['B'], 6) if b else 'none (I_lo <= 0)'}")
        return
    for e in list(range(5, 41)):
        n = 2 ** e
        ks = []
        for k in range(3, 200):
            lam = Clique(n, k).lam
            if lam < mp.mpf(2) ** -12:
                break
            if lam <= 64:
                ks.append(k)
        for k in ks:
            c = Clique(n, k)
            b = c.bound()
            lam = c.lam
            asym = 2 + log2(mp.e * (5 + 4 * lam))
            if b is None:
                print(f"n=2^{e:<2d} k={k:3d} lambda={mp.nstr(lam, 4):>10}: I lower bound not positive")
                continue
            print(f"n=2^{e:<2d} k={k:3d} lambda={mp.nstr(lam, 4):>10}: B={mp.nstr(b['B'], 5):>8} "
                  f"(direct {mp.nstr(b['B_direct'], 5)}, tree {mp.nstr(b['B_tree'], 5)}) "
                  f"[A'/I {mp.nstr(b['Ap'], 3)}, V/I {mp.nstr(b['V_over_I'], 4)}, T/I {mp.nstr(b['T_over_I'], 4)}, "
                  f"jensen {mp.nstr(b['jensen'], 4)}, R/2I {mp.nstr(b['R_over_2I'], 4)}, I_lo/I_up {mp.nstr(b['I_lo'] / b['I_up'], 4)}, "
                  f"I_lo {mp.nstr(b['I_lo'], 4)}]  asym {mp.nstr(asym, 4)}")


if __name__ == "__main__":
    main()
