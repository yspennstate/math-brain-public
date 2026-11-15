"""mc_chain.py - Monte Carlo test of the chain condition of FLOW 12(l) at small influence.

For a Boolean f, a coordinate i and a chain of sets  R_1 < R_2 < ... < R_J = all other coordinates:
    W(R) = E h(x) h(x^R),   V(R) = E g(x)^2 - E g(x) g(x^R),     h = D_i f,  g = E_i f,
where x^R is x with the coordinates of R resampled.  With mu the squared spectrum and U its sample,
W(R) = P[i in U, U n R empty] and V(R) = P[i not in U, U n R nonempty].  The cells
    j = 0: T empty;   j >= 1: T misses R_{j-1} and meets R_j
give  E_i <= L := sum_j Phi(A_j, B_j),  A_j = V(R_j) - V(R_{j-1}),  B_j = W(R_{j-1}) - W(R_j)
(Phi is superadditive, so a coarse chain bounds every ordering that refines it from above), and
    M := max_j W(R_j) V(R_{j+1}) / Inf_i^2   is the constant of the sufficient condition 12(e).
The trivial bound is h2(Inf_i)/Inf_i.  All samples of one run share x and the fresh bits y (nested coupling),
so the estimates of W and V are monotone along the chain up to noise.

Samples are bit-sliced: X has shape (n, K) uint64, one bit per sample.

usage:  python mc_chain.py selftest
        python mc_chain.py run  NAME  WORDS  BATCHES  SEED  OUT.json     (samples = 64 * WORDS * BATCHES)
        python mc_chain.py show OUT.json [OUT2.json ...]                 (sums the raw counts of all files)
names:  hex:L   run:n:w   rdnf:n:w:m:seed   thand:m:w:theta   maj:n   tribes:m:w
"""
import sys
import json
import math
import time
import numpy as np

ALL = np.uint64(0xFFFFFFFFFFFFFFFF)


def popcount(a):
    if hasattr(np, "bitwise_count"):
        return int(np.bitwise_count(a).sum(dtype=np.int64))
    return int(np.unpackbits(np.ascontiguousarray(a).view(np.uint8)).sum(dtype=np.int64))


def eta(x):
    return 0.0 if x <= 0 else -x * math.log2(x)


def phi(p, q):
    p, q = max(p, 0.0), max(q, 0.0)
    return eta(p) + eta(q) - eta(p + q)


def h2(d):
    return eta(d) + eta(1 - d)


def geometric(sizes_first, total, ratio=1.5):
    s = sorted(set(min(max(int(v), 1), total) for v in sizes_first))
    while s[-1] < total:
        nxt = max(s[-1] + 1, int(round(s[-1] * ratio)))
        s.append(min(nxt, total))
    return s


# ---------------------------------------------------------------- functions

class Hex:
    """Left-right crossing by open cells of the L x L rhombus of the triangular lattice (the Hex board)."""

    def __init__(self, L):
        self.L, self.n = L, L * L
        c = L // 2
        self.i = c * L + c
        d = {}
        for r in range(L):
            for cc in range(L):
                dr, dc = r - c, cc - c
                d[r * L + cc] = max(abs(dr), abs(dc), abs(dr + dc))
        self.order = sorted((j for j in range(self.n) if j != self.i), key=lambda j: (d[j], j))
        radii = [1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96]
        sizes = []
        for rad in radii:
            k = sum(1 for j in self.order if d[j] <= rad)
            if not sizes or k > sizes[-1]:
                sizes.append(k)
        if sizes[-1] < self.n - 1:
            sizes.append(self.n - 1)
        self.sizes = sorted(set(sizes) | set(geometric([1, 2, 3, 4, 5, 6], self.n - 1, 1.35)))
        self.name = "hex:%d" % L

    def eval(self, X):
        L = self.L
        op = X.reshape(L, L, -1)
        reach = np.zeros_like(op)
        reach[:, 0] = op[:, 0]
        it = 0
        while True:
            nb = np.zeros_like(op)
            nb[:, 1:] |= reach[:, :-1]
            nb[:, :-1] |= reach[:, 1:]
            nb[1:, :] |= reach[:-1, :]
            nb[:-1, :] |= reach[1:, :]
            nb[1:, :-1] |= reach[:-1, 1:]
            nb[:-1, 1:] |= reach[1:, :-1]
            new = reach | (op & nb)
            it += 1
            if it % 4 == 0 and np.array_equal(new, reach):
                break
            reach = new
        return np.bitwise_or.reduce(reach[:, L - 1], axis=0)


class Run:
    """A run of w consecutive ones somewhere in a cyclic string of length n."""

    def __init__(self, n, w):
        self.n, self.w, self.i = n, w, 0
        order = []
        for dist in range(1, n // 2 + 1):
            order.append(dist)
            if n - dist != dist:
                order.append(n - dist)
        self.order = order
        self.sizes = geometric(list(range(1, 2 * w - 1)), n - 1, 1.5)
        self.name = "run:%d:%d" % (n, w)

    def eval(self, X):
        a = X.copy()
        for s in range(1, self.w):
            a &= np.roll(X, -s, axis=0)
        return np.bitwise_or.reduce(a, axis=0)


class RDNF:
    """Random monotone DNF: m terms, each the AND of w distinct variables chosen uniformly from n."""

    def __init__(self, n, w, m, seed, mode="bfs"):
        rng = np.random.default_rng(seed)
        self.n, self.w, self.m = n, w, m
        self.mode = mode
        self.terms = np.array([rng.choice(n, size=w, replace=False) for _ in range(m)])
        deg = np.bincount(self.terms.ravel(), minlength=n)
        self.i = int(np.argmax(deg))
        # order: breadth-first in the term hypergraph from i; inside a layer, most shared terms with the
        # earlier layers first
        member = [[] for _ in range(n)]
        for t, term in enumerate(self.terms):
            for v in term:
                member[v].append(t)
        dist = {self.i: 0}
        frontier = [self.i]
        order = []
        while frontier:
            score = {}
            for v in frontier:
                for t in member[v]:
                    for u in self.terms[t]:
                        u = int(u)
                        if u not in dist:
                            score[u] = score.get(u, 0) + 1
            layer = sorted(score, key=lambda u: (-score[u], u))
            for u in layer:
                dist[u] = 1
            order.extend(layer)
            frontier = layer
        order.extend(j for j in range(n) if j not in dist)
        self.order = order
        self.sizes = geometric(list(range(1, 9)), n - 1, 1.3)
        self.name = "rdnf:%d:%d:%d:%d" % (n, w, m, seed)
        self.deg = int(deg[self.i])
        if mode != "bfs":
            # mates of i, term by term (the terms through i one after another)
            mates, seen = [], {self.i}
            for t in member[self.i]:
                for u in self.terms[t]:
                    u = int(u)
                    if u not in seen:
                        seen.add(u)
                        mates.append(u)
            rest = [u for u in order if u not in seen]
            nm, nr = len(mates), len(rest)
            if mode == "terms":        # mates closest, term by term, one coordinate per step; then the rest
                self.order = mates + rest
                self.sizes = geometric(list(range(1, nm + 1)), n - 1, 1.3)
            elif mode == "far":        # every other coordinate closer than the mates; mates one per step at the end
                self.order = rest + mates
                self.sizes = sorted(set(geometric(list(range(1, 9)), nr, 1.3)) | set(range(nr, n)))
            elif mode == "rand":       # a uniformly random order, single steps over the first nm coordinates
                perm = [int(v) for v in rng.permutation(n) if int(v) != self.i]
                self.order = perm
                self.sizes = geometric(list(range(1, nm + 1)), n - 1, 1.3)
            else:
                raise SystemExit("unknown rdnf mode " + mode)
            self.name += ":" + mode

    def eval(self, X):
        t = X[self.terms[:, 0]].copy()
        for k in range(1, self.w):
            t &= X[self.terms[:, k]]
        return np.bitwise_or.reduce(t, axis=0)


def count_ge(T, theta):
    """T: (m, K) uint64 bit-sliced; returns the (K,) uint64 bit-slice of [number of ones among the m rows >= theta]."""
    bits = np.unpackbits(np.ascontiguousarray(T).view(np.uint8), axis=1)
    cnt = bits.sum(axis=0, dtype=np.int32)
    return np.packbits(cnt >= theta).view(np.uint64)


class ThAnd:
    """At least theta of m disjoint ANDs of width w are satisfied."""

    def __init__(self, m, w, theta):
        self.m, self.w, self.theta = m, w, theta
        self.n, self.i = m * w, 0
        self.order = list(range(1, self.n))
        if w > 1:
            blocks = geometric([1, 2, 3, 4, 5, 6], m - 1, 1.4)
            self.sizes = list(range(1, w)) + [w - 1 + w * k for k in blocks]
        else:
            self.sizes = geometric([1, 2, 3, 4, 5, 6], self.n - 1, 1.4)
        self.name = "thand:%d:%d:%d" % (m, w, theta)

    def eval(self, X):
        K = X.shape[1]
        B = X.reshape(self.m, self.w, K)
        t = B[:, 0].copy()
        for k in range(1, self.w):
            t &= B[:, k]
        return count_ge(t, self.theta)


def make(name):
    p = name.split(":")
    if p[0] == "hex":
        return Hex(int(p[1]))
    if p[0] == "run":
        return Run(int(p[1]), int(p[2]))
    if p[0] == "rdnf":
        return RDNF(int(p[1]), int(p[2]), int(p[3]), int(p[4]), p[5] if len(p) > 5 else "bfs")
    if p[0] == "thand":
        return ThAnd(int(p[1]), int(p[2]), int(p[3]))
    if p[0] == "maj":
        n = int(p[1])
        return ThAnd(n, 1, (n + 1) // 2)
    if p[0] == "tribes":
        return ThAnd(int(p[1]), int(p[2]), 1)
    raise SystemExit("unknown function " + name)


# ---------------------------------------------------------------- sampling

def sample(fn, words, batches, seed, progress=None):
    rng = np.random.default_rng(seed)
    n, i = fn.n, fn.i
    J = len(fn.sizes)
    pos = np.full(n, n + 1, dtype=np.int64)          # rank of each coordinate in the order (1-based)
    for r, j in enumerate(fn.order, 1):
        pos[j] = r
    c = {"N": 0, "g0sq": 0, "h0": 0, "g0": 0,
         "hh_p": [0] * J, "hh_m": [0] * J, "gg_p": [0] * J, "gg_m": [0] * J}
    t0 = time.time()
    for b in range(batches):
        x = rng.integers(0, 2 ** 64, size=(n, words), dtype=np.uint64)
        y = rng.integers(0, 2 ** 64, size=(n, words), dtype=np.uint64)

        def both(z):
            z[i] = ALL
            f1 = fn.eval(z)
            z[i] = 0
            f0 = fn.eval(z)
            return f1 ^ f0, f1                                 # pivotal mask, sign (1 = true at x_i = 1)

        piv0, s0 = both(x.copy())
        np0 = ~piv0
        c["N"] += 64 * words
        c["g0sq"] += popcount(np0)
        c["h0"] += popcount(piv0 & s0) - popcount(piv0 & ~s0)
        c["g0"] += popcount(np0 & s0) - popcount(np0 & ~s0)
        for j, size in enumerate(fn.sizes):
            z = np.where((pos <= size)[:, None], y, x)
            pj, sj = both(z)
            same = ~(s0 ^ sj)
            c["hh_p"][j] += popcount(piv0 & pj & same)
            c["hh_m"][j] += popcount(piv0 & pj & ~same)
            c["gg_p"][j] += popcount(np0 & ~pj & same)
            c["gg_m"][j] += popcount(np0 & ~pj & ~same)
        if progress and (b + 1) % progress == 0:
            print("  batch %d/%d  %.0f s" % (b + 1, batches, time.time() - t0), flush=True)
    c["name"], c["sizes"], c["n"], c["i"] = fn.name, list(fn.sizes), n, i
    c["deg"] = getattr(fn, "deg", 0)
    c["seconds"] = time.time() - t0
    return c


def merge(cs):
    out = dict(cs[0])
    for k in ("hh_p", "hh_m", "gg_p", "gg_m"):
        out[k] = list(out[k])
    for c in cs[1:]:
        assert c["name"] == out["name"] and c["sizes"] == out["sizes"]
        for k in ("N", "g0sq", "h0", "g0", "seconds"):
            out[k] += c[k]
        for k in ("hh_p", "hh_m", "gg_p", "gg_m"):
            out[k] = [a + b for a, b in zip(out[k], c[k])]
    return out


def report(c, out=sys.stdout):
    N = float(c["N"])
    J = len(c["sizes"])
    Eg2 = c["g0sq"] / N
    delta = 1.0 - Eg2                                       # E h^2 = P[i pivotal] = Inf_i
    Eh, Eg = c["h0"] / N, c["g0"] / N
    W = [delta] + [(c["hh_p"][j] - c["hh_m"][j]) / N for j in range(J)]
    V = [0.0] + [Eg2 - (c["gg_p"][j] - c["gg_m"][j]) / N for j in range(J)]
    W[J] = Eh * Eh                                          # the last set is everything: exact forms
    V[J] = Eg2 - Eg * Eg
    L = phi(Eg * Eg, Eh * Eh)
    rows = []
    for j in range(1, J + 1):
        A, B = V[j] - V[j - 1], W[j - 1] - W[j]
        L += phi(A, B)
        rows.append((c["sizes"][j - 1], W[j] / delta, V[j] / delta, phi(A, B) / delta))
    M = max([V[1] / delta] + [W[j] * V[j + 1] / delta ** 2 for j in range(1, J)])
    triv = h2(delta) / delta
    print("%s  n=%d  i=%d  samples=%d  (%.0f s)" % (c["name"], c["n"], c["i"], c["N"], c["seconds"]), file=out)
    if c.get("deg"):
        print("  terms through i: %d   log2 = %.2f   steps in the chain: %d"
              % (c["deg"], math.log2(c["deg"]), J), file=out)
    print("  Inf_i = %.6f (+- %.6f)   E f-part: Eg = %.4f  Eh = %.5f" % (delta, math.sqrt(delta / N), Eg, Eh), file=out)
    print("  chain bound L/Inf = %.4f    trivial h2(Inf)/Inf = %.4f    ratio = %.3f    M = %.3f"
          % (L / delta, triv, L / delta / triv, M), file=out)
    print("     |R|     W/Inf     V/Inf   Phi_j/Inf   W_j V_{j+1}/Inf^2", file=out)
    for j, (sz, w, v, ph) in enumerate(rows, 1):
        prod = W[j] * V[j + 1] / delta ** 2 if j < J else float("nan")
        print("  %6d  %8.5f  %8.4f  %8.4f  %8.3f" % (sz, w, v, ph, prod), file=out)
    print(file=out)
    return L / delta, triv, M, delta


# ---------------------------------------------------------------- self-test against exact Fourier

def wht(v):
    v = v.astype(np.float64).copy()
    n = v.size.bit_length() - 1
    hlen = 1
    while hlen < v.size:
        v = v.reshape(-1, 2, hlen)
        a, b = v[:, 0].copy(), v[:, 1].copy()
        v[:, 0], v[:, 1] = a + b, a - b
        v = v.reshape(-1)
        hlen *= 2
    return v / (1 << n)


def scalar_ref(name, bits):
    """Independent scalar evaluation (plain Python, no shared code with the bit-sliced evaluators)."""
    p = name.split(":")
    if p[0] == "hex":
        L = int(p[1])
        seen = set((r, 0) for r in range(L) if bits[r * L])
        stack = list(seen)
        while stack:
            r, c = stack.pop()
            if c == L - 1:
                return 1
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (1, -1)):
                rr, cc = r + dr, c + dc
                if 0 <= rr < L and 0 <= cc < L and bits[rr * L + cc] and (rr, cc) not in seen:
                    seen.add((rr, cc))
                    stack.append((rr, cc))
        return 0
    if p[0] == "run":
        n, w = int(p[1]), int(p[2])
        return int(any(all(bits[(s + k) % n] for k in range(w)) for s in range(n)))
    if p[0] == "rdnf":
        fn = make(name)
        return int(any(all(bits[int(v)] for v in term) for term in fn.terms))
    if p[0] in ("thand", "maj", "tribes"):
        if p[0] == "thand":
            m, w, theta = int(p[1]), int(p[2]), int(p[3])
        elif p[0] == "maj":
            m, w, theta = int(p[1]), 1, (int(p[1]) + 1) // 2
        else:
            m, w, theta = int(p[1]), int(p[2]), 1
        return int(sum(all(bits[b * w + k] for k in range(w)) for b in range(m)) >= theta)
    raise SystemExit("no reference for " + name)


def evaluator_check(name, words=4, seed=3):
    fn = make(name)
    rng = np.random.default_rng(seed)
    X = rng.integers(0, 2 ** 64, size=(fn.n, words), dtype=np.uint64)
    got = np.unpackbits(fn.eval(X).view(np.uint8))
    cols = np.unpackbits(np.ascontiguousarray(X).view(np.uint8), axis=1)      # (n, 64 * words)
    bad = sum(int(got[s]) != scalar_ref(name, cols[:, s]) for s in range(64 * words))
    frac = float(got.mean())
    print("%-18s evaluator against scalar reference: %d of %d differ   P[f = 1] in the sample %.3f"
          % (name, bad, 64 * words, frac))
    return bad == 0


def selftest():
    ok = True
    for name in ("hex:3", "hex:7", "hex:12", "run:11:3", "run:90:6", "rdnf:12:3:7:1", "rdnf:200:8:177:2",
                 "thand:4:3:2", "thand:40:4:3", "maj:101", "tribes:20:4"):
        ok = evaluator_check(name) and ok
    for name in ("rdnf:12:3:7:1", "hex:3", "thand:4:3:2", "run:11:3"):
        fn = make(name)
        n, i = fn.n, fn.i
        # truth table through the bit-sliced evaluator
        size = 1 << n
        words = max(1, size // 64)
        idx = np.arange(words * 64, dtype=np.uint64)
        X = np.zeros((n, words), dtype=np.uint64)
        for j in range(n):
            bits = ((idx >> np.uint64(j)) & np.uint64(1)).astype(np.uint8)
            X[j] = np.packbits(bits).view(np.uint64)
        fb = np.unpackbits(fn.eval(X).view(np.uint8))[:size].astype(np.float64)
        mu = wht(1.0 - 2.0 * fb) ** 2
        S = np.arange(size)
        has_i = (S >> i) & 1 == 1
        c = sample(fn, 2048, 8, 7)
        N = float(c["N"])
        delta_mc = 1.0 - c["g0sq"] / N
        delta = float(mu[has_i].sum())
        worst = abs(delta_mc - delta)
        mask = 0
        k = 0
        for j, sz in enumerate(fn.sizes):
            while k < sz:
                mask |= 1 << fn.order[k]
                k += 1
            meets = (S & mask) != 0
            W = float(mu[has_i & ~meets].sum())
            V = float(mu[~has_i & meets].sum())
            Wm = (c["hh_p"][j] - c["hh_m"][j]) / N
            Vm = c["g0sq"] / N - (c["gg_p"][j] - c["gg_m"][j]) / N
            worst = max(worst, abs(W - Wm), abs(V - Vm))
        tol = 6.0 / math.sqrt(N)
        print("%-16s Inf exact %.6f mc %.6f   worst |exact - mc| over W, V = %.5f (tolerance %.5f)  %s"
              % (name, delta, delta_mc, worst, tol, "ok" if worst < tol else "FAIL"))
        ok = ok and worst < tol
    print("SELFTEST", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def main():
    if sys.argv[1] == "selftest":
        raise SystemExit(selftest())
    if sys.argv[1] == "run":
        name, words, batches, seed, outp = sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
        fn = make(name)
        c = sample(fn, words, batches, seed, progress=max(1, batches // 10))
        with open(outp, "w", encoding="utf-8") as fh:
            json.dump(c, fh)
        report(c)
        return
    if sys.argv[1] == "show":
        groups = {}
        for p in sys.argv[2:]:
            with open(p, encoding="utf-8") as fh:
                c = json.load(fh)
            groups.setdefault(c["name"], []).append(c)
        for name in groups:
            report(merge(groups[name]))
        return
    raise SystemExit(__doc__)


if __name__ == "__main__":
    main()
