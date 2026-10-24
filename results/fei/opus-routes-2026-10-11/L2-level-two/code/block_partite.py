"""Corollary K of NOTES section 5e: K-partite GF(2) polynomials.

f = (-1)^P with every monomial of P using at most one variable from each of K blocks X_1..X_K. Then every block has
signed-character fibers over the rest, Lemma B gives H(S_{X_k}) <= 2 I_{X_{-k}}, and subadditivity gives
    B <= H(S) <= sum_k H(S_{X_k}) <= 2 sum_k I_{X_{-k}} = 2 (K - 1) I.
This script checks the chain on: exhaustive small block shapes, random members of larger shapes, and a greedy search for
the largest H/I inside the class. A side search over general cubic polynomials (no block condition) asks whether
degree alone keeps H/I below 4; that part is evidence only.
Usage: python -B block_partite.py   (writes ../data/block_partite.json; prints the log)
"""
import itertools, json, math, os, sys, time
import numpy as np

LOG2 = math.log(2.0)


def fwht(a):
    a = a.astype(float).copy()
    h, n = 1, len(a)
    while h < n:
        a = a.reshape(-1, 2 * h)
        x, y = a[:, :h].copy(), a[:, h:].copy()
        a[:, :h], a[:, h:] = x + y, x - y
        a = a.reshape(-1)
        h *= 2
    return a / n


def ent(w):
    w = w[w > 1e-300]
    return float(-(w * np.log2(w)).sum())


def allowed_monomials(blocks):
    """bitmasks of monomials with at most one variable per block (constant 1 included as 0)"""
    choices = [[0] + [1 << v for v in b] for b in blocks]
    return sorted({sum(c) for c in itertools.product(*choices)})


def truth(mons, n):
    idx = np.arange(1 << n)
    P = np.zeros(1 << n, dtype=np.int64)
    for m in mons:
        P ^= ((idx & m) == m).astype(np.int64)
    return 1 - 2 * P


def stats(F, n, blocks):
    p = fwht(F) ** 2
    idx = np.arange(1 << n)
    infl = np.array([p[((idx >> j) & 1) == 1].sum() for j in range(n)])
    I = float(infl.sum())
    H = ent(p)
    Hk, Ik = [], []
    for b in blocks:
        mask = sum(1 << v for v in b)
        Hk.append(ent(np.bincount(idx & mask, weights=p, minlength=1 << n)))
        Ik.append(float(infl[b].sum()))
    B = 0.0
    for i in range(n):
        lo = idx[((idx >> i) & 1) == 0]
        a, d = p[lo], p[lo | (1 << i)]
        t = a + d
        ok = (a > 1e-300) & (d > 1e-300)
        B += float((-a[ok] * np.log2(a[ok] / t[ok]) - d[ok] * np.log2(d[ok] / t[ok])).sum())
    return dict(H=H, I=I, B=B, Hk=Hk, Ik=Ik)


def judge(st, K):
    """violations of B <= H <= sum Hk, Hk <= 2 (I - Ik), sum Hk <= 2 (K-1) I"""
    v = 0
    v += st["B"] > st["H"] + 1e-9
    v += st["H"] > sum(st["Hk"]) + 1e-9
    v += any(h > 2 * (st["I"] - i) + 1e-9 for h, i in zip(st["Hk"], st["Ik"]))
    v += sum(st["Hk"]) > 2 * (K - 1) * st["I"] + 1e-9
    return int(v)


def blocks_of(shape):
    out, c = [], 0
    for s in shape:
        out.append(list(range(c, c + s)))
        c += s
    return out


class Tally:
    def __init__(self, name, K):
        self.name, self.K = name, K
        self.n = self.viol = 0
        self.best = (0.0, None)
        self.best_blockslack = math.inf

    def add(self, st, mons):
        self.n += 1
        self.viol += judge(st, self.K)
        if st["I"] > 1e-12:
            r = st["H"] / st["I"]
            if r > self.best[0]:
                self.best = (r, sorted(mons))
            for h, i in zip(st["Hk"], st["Ik"]):
                if st["I"] - i > 1e-12:
                    self.best_blockslack = min(self.best_blockslack, 2 * (st["I"] - i) - h)

    def row(self):
        return dict(name=self.name, K=self.K, cases=self.n, violations=self.viol, max_H_over_I=self.best[0],
                    bound=2 * (self.K - 1), argmax_monomials=self.best[1],
                    min_block_slack=None if self.best_blockslack == math.inf else self.best_blockslack)


def exhaustive(shape):
    blocks, n, K = blocks_of(shape), sum(shape), len(shape)
    mons = [m for m in allowed_monomials(blocks) if m != 0]   # the constant only flips the sign
    tl = Tally(f"exhaustive {shape}", K)
    for code in range(1 << len(mons)):
        chosen = [mons[k] for k in range(len(mons)) if (code >> k) & 1]
        tl.add(stats(truth(chosen, n), n, blocks), chosen)
    return tl


def random_members(shape, count, rng, density):
    blocks, n, K = blocks_of(shape), sum(shape), len(shape)
    mons = [m for m in allowed_monomials(blocks) if m != 0]
    tl = Tally(f"random {shape} density {density}", K)
    for _ in range(count):
        chosen = [m for m in mons if rng.random() < density]
        tl.add(stats(truth(chosen, n), n, blocks), chosen)
    return tl


def greedy(shape, restarts, rng, mons=None, name=None, K=None, steps=400):
    """local search maximizing H/I by single monomial flips; mons defaults to the K-partite monomials"""
    blocks, n = blocks_of(shape), sum(shape)
    if mons is None:
        mons = [m for m in allowed_monomials(blocks) if m != 0]
        K = len(shape)
    tl = Tally(name or f"greedy {shape}", K)
    for _ in range(restarts):
        cur = set(m for m in mons if rng.random() < 0.3)
        st = stats(truth(cur, n), n, blocks)
        tl.add(st, cur)
        score = st["H"] / st["I"] if st["I"] > 1e-12 else 0.0
        for _ in range(steps):
            m = mons[rng.integers(len(mons))]
            nxt = cur ^ {m}
            st2 = stats(truth(nxt, n), n, blocks)
            tl.add(st2, nxt)
            s2 = st2["H"] / st2["I"] if st2["I"] > 1e-12 else 0.0
            if s2 >= score:
                cur, score = nxt, s2
    return tl


def main():
    t0 = time.time()
    rng = np.random.default_rng(20261012)
    rows = []

    def show(tl):
        r = tl.row()
        rows.append(r)
        print(f"  {r['name']:40s} cases={r['cases']:7d} viol={r['violations']}  max H/I={r['max_H_over_I']:.6f}"
              f"  bound 2(K-1)={r['bound']}  min block slack={r['min_block_slack']:.2e}", flush=True)

    print("K-partite GF(2) polynomials: B <= H <= sum_k H(S_Xk) <= 2 sum_k I_X-k = 2(K-1) I")
    print("(1) exhaustive shapes")
    for shape in [(1, 1), (2, 1), (2, 2), (3, 1), (1, 1, 1), (2, 1, 1), (3, 1, 1), (2, 2, 1), (1, 1, 1, 1)]:
        show(exhaustive(shape))
    print("(1b) negative control: any monomials allowed, judged with the block shape; the checks must trip")
    for shape in [(2, 2, 2), (3, 3)]:
        blocks, n = blocks_of(shape), sum(shape)
        tl = Tally(f"control, not partite, {shape}", len(shape))
        for _ in range(300):
            chosen = [m for m in range(1, 1 << n) if bin(m).count("1") <= 3 and rng.random() < 0.15]
            tl.add(stats(truth(chosen, n), n, blocks), chosen)
        r = tl.row()
        r["note"] = "negative control: violations expected"
        rows.append(r)
        print(f"  {r['name']:40s} cases={r['cases']:7d} viol={r['violations']} (expected > 0)", flush=True)
    print("(2) random members")
    for shape, cnt in [((3, 3), 300), ((4, 4), 200), ((2, 2, 2), 400), ((3, 3, 3), 150), ((3, 3, 2), 200),
                       ((2, 2, 2, 2), 200), ((3, 2, 2, 2), 100), ((2, 2, 2, 2, 2), 60)]:
        for dens in (0.2, 0.5):
            show(random_members(shape, cnt, rng, dens))
    print("(3) greedy search for the largest H/I in the class")
    for shape, rs in [((2, 2), 30), ((3, 3), 15), ((2, 2, 2), 30), ((3, 2, 2), 15), ((3, 3, 3), 6), ((2, 2, 2, 2), 10)]:
        show(greedy(shape, rs, rng))
    print("(4) side search, evidence only: general polynomials of GF(2) degree <= 3 (no block condition), H/I against 4")
    for n in (5, 6, 7):
        mons = [m for m in range(1, 1 << n) if bin(m).count("1") <= 3]
        tl = greedy((n,), 12 if n < 7 else 6, rng, mons=mons, name=f"greedy cubic n={n}", K=3)
        r = tl.row()
        r["note"] = "K=3 here only labels the bound 4 = 2(deg-1); the block checks are vacuous (one block)"
        rows.append(r)
        print(f"  {r['name']:40s} cases={r['cases']:7d} max H/I={r['max_H_over_I']:.6f}  (4 = 2(deg-1))", flush=True)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "block_partite.json")
    with open(out, "w", encoding="utf-8", newline="") as fh:
        json.dump(dict(script="code/block_partite.py", seed=20261012, rows=rows, seconds=time.time() - t0), fh,
                  indent=1)
        fh.write("\n")
    print(f"done in {time.time() - t0:.1f} s")


if __name__ == "__main__":
    main()
