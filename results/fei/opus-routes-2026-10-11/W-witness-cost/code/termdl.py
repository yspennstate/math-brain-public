"""Term decision lists f = tau_1 ? g_1 : tau_2 ? g_2 : ... : g_{m+1} (terms = AND of fresh blocks X_k of width w_k,
outputs g_j on fresh blocks), represented by the UNFOLDED decision tree: one gate per path
pi = (t_1..t_{j-1}) -> output j, where t_k = first failing position in block k (path tests x_{k,1..t_k}).
Gate h_pi = [x in cell(pi)] AND [g_j = 1].

Exact spectral law (NOTES section 11) sampled by Monte Carlo; code length per sampled set A bounded by
  Lambda_1 + log(1/sum_{owners} pi) + E_{owner ~ pi-weights}[rank cost] + log(s(s+1)) + 1 + s log(2ea/(a-1)) + data rank,
which is a valid upper bound on log(1/Q_{1,1}(A)) by Lemma 3.2 and Jensen (sum_pi w_pi e^{x_pi} >= e^{sum w x}).
Outputs supported: 'dict' (a fresh dictator, mean 0), 'and'/'or' of width u, 'const+1'/'const-1'.
EVIDENCE only (Monte Carlo + floating point).
"""
import math
import random

A_EXP = 6.0 / 5.0


def out_stats(kind, u=1):
    """(P(g=1), Var, I(g), list of (B-size, mass) of nonempty spectrum with B-rank cost function)."""
    if kind == 'dict':
        return 0.5, 1.0, 1.0
    if kind in ('and', 'or'):
        d = 2.0 ** (-u)
        P = d if kind == 'and' else 1 - d
        return P, 4 * d * (1 - d), 2 * u * d
    if kind == 'const+1':
        return 1.0, 0.0, 0.0
    if kind == 'const-1':
        return 0.0, 0.0, 0.0
    raise ValueError(kind)


class TermDL:
    def __init__(self, widths, outputs):
        """widths: list of m term widths; outputs: list of m+1 (kind, u)."""
        self.w = widths
        self.m = len(widths)
        self.q = [2.0 ** (-w) for w in widths]
        self.out = outputs
        st = [out_stats(k, u) for k, u in outputs]
        self.P = [s[0] for s in st]
        self.Var = [s[1] for s in st]
        self.Ig = [s[2] for s in st]
        self.mu = [2 * p - 1 for p in self.P]
        m = self.m
        # reach probabilities and E_j probabilities
        self.reach = [1.0] * (m + 2)
        for k in range(m):
            self.reach[k + 1] = self.reach[k] * (1 - self.q[k])
        self.PE = [self.reach[j] * (self.q[j] if j < m else 1.0) for j in range(m + 1)]
        # conditional mean after K false: m_after[K] = E[mu_J | tau_0..tau_K false]
        self.m_after = [0.0] * (m + 1)
        acc = self.mu[m]
        self.m_after[m - 1] = acc if m >= 1 else 0
        for K in range(m - 2, -1, -1):
            acc = self.q[K + 1] * self.mu[K + 1] + (1 - self.q[K + 1]) * acc
            self.m_after[K] = acc
        # masses by type
        self.types = []
        for j in range(m + 1):
            if self.Var[j] > 0:
                self.types.append(('blk', j, self.PE[j] * self.Var[j]))
        for K in range(m):
            dK = self.mu[K] - self.m_after[K]
            wK = self.reach[K] * self.q[K] * (1 - self.q[K]) * dK * dK
            if wK > 0:
                self.types.append(('phi', K, wK))
        self.v = sum(t[2] for t in self.types)
        self.Pf1 = sum(self.PE[j] * self.P[j] for j in range(m + 1))

    # ----- exact influence -----
    def influence(self):
        I = 0.0
        ene = lambda w: (w / 2.0) * (2 ** w) / (2 ** w - 1)  # E|S| for uniform nonempty S
        pref = [0.0] * (self.m + 1)
        for k in range(self.m):
            pref[k + 1] = pref[k] + self.q[k] * ene(self.w[k])
        for typ, j, mass in self.types:
            if typ == 'blk':
                ET = pref[j] + (self.w[j] / 2.0 if j < self.m else 0.0)
                I += mass * ET + self.PE[j] * self.Ig[j]
            else:
                I += mass * (pref[j] + ene(self.w[j]))
        return I

    # ----- sampling -----
    def sample_S(self, rng, k, nonempty=None):
        """Sample S_k: if nonempty None: empty w.p. 1-q_k else uniform nonempty; True: uniform nonempty;
        'all': uniform over all subsets."""
        w = self.w[k]
        if nonempty is None:
            if rng.random() < 1 - self.q[k]:
                return ()
            nonempty = True
        while True:
            S = tuple(i for i in range(w) if rng.random() < 0.5)
            if nonempty == 'all' or S:
                return S

    def sample_set(self, rng):
        r = rng.random() * self.v
        for typ, j, mass in self.types:
            r -= mass
            if r <= 0:
                break
        Ss = {}
        for k in range(j):
            Ss[k] = self.sample_S(rng, k)
        if typ == 'blk':
            if j < self.m:
                Ss[j] = self.sample_S(rng, j, 'all')
            data = 1  # a nonempty data set; size handled below
        else:
            Ss[j] = self.sample_S(rng, j, True)
            data = 0
        return typ, j, Ss

    # ----- owner distribution and rank cost -----
    @staticmethod
    def P_t_ge(m_, w):
        """P(t >= m_ AND block false) for t = first failure position (uniform bits)."""
        if m_ <= 0:
            return 1 - 2.0 ** (-w)
        return 2.0 ** (1 - m_) - 2.0 ** (-w)

    def sample_t(self, rng, k, mmin):
        """Sample failure position t >= max(mmin,1) of block k from P(t) proportional to 2^{-t}."""
        w = self.w[k]
        lo = max(mmin, 1)
        weights = [2.0 ** (-t) for t in range(lo, w + 1)]
        r = rng.random() * sum(weights)
        for t, wt in zip(range(lo, w + 1), weights):
            r -= wt
            if r <= 0:
                return t
        return w

    def owner_mass_and_sampler(self, typ, j, Ss):
        """Return (sum of pi over owners, list of (prob, output index J, fixed-true block)) for sampling."""
        base = 1.0
        for k in range(j):
            base *= self.P_t_ge(max(Ss[k]) + 1 if Ss[k] else 0, self.w[k])
        if typ == 'blk':
            qj = self.q[j] if j < self.m else 1.0
            return base * qj * self.P[j], [(1.0, j)]
        # phi-set with top block K=j: owners = path to J=K (block K full) or J>K (t_K >= max S_K)
        K = j
        opts = []
        o0 = self.q[K] * self.P[K]
        opts.append((o0, K))
        mK = max(Ss[K]) + 1
        tail = self.P_t_ge(mK, self.w[K])
        acc = 1.0
        for J in range(K + 1, self.m + 1):
            qJ = self.q[J] if J < self.m else 1.0
            opts.append((tail * acc * qJ * self.P[J], J))
            if J < self.m:
                acc *= (1 - self.q[J])
        tot = sum(o for o, _ in opts)
        return base * tot, [(o / tot, J) for o, J in opts if tot > 0]

    def rank_cost(self, rng, typ, j, Ss, order, s, nsamp=8, exactZ=False, bsz=0):
        """E over owner paths of a*sum log+(r/s) for control elements, by sampling owners.
        With exactZ, also adds log2 Z_s of the sampled gate (path conjunction ranks 1..L plus the output's
        own ranks 1..u) minus the uniform bound s*log2(2ea/(a-1)) that code_length_mc adds separately."""
        mass, opts = self.owner_mass_and_sampler(typ, j, Ss)
        tot = 0.0
        for _ in range(nsamp):
            r = rng.random()
            for p, J in opts:
                r -= p
                if r <= 0:
                    break
            # build path: for k < J: t_k (>= max S_k+1 if S_k nonempty, for k<=j constraints), J block full
            segs = []
            for k in range(J):
                mmin = (max(Ss[k]) + 1) if (k in Ss and Ss[k]) else 0
                if k < j or (typ == 'phi' and k == j and J > j):
                    t = self.sample_t(rng, k, mmin)
                else:
                    t = self.sample_t(rng, k, 0)
                segs.append((k, t, False))
            if J < self.m:
                segs.append((J, self.w[J], True))
            # order
            if order == 'natural':
                seq = segs
            elif order == 'sorted':
                full = [g for g in segs if g[2]]
                pre = sorted([g for g in segs if not g[2]], key=lambda g: (-g[1], g[0]))
                seq = full + pre
            elif order == 'deficit':
                full = [g for g in segs if g[2]]
                pre = sorted([g for g in segs if not g[2]], key=lambda g: (self.w[g[0]] - g[1], g[1], g[0]))
                seq = full + pre
            else:
                raise ValueError(order)
            pos = 0
            cost = 0.0
            for k, t, isfull in seq:
                if k in Ss:
                    for i in Ss[k]:
                        assert i < t
                        rnk = pos + i + 1
                        if rnk > s:
                            cost += A_EXP * math.log2(rnk / s)
                pos += t
            if exactZ:
                L = pos
                u = self.out[J][1] if self.out[J][0] in ('and', 'or') else (1 if self.out[J][0] == 'dict' else 0)
                th = [min(1.0, (s / r) ** A_EXP) for r in range(1, L + 1)] + [min(1.0, (s / r) ** A_EXP) for r in range(1, u + 1)]
                e = [0.0] * (s + 1); e[0] = 1.0
                for x in th:
                    for k in range(s, 0, -1):
                        e[k] += e[k - 1] * x
                cost += math.log2(e[s]) - s * math.log2(2 * math.e * A_EXP / (A_EXP - 1))
            tot += cost
        return mass, tot / nsamp

    def code_length_mc(self, rng, order, nsets=4000, exactZ=False):
        Lam_bound = math.log2(math.e) * self.Pf1
        hv = 0.0 if self.v >= 1 else (-(self.v * math.log2(self.v)) - (1 - self.v) * math.log2(1 - self.v) if self.v > 0 else 0)
        acc = 0.0
        acc_root = 0.0
        acc_rank = 0.0
        for _ in range(nsets):
            typ, j, Ss = self.sample_set(rng)
            nctrl = sum(len(S) for S in Ss.values())
            s = nctrl + (1 if typ == 'blk' else 0)  # dictator/AND/OR data part: count 1 element (dict) - see note
            if typ == 'blk' and self.out[j][0] in ('and', 'or'):
                # sample data set size: uniform nonempty subset of u vars
                u = self.out[j][1]
                while True:
                    bsz = sum(1 for _ in range(u) if rng.random() < 0.5)
                    if bsz:
                        break
                s = nctrl + bsz
            mass, rk = self.rank_cost(rng, typ, j, Ss, order, s, exactZ=exactZ)
            root = -math.log2(min(mass, 0.5)) if mass < 0.5 else 1.0
            other = math.log2(s * (s + 1)) + 1 + s * math.log2(2 * math.e * A_EXP / (A_EXP - 1))
            acc += root + rk + other
            acc_root += root
            acc_rank += rk
        n = nsets
        return dict(total=hv + self.v * Lam_bound + self.v * acc / n, root=self.v * acc_root / n,
                    rank=self.v * acc_rank / n, v=self.v)
