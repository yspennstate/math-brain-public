#!/usr/bin/env python3
"""Two-level tree DNF: exact erasure entropy at the root against the nested and the r-element witnesses.

The function (FLOW 12(o), test T1).  Root variable x; D blocks t of L = w - 1 mates z_{t,j}; each mate carries
Q_{t,j} = OR of D - 1 disjoint ANDs of width L on fresh variables (so P[Q = 1] = q = 1 - (1 - 2^-L)^(D-1)):

    f = [ x and OR_t AND_j z_{t,j} ]  or  OR_{t,j} [ z_{t,j} and Q_{t,j} ].

With N_t = prod_j (1 - z_{tj} Q_{tj}), A_t = prod_j z_{tj}, N = prod_t N_t, M = prod_t (1 - A_t) N_t (0/1 values)
the +-1 function has  g = E_x f = N + M - 1  and  h = D_x f = N - M  (up to sign).  In the orthonormal basis
{1, chi_z, phi_Q, chi_z phi_Q} per mate (phi = (Q - q)/sigma) the spectrum is a tensor product over the blocks,
and the spectral measure of f is this "biased" spectrum times independent normalised spectra of the Q's, which
do not depend on whether the root is in the set.  Hence, with a = prod_t n(tau_t), b = prod_t m(tau_t),

    E_root = sum over type tuples T of  Phi( (a + b)^2 , (a - b)^2 ),      Inf_root = sum_T (a - b)^2

(the empty tuple has (a + b - 1)^2 in the first slot).  The sum is estimated by importance sampling with an
exactly known proposal; every summand is evaluated exactly.  The witnesses for the order "leaves first, mates
last" are closed forms in the block resampling moments and are evaluated in 80-digit decimals.

usage:  tree_dnf.py selftest
        tree_dnf.py run W D [SAMPLES [SEED [RMAX]]]      (RMAX = 1, 2 or 3: largest witness window computed)
"""
import sys, math, time
from decimal import Decimal, getcontext
import numpy as np

getcontext().prec = 80


def h2(x):
    x = np.clip(x, 0.0, 1.0)
    with np.errstate(divide="ignore", invalid="ignore"):
        r = -(np.where(x > 0, x * np.log2(x), 0.0) + np.where(x < 1, (1 - x) * np.log2(1 - x), 0.0))
    return r


def Phi(p, q):
    s = p + q
    with np.errstate(divide="ignore", invalid="ignore"):
        r = np.where(s > 0, s * h2(np.where(s > 0, q / s, 0.0)), 0.0)
    return r


def phi_scalar(p, q):
    p, q = float(p), float(q)
    if p <= 0 or q <= 0:
        return 0.0
    s = p + q
    return -(p * math.log2(p / s) + q * math.log2(q / s))


class Tree:
    def __init__(self, w, D):
        self.w, self.D, self.L = w, D, w - 1
        L = self.L
        q = 1.0 - (1.0 - 2.0 ** -L) ** (D - 1)
        self.q = q
        sg = math.sqrt(q * (1 - q))
        a = [1 - q / 2, q / 2, -sg / 2, sg / 2]            # 1 - zQ
        b = [(1 - q) / 2, -(1 - q) / 2, -sg / 2, sg / 2]   # z (1 - Q)
        types, mult, nv, bv = [], [], [], []
        for c0 in range(L + 1):
            for c1 in range(L + 1 - c0):
                for c2 in range(L + 1 - c0 - c1):
                    c3 = L - c0 - c1 - c2
                    types.append((c0, c1, c2, c3))
                    mult.append(math.factorial(L) // (math.factorial(c0) * math.factorial(c1)
                                                      * math.factorial(c2) * math.factorial(c3)))
                    nv.append(a[0] ** c0 * a[1] ** c1 * a[2] ** c2 * a[3] ** c3)
                    bv.append(b[0] ** c0 * b[1] ** c1 * b[2] ** c2 * b[3] ** c3)
        self.types = types
        self.mult = np.array(mult, dtype=float)
        self.n = np.array(nv)
        self.beta = np.array(bv)
        self.m = self.n - self.beta
        for k, t in enumerate(types):
            if t[0] == 0 and t[1] == 0:
                self.m[k] = 0.0                              # identical factors: exactly zero
        self.zero = types.index((L, 0, 0, 0))
        self.Zn = float((self.mult * self.n ** 2).sum())
        self.Zm = float((self.mult * self.m ** 2).sum())
        self.Zb = float((self.mult * self.beta ** 2).sum())
        self.pn = self.mult * self.n ** 2 / self.Zn
        self.pm = self.mult * self.m ** 2 / self.Zm
        self.pb = self.mult * self.beta ** 2 / self.Zb
        self.inf = self.Zn ** D - self.Zm ** D
        # decimal tables of the block resampling moments (r mates of the block resampled)
        qd = 1 - (1 - Decimal(2) ** -L) ** (D - 1)
        self.NN = [(1 - qd / 2) ** (L - r) * (1 - 3 * qd / 4) ** r for r in range(L + 1)]
        bb = [((1 - qd) / 2) ** (L - r) * ((1 - qd) / 4) ** r for r in range(L + 1)]
        Nb = ((1 - qd) / 2) ** L
        self.NM = [x - Nb for x in self.NN]
        self.MM = [self.NN[r] - 2 * Nb + bb[r] for r in range(L + 1)]
        self.EN = self.NN[0] ** D
        self.EM = self.NM[0] ** D
        self.inf_d = self.EN - self.EM

    # ---------- exact value of the sum, for small cases ----------
    def exact(self):
        K, D = len(self.types), self.D
        if K ** D > 4_000_000:
            return None
        idx = np.indices((K,) * D).reshape(D, -1).T
        return self._terms(idx)[0].sum()

    def _terms(self, idx):
        nv, mv, bv = self.n[idx], self.m[idx], self.beta[idx]
        mu = self.mult[idx].prod(axis=1)
        a = nv.prod(axis=1)
        b = mv.prod(axis=1)
        D = self.D
        pm = np.ones((idx.shape[0], D))
        sn = np.ones((idx.shape[0], D))
        for t in range(1, D):
            pm[:, t] = pm[:, t - 1] * mv[:, t - 1]
        for t in range(D - 2, -1, -1):
            sn[:, t] = sn[:, t + 1] * nv[:, t + 1]
        diff = (pm * bv * sn).sum(axis=1)
        p = (a + b) ** 2
        z = (idx == self.zero).all(axis=1)
        p = np.where(z, (a + b - 1) ** 2, p)
        q = diff ** 2
        return mu * Phi(p, q), mu * q, mu * (p + q), (a, b, pm, bv, sn)

    # ---------- importance sampling ----------
    def mc(self, samples, seed, batch=50_000):
        rng = np.random.default_rng(seed)
        D, K = self.D, len(self.types)
        batch = max(500, min(batch, 1_500_000 // D))
        wts = np.array([0.25, 0.25] + [0.5 / D] * D)
        s1 = np.zeros(3)
        s2 = np.zeros(3)
        done = 0
        cols = np.arange(D)[None, :]
        while done < samples:
            B = min(batch, samples - done)
            comp = rng.choice(D + 2, size=B, p=wts)
            In = rng.choice(K, size=(B, D), p=self.pn)
            Im = rng.choice(K, size=(B, D), p=self.pm)
            Ib = rng.choice(K, size=(B, D), p=self.pb)
            tcol = (comp - 2)[:, None]
            tele = (comp >= 2)[:, None]
            use_m = (comp == 1)[:, None] | (tele & (cols < tcol))
            use_b = tele & (cols == tcol)
            idx = np.where(use_m, Im, np.where(use_b, Ib, In))
            f, qq, tot, (a, b, pm, bv, sn) = self._terms(idx)
            mu = self.mult[idx].prod(axis=1)
            dens = 0.25 * a ** 2 / self.Zn ** D + 0.25 * b ** 2 / self.Zm ** D
            tt = np.arange(D)[None, :]
            dens = dens + (0.5 / D) * ((pm ** 2 / self.Zm ** tt) * (bv ** 2 / self.Zb)
                                       * (sn ** 2 / self.Zn ** (D - 1 - tt))).sum(axis=1)
            dens = dens * mu
            for k, v in enumerate((f, qq, tot)):
                x = v / dens
                s1[k] += x.sum()
                s2[k] += (x * x).sum()
            done += B
        mean = s1 / done
        se = np.sqrt(np.maximum(s2 / done - mean ** 2, 0) / done)
        return mean, se

    # ---------- witnesses for "leaves first, mates last" ----------
    def _prod(self, tab, c):
        r = Decimal(1)
        for x in c:
            r *= tab[x]
        return r

    def WG(self, c):
        """W(R) = P[root in U, U misses R],  G(R) = P[root not in U, U misses R]; c = resampled mates per block."""
        a, b, d = self._prod(self.NN, c), self._prod(self.NM, c), self._prod(self.MM, c)
        return a - 2 * b + d, a + 2 * b + d - 2 * (self.EN + self.EM) + 1

    def order(self, kind):
        D, L = self.D, self.L
        if kind == "block":
            return [t for t in range(D) for _ in range(L)]
        return [t for _ in range(L) for t in range(D)]       # round robin

    def _base(self, c):
        return (self._prod(self.NN, c), self._prod(self.NM, c), self._prod(self.MM, c))

    def _wg(self, base, c, blocks=()):
        """WG of c with one mate fewer in each listed block (a block may be listed more than once)."""
        a, b, d = base
        if blocks:
            cnt = {}
            for t in blocks:
                cnt[t] = cnt.get(t, 0) + 1
            for t, k in cnt.items():
                x = c[t]
                a = a * self.NN[x - k] / self.NN[x]
                b = b * self.NM[x - k] / self.NM[x]
                d = d * self.MM[x - k] / self.MM[x]
        return a - 2 * b + d, a + 2 * b + d - 2 * (self.EN + self.EM) + 1

    def witness(self, kind, rmax=2):
        """{r: L^r} for the statistic "the last r revealed elements of U among the mates" (mates revealed last).

        Same quantity as witness_slow; blocks with the same number of resampled mates are grouped, so the cost
        is linear in the number of mates."""
        D, L = self.D, self.L
        od = self.order(kind)
        Z = len(od)
        pref = [[0] * D]
        for k in range(Z):
            c = pref[-1][:]
            c[od[k]] += 1
            pref.append(c)
        bases = [self._base(c) for c in pref]
        WGp = [self._wg(bases[k], pref[k]) for k in range(Z + 1)]
        out = {}
        none = phi_scalar(WGp[Z][1], WGp[Z][0])
        tot = none
        for k in range(1, Z + 1):
            tot += phi_scalar(WGp[k - 1][1] - WGp[k][1], WGp[k - 1][0] - WGp[k][0])
        out[1] = tot
        if rmax < 2:
            return out

        def classes(c, cb, special=None):
            g = {}
            for t in range(D):
                if cb[t] == 0:
                    continue
                e = g.setdefault((c[t], t == special), [[], 0, cb[t]])
                if len(e[0]) < 2:
                    e[0].append(t)
                e[1] += 1
            return g

        def pairs(c, cb, special, fn):
            g = classes(c, cb, special)
            keys = sorted(g)
            s = 0.0
            for ia, ka in enumerate(keys):
                ra, na, ma = g[ka]
                if ma >= 2:
                    s += na * (ma * (ma - 1) // 2) * fn(ra[0], ra[0])
                if na >= 2:
                    s += (na * (na - 1) // 2) * ma * ma * fn(ra[0], ra[1])
                for kb in keys[ia + 1:]:
                    rb, nb, mb = g[kb]
                    s += na * ma * nb * mb * fn(ra[0], rb[0])
            return s

        cz, bz = pref[Z], bases[Z]
        wz, gz = WGp[Z]
        single = 0.0
        for rep, num, mult in classes(cz, cz).values():
            w1, g1 = self._wg(bz, cz, (rep[0],))
            single += num * mult * phi_scalar(g1 - gz, w1 - wz)
        tot2 = none + single
        for k2 in range(2, Z + 1):
            c2, b2, t2 = pref[k2], bases[k2], od[k2 - 1]
            wf, gf = WGp[k2]
            wa, ga = self._wg(b2, c2, (t2,))
            for rep, num, mult in classes(c2, pref[k2 - 1], t2).values():
                t1 = rep[0]
                wb, gb = self._wg(b2, c2, (t1,))
                wc, gc = self._wg(b2, c2, (t1, t2))
                tot2 += num * mult * phi_scalar(gc - ga - gb + gf, wc - wa - wb + wf)
        out[2] = tot2
        if rmax < 3:
            return out

        def exact_pair(ta, tb):
            x = [self._wg(bz, cz, s) for s in ((ta, tb), (ta,), (tb,))]
            return phi_scalar(x[0][1] - x[1][1] - x[2][1] + gz, x[0][0] - x[1][0] - x[2][0] + wz)

        tot3 = none + single + pairs(cz, cz, None, exact_pair)
        for k3 in range(3, Z + 1):
            c3, b3, t3 = pref[k3], bases[k3], od[k3 - 1]

            def triple(ta, tb):
                w = g = Decimal(0)
                for sub, sign in (((ta, tb, t3), 1), ((ta, tb), -1), ((ta, t3), -1), ((tb, t3), -1),
                                  ((ta,), 1), ((tb,), 1), ((t3,), 1), ((), -1)):
                    ww, gg = self._wg(b3, c3, sub)
                    w += sign * ww
                    g += sign * gg
                return phi_scalar(g, w)

            tot3 += pairs(c3, pref[k3 - 1], t3, triple)
        out[3] = tot3
        return out

    def witness_slow(self, kind, rmax=2):
        """Direct evaluation, kept as the reference for the self-test."""
        D, L = self.D, self.L
        od = self.order(kind)
        Z = len(od)
        pref = [[0] * D]
        for k in range(Z):
            c = pref[-1][:]
            c[od[k]] += 1
            pref.append(c)
        WGp = [self.WG(c) for c in pref]
        out = {}
        # r = 1
        tot = 0.0
        for k in range(1, Z + 1):
            tot += phi_scalar(WGp[k - 1][1] - WGp[k][1], WGp[k - 1][0] - WGp[k][0])
        out[1] = tot + phi_scalar(WGp[Z][1], WGp[Z][0])
        if rmax < 2:
            return out

        def less(c, *blocks):
            c = c[:]
            for t in blocks:
                c[t] -= 1
            return c

        # r = 2: atoms "U meets the mates exactly in {k1, k2} among the last k2", singles, none
        tot2 = phi_scalar(WGp[Z][1], WGp[Z][0])
        cz = pref[Z]
        for k1 in range(1, Z + 1):                            # U meets the mates in {k1} only
            w1, g1 = self.WG(less(cz, od[k1 - 1]))
            tot2 += phi_scalar(g1 - WGp[Z][1], w1 - WGp[Z][0])
        # cache F(R_k2 minus one element of block t) by (k2, t)
        cache1 = {}
        for k2 in range(2, Z + 1):
            c2 = pref[k2]
            w_full, g_full = WGp[k2]
            t2 = od[k2 - 1]
            if (k2, t2) not in cache1:
                cache1[(k2, t2)] = self.WG(less(c2, t2))
            w_a, g_a = cache1[(k2, t2)]                       # R minus k2
            seen = {}
            for k1 in range(1, k2):
                t1 = od[k1 - 1]
                if t1 not in seen:
                    seen[t1] = (self.WG(less(c2, t1)), self.WG(less(c2, t1, t2)))
                (w_b, g_b), (w_c, g_c) = seen[t1]             # R minus k1 ; R minus k1, k2
                tot2 += phi_scalar(g_c - g_a - g_b + g_full, w_c - w_a - w_b + w_full)
        out[2] = tot2
        if rmax < 3:
            return out
        # r = 3: atoms with exactly {k1 < k2 < k3} among the last k3; pairs alone; singles; none
        tot3 = phi_scalar(WGp[Z][1], WGp[Z][0])
        for k1 in range(1, Z + 1):
            w1, g1 = self.WG(less(cz, od[k1 - 1]))
            tot3 += phi_scalar(g1 - WGp[Z][1], w1 - WGp[Z][0])
        memo = {}

        def F(c, blocks):
            key = (tuple(c), tuple(sorted(blocks)))
            if key not in memo:
                memo[key] = self.WG(less(c, *blocks))
            return memo[key]

        for k2 in range(2, Z + 1):                            # U meets the mates exactly in {k1, k2}
            for t1 in set(od[:k2 - 1]):
                cnt = od[:k2 - 1].count(t1)
                t2 = od[k2 - 1]
                w = F(cz, (t1, t2))[0] - F(cz, (t1,))[0] - F(cz, (t2,))[0] + WGp[Z][0]
                g = F(cz, (t1, t2))[1] - F(cz, (t1,))[1] - F(cz, (t2,))[1] + WGp[Z][1]
                tot3 += cnt * phi_scalar(g, w)
        for k3 in range(3, Z + 1):
            c3 = pref[k3]
            t3 = od[k3 - 1]
            memo.clear()
            before = od[:k3 - 1]
            # multiset of unordered pairs of blocks among the first k3 - 1 positions
            cntb = {}
            for t in before:
                cntb[t] = cntb.get(t, 0) + 1
            keys = sorted(cntb)
            for ia, ta in enumerate(keys):
                for tb in keys[ia:]:
                    npairs = cntb[ta] * (cntb[ta] - 1) // 2 if ta == tb else cntb[ta] * cntb[tb]
                    if npairs == 0:
                        continue
                    w = g = Decimal(0)
                    for sub, sign in (((ta, tb, t3), 1), ((ta, tb), -1), ((ta, t3), -1), ((tb, t3), -1),
                                      ((ta,), 1), ((tb,), 1), ((t3,), 1), ((), -1)):
                        ww, gg = F(c3, sub)
                        w += sign * ww
                        g += sign * gg
                    tot3 += npairs * phi_scalar(g, w)
        out[3] = tot3
        return out


def report(w, D, samples, seed, rmax, out=sys.stdout):
    t0 = time.time()
    T = Tree(w, D)
    inf = T.inf
    triv = float(h2(np.array(inf))) / inf
    print("tree DNF  w=%d  D=%d  mates=%d  types per block=%d  q=%.5f  P[N=1]=%.4f"
          % (w, D, D * T.L, len(T.types), T.q, T.Zn ** D), file=out)
    print("  Inf_root = %.6e   trivial h2(Inf)/Inf = %.4f   log2 D + 2 = %.4f" % (inf, triv, math.log2(D) + 2),
          file=out)
    ex = T.exact()
    if ex is not None:
        print("  E_root/Inf exact enumeration = %.5f" % (ex / inf), file=out)
    if samples:
        mean, se = T.mc(samples, seed)
        print("  E_root/Inf importance sampling = %.5f +- %.5f   (checks: Inf ratio %.5f +- %.5f, total mass %.5f +- %.5f; %d samples)"
              % (mean[0] / inf, se[0] / inf, mean[1] / inf, se[1] / inf, mean[2], se[2], samples), file=out)
    for kind in ("block", "robin"):
        wv = T.witness(kind, rmax)
        print("  mates last, %-5s order:  " % kind
              + "   ".join("L%d/Inf = %.5f" % (r, wv[r] / inf) for r in sorted(wv)), file=out)
    print("  (%.0f s)" % (time.time() - t0), file=out)
    out.flush()


def selftest():
    ok = True
    # 1. importance sampling against exact enumeration on small cases
    for w, D in ((3, 2), (4, 2), (3, 3), (5, 2)):
        T = Tree(w, D)
        ex = T.exact()
        mean, se = T.mc(400_000, 1)
        good = (abs(mean[0] - ex) < 5 * se[0] + 1e-12 and abs(mean[1] - T.inf) < 5 * se[1] + 1e-12
                and abs(mean[2] - 1) < 5 * se[2] + 1e-9)
        ok &= good
        print("w=%d D=%d  E exact %.6f  mc %.6f +- %.6f   Inf exact %.6f mc %.6f   mass %.6f   %s"
              % (w, D, ex, mean[0], se[0], T.inf, mean[1], mean[2], "ok" if good else "FAIL"))
    # 2. the model against a brute-force truth table (w = 3, D = 2: 1 + 4 + 4*2 variables = 13)
    w, D = 3, 2
    T = Tree(w, D)
    L = w - 1
    nz = D * L
    nvar = 1 + nz + nz * (D - 1) * L
    xs = np.arange(1 << nvar, dtype=np.int64)
    bit = lambda k: (xs >> k) & 1
    z = [bit(1 + k) for k in range(nz)]
    Bv = np.zeros_like(xs)
    for t in range(D):
        At = np.ones_like(xs)
        for j in range(L):
            At &= z[t * L + j]
        Bv |= At
    G = np.zeros_like(xs)
    pos = 1 + nz
    for k in range(nz):
        Qk = np.zeros_like(xs)
        for s in range(D - 1):
            Cs = np.ones_like(xs)
            for j in range(L):
                Cs &= bit(pos)
                pos += 1
            Qk |= Cs
        G |= z[k] & Qk
    f = (bit(0) & Bv) | G
    v = (1 - 2 * f).astype(np.float64)
    hlen = 1
    while hlen < len(v):                                      # Walsh-Hadamard
        v = v.reshape(-1, 2, hlen)
        v = np.stack((v[:, 0] + v[:, 1], v[:, 0] - v[:, 1]), axis=1).reshape(-1)
        hlen *= 2
    mu = (v / len(v)) ** 2
    p, q = mu[0::2], mu[1::2]                                 # root is bit 0
    E_bf = float(Phi(p, q).sum())
    inf_bf = float(q.sum())
    good = abs(E_bf - T.exact()) < 1e-9 and abs(inf_bf - T.inf) < 1e-12
    ok &= good
    print("truth table (13 variables): E %.9f  model %.9f   Inf %.9f  model %.9f   %s"
          % (E_bf, T.exact(), inf_bf, T.inf, "ok" if good else "FAIL"))
    # 3. witnesses against the truth table: statistic = last r revealed mates of U, mates last, block order
    masks = np.arange(len(mu) // 2, dtype=np.int64)           # T = set without the root, bit k-1 of masks
    zmask = masks & ((1 << nz) - 1)
    for kind in ("block", "robin"):
        od = T.order(kind)
        # position k (1-based) is a mate of block od[k-1]; map to concrete mates in order of appearance
        used = [0] * D
        zidx = []
        for t in od:
            zidx.append(t * L + used[t])
            used[t] += 1
        wv = T.witness(kind, 3)
        for r in (1, 2, 3):
            key = np.zeros_like(masks)
            cnt = np.zeros_like(masks)
            for k, zi in enumerate(zidx):                     # k = 0 is the last revealed
                present = (zmask >> zi) & 1
                take = (present == 1) & (cnt < r)
                key = np.where(take, key | (1 << k), key)
                cnt = cnt + take
            A = np.bincount(key, weights=p, minlength=1 << nz)
            Bq = np.bincount(key, weights=q, minlength=1 << nz)
            Lbf = float(Phi(A, Bq).sum())
            good = abs(Lbf - wv[r]) < 1e-9
            ok &= good
            print("witness r=%d %-5s: truth table %.9f  closed form %.9f   %s"
                  % (r, kind, Lbf, wv[r], "ok" if good else "FAIL"))
    # 4. grouped evaluation against the direct one
    for w, D in ((4, 3), (5, 4), (6, 3)):
        T = Tree(w, D)
        for kind in ("block", "robin"):
            fa, sl = T.witness(kind, 3), T.witness_slow(kind, 3)
            good = all(abs(fa[r] - sl[r]) < 1e-12 for r in (1, 2, 3))
            ok &= good
            print("grouped vs direct w=%d D=%d %-5s: %s   %s"
                  % (w, D, kind, " ".join("%.10f" % fa[r] for r in (1, 2, 3)), "ok" if good else "FAIL"))
    print("SELFTEST PASS" if ok else "SELFTEST FAIL")
    return ok


def main():
    if len(sys.argv) >= 2 and sys.argv[1] == "selftest":
        sys.exit(0 if selftest() else 1)
    if len(sys.argv) >= 4 and sys.argv[1] == "run":
        w, D = int(sys.argv[2]), int(sys.argv[3])
        samples = int(sys.argv[4]) if len(sys.argv) > 4 else 1_000_000
        seed = int(sys.argv[5]) if len(sys.argv) > 5 else 1
        rmax = int(sys.argv[6]) if len(sys.argv) > 6 else 2
        report(w, D, samples, seed, rmax)
        return
    print(__doc__)


if __name__ == "__main__":
    main()
