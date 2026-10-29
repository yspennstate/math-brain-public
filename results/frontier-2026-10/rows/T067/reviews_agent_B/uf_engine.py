"""Independent exact replay of the T067 universal-fusion envelope (second audit, agent B).

Written from the text of T067-UNIVERSAL-FUSION-001 v1 and the BAND*-UPPER texts only.
Orbit masses are integers summing to S = 2^bits. One depth = physical edge on the old law,
then d conditionally independent copies combined by binary powers; after the edge and after
every fusion each orbit mass is floored and the deficit goes to the pure orbit (N,0,0).

Fusion arithmetic: a left orbit k (representative) and a right grid point h (one of v
orientations of its orbit) carry joint mass m_k m_h (1/v) 3(k.h)/N^2; the fused point
N k_i h_i/(k.h) is split barycentrically with integer weights W over k.h, so each vertex gets
m_k m_h * (6W/v) / (2N^2). Raw sums are exact via CRT over three 31-bit primes (bound 2^79).
"""
import json, sys, time
from fractions import Fraction
import numpy as np

PRIMES = (2147483647, 2147483629, 2147483587)  # 2^31-1 and two primes below it (checked below)


def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


assert all(is_prime(p) for p in PRIMES)


def orbits(N):
    ob = [(a, b, N - a - b) for a in range(N, -1, -1) for b in range(min(a, N - a), -1, -1) if N - a - b <= b]
    return ob


class Grid:
    def __init__(self, N):
        self.N = N
        self.ob = orbits(N)
        self.n = len(self.ob)
        self.key = np.full((N + 1) * (N + 1), -1, dtype=np.int64)
        for i, (a, b, c) in enumerate(self.ob):
            self.key[a * (N + 1) + b] = i
        self.pure = self.key[N * (N + 1) + 0]
        self.sq = np.array([3 * (a * a + b * b + c * c) - N * N for a, b, c in self.ob], dtype=object)

    def idx(self, pts):  # pts: (M,3) int64 array, any order -> orbit index
        s = -np.sort(-pts, axis=1)
        return self.key[s[:, 0] * (self.N + 1) + s[:, 1]]

    def split(self, num, den):
        """num: (M,3) int64 numerators, den: (M,) common denominators, rows sum to N*den.
        Returns list of (rowidx, vertex points (M',3), integer weights over den)."""
        f = num // den[:, None]
        r = num % den[:, None]
        tot = r.sum(axis=1)
        out = []
        z = tot == 0
        if z.any():
            out.append((np.nonzero(z)[0], f[z], den[z]))
        o = tot == den
        t = tot == 2 * den
        assert np.all(z | o | t)
        for i in range(3):
            e = np.zeros(3, dtype=np.int64); e[i] = 1
            if o.any():
                out.append((np.nonzero(o)[0], f[o] + e, r[o, i]))
            if t.any():
                out.append((np.nonzero(t)[0], f[t] + 1 - e, den[t] - r[t, i]))
        return out

    def signal(self, m, S):
        return Fraction(int(sum(int(mi) * s for mi, s in zip(m, self.sq))), S * 3 * self.N * self.N)


def edge_table(g, A, B):
    N = g.N
    k = np.array(g.ob, dtype=np.int64)
    num = (B - A) * N + 3 * A * k
    den = np.full(len(k), 3 * B, dtype=np.int64)
    rows = {}
    for ri, pts, w in g.split(num, den):
        for a, d, ww in zip(ri, g.idx(pts), w):
            if ww:
                rows[(int(a), int(d))] = rows.get((int(a), int(d)), 0) + int(ww)
    for a in range(g.n):
        assert sum(v for (x, _), v in rows.items() if x == a) == 3 * B
    return rows, 3 * B


def fusion_table(g):
    N = g.N
    k = np.array(g.ob, dtype=np.int64)
    pts, holder, vcnt = [], [], []
    for j, o in enumerate(g.ob):
        ps = sorted(set(__import__("itertools").permutations(o)))
        for p in ps:
            pts.append(p); holder.append(j); vcnt.append(len(ps))
    H = np.array(pts, dtype=np.int64); own = np.array(holder, dtype=np.int64); v = np.array(vcnt, dtype=np.int64)
    Ls, Rs, Ds, Cs = [], [], [], []
    for l in range(g.n):
        s = H @ k[l]
        ok = s > 0
        num = N * (k[l][None, :] * H[ok])
        den = s[ok]
        r_own, r_v = own[ok], v[ok]
        for ri, vp, w in g.split(num, den):
            keep = w > 0
            ri, vp, w = ri[keep], vp[keep], w[keep]
            c = 6 * w
            assert np.all(c % r_v[ri] == 0)
            Ls.append(np.full(len(ri), l, dtype=np.int32)); Rs.append(r_own[ri].astype(np.int32))
            Ds.append(g.idx(vp).astype(np.int32)); Cs.append(c // r_v[ri])
    L = np.concatenate(Ls); R = np.concatenate(Rs); D = np.concatenate(Ds); C = np.concatenate(Cs)
    # aggregate identical (l, r, d)
    key = (L.astype(np.int64) * g.n + R) * g.n + D
    order = np.argsort(key, kind="stable")
    key, C = key[order], C[order]
    u, start = np.unique(key, return_index=True)
    C = np.add.reduceat(C, start)
    D = (u % g.n).astype(np.int32); R = ((u // g.n) % g.n).astype(np.int32); L = (u // (g.n * g.n)).astype(np.int32)
    # row sums: for each ordered orbit pair, sum C = 2N^2
    rs = np.zeros((g.n, g.n), dtype=np.int64)
    np.add.at(rs, (L, R), C)
    assert np.all(rs == 2 * N * N), "fusion rows must sum to 2N^2"
    o = np.argsort(D, kind="stable")
    L, R, D, C = L[o], R[o], D[o], C[o]
    starts = np.r_[0, np.nonzero(np.diff(D))[0] + 1]
    return dict(L=L, R=R, C=C, dest=D[starts], starts=starts, den=2 * N * N)


def crt(res):
    M = 1
    x = 0
    for r, p in zip(res, PRIMES):
        # x = x mod M, need x' = r mod p
        t = ((r - x) * pow(M, -1, p)) % p
        x += M * t
        M *= p
    return x


def round_up(g, raw, den, S):
    """raw: dict or list of exact raw sums over den*S; returns floored masses + deficit to pure."""
    m = [0] * g.n
    for d, x in raw.items():
        m[d] = x // den
    rem = S - sum(m)
    assert rem >= 0
    m[g.pure] += rem
    return m, rem


def apply_edge(g, et, m, S):
    rows, den = et
    raw = {}
    for (a, d), w in rows.items():
        if m[a]:
            raw[d] = raw.get(d, 0) + m[a] * w
    return round_up(g, raw, den, S)


def fuse(g, ft, m1, m2, S):
    L, R, C = ft["L"], ft["R"], ft["C"]
    res = []
    for p in PRIMES:
        a = np.array([x % p for x in m1], dtype=np.int64)
        b = np.array([x % p for x in m2], dtype=np.int64)
        t = (a[L] * b[R]) % p
        t = (t * C) % p
        res.append(np.add.reduceat(t, ft["starts"]) % p)
    raw = {int(d): crt([int(r[i]) for r in res]) for i, d in enumerate(ft["dest"])}
    tot = sum(raw.values())
    assert tot == S * S * ft["den"], "fusion total must be S^2*2N^2 exactly (CRT sanity)"
    return round_up(g, raw, S * ft["den"], S)


def depth_step(g, et, ft, m, d, S, order):
    nodes = []
    e, r = apply_edge(g, et, m, S); nodes.append(r)
    bits = [j for j in range(d.bit_length()) if (d >> j) & 1]
    P = e
    powers = {0: e}
    acc = None
    for j in range(d.bit_length()):
        if j > 0:
            P, r = fuse(g, ft, P, P, S); nodes.append(r); powers[j] = P
        if order == "interleave" and j in bits:
            if acc is None:
                acc = P
            else:
                acc, r = fuse(g, ft, acc, P, S); nodes.append(r)
    if order in ("asc", "desc"):
        seq = bits if order == "asc" else bits[::-1]
        acc = powers[seq[0]]
        for j in seq[1:]:
            acc, r = fuse(g, ft, acc, powers[j], S); nodes.append(r)
    return acc, nodes


if __name__ == "__main__":
    d = int(sys.argv[1]); eta = Fraction(sys.argv[2]); steps = int(sys.argv[3]); order = sys.argv[4]
    N = int(sys.argv[5]) if len(sys.argv) > 5 else 96
    bits = int(sys.argv[6]) if len(sys.argv) > 6 else 32
    out = sys.argv[7] if len(sys.argv) > 7 else None
    S = 1 << bits
    g = Grid(N)
    t0 = time.time()
    et = edge_table(g, eta.numerator, eta.denominator)
    ft = fusion_table(g)
    print(f"orbits {g.n} fusion entries {len(ft['C'])} tables {time.time()-t0:.1f}s", flush=True)
    m = [0] * g.n; m[g.pure] = S
    rows = []
    for t in range(1, steps + 1):
        m, nodes = depth_step(g, et, ft, m, d, S, order)
        x = g.signal(m, S)
        rows.append({"depth": t, "x": f"{x.numerator}/{x.denominator}", "nodes": nodes})
        print(t, x, float(x), nodes, f"{time.time()-t0:.0f}s", flush=True)
        if out:
            json.dump({"d": d, "eta": str(eta), "N": N, "bits": bits, "order": order, "rows": rows,
                       "masses": m, "orbit_keys": [list(o) for o in g.ob]}, open(out, "w"), indent=0)
