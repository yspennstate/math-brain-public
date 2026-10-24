"""Fast exhaustive K2 search at n = 6 (|A| = 2 fixed, |C| = 4) using additivity over rows.

H(f) = sum_T a(V_T),  a(V) = w (L + H(q)),  L = log2(1/w);   I(f) = sum_T [ b(V_T) + |T| w(V_T) ],  b = w I(q).
For a test value lam we maximise  sum_T [a - lam (b + |T| w)]  over valid quadruples; the global maximum is
> 0 iff some f has H/I > lam.  Dinkelbach iteration gives the exact maximum ratio over the enumerated set.
Validity: rows 1,2,12 have the same half-mask as row 0, their two-masks partition the zero set of row 0,
and at each half point the product of the four signs is -1.  Row 0 is a canonical orbit representative
and has maximal weight (see rows4.py for the symmetry argument).
Floats are evidence only; the best function is re-verified exactly afterwards."""
import numpy as np, itertools, math, sys, json, time
from collections import defaultdict
sys.path.insert(0, ".")
import rows4 as R4

M = 4; N = 16

def row_stats(rows):
    Hm = R4.hadamard(M)
    V = np.array(rows, dtype=np.int64)
    W = V @ Hm.T                      # integer, ghat(U) = W/(2N)
    s = (V * V).sum(axis=1)           # w = s/(4N)
    w = s / (4.0 * N)
    Q = (W * W).astype(np.float64)
    tot = Q.sum(axis=1)
    pops = np.array([bin(U).count("1") for U in range(N)], dtype=np.float64)
    a = np.zeros(len(rows)); b = np.zeros(len(rows))
    nz = tot > 0
    q = np.zeros_like(Q)
    q[nz] = Q[nz] / tot[nz, None]
    with np.errstate(divide="ignore", invalid="ignore"):
        lq = np.where(q > 0, np.log2(np.where(q > 0, q, 1.0)), 0.0)
    Hq = -(q * lq).sum(axis=1)
    Iq = (q * pops[None, :]).sum(axis=1)
    L = np.zeros(len(rows))
    L[nz] = -np.log2(w[nz])
    a[nz] = w[nz] * (L[nz] + Hq[nz])
    b[nz] = w[nz] * Iq[nz]
    return s, w, a, b

def masks_arr(rows):
    V = np.abs(np.array(rows, dtype=np.int64))
    pw = (1 << np.arange(N, dtype=np.int64))
    half = ((V == 1) * pw).sum(axis=1)
    two = ((V == 2) * pw).sum(axis=1)
    return half, two

def sign_code(row, halfpts):
    c = 0
    for k, x in enumerate(halfpts):
        if row[x] < 0:
            c |= 1 << k
    return c

def one_pass(lam, rows, s, w, a, b, half, two, reps, rep_idx, by_half):
    best_val = -1e18; best_f = None
    full = (1 << N) - 1
    for r0i in rep_idx:
        r0 = rows[r0i]
        h0 = int(half[r0i]); t0m = int(two[r0i])
        z0 = full & ~h0 & ~t0m
        halfpts = [x for x in range(N) if h0 >> x & 1]
        nh = len(halfpts)
        base = a[r0i] - lam * b[r0i]
        cand = by_half.get(h0, [])
        if len(cand) == 0:
            continue
        cand = np.array(cand)
        cand = cand[(two[cand] & ~z0) == 0]
        cand = cand[s[cand] <= s[r0i]]
        if len(cand) == 0:
            continue
        # best value per (two-mask, sign code) for slot |T|=1 and |T|=2
        best1 = defaultdict(dict); best3 = defaultdict(dict)
        arg1 = defaultdict(dict); arg3 = defaultdict(dict)
        for ci in cand:
            tm = int(two[ci]); sc = sign_code(rows[ci], halfpts)
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
            S2s = keys[(keys & ~rem1) == 0]
            for S2 in S2s:
                S2 = int(S2)
                S3 = rem1 & ~S2
                if S3 not in keyset:
                    continue
                b1 = best1[S1]; b2 = best1[S2]; b3 = best3[S3]
                for sc1, v1 in b1.items():
                    for sc2, v2 in b2.items():
                        sc3 = s0 ^ sc1 ^ sc2 ^ allones
                        v3 = b3.get(sc3)
                        if v3 is None:
                            continue
                        tot = base + v1 + v2 + v3
                        if tot > best_val:
                            best_val = tot
                            best_f = (r0i, arg1[S1][sc1], arg1[S2][sc2], arg3[S3][sc3])
    return best_val, best_f

def main(pkl, out):
    t0 = time.time()
    fs = {r: R4.full_support_small(r) for r in range(4)}
    fs[4] = R4.full_support_4(pkl)
    rows = R4.all_rows(fs)
    s, w, a, b = row_stats(rows)
    half, two = masks_arr(rows)
    pos = {r: i for i, r in enumerate(rows)}
    reps = []
    for r in range(M + 1):
        Rr = tuple(range(r))
        for phi in R4.canon_phi_reps(fs[r], r):
            reps.append(R4.embed(phi, Rr, 0))
    rep_idx = [pos[r] for r in reps]
    by_half = defaultdict(list)
    for i in range(len(rows)):
        by_half[int(half[i])].append(i)
    print("rows", len(rows), "reps", len(reps), "setup", round(time.time() - t0, 1), flush=True)
    lam = 2.9
    history = []
    while True:
        val, fbest = one_pass(lam, rows, s, w, a, b, half, two, reps, rep_idx, by_half)
        Hf = sum(a[i] for i in fbest)
        If = sum(b[i] for i in fbest) + w[fbest[1]] + w[fbest[2]] + 2 * w[fbest[3]]
        ratio = Hf / If
        history.append(dict(lam=lam, val=val, ratio=ratio, H=Hf, I=If, rows=[rows[i] for i in fbest]))
        print("lam", lam, "max", val, "best ratio", ratio, "time", round(time.time() - t0, 1), flush=True)
        if ratio <= lam + 1e-12:
            break
        lam = ratio
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(history, fh, indent=1)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
