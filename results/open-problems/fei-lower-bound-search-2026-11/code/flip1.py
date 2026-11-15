# Single-point flips of a seed gate: for one point x from each orbit of the structure's group, flip f(x) alone and
# score the result from the full transform (rank-one update), with no symmetry kept.  The best few are scored again
# from the explicit flipped truth table (sym_search.explicit), and the whole-class flip of the same class is printed
# beside it.   usage: python3 flip1.py CODEDIR WTABLE STRUCT SEEDNAME OUT
import sys
import time
import numpy as np
sys.path.insert(0, sys.argv[1])
import sym_search as S

tab = np.loadtxt(sys.argv[2]); wt, ww = tab[:, 0], tab[:, -1]


def wfun(p):
    p = min(max(p, 1e-15), 1 - 1e-15)
    return float(np.interp(np.log2(p / (1 - p)), wt, ww))


c = wfun(0.5)
name, seedname, out = sys.argv[3], sys.argv[4], sys.argv[5]
fo = open(out, "a")


def say(s):
    print(s, flush=True); fo.write(s + "\n"); fo.flush()


t0 = time.time()
m, gens, edges = S.struct(name)
N = 1 << m
f = dict(S.graph_seeds(m, edges, N))[seedname].copy()
G0, J0, pp0, sl0 = S.explicit(f, wfun, c)
reps, cls, sizes = S.orbits(m, gens)
K = len(reps)
inv = bool(np.array_equal(f, f[reps][cls]))
say("# %s seed %s m=%d classes=%d c=%.12f invariant %s" % (name, seedname, m, K, c, inv))
say("seed slack %+.12f G %.12f J %.12f p' %.12f" % (sl0, G0, J0, pp0))
i0 = int(np.argmin(np.abs(wt)))
say("W table near even odds (log-odds, W): " + " ".join("(%.6f, %.9f)" % (wt[i], ww[i]) for i in range(max(0, i0 - 3), min(len(wt), i0 + 4))))
d = 2.0 / N
say("W change for one point: p' up %+.3e, p' down %+.3e" % (wfun(pp0 + d / 2) - wfun(pp0), wfun(pp0 - d / 2) - wfun(pp0)))

a = f.reshape(1, N).copy(); S.fwht_rows(a); a = a[0] / N
pc = S.popcounts(N)
idx = np.arange(N, dtype=np.int64)
base = G0 - c * J0
res = np.empty((K, 3))
for k in range(K):
    x = int(reps[k])
    chi = 1.0 - 2.0 * (pc[idx & x] & 1)
    a2 = a - (2.0 * f[x] / N) * chi
    mean = a2[0]
    w = a2 * a2; w[0] = 0.0
    V = w.sum()
    nz = w > 0
    pi = w[nz] / V
    G = float(-(pi * np.log2(pi)).sum()); J = float((pc * w).sum() / V); pp = 0.5 * (1 - mean)
    res[k] = (G - c * J + wfun(pp) - sl0, G - c * J - base, wfun(pp) - wfun(pp0))
    if k % 500 == 0:
        print("progress", k, K, "%.0f s" % (time.time() - t0), flush=True)
dl = res[:, 0]
order = np.argsort(-dl)
say("single-point flips: %d classes, above 0: %d, best %+.3e, worst %+.3e, median %+.3e; without the W term: above 0 %d, best %+.3e"
    % (K, int((dl > 0).sum()), dl.max(), dl.min(), float(np.median(dl)), int((res[:, 1] > 0).sum()), res[:, 1].max()))
E = m // 2
for k in order[:6]:
    x = int(reps[k])
    g = f.copy(); g[x] = -g[x]
    G2, J2, pp2, sl2 = S.explicit(g, wfun, c)
    h = f.copy(); h[cls == k] *= -1.0
    G3, J3, pp3, sl3 = S.explicit(h, wfun, c)
    say("top class %d size %d point cells %s coins %s f %+d: one point %+.4e (GJ part %+.4e, W part %+.4e) explicit %+.4e | size x one point %+.4e, whole class %+.6e"
        % (k, int(sizes[k]), format(x & ((1 << E) - 1), "0%db" % E), format(x >> E, "0%db" % E), int(f[x]), dl[k], res[k, 1], res[k, 2],
           sl2 - sl0, sizes[k] * dl[k], sl3 - sl0))
say("sum over classes of size x one-point change %+.6e; done %.0f s" % (float((sizes * dl).sum()), time.time() - t0))
np.save(out + ".npy", res)
