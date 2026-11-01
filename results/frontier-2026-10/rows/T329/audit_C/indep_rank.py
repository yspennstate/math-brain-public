"""Independent check of T329's hashing step (agent C, 20 Oct): probability that a group's k hash vectors
(low m bits of a random degree-(k-1) polynomial mod P at k distinct keys) are GF(2)-dependent, against the bound
2^k (2^-m + 1/P). Rank computed by a column-pivot elimination over python ints (different from the dossier's row solve)."""
import random, sys
def isprime(p):
    if p < 2: return False
    i = 2
    while i * i <= p:
        if p % i == 0: return False
        i += 1
    return True
def rank_gf2(vecs, m):
    rows = list(vecs); r = 0
    for col in range(m):
        piv = next((i for i in range(r, len(rows)) if rows[i] >> col & 1), None)
        if piv is None: continue
        rows[r], rows[piv] = rows[piv], rows[r]
        for i in range(len(rows)):
            if i != r and rows[i] >> col & 1: rows[i] ^= rows[r]
        r += 1
    return r
rng = random.Random(int(sys.argv[1]) if len(sys.argv) > 1 else 1)
for k, N in ((8, 2**20), (10, 2**24), (12, 2**24)):
    for dm in (0, 1, 2, 4, 6):
        m = k + dm
        P = max(N, 2 ** (m + 6)) + 1
        while not isprime(P): P += 1
        trials, bad = 4000, 0
        for _ in range(trials):
            keys = rng.sample(range(N), k)
            c = [rng.randrange(P) for _ in range(k)]
            hv = []
            for u in keys:
                v = 0
                for ci in reversed(c): v = (v * u + ci) % P
                hv.append(v % (2 ** m))
            bad += rank_gf2(hv, m) < k
        bound = min(1.0, (2 ** k - 1) * (2.0 ** -m + 1.0 / P))
        print(f"k={k:2d} m=k+{dm} P~2^{P.bit_length()}  P(dependent)={bad/trials:.4f}  union bound={bound:.4f}  ok={bad/trials <= bound + 3*(bound/trials)**0.5 + 1e-9}")
