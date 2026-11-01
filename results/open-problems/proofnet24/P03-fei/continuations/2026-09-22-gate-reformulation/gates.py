"""Does the read-once AND/OR potential survive gates of larger fan-in?

For a k-input gate G and input biases p in (0,1)^k the composition lemma makes the induction close iff

   D_G(p) = sum_i It_i(G;p) * (Gamma(p_i) + h(V_i))/V_i  -  Ht_G(p)  -  Gamma(p_out)   >=  0 .

Existence of a symmetric Gamma >= 0 with Gamma(1/2) <= C satisfying this for EVERY Boolean gate of EVERY arity is
equivalent to FEI with constant C (an arbitrary f is a single gate on n fresh variables).  Verifying it up to arity
k proves FEI for every read-once formula over gates of fan-in <= k.  Arity 2 is the AND/OR constraint itself and is
the positive control: its minimum must reproduce the certificate's own margin.

Negating an input maps p_i -> 1-p_i and G to another truth table; negating the output maps p_out -> 1-p_out;
permuting inputs permutes p.  Gamma, h(V) and V are symmetric, so enumerating ALL truth tables lets us restrict the
bias grid to p_1 <= ... <= p_k <= 1/2 with no loss.
usage: gates.py <k> <npz> <c> <tag> [nx] [procs]"""
import sys, os, math, time, json
import numpy as np
from multiprocessing import Pool
import gam
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass

def transform(ps):
    """Kronecker biased-Walsh matrix A[S, x]; input 0 is the least significant bit of both indices."""
    A = np.ones((1, 1))
    for p in ps:
        s2 = math.sqrt(p * (1 - p))                 # sigma/2
        M = np.array([[1 - p, p], [s2, -s2]])
        A = np.kron(M, A)
    return A

_G = {}
def _init(npz, c, k, TT):
    _G["gam"] = gam.Gam(npz, c); _G["k"] = k; _G["TT"] = TT

def block(args):
    """one bias vector: min over all truth tables of D_G, and the argmin"""
    ps = args
    Gm, k, TT = _G["gam"], _G["k"], _G["TT"]
    A = transform(ps)
    C = TT @ A.T                                    # (ntt, 2^k)
    pS = C * C
    with np.errstate(divide="ignore", invalid="ignore"):
        Ht = -np.where(pS > 1e-300, pS * np.log2(np.maximum(pS, 1e-300)), 0.0).sum(axis=1)
    p_out = np.clip((1.0 - C[:, 0]) * 0.5, 0.0, 1.0)
    pa = np.asarray(ps, float); V = 4 * pa * (1 - pa)
    base = (Gm(pa) + gam.h2(V)) / V                 # (k,)
    It = np.stack([pS[:, [s for s in range(1 << k) if (s >> i) & 1]].sum(axis=1) for i in range(k)], axis=1)
    D = It @ base - Ht - Gm(p_out)
    j = int(np.argmin(D))
    return float(D[j]), j, tuple(float(v) for v in ps)

def grid_xs(nx):
    """x = log2(1/p) node set: dense near 1 (p near 1/2), geometric out to p = 2^-30"""
    a = np.linspace(1.0, 4.0, max(2, nx - 8))
    b = np.array([4.5, 5.0, 6.0, 7.0, 9.0, 12.0, 18.0, 30.0])
    return np.unique(np.concatenate([a, b]))

def combos(vals, k):
    """all non-decreasing k-tuples from vals (input-permutation quotient)"""
    out = []
    def rec(start, cur):
        if len(cur) == k:
            out.append(tuple(cur)); return
        for i in range(start, len(vals)):
            cur.append(vals[i]); rec(i, cur); cur.pop()
    rec(0, [])
    return out

if __name__ == "__main__":
    k = int(sys.argv[1]); npz = sys.argv[2]; c = float(sys.argv[3]); tag = sys.argv[4]
    nx = int(sys.argv[5]) if len(sys.argv) > 5 else 24
    procs = int(sys.argv[6]) if len(sys.argv) > 6 else 6
    n = 1 << k; ntt = 1 << n
    idx = np.arange(ntt, dtype=np.uint64)[:, None]
    TT = 1.0 - 2.0 * ((idx >> np.arange(n, dtype=np.uint64)[None, :]) & 1).astype(np.float64)  # bit=1 -> value -1 (true)
    xs = grid_xs(nx); ps_vals = list(2.0 ** -xs)
    B = combos(ps_vals, k)
    print("arity %d: %d truth tables, %d bias vectors (x nodes %d), c=%.5g, Gamma(1/2)=%.7f"
          % (k, ntt, len(B), len(xs), c, gam.Gam(npz, c).cap), flush=True)
    t0 = time.time(); res = []
    with Pool(procs, initializer=_init, initargs=(npz, c, k, TT)) as pool:
        for i, r in enumerate(pool.imap_unordered(block, B, chunksize=8)):
            res.append(r)
            if (i + 1) % 2000 == 0:
                print("  %d/%d  %.0f s  running min %.6f" % (i + 1, len(B), time.time() - t0, min(x[0] for x in res)), flush=True)
    res.sort()
    print("min D over the grid: %.8f   (%.0f s)" % (res[0][0], time.time() - t0))
    print("twenty worst (D, truth table, biases):")
    for D, tt, ps in res[:20]:
        print("   %+.7f  tt=%-12d p=%s" % (D, tt, ["%.5f" % v for v in ps]))
    json.dump([[D, tt, list(ps)] for D, tt, ps in res[:4000]], open("gates_%s.json" % tag, "w"))
    print("wrote gates_%s.json" % tag)
