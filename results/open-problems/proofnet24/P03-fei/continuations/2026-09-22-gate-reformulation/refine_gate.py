"""Local refinement of the worst GENUINE gate found by the grid sweep, and a test of whether that worst point is
interior or is a degenerating configuration that reduces the gate to a smaller one.

The grid comparison says genuine k-input gates ask for a slightly SMALLER margin than the two-input AND. Two ways
that could be an artifact: the grid could miss an interior bad point, and the grid minimum could sit at a corner
where one input's bias is 0 or 1, so that the "genuine" gate is really a two-input gate in disguise. This
refines each candidate by coordinate descent in log2(1/p) and reports the influence each input still carries.
usage: refine_gate.py <k> <npz> <tt> <p1> ... <pk>"""
import sys, numpy as np, gam
from bigates import spec

def stat(vals, ps, Gm):
    k = len(ps); n = 1 << k
    C = spec(vals, np.asarray(ps, float)); pS = C * C
    Ht = -float((pS * np.log2(np.maximum(pS, 1e-300))).sum())
    SEL = np.array([[(S >> i) & 1 for i in range(k)] for S in range(n)], float)
    It = pS @ SEL
    p_out = float(np.clip((1 - C[0]) * 0.5, 0, 1))
    pa = np.asarray(ps, float); V = 4 * pa * (1 - pa)
    base = (Gm(pa) + gam.h2(V)) / V
    D = float(It @ base) - Ht - float(Gm(np.array([p_out]))[0])
    den = float(It.sum()) / 4.0 - p_out * (1 - p_out)
    return D, den, It, p_out

def refine(vals, ps, Gm, rounds=400):
    k = len(ps); ps = list(ps); 
    def need(q):
        D, den, It, po = stat(vals, q, Gm)
        return (-D / den) if den > 1e-12 else -1e9
    cur = need(ps); step = 0.5
    while step > 1e-10:
        moved = False
        for i in range(k):
            for s in (step, -step):
                q = list(ps); q[i] = min(max(q[i] * (2.0 ** -s), 1e-300), 1 - 1e-16)
                v = need(q)
                if v > cur:
                    cur, ps, moved = v, q, True
                q = list(ps); q[i] = min(max(1 - (1 - q[i]) * (2.0 ** -s), 1e-300), 1 - 1e-16)
                v = need(q)
                if v > cur:
                    cur, ps, moved = v, q, True
        if not moved:
            step *= 0.5
    return cur, ps

if __name__ == "__main__":
    k = int(sys.argv[1]); npz = sys.argv[2]; tt = int(sys.argv[3])
    ps = [float(x) for x in sys.argv[4:4 + k]]
    Gm = gam.Gam(npz, 0.0)
    n = 1 << k
    vals = 1.0 - 2.0 * ((tt >> np.arange(n)) & 1).astype(float)
    D, den, It, po = stat(vals, ps, Gm)
    print("start  tt=%d p=%s  need=%.7e  It=%s  p_out=%.6f" % (tt, ["%.6g" % v for v in ps], -D / den, ["%.3e" % v for v in It], po))
    c, ps2 = refine(vals, ps, Gm)
    D, den, It, po = stat(vals, ps2, Gm)
    print("refined            p=%s  need=%.7e" % (["%.8g" % v for v in ps2], c))
    print("   influence carried by each input: %s   (an input at ~0 means the gate has degenerated)" % ["%.4e" % v for v in It])
    print("   inputs with influence below 1e-9: %d of %d ; p_out=%.6f ; constant = %.7f"
          % (int((It < 1e-9).sum()), k, po, Gm.cap + max(c, 0) / 4))
