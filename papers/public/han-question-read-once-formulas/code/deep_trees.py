"""Closed form Q = 2L - 1 - 4 sum_{1<=l<L} p_l - 2 p_L + |1 - 2 p_L| on deep read-once NOR trees, in floats
(the exact fractions grow without bound in size). Fan-in s_l is the least s with (1 - p_{l-1})^s <= 1/4."""
import math
for L in (1, 2, 5, 10, 20, 40, 80):
    p, ps, fans = 0.5, [], []
    for _ in range(L):
        s = 1
        while (1 - p) ** s > 0.25:
            s += 1
        fans.append(s)
        p = (1 - p) ** s
        ps.append(p)
    pL = ps[-1]
    Q = 2 * L - 1 - 4 * sum(ps[:-1]) - 2 * pL + abs(1 - 2 * pL)
    logn = sum(math.log2(s) for s in fans)
    print("L=%2d fan-ins %s max %d log2 n=%.1f Q=%.4f Q/L=%.3f Q/log2n=%.3f" % (L, fans[:6], max(fans), logn, Q, Q / L, Q / logn))
