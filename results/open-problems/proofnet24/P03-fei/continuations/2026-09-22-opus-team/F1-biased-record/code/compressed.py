"""Fast exact evaluation of g when only the inputs in a small set K are biased (the rest at 1/2).

For B a subset of the unbiased coordinates and A a subset of K,
    Ghat_mu(A u B) = prod_{i in A} sqrt(V_i) * sum_{S subset K minus A} prod_{j in S} mu_j * ghat(A u S u B).
Group the sets B by the key (|B|, (ghat(A u B))_{A subset K}); every quantity is a sum over classes with multiplicity.
Returns Htilde, It_i for i in K, the sum of It over the unbiased inputs, and Pr[F true].
"""
import numpy as np
from collections import Counter
from gate import load_table, biased_spectrum, N

_W = None


def walsh():
    global _W
    if _W is None:
        t = load_table()
        c = biased_spectrum(t, [0.5] * N)
        _W = np.rint(c * (1 << N)).astype(np.int64)
    return _W


class Compressed:
    def __init__(self, K):
        self.K = list(K)
        k = len(K)
        W = walsh()
        idx = np.arange(1 << N, dtype=np.int64)
        Kmask = sum(1 << i for i in K)
        B = idx[(idx & Kmask) == 0]
        pcB = np.array([bin(int(x)).count("1") for x in B])
        subs = []
        for a in range(1 << k):
            m = sum(1 << K[j] for j in range(k) if (a >> j) & 1)
            subs.append(m)
        cols = np.stack([W[B | m] for m in subs], axis=1)            # (|B|, 2^k)
        keys = np.concatenate([pcB[:, None], cols], axis=1)
        uniq, inv, cnt = np.unique(keys, axis=0, return_inverse=True, return_counts=True)
        self.level = uniq[:, 0].astype(float)
        self.coef = uniq[:, 1:].astype(float) / float(1 << N)          # (ncls, 2^k): ghat(A u B), A indexed by bitmask over K
        self.mult = cnt.astype(float)
        self.k = k
        # ghat(S) for S subset K (B empty) for the output mean
        self.ghatK = np.array([W[m] for m in subs], dtype=float) / float(1 << N)

    def evaluate(self, p):
        """p: array (..., k) of truth probabilities of the biased inputs. Returns dict of arrays of shape (...)."""
        p = np.asarray(p, dtype=float)
        mu = 1.0 - 2.0 * p
        sq = np.sqrt(np.clip(1.0 - mu * mu, 0.0, None))
        k = self.k
        shp = p.shape[:-1]
        # transform the class coefficient vectors axis by axis (same 2x2 transform as in gate.py, in the mu basis)
        # coefficient vector over A (bitmask); for each coordinate j: new[A without j] = old[A w/o j] + mu_j old[A w j], new[A with j] = sqrt(V_j) old[A w j]
        cur = np.broadcast_to(self.coef, shp + self.coef.shape).copy()      # (..., ncls, 2^k)
        for j in range(k):
            bit = 1 << j
            lo_idx = [a for a in range(1 << k) if not a & bit]
            hi_idx = [a | bit for a in lo_idx]
            lo = cur[..., lo_idx]; hi = cur[..., hi_idx]
            m = mu[..., j][..., None, None]; s = sq[..., j][..., None, None]
            cur[..., lo_idx] = lo + m * hi
            cur[..., hi_idx] = s * hi
        w = cur * cur
        with np.errstate(divide="ignore", invalid="ignore"):
            ent = np.where(w > 0, -w * np.log2(np.where(w > 0, w, 1.0)), 0.0)
        mult = self.mult
        Ht = (ent.sum(axis=-1) * mult).sum(axis=-1)
        It = []
        for j in range(k):
            bit = 1 << j
            hi_idx = [a for a in range(1 << k) if a & bit]
            It.append((w[..., hi_idx].sum(axis=-1) * mult).sum(axis=-1))
        Irest = (w.sum(axis=-1) * mult * self.level).sum(axis=-1)
        # output mean: Ghat(empty) = sum_S prod_{j in S} mu_j ghat(S)
        EF = np.zeros(shp)
        for a in range(1 << k):
            term = np.full(shp, self.ghatK[a])
            for j in range(k):
                if (a >> j) & 1:
                    term = term * mu[..., j]
            EF = EF + term
        return {"Ht": Ht, "It": np.stack(It, axis=-1), "Irest": Irest, "pout": 0.5 * (1.0 - EF)}


if __name__ == "__main__":
    from gate import evaluate
    t = load_table()
    rng = np.random.default_rng(1)
    for K in ([0], [9], [0, 1], [0, 4], [0, 9], [0, 10], [9, 10], [9, 11], [0, 1, 9], [0, 4, 10, 13]):
        cm = Compressed(K)
        p = rng.uniform(0.02, 0.98, size=len(K))
        r = cm.evaluate(p)
        pv = [0.5] * N
        for j, i in enumerate(K):
            pv[i] = p[j]
        Ht, It, po = evaluate(t, pv)
        rest = It.sum() - sum(It[i] for i in K)
        print("K=%-14s classes=%5d  dHt=%.1e dIt=%.1e dIrest=%.1e dpout=%.1e" % (K, len(cm.mult), abs(r["Ht"] - Ht), np.abs(r["It"] - It[K]).max(), abs(r["Irest"] - rest), abs(r["pout"] - po)))
