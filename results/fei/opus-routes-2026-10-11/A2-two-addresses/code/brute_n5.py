"""Exhaustive scan of K2 at n=5 with the address pair fixed to the two high bits (y), C = 3 low bits (x).
Every f in K2 on 5 variables is a coordinate permutation of one of these.  The fiber f(.,x0) at x0=0 is
fixed to one representative of each of the two fiber orbits (signed character / 2-bit bent) under
y-translations, y-character multiplication and global negation (these preserve K2 with the same A, H, I).

Rows are kept as integers G_T(x) = sum_y f(y,x) chi_T(y) in {0,+-2,+-4}; W_{T u U} = sum_x G_T(x) chi_U(x).
Float logs: evidence only."""
import numpy as np, numba as nb, math, sys, json, time

# fiber pattern p in 0..15: bit y of p set means f(y,x) = -1, y in 0..3 (bit0 = y_low)
def fiber_rows():
    tab = np.zeros((16, 4), dtype=np.int64)
    for p in range(16):
        for T in range(4):
            s = 0
            for y in range(4):
                fv = -1 if (p >> y) & 1 else 1
                chi = -1 if bin(T & y).count("1") % 2 else 1
                s += fv * chi
            tab[p, T] = s
    return tab

TAB = fiber_rows()

@nb.njit(cache=True)
def wht8(a):
    b = a.copy()
    h = 1
    while h < 8:
        for i in range(0, 8, 2 * h):
            for j in range(i, i + h):
                u = b[j]; v = b[j + h]
                b[j] = u + v; b[j + h] = u - v
        h *= 2
    return b

@nb.njit(cache=True)
def is_prod3(q):
    for i in range(3):
        bit = 1 << i
        a0 = -1; b0 = -1
        for U in range(8):
            if U & bit:
                continue
            a = q[U]; b = q[U | bit]
            if a != 0 or b != 0:
                if a0 < 0:
                    a0 = a; b0 = b
                elif a * b0 != b * a0:
                    return False
    return True

@nb.njit(cache=True)
def popc(x):
    c = 0
    while x:
        c += x & 1
        x >>= 1
    return c

@nb.njit(cache=True)
def run(tab, p0, topk):
    best = np.zeros(topk)
    bestcode = np.zeros(topk, dtype=np.int64)
    G = np.zeros((4, 8), dtype=np.int64)
    q = np.zeros(8, dtype=np.int64)
    W = np.zeros(32, dtype=np.int64)
    count = 0
    total = 16 ** 7
    for code in range(total):
        c = code
        for T in range(4):
            G[T, 0] = tab[p0, T]
        for x in range(1, 8):
            p = c & 15
            c >>= 4
            for T in range(4):
                G[T, x] = tab[p, T]
        ok = True
        for T in range(4):
            Wt = wht8(G[T])
            for U in range(8):
                q[U] = Wt[U] * Wt[U]
                W[U + 8 * T] = Wt[U]
            if not is_prod3(q):
                ok = False
                break
        if not ok:
            continue
        count += 1
        # H, I in bits; total sum W^2 = 4^5 = 1024
        H = 0.0; I = 0.0
        for S in range(32):
            if W[S] != 0:
                pr = W[S] * W[S] / 1024.0
                H -= pr * math.log2(pr)
                # S = U + 8T: |S| = popc(U) + popc(T)
                I += pr * (popc(S & 7) + popc(S >> 3))
        if I > 0:
            r = H / I
            if r > best[topk - 1] + 1e-12:
                # insert
                k = topk - 1
                while k > 0 and best[k - 1] < r:
                    best[k] = best[k - 1]; bestcode[k] = bestcode[k - 1]
                    k -= 1
                best[k] = r; bestcode[k] = code
    return count, best, bestcode

if __name__ == "__main__":
    out = {}
    t0 = time.time()
    # representatives: p0 = 0 (constant +1 fiber), p0 = 8 (f(y)=-1 iff y=3: 2-bit AND-type bent)
    for p0 in (0, 8):
        cnt, best, bestcode = run(TAB, p0, 20)
        out[str(p0)] = dict(count=int(cnt), best=[float(b) for b in best], codes=[int(c) for c in bestcode])
        print(p0, cnt, best[:5], bestcode[:5], time.time() - t0, flush=True)
    with open(sys.argv[1], "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1)
