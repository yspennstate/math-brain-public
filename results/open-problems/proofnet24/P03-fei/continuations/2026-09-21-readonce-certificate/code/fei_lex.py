"""Lexicographic (read-once chain) functions f = x1 op1 (x2 op2 (x3 ... x_n)), the family behind Hod's
FEI lower bound. For each pattern: H/I, the min-step rho0 = min_i Delta_i H / Inf_i, the total-step
sum_i Delta_i H / I, and which coordinate attains the min. Any inductive proof with a fixed step constant C
needs C >= sup H/I, so if these reach H/I near 6.28 some restriction of them has min-step >= 6.28."""
import sys, itertools
import numpy as np
sys.path.insert(0, r"~\AppData\Local\Temp\claude\<project>\07f56e82-b3da-42b4-8041-02c1a661a843\scratchpad\fei")
from fei_step_tribes import steps

def chain_tt(pattern, n):
    """pattern: string of 'A'/'O' of length n-1; bit x_i is bit i of the index; +1 = true"""
    idx = np.arange(1 << n)
    bits = [((idx >> i) & 1).astype(bool) for i in range(n)]
    val = bits[n - 1]
    for i in range(n - 2, -1, -1):
        val = (bits[i] & val) if pattern[i] == "A" else (bits[i] | val)
    return np.where(val, 1, -1)

def report(pattern, n):
    f = chain_tt(pattern, n)
    rho0, tau, ratios, H, I = steps(f, n)
    amin = int(np.nanargmin(ratios))
    return H / I, rho0, tau, amin, H, I

if __name__ == "__main__":
    print("pattern (period, n): H/I  min-step  total-step  argmin-coordinate")
    best = {}
    for per in (1, 2, 3, 4):
        for base in itertools.product("AO", repeat=per):
            base = "".join(base)
            if per > 1 and any(base == base[:d] * (per // d) for d in range(1, per) if per % d == 0):
                continue  # a shorter period
            for n in (8, 12, 14, 16):
                pat = (base * n)[: n - 1]
                hi, rho0, tau, amin, H, I = report(pat, n)
                key = base
                if hi > best.get(key, (0,))[0]:
                    best[key] = (hi, rho0, tau, n)
                if n in (12, 16):
                    print("  %-4s n=%2d  H/I %.4f  min-step %.4f  total-step %.4f  argmin i=%d  (H %.3f I %.3f)" % (base, n, hi, rho0, tau, amin, H, I))
    print("best H/I per pattern (H/I, min-step, total-step, n):")
    for k, v in sorted(best.items(), key=lambda kv: -kv[1][0]):
        print("  %-4s %.4f %.4f %.4f n=%d" % (k, *v))
    # the alternating chain further out
    for n in (18, 20):
        for base in ("AO", "OA"):
            pat = (base * n)[: n - 1]
            hi, rho0, tau, amin, H, I = report(pat, n)
            print("  %-4s n=%2d  H/I %.4f  min-step %.4f  total-step %.4f  argmin i=%d" % (base, n, hi, rho0, tau, amin))
    # random patterns at n=14: does anything beat the periodic ones?
    rng = np.random.default_rng(1)
    top = []
    for _ in range(300):
        pat = "".join(rng.choice(list("AO"), 13))
        hi, rho0, tau, amin, H, I = report(pat, 14)
        top.append((rho0, hi, tau, pat))
    top.sort(reverse=True)
    print("random patterns n=14, top 5 by min-step (min-step, H/I, total-step, pattern):")
    for t in top[:5]:
        print("  %.4f %.4f %.4f %s" % t)
    top.sort(key=lambda t: -t[1])
    print("random patterns n=14, top 3 by H/I:")
    for t in top[:3]:
        print("  min-step %.4f H/I %.4f total-step %.4f %s" % t)
