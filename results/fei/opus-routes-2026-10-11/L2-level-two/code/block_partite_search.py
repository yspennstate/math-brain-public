"""Search for the largest H/I among K-partite GF(2) polynomials (evidence for D_K, NOTES section 5e, Corollary K).

Simulated annealing over sets of allowed monomials (at most one variable per block), objective H/I, with restarts from
random sets and from the single monomial that takes one variable from each block (AND of K bits up to sign). Every
accepted state is re-checked against Corollary K (H <= 2 (K - 1) I) and the per-block Lemma B bound.
Usage: python -B block_partite_search.py   (writes ../data/block_partite_search.json and prints the log)
"""
import itertools, json, math, os, time
import numpy as np


def fwht_inplace(a):
    h, n = 1, len(a)
    while h < n:
        a = a.reshape(-1, 2 * h)
        x = a[:, :h].copy()
        a[:, :h] += a[:, h:]
        a[:, h:] = x - a[:, h:]
        a = a.reshape(-1)
        h *= 2
    return a


class Space:
    def __init__(self, shape):
        self.shape = shape
        self.K = len(shape)
        self.n = sum(shape)
        blocks, c = [], 0
        for s in shape:
            blocks.append(list(range(c, c + s)))
            c += s
        self.blocks = blocks
        choices = [[0] + [1 << v for v in b] for b in blocks]
        self.mons = sorted({sum(ch) for ch in itertools.product(*choices)} - {0})
        idx = np.arange(1 << self.n)
        self.rows = np.array([((idx & m) == m) for m in self.mons], dtype=np.int8)
        self.pop = np.array([bin(i).count("1") for i in range(1 << self.n)], dtype=float)
        self.masks = [sum(1 << v for v in b) for b in blocks]
        self.idx = idx
        self.full = (1 << self.n) - 1

    def eval(self, P):
        F = (1 - 2 * P).astype(float)
        c = fwht_inplace(F) / (1 << self.n)
        p = c * c
        I = float(self.pop @ p)
        q = p[p > 1e-300]
        H = float(-(q * np.log2(q)).sum())
        return H, I, p

    def check(self, p, H, I):
        bad = 0
        tot = 0.0
        for b, mask in zip(self.blocks, self.masks):
            marg = np.bincount(self.idx & mask, weights=p, minlength=1 << self.n)
            m = marg[marg > 1e-300]
            Hk = float(-(m * np.log2(m)).sum())
            Ik = float(sum(p[((self.idx >> v) & 1) == 1].sum() for v in b))
            bad += Hk > 2 * (I - Ik) + 1e-9
            tot += Hk
        bad += H > tot + 1e-9
        bad += tot > 2 * (self.K - 1) * I + 1e-9
        return int(bad)


def anneal(sp, rng, start, steps, T0=0.08, T1=0.002):
    P = np.zeros(1 << sp.n, dtype=np.int8)
    cur = np.zeros(len(sp.mons), dtype=bool)
    for k in start:
        cur[k] = True
        P ^= sp.rows[k]
    H, I, p = sp.eval(P)
    s = H / I if I > 1e-12 else 0.0
    best = (s, cur.copy(), H, I)
    viol = sp.check(p, H, I)
    for t in range(steps):
        T = T0 * (T1 / T0) ** (t / max(1, steps - 1))
        k = int(rng.integers(len(sp.mons)))
        P ^= sp.rows[k]
        H2, I2, p2 = sp.eval(P)
        s2 = H2 / I2 if I2 > 1e-12 else 0.0
        if s2 >= s or rng.random() < math.exp((s2 - s) / T):
            cur[k] = not cur[k]
            s, H, I, p = s2, H2, I2, p2
            if s > best[0] + 1e-12:
                best = (s, cur.copy(), H, I)
                viol += sp.check(p, H, I)
        else:
            P ^= sp.rows[k]
    return best, viol


def main():
    t0 = time.time()
    rng = np.random.default_rng(20261012)
    rows = []
    print("simulated annealing for max H/I over K-partite GF(2) polynomials")
    plan = [((2, 2, 2), 12, 3000), ((3, 3, 2), 10, 3000), ((3, 3, 3), 8, 3000), ((4, 3, 3), 6, 2500),
            ((4, 4, 4), 4, 2000), ((2, 2, 2, 2), 10, 3000), ((3, 3, 3, 3), 4, 2000)]
    for shape, restarts, steps in plan:
        sp = Space(shape)
        tops, viol = [], 0
        andK = [sp.mons.index(sum(1 << b[0] for b in sp.blocks))]
        for r in range(restarts):
            if r % 3 == 0:
                start = andK
            else:
                dens = float(rng.uniform(0.05, 0.3))
                start = [k for k in range(len(sp.mons)) if rng.random() < dens]
            best, v = anneal(sp, rng, start, steps)
            viol += v
            tops.append((best[0], int(best[1].sum())))
        H_and, I_and, _ = sp.eval(sp.rows[andK[0]].copy())
        mx = max(tops)
        row = dict(shape=list(shape), K=sp.K, monomials=len(sp.mons), restarts=restarts, steps=steps,
                   max_H_over_I=mx[0], monomials_at_max=mx[1], and_K=H_and / I_and, bound=2 * (sp.K - 1),
                   violations=viol, all_restarts=[round(a, 6) for a, _ in sorted(tops, reverse=True)])
        rows.append(row)
        print(f"  {str(shape):14s} K={sp.K} monomials={len(sp.mons):3d}  max H/I={mx[0]:.6f} ({mx[1]} monomials)  "
              f"AND_K={H_and / I_and:.6f}  bound={2 * (sp.K - 1)}  violations={viol}  "
              f"restarts: {', '.join(f'{a:.4f}' for a, _ in sorted(tops, reverse=True)[:5])}", flush=True)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "block_partite_search.json")
    with open(out, "w", encoding="utf-8", newline="") as fh:
        json.dump(dict(script="code/block_partite_search.py", seed=20261012, rows=rows, seconds=time.time() - t0), fh,
                  indent=1)
        fh.write("\n")
    print(f"done in {time.time() - t0:.1f} s")


if __name__ == "__main__":
    main()
