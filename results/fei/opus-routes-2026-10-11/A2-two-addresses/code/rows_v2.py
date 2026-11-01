"""Exhaustive K2 search with the address pair fixed and |C| = m (m = 3 or 4), corrected symmetry use.

Only symmetries that preserve BOTH H and I are used: x-translations (signs of coefficients), x-coordinate
permutations, and global negation, applied to the whole function.  (Character multiplication preserves H
but changes I, and so does moving rows between address positions; neither is used.)  Row 0 (T = empty)
runs over orbit representatives of ALL product rows (including the zero row); rows 1, 2, 12 run over all
product rows compatible with row 0.  H and I are additive over rows, so a Dinkelbach iteration finds the
exact maximum of H/I over the enumerated set (floats for logs: evidence).

Usage: python rows_v2.py m [pkl_for_m4] out.json [--count]
"""
import numpy as np, itertools, math, sys, json, time
from collections import defaultdict
sys.path.insert(0, ".")
import rows4 as R4

def product_rows(m, pkl=None):
    if m == 4:
        fs = {r: R4.full_support_small(r) for r in range(4)}
        fs[4] = R4.full_support_4(pkl)
        return R4.all_rows(fs)
    # m <= 3: brute force over 5^(2^m)
    import rows_search as RS
    return sorted(set(RS.product_rows(m)))

def hadamard(m):
    Hm = np.array([[1]], dtype=np.int64)
    for _ in range(m):
        Hm = np.block([[Hm, Hm], [Hm, -Hm]])
    return Hm

def row_stats(rows, m):
    N = 1 << m
    Hm = hadamard(m)
    V = np.array(rows, dtype=np.int64)
    W = V @ Hm.T
    s = (V * V).sum(axis=1)
    w = s / (4.0 * N)
    Q = (W * W).astype(np.float64)
    tot = Q.sum(axis=1)
    pops = np.array([bin(U).count("1") for U in range(N)], dtype=np.float64)
    nz = tot > 0
    q = np.zeros_like(Q)
    q[nz] = Q[nz] / tot[nz, None]
    lq = np.where(q > 0, np.log2(np.where(q > 0, q, 1.0)), 0.0)
    Hq = -(q * lq).sum(axis=1)
    Iq = (q * pops[None, :]).sum(axis=1)
    a = np.zeros(len(rows)); b = np.zeros(len(rows))
    a[nz] = w[nz] * (-np.log2(w[nz]) + Hq[nz])
    b[nz] = w[nz] * Iq[nz]
    return s, w, a, b

def masks_arr(rows, m):
    N = 1 << m
    V = np.abs(np.array(rows, dtype=np.int64))
    pw = (1 << np.arange(N, dtype=np.int64))
    return ((V == 1) * pw).sum(axis=1), ((V == 2) * pw).sum(axis=1)

def orbit_reps(rows, m):
    """Representatives under x -> perm(x xor a) and negation (H- and I-preserving)."""
    N = 1 << m
    V = np.array(rows, dtype=np.int64)
    base = 5 ** np.arange(N, dtype=np.int64)
    enc = lambda A: ((A % 5) * base).sum(axis=1)   # values -2..2 -> 0..4 via mod 5
    best = None
    for perm in itertools.permutations(range(m)):
        for a in range(N):
            # new row: newV[pi(x xor a)] = V[x]  <=>  newV[y] = V[pi^{-1}(y) xor a]
            src = np.zeros(N, dtype=np.int64)
            for y in range(N):
                x = 0
                for k in range(m):
                    if y >> perm[k] & 1:
                        x |= 1 << k
                src[y] = x ^ a
            A = V[:, src]
            for sg in (1, -1):
                c = enc(sg * A)
                best = c if best is None else np.minimum(best, c)
    _, idx = np.unique(best, return_index=True)
    return sorted(int(i) for i in idx)

def sign_code(row, halfpts):
    c = 0
    for k, x in enumerate(halfpts):
        if row[x] < 0:
            c |= 1 << k
    return c

def one_pass(lam, m, rows, s, w, a, b, half, two, rep_idx, by_half, count_only=False):
    N = 1 << m
    full = (1 << N) - 1
    best_val = -1e18; best_f = None; count = 0
    for r0i in rep_idx:
        r0 = rows[r0i]
        h0 = int(half[r0i]); t0m = int(two[r0i])
        z0 = full & ~h0 & ~t0m
        halfpts = [x for x in range(N) if h0 >> x & 1]
        nh = len(halfpts)
        base = a[r0i] - lam * b[r0i]
        cand = by_half.get(h0)
        if cand is None:
            continue
        cand = cand[(two[cand] & ~z0) == 0]
        if len(cand) == 0:
            continue
        best1 = defaultdict(dict); best3 = defaultdict(dict)
        arg1 = defaultdict(dict); arg3 = defaultdict(dict)
        cnt = defaultdict(lambda: defaultdict(int))
        for ci in cand:
            tm = int(two[ci]); sc = sign_code(rows[ci], halfpts)
            cnt[tm][sc] += 1
            v1 = a[ci] - lam * (b[ci] + w[ci]); v3 = a[ci] - lam * (b[ci] + 2 * w[ci])
            if v1 > best1[tm].get(sc, -1e18):
                best1[tm][sc] = v1; arg1[tm][sc] = ci
            if v3 > best3[tm].get(sc, -1e18):
                best3[tm][sc] = v3; arg3[tm][sc] = ci
        keys = np.array(sorted(best1.keys()), dtype=np.int64)
        keyset = set(int(k) for k in keys)
        s0 = sign_code(r0, halfpts)
        allones = (1 << nh) - 1
        for S1 in keys:
            S1 = int(S1)
            rem1 = z0 & ~S1
            for S2 in keys[(keys & ~rem1) == 0]:
                S2 = int(S2)
                S3 = rem1 & ~S2
                if S3 not in keyset:
                    continue
                for sc1, v1 in best1[S1].items():
                    for sc2, v2 in best1[S2].items():
                        sc3 = s0 ^ sc1 ^ sc2 ^ allones
                        v3 = best3[S3].get(sc3)
                        if v3 is None:
                            continue
                        if count_only:
                            count += cnt[S1][sc1] * cnt[S2][sc2] * cnt[S3][sc3]
                            continue
                        tot = base + v1 + v2 + v3
                        if tot > best_val:
                            best_val = tot
                            best_f = (r0i, arg1[S1][sc1], arg1[S2][sc2], arg3[S3][sc3])
    return (count if count_only else (best_val, best_f))

def main():
    m = int(sys.argv[1])
    pkl = sys.argv[2] if m == 4 else None
    out = sys.argv[3] if m == 4 else sys.argv[2]
    count_only = "--count" in sys.argv
    t0 = time.time()
    rows = product_rows(m, pkl)
    s, w, a, b = row_stats(rows, m)
    half, two = masks_arr(rows, m)
    by_half = defaultdict(list)
    for i in range(len(rows)):
        by_half[int(half[i])].append(i)
    by_half = {k: np.array(v, dtype=np.int64) for k, v in by_half.items()}
    if count_only:
        rep_idx = list(range(len(rows)))   # no symmetry: exact count of functions with this address pair
        c = one_pass(0.0, m, rows, s, w, a, b, half, two, rep_idx, by_half, count_only=True)
        print("m", m, "functions in K2 with the fixed address pair:", c, "time", round(time.time() - t0, 1))
        return
    rep_idx = orbit_reps(rows, m)
    print("m", m, "rows", len(rows), "row-0 reps", len(rep_idx), "setup", round(time.time() - t0, 1), flush=True)
    lam = 2.9
    hist = []
    while True:
        val, fb = one_pass(lam, m, rows, s, w, a, b, half, two, rep_idx, by_half)
        Hf = sum(a[i] for i in fb)
        If = sum(b[i] for i in fb) + w[fb[1]] + w[fb[2]] + 2 * w[fb[3]]
        hist.append(dict(lam=lam, val=val, ratio=Hf / If, H=Hf, I=If, rows=[rows[i] for i in fb]))
        print("lam", lam, "max", val, "ratio", Hf / If, "rows", [rows[i] for i in fb], "t", round(time.time() - t0, 1), flush=True)
        if Hf / If <= lam + 1e-12:
            break
        lam = Hf / If
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(hist, fh, indent=1)

if __name__ == "__main__":
    main()
