"""The windowed unnormalized test (P'):

  for t in [0, T0]:  G(t) <= a e^{2t} M(t) + b Kr(t) + c N(t),

G(t) = sum_S |S| e^{-2t|S|} w L_S, M = sum |S|^2 e^{-2t|S|} w, N = sum |S| e^{-2t|S|} w,
Kr = sum_S e^{-2t|S|} w sum_{i in S} log(1/Inf_i).  If (P') holds then
  (1 - e^{-2 T0}) (H - W0 log(1/W0)) <= int_0^{T0} 2 G <= a (2 I + 2 T0 W^1) + 2 b I + c,
so FEI follows.  For fixed b, c this script reports the least a that works for each function:
  a*(f) = sup_{t in [0,T0]} (G - b Kr - c N) / (e^{2t} M).
Also: the rest of the family table on a reduced t-grid (n up to 20).
"""
import math
import numpy as np
from fei_core import *
from exhaust_n4 import hadamard

lowprio()


def astar_spec(sp, b, c, T0, nt=41):
    inf = sp.influences()
    li = np.where(inf > 0, -np.log(np.maximum(inf, 1e-300)), 0.0)
    s = np.zeros(sp.ws.size)
    for i in range(sp.n):
        s += li[i] * ((sp.idx >> i) & 1)
    best = -1e300; tb = None
    for t in np.linspace(0, T0, nt):
        u = sp.ws * np.exp(-2 * t * sp.ks)
        G = float((u * sp.ks * sp.L).sum()); M = float((u * sp.ks ** 2).sum())
        Nn = float((u * sp.ks).sum()); Kr = float((u * s).sum())
        if M <= 0:
            continue
        v = (G - b * Kr - c * Nn) / (math.exp(2 * t) * M)
        if v > best:
            best, tb = v, t
    return best, tb


def exhaustive(n, b, c, T0, nt=41):
    N = 1 << n
    nf = 1 << N
    codes = np.arange(nf, dtype=np.int64)
    F = np.empty((nf, N))
    for x in range(N):
        F[:, x] = np.where((codes >> x) & 1, -1.0, 1.0)
    A = F @ hadamard(n) / N
    W = A * A; W[W < 1e-15] = 0
    k = popcounts(n).astype(float)
    L = np.where(W > 0, -np.log(np.where(W > 0, W, 1)), 0)
    idx = np.arange(N)
    inf = np.stack([(W[:, ((idx >> i) & 1) == 1]).sum(1) for i in range(n)], 1)
    linf = np.where(inf > 0, -np.log(np.maximum(inf, 1e-300)), 0.0)
    member = np.stack([((idx >> i) & 1) for i in range(n)], 0).astype(float)
    s = linf @ member
    nonconst = (W * k).sum(1) > 1e-12
    best = np.full(nf, -1e300)
    for t in np.linspace(0, T0, nt):
        u = W * np.exp(-2 * t * k)
        G = (u * k * L).sum(1); M = (u * k * k).sum(1); Nn = (u * k).sum(1); Kr = (u * s).sum(1)
        v = np.where(nonconst & (M > 0), (G - b * Kr - c * Nn) / (math.exp(2 * t) * np.where(M > 0, M, 1)), -1e300)
        best = np.maximum(best, v)
    return best.max(), int(best.argmax())


def main():
    lines = []
    def P(*a):
        s = ' '.join(str(x) for x in a); lines.append(s); print(s, flush=True)
    for (b, c, T0) in [(2.0, 1.0, 1.0), (0.0, 0.0, 1.0), (2.0, 1.0, 2.0)]:
        P("## (P') least a, with b=%g c=%g T0=%g" % (b, c, T0))
        for n in [2, 3, 4]:
            P("exhaustive n=%d: sup a* = %.5f at f=%d" % ((n,) + exhaustive(n, b, c, T0)))
        fams = []
        for nn in [8, 12, 16]:
            base = parity(nn, [0, 1])
            fams.append(("x0x1 edge 2-flip n=%d" % nn, flip(base, [0, 1])))
        for m in [3, 5, 7]:
            fams.append(("bent IP n=%d" % (2 * m), inner_product(m)))
        for nn in [10, 14]:
            fams.append(("const 1-flip n=%d" % nn, flip(np.ones(1 << nn, dtype=np.int8), [0])))
        for (w, cc) in [(3, 5), (4, 5), (5, 4)]:
            fams.append(("tribes %dx%d" % (w, cc), tribes(w, cc)))
        for nn in [9, 13, 17, 21]:
            fams.append(("maj n=%d" % nn, majority(nn)))
        for nn in [12, 16]:
            idx = np.arange(1 << nn, dtype=np.int64)
            f = np.where((idx & 1) == 1, -1, 1).astype(np.int8) * majority(nn - 1)[idx >> 1]
            fams.append(("x0*Maj%d" % (nn - 1), f.astype(np.int8)))
        fams.append(("addressing a=3", addressing(3)))
        fams.append(("Numaro g", load_numaro()))
        for name, f in fams:
            a, tb = astar_spec(Spec.from_table(f), b, c, T0)
            P("  %-24s a*=%.5f (t=%.3f)" % (name, a, tb))
    with open('../logs/window_test.log', 'w') as fh:
        fh.write('\n'.join(lines) + '\n')


if __name__ == '__main__':
    main()
