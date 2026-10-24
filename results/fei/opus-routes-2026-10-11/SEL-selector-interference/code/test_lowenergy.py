"""E1: low-energy collision credit.

For every Boolean F on a+n bits, view the low a bits as a fresh selector block.  Check:
  (id)  cost := H(F) - avg_b H(g_b) = H(S_x|S_y) + I(X;Y)            (exact identity, BR eq.(4))
  (U)   cost <= 2 H(S_x|S_y)                                          (Maassen-Uffink)
  (L)   I(X;Y) <= (2/ln2) I_sel                                       (BR Theorem, log-Sobolev)
  (B1)  cost <= 2 sum_i h(Inf_i)
  (B2)  cost <= sum_i h(Inf_i) + (2/ln2) I_sel
All exhaustively for 4 total bits (every split a=1,2,3) and randomly for larger sizes.
Floating point, tolerance 1e-9: this is EVIDENCE for corollaries whose proofs are analytic.
"""
import sys
import numpy as np
from fei_lib import fwht_int, entropy_from_W, popcounts

LN2 = np.log(2.0)


def h2(t):
    t = np.clip(np.asarray(t, dtype=np.float64), 0.0, 1.0)
    out = np.zeros_like(t)
    m = (t > 0) & (t < 1)
    out[m] = -t[m] * np.log2(t[m]) - (1 - t[m]) * np.log2(1 - t[m])
    return out


def analyse(F, a, n):
    """F: +-1 table on a+n bits, selector = low a bits."""
    N = 1 << a
    W = fwht_int(F).astype(np.float64)
    tot = a + n
    P = (W * W) / float(4 ** tot)              # spectral law, index = S + 2^a T
    P2 = P.reshape(1 << n, N)                  # rows T, columns S
    HF = entropy_from_W(W, tot)
    R = P2.sum(axis=1)                         # data marginal
    HSy = float(-np.sum(R[R > 0] * np.log2(R[R > 0])))
    HSx_given_Sy = HF - HSy
    # branches
    B = F.reshape(1 << n, N).T                 # B[b, y]
    Hb = []
    Gh = np.zeros((N, 1 << n))
    for b in range(N):
        Wb = fwht_int(B[b])
        Hb.append(entropy_from_W(Wb, n))
        Gh[b] = Wb / float(1 << n)
    avgH = float(np.mean(Hb))
    cost = HF - avgH
    # I(X;Y) = a - sum_T R_T H(r_T)
    MI = 0.0
    for T in range(1 << n):
        if R[T] <= 0:
            continue
        r = Gh[:, T] ** 2 / (N * R[T])
        r = r[r > 0]
        MI += R[T] * (a - float(-np.sum(r * np.log2(r))))
    pcS = popcounts(a)
    Isel = float(np.sum(P2 * pcS[None, :]))
    infl = []
    idx = np.arange(N)
    for i in range(a):
        infl.append(float(np.sum(P2[:, ((idx >> i) & 1) == 1])))
    infl = np.array(infl)
    sh = float(np.sum(h2(infl)))
    return dict(HF=HF, cost=cost, HxGy=HSx_given_Sy, MI=MI, Isel=Isel, sumh=sh,
                id_err=abs(cost - (HSx_given_Sy + MI)))


def check(res, tol=1e-9):
    bad = []
    if res['id_err'] > 1e-8:
        bad.append('id')
    if res['cost'] > 2 * res['HxGy'] + tol:
        bad.append('U')
    if res['MI'] > (2 / LN2) * res['Isel'] + tol:
        bad.append('L')
    if res['cost'] > 2 * res['sumh'] + tol:
        bad.append('B1')
    if res['cost'] > res['sumh'] + (2 / LN2) * res['Isel'] + tol:
        bad.append('B2')
    return bad


def exhaustive4():
    counts = {}
    worst = {}
    for code in range(1 << 16):
        F = np.array([1 - 2 * ((code >> i) & 1) for i in range(16)], dtype=np.int64)
        for a in (1, 2, 3):
            res = analyse(F, a, 4 - a)
            bad = check(res)
            for b in bad:
                counts[(a, b)] = counts.get((a, b), 0) + 1
            # track tightness of B2 relative to Isel
            if res['Isel'] > 0:
                ratio = (res['cost']) / (res['sumh'] + (2 / LN2) * res['Isel'])
                key = ('B2ratio', a)
                if ratio > worst.get(key, (0,))[0]:
                    worst[key] = (ratio, code)
                ratio1 = res['cost'] / (2 * res['sumh']) if res['sumh'] > 0 else 0
                key = ('B1ratio', a)
                if ratio1 > worst.get(key, (0,))[0]:
                    worst[key] = (ratio1, code)
    return counts, worst


def randomized(trials, a, n, seed=1, bias=None):
    rng = np.random.default_rng(seed)
    counts = {}
    for _ in range(trials):
        if bias is None:
            F = rng.choice([-1, 1], size=1 << (a + n)).astype(np.int64)
        else:
            # low-energy: start from one random branch, perturb a few points per branch
            base = rng.choice([-1, 1], size=1 << n)
            B = np.tile(base, (1 << a, 1))
            flips = rng.random(B.shape) < bias
            B = np.where(flips, -B, B)
            F = B.T.reshape(-1).astype(np.int64)
        res = analyse(F, a, n)
        for b in check(res):
            counts[b] = counts.get(b, 0) + 1
    return counts


if __name__ == '__main__':
    c, w = exhaustive4()
    print('exhaustive n=4 violations:', c)
    print('worst ratios:', w)
    for (a, n, bias) in [(3, 4, None), (4, 4, 0.02), (4, 5, 0.01), (5, 4, 0.05), (2, 6, 0.001)]:
        print(a, n, bias, randomized(200, a, n, seed=a * 100 + n, bias=bias))
