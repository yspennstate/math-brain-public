"""Row-based exhaustive search of K2 with a fixed address pair and |C| = m (m <= 3 here).

A row is V = 2 g_T : {0..2^m-1} -> {0,+-1,+-2}.  Pointwise, (V_0,V_1,V_2,V_3)(x) (T = 0,{a1},{a2},{a1,a2})
is one-hot +-2, or all +-1 with product of signs -1.  Each row with nonzero weight must have a product
squared-Walsh law.  We enumerate every product row, then every compatible quadruple, and compute
H and I of f exactly in integers (logs in floats: evidence only).

Spectrum of f: fhat(T u U) = ghat_T(U) = What_T(U) / (2 * 2^m) where What_T = WHT(V_T) (integer).
So W_f(T u U) = 2^(m+2) fhat = 2 * What_T(U), and sum W_f^2 = 4^(m+2)."""
import numpy as np, itertools, math, sys, json, time
from collections import defaultdict

def hadamard(m):
    Hm = np.array([[1]], dtype=np.int64)
    for _ in range(m):
        Hm = np.block([[Hm, Hm], [Hm, -Hm]])
    return Hm  # Hm[U, x] = chi_U(x) with bit conventions (bit i of x set <-> x_i = -1)

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

def product_rows(m):
    N = 1 << m
    Hm = hadamard(m)
    vals = np.array([0, 1, -1, 2, -2], dtype=np.int64)
    out = []
    # enumerate 5^N vectors in chunks
    idx = np.arange(5 ** N, dtype=np.int64)
    chunk = 1 << 18
    for start in range(0, 5 ** N, chunk):
        ids = idx[start:start + chunk]
        V = np.empty((len(ids), N), dtype=np.int64)
        t = ids.copy()
        for x in range(N):
            V[:, x] = vals[t % 5]
            t //= 5
        Wt = V @ Hm.T
        Q = Wt * Wt
        # product test vectorised: for each coordinate i, rows (Q[U],Q[U|bit]) proportional
        ok = np.ones(len(ids), dtype=bool)
        for i in range(m):
            bit = 1 << i
            Us = [U for U in range(N) if not U & bit]
            A = Q[:, Us]; B = Q[:, [U | bit for U in Us]]
            # all 2x2 minors A_j B_k - A_k B_j == 0
            for j in range(len(Us)):
                for k in range(j + 1, len(Us)):
                    ok &= (A[:, j] * B[:, k] == A[:, k] * B[:, j])
        for row in V[ok]:
            out.append(tuple(int(v) for v in row))
    return out

def valid_point(v):
    """v = (V0,V1,V2,V3) at a point."""
    mags = [abs(t) for t in v]
    if sorted(mags) == [0, 0, 0, 2]:
        return True
    if mags == [1, 1, 1, 1]:
        s = 1
        for t in v:
            s *= (1 if t > 0 else -1)
        return s == -1
    return False

def HI_of(rows, m):
    """rows: list of 4 tuples (V_T).  Returns (H, I, Wf) using integer Walsh."""
    N = 1 << m
    Hm = hadamard(m)
    tot = 4 ** (m + 2)
    H = 0.0; I = 0.0
    pops = [bin(U).count("1") for U in range(N)]
    Tpop = [0, 1, 1, 2]
    Wf = {}
    for T in range(4):
        Wt = Hm @ np.array(rows[T], dtype=np.int64)
        for U in range(N):
            w = 2 * int(Wt[U])
            if w:
                p = w * w / tot
                H -= p * math.log2(p)
                I += p * (pops[U] + Tpop[T])
                Wf[(T, U)] = w
    assert sum(w * w for w in Wf.values()) == tot
    return H, I, Wf

def search(m, topk=40):
    t0 = time.time()
    cands = product_rows(m)
    N = 1 << m
    print("m", m, "product rows (incl. zero row):", len(cands), "time", round(time.time() - t0, 1), flush=True)
    bymag = defaultdict(list)
    for r in cands:
        bymag[tuple(abs(v) for v in r)].append(r)
    zero = tuple([0] * N)
    results = []
    seen = 0
    for r0 in cands:
        # magnitude pattern of rows 1 and 2 given r0: |r0|=2 -> 0, |r0|=1 -> 1, r0=0 -> 0 or 2
        zeros = [x for x in range(N) if r0[x] == 0]
        halfs = [x for x in range(N) if abs(r0[x]) == 1]
        for sub1 in range(1 << len(zeros)):
            mag1 = [0] * N
            for x in halfs:
                mag1[x] = 1
            for k, x in enumerate(zeros):
                if sub1 >> k & 1:
                    mag1[x] = 2
            L1 = bymag.get(tuple(mag1), [])
            if not L1:
                continue
            rest = [x for k, x in enumerate(zeros) if not sub1 >> k & 1]
            for sub2 in range(1 << len(rest)):
                mag2 = [0] * N
                for x in halfs:
                    mag2[x] = 1
                for k, x in enumerate(rest):
                    if sub2 >> k & 1:
                        mag2[x] = 2
                L2 = bymag.get(tuple(mag2), [])
                if not L2:
                    continue
                mag3 = [0] * N
                for x in halfs:
                    mag3[x] = 1
                for k, x in enumerate(rest):
                    if not sub2 >> k & 1:
                        mag3[x] = 2
                L3 = bymag.get(tuple(mag3), [])
                if not L3:
                    continue
                for r1 in L1:
                    for r2 in L2:
                        for r3 in L3:
                            # sign constraint at half points
                            okp = True
                            for x in halfs:
                                if r0[x] * r1[x] * r2[x] * r3[x] != -1:
                                    okp = False
                                    break
                            if not okp:
                                continue
                            rows = (r0, r1, r2, r3)
                            seen += 1
                            H, I, _ = HI_of(rows, m)
                            if I > 0:
                                results.append((H / I, H, I, rows))
                                if len(results) > 20000:
                                    results.sort(key=lambda t: -t[0])
                                    del results[topk:]
    results.sort(key=lambda t: -t[0])
    print("m", m, "functions found:", seen, "time", round(time.time() - t0, 1), flush=True)
    return seen, results[:topk]

if __name__ == "__main__":
    m = int(sys.argv[1])
    seen, top = search(m)
    for r in top[:15]:
        print(round(r[0], 6), round(r[1], 6), round(r[2], 6), r[3])
    with open(sys.argv[2], "w", encoding="utf-8") as fh:
        json.dump(dict(m=m, count=seen, top=[dict(ratio=r[0], H=r[1], I=r[2], rows=r[3]) for r in top]), fh, indent=1)
