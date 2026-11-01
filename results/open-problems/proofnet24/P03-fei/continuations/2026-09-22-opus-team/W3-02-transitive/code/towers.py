"""Leveled towers of transitive gates with identical (biased) inputs.

A leveled tower F_{j+1} = G_j(F_j, ..., F_j) (independent copies of F_j on disjoint variables) is
transitive whenever every G_j is transitive (the wreath product of the automorphism groups acts
transitively on the leaves).  Exact recursion from the composition identity (CONTEXT.md sect. 3) with
all inputs of the same bias p (Pr[true], true = -1), V = 4p(1-p):
    p_out = Pr[G = -1],   I_out = A * I_in,   H_out = Htilde_G(p) + A * (H_in - h2(V)),
    A = sum_i It_i / V,   It_i = sum_{T contains i} Ghat_p(T)^2.
Beam search over gate sequences for the largest H/I at the top, and for the smallest slack
s_C = C I - H at exactly balanced towers (self-dual gates keep p = 1/2).
"""
import sys, os, json, math, time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import tlib

tlib.setup_process()


def h2(v):
    if v <= 0 or v >= 1:
        return 0.0
    return -v * math.log2(v) - (1 - v) * math.log2(1 - v)


class AndGate:
    """AND_k (or OR_k if dual) in closed form: Ghat(T)^2 = 4 p^(2k-t) (1-p)^t for |T| = t >= 1."""
    def __init__(self, k, dual=False):
        self.k = k; self.dual = dual
        self.name = ('OR%d' if dual else 'AND%d') % k

    def biased(self, p):
        k = self.k
        q = 1 - p if self.dual else p     # probability that an input is 'true' for the AND form
        V = 4 * p * (1 - p)
        c0 = 1 - 2 * q ** k
        Ht = -c0 * c0 * math.log2(c0 * c0) if 0 < c0 * c0 < 1 else 0.0
        lq = math.log2(q); l1 = math.log2(1 - q)
        for t in range(1, k + 1):
            lg = 2 + (2 * k - t) * lq + t * l1          # log2 of Ghat^2
            Ht += math.comb(k, t) * (2.0 ** lg) * (-lg)
        A = k * q ** (k - 1)
        pout = q ** k
        if self.dual:
            pout = 1 - pout
        return (pout, Ht, A, V)


class Gate:
    def __init__(self, name, table):
        self.name = name
        self.table = np.asarray(table, dtype=np.float64)  # +-1, index bit i = 1 <=> input i true (-1)
        self.k = len(self.table).bit_length() - 1
        self.cache = {}

    def biased(self, p):
        key = round(p, 15)
        if key in self.cache:
            return self.cache[key]
        k = self.k
        mu = 1.0 - 2.0 * p
        V = 1.0 - mu * mu
        a = self.table.copy()
        if V <= 0:
            raise ValueError
        s = math.sqrt(V)
        fp = (1.0 - mu) / s    # phi(+1)
        fm = (-1.0 - mu) / s   # phi(-1)
        N = len(a)
        h = 1
        while h < N:
            a = a.reshape(-1, 2, h)
            x0 = a[:, 0, :].copy()   # x_i = +1 (not true)
            x1 = a[:, 1, :].copy()   # x_i = -1 (true)
            a[:, 0, :] = (1 - p) * x0 + p * x1
            a[:, 1, :] = (1 - p) * fp * x0 + p * fm * x1
            a = a.reshape(N)
            h *= 2
        c = a
        P = c * c
        sizes = tlib.popcount(np.arange(N))
        Ht = float(tlib.phi(P[1:]).sum() + tlib.phi(P[:1]).sum())
        It = float((sizes * P).sum())      # sum_i It_i
        # output probability of true (= -1): (1 - mean)/2 ; mean = c[0]
        pout = (1.0 - c[0]) / 2.0
        res = (pout, Ht, It / V, V)
        if len(self.cache) < 200000:
            self.cache[key] = res
        return res


def sym_table(k, vals):
    """Symmetric gate: vals[j] = output (+-1) when exactly j inputs are true."""
    x = np.arange(1 << k)
    w = tlib.popcount(x)
    return np.array([vals[j] for j in w], dtype=np.float64)


def gate_library(extra=()):
    gates = []
    for k in list(range(2, 17)) + [20, 24, 32, 48, 64]:
        gates.append(AndGate(k)); gates.append(AndGate(k, dual=True))
    for k in (3, 5, 7):
        gates.append(Gate('MAJ%d' % k, sym_table(k, [1 if j <= k // 2 else -1 for j in range(k + 1)])))
    for k in range(3, 9):
        for t in range(2, k):
            gates.append(Gate('THR%d_%d' % (k, t), sym_table(k, [1 if j < t else -1 for j in range(k + 1)])))
    for nm, tab in extra:
        gates.append(Gate(nm, tab))
    return gates


def step(state, g):
    p, H, I, hist = state
    pout, Ht, A, V = g.biased(p)
    return (pout, Ht + A * (H - h2(V)), A * I, hist + (g.name,))


def beam(gates, depth, nbins=240, keep=6, Imax=1e30):
    states = [(0.5, 0.0, 1.0, ())]
    best = []
    for d in range(depth):
        new = []
        for st in states:
            for g in gates:
                ns = step(st, g)
                if ns[2] > Imax or not (1e-12 < ns[0] < 1 - 1e-12):
                    continue
                new.append(ns)
                # NOT is free: p -> 1-p
                new.append((1 - ns[0], ns[1], ns[2], ns[3] + ('NOT',)))
        # prune: bins in logit(p); keep the best H/I per bin, plus low-I representatives
        buckets = {}
        for ns in new:
            p = ns[0]
            z = math.log(p / (1 - p))
            b = int(round(z * nbins / 30.0))
            buckets.setdefault(b, []).append(ns)
        states = []
        for b, lst in buckets.items():
            # Pareto front in (low I, high H/I), subsampled to at most `keep` points
            lst.sort(key=lambda s: (s[2], -s[1] / s[2]))
            front = []
            bestr = -1e18
            for s_ in lst:
                r_ = s_[1] / s_[2]
                if r_ > bestr + 1e-12:
                    front.append(s_); bestr = r_
            if len(front) > keep:
                idx = np.linspace(0, len(front) - 1, keep).round().astype(int)
                front = [front[i] for i in sorted(set(idx.tolist()))]
            states.extend(front)
        r = max(states, key=lambda s: s[1] / s[2])
        best.append((d + 1, r[1] / r[2], r[0], r[2], r[3]))
        print("depth %2d  states %5d  best H/I %.6f  p=%.4f I=%.3g  %s" % (d + 1, len(states), r[1] / r[2], r[0], r[2], ' '.join(r[3][-12:])), flush=True)
    return best, states


if __name__ == '__main__':
    depth = int(sys.argv[1]) if len(sys.argv) > 1 else 12
    extra = []
    ex_file = os.path.join(HERE, '..', 'logs', 'gates_extra.json')
    if os.path.exists(ex_file):
        for nm, tab in json.load(open(ex_file)):
            extra.append((nm, tab))
    gates = gate_library(extra)
    print("gates:", len(gates), [g.name for g in gates if not g.name.startswith('THR')])
    t0 = time.time()
    best, states = beam(gates, depth)
    print("time %.1f" % (time.time() - t0))
