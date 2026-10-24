"""Exhaustive K2 search at n = 6 (two fixed addresses, |C| = m = 4) by rows.

Rows V_T = 2 g_T : {0..15} -> {0,+-1,+-2}.  Every product row is chi_{D1}(x) * phi(x_R) with phi a
full-support product function on R.  Full-support product functions:
  r <= 3 : brute force over 5^(2^r) value vectors;
  r = 4  : V_lo=(S+D)/2, V_hi=(S-D)/2 with S, D full-support product-magnitude on 3 bits (values in
           [-4,4]) sharing one normalized magnitude pattern (prod3_wide.pkl).
Symmetry: by y-character multiplication any row can be moved to T = empty, so WLOG row 0 has maximal
weight; by x-translations, x-characters, x-permutations and global negation, row 0 can be taken as a
canonical representative phi0 on the first r coordinates (constant in the others) with D1 = empty.
"""
import numpy as np, itertools, math, sys, json, time, pickle
from collections import defaultdict

M = 4
N = 1 << M

def hadamard(m):
    Hm = np.array([[1]], dtype=np.int64)
    for _ in range(m):
        Hm = np.block([[Hm, Hm], [Hm, -Hm]])
    return Hm

def is_product_law(q, m):
    for i in range(m):
        bit = 1 << i
        ref = None
        for U in range(1 << m):
            if U & bit:
                continue
            a, b = int(q[U]), int(q[U | bit])
            if a or b:
                if ref is None:
                    ref = (a, b)
                elif a * ref[1] != b * ref[0]:
                    return False
    return True

def full_support_small(r):
    """All full-support product phi on r bits, values {0,+-1,+-2}, r <= 3."""
    if r == 0:
        return [(1,), (-1,), (2,), (-2,)]
    n = 1 << r
    Hr = hadamard(r)
    vals = np.array([0, 1, -1, 2, -2], dtype=np.int64)
    ids = np.arange(5 ** n, dtype=np.int64)
    V = np.empty((len(ids), n), dtype=np.int64)
    t = ids.copy()
    for x in range(n):
        V[:, x] = vals[t % 5]
        t //= 5
    W = V @ Hr.T
    A = np.abs(W)
    ok = np.all(A > 0, axis=1)
    for i in range(r):
        bit = 1 << i
        Us = [U for U in range(n) if not U & bit]
        for j in range(len(Us)):
            for k in range(j + 1, len(Us)):
                u, v = Us[j], Us[k]
                ok &= (A[:, u | bit] * A[:, v] == A[:, u] * A[:, v | bit])
    return [tuple(int(v) for v in row) for row in V[ok]]

def full_support_4(pkl):
    with open(pkl, "rb") as fh:
        groups = pickle.load(fh)
    out = set()
    for key, lst in groups.items():
        arrS = np.array([s for s, g in lst], dtype=np.int64)
        for S, _ in lst:
            S = np.array(S, dtype=np.int64)
            # D ranges over the same group; need same parity and |S|+|D| <= 4 pointwise
            okpar = np.all(((arrS - S[None, :]) % 2) == 0, axis=1)
            okmag = np.all(np.abs(arrS) + np.abs(S)[None, :] <= 4, axis=1)
            for D in arrS[okpar & okmag]:
                lo = (S + D) // 2
                hi = (S - D) // 2
                # V(x, x4): index x + 8*x4  (bit 3 = coordinate 3)
                out.add(tuple(int(v) for v in lo) + tuple(int(v) for v in hi))
    return sorted(out)

def embed(phi, R, D1):
    """phi on |R| bits (index by bits in order of R) -> 4-bit row times chi_{D1}."""
    row = []
    for x in range(N):
        idx = 0
        for k, c in enumerate(R):
            if x >> c & 1:
                idx |= 1 << k
        s = -1 if bin(x & D1).count("1") % 2 else 1
        row.append(s * phi[idx])
    return tuple(row)

def all_rows(fs):
    rows = set()
    rows.add(tuple([0] * N))
    for r in range(M + 1):
        for R in itertools.combinations(range(M), r):
            rest = [c for c in range(M) if c not in R]
            for dsz in range(len(rest) + 1):
                for Dset in itertools.combinations(rest, dsz):
                    D1 = sum(1 << c for c in Dset)
                    for phi in fs[r]:
                        rows.add(embed(phi, R, D1))
    return sorted(rows)

def canon_phi_reps(phis, r):
    """Orbit representatives of full-support phi on r bits under translations, character mult,
    coordinate permutations and negation."""
    n = 1 << r
    seen = set()
    reps = []
    perms = list(itertools.permutations(range(r)))
    for phi in phis:
        if phi in seen:
            continue
        reps.append(phi)
        orbit = set()
        for p in perms:
            for a in range(n):
                for V in range(n):
                    for sg in (1, -1):
                        new = [0] * n
                        for x in range(n):
                            # permute bits of x
                            y = 0
                            for k in range(r):
                                if x >> k & 1:
                                    y |= 1 << p[k]
                            val = phi[x ^ a] if True else 0
                            chi = -1 if bin(y & V).count("1") % 2 else 1
                            new[y] = sg * chi * phi[x ^ a]
                        orbit.add(tuple(new))
        seen |= orbit
    return reps

def masks(row):
    half = 0; two = 0
    for x, v in enumerate(row):
        if abs(v) == 1:
            half |= 1 << x
        elif abs(v) == 2:
            two |= 1 << x
    return half, two

def weight_num(row):
    return sum(v * v for v in row)  # w_T = weight_num / (4 * N)

def HI(rows):
    Hm = hadamard(M)
    tot = 4 ** (M + 2)
    H = 0.0; I = 0.0
    Tpop = [0, 1, 1, 2]
    s2 = 0
    for T in range(4):
        Wt = Hm @ np.array(rows[T], dtype=np.int64)
        for U in range(N):
            w = 2 * int(Wt[U])
            if w:
                s2 += w * w
                p = w * w / tot
                H -= p * math.log2(p)
                I += p * (bin(U).count("1") + Tpop[T])
    assert s2 == tot
    return H, I

def main(pkl, out):
    t0 = time.time()
    fs = {r: full_support_small(r) for r in range(4)}
    fs[4] = full_support_4(pkl)
    print({r: len(fs[r]) for r in fs}, "time", round(time.time() - t0, 1), flush=True)
    rows = all_rows(fs)
    print("all product rows on 4 bits (incl zero):", len(rows), round(time.time() - t0, 1), flush=True)
    # index by half-mask then two-mask
    idx = defaultdict(lambda: defaultdict(list))
    for row in rows:
        h, t = masks(row)
        idx[h][t].append(row)
    # representatives for row 0
    reps = []
    for r in range(M + 1):
        R = tuple(range(r))
        for phi in canon_phi_reps(fs[r], r):
            reps.append(embed(phi, R, 0))
    print("row-0 representatives:", len(reps), round(time.time() - t0, 1), flush=True)
    best = []
    nfun = 0
    full = (1 << N) - 1
    for r0 in reps:
        w0 = weight_num(r0)
        h0, t0m = masks(r0)
        z0 = full & ~h0 & ~t0m
        cand = idx.get(h0, {})
        # two-masks inside z0 with rows of weight <= w0
        keys = {}
        for tm, lst in cand.items():
            if tm & ~z0:
                continue
            l2 = [r for r in lst if weight_num(r) <= w0]
            if l2:
                keys[tm] = l2
        klist = list(keys.keys())
        halfpts = [x for x in range(N) if h0 >> x & 1]
        for S1 in klist:
            rem1 = z0 & ~S1
            for S2 in klist:
                if S2 & ~rem1:
                    continue
                S3 = rem1 & ~S2
                if S3 not in keys:
                    continue
                for r1 in keys[S1]:
                    for r2 in keys[S2]:
                        for r3 in keys[S3]:
                            ok = True
                            for x in halfpts:
                                if r0[x] * r1[x] * r2[x] * r3[x] != -1:
                                    ok = False
                                    break
                            if not ok:
                                continue
                            nfun += 1
                            Hh, Ii = HI((r0, r1, r2, r3))
                            if Ii > 0:
                                best.append((Hh / Ii, Hh, Ii, (r0, r1, r2, r3)))
                                if len(best) > 5000:
                                    best.sort(key=lambda t: -t[0])
                                    del best[50:]
    best.sort(key=lambda t: -t[0])
    print("functions examined (row 0 canonical & heaviest):", nfun, round(time.time() - t0, 1), flush=True)
    for b in best[:10]:
        print(round(b[0], 6), round(b[1], 6), round(b[2], 6), b[3], flush=True)
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(dict(count=nfun, top=[dict(ratio=b[0], H=b[1], I=b[2], rows=b[3]) for b in best[:50]]), fh, indent=1)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
