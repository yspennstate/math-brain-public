# E0062: Volterra QSO on S^3 whose sign tournament is a 4-cycle with two ties
#   x1' = x1(1 + a x2 - d x4), x2' = x2(1 - a x1 + b x3),
#   x3' = x3(1 - b x2 + c x4), x4' = x4(1 + d x1 - c x3).
# Iterated in log coordinates so that astronomically small coordinates do not
# underflow to an exact zero (an exact zero would put the orbit on an invariant
# face and fake convergence).
import numpy as np, math, sys, time
np.seterr(all="ignore")

def run(a, b, c, d, x0, nsteps, tag):
    A = np.array([[0, a, 0, -d], [-a, 0, b, 0], [0, -b, 0, c], [d, 0, -c, 0]], float)
    L = np.log(np.array(x0, float))
    S = np.zeros(4)            # running sum of x
    cesaro = []                # (n, mean) at n = 2^k
    visits = []                # (vertex, entry step) when max coord > 0.999 and vertex changes
    cur = -1
    nxt = 1
    t0 = time.time()
    for n in range(1, nsteps + 1):
        x = np.exp(L)
        S += x
        L = L + np.log1p(A @ x)
        L -= math.log(np.exp(L).sum())   # renormalise (drift is 1e-16 per step)
        m = int(np.argmax(L))
        if L[m] > math.log(0.999) and m != cur:
            cur = m; visits.append((m + 1, n))
        if n == nxt:
            cesaro.append((n, (S / n).copy())); nxt *= 2
    print(f"--- {tag}: a,b,c,d = {a},{b},{c},{d}; x0 = {x0}; {nsteps} steps, {time.time()-t0:.1f}s")
    print("final log x:", np.round(L, 3))
    for n, mean in cesaro[-8:]:
        print(f"  n={n:>9d}  Cesaro mean = {np.round(mean, 4)}")
    print("  visits (vertex, entry step), last 12:", visits[-12:])
    if len(visits) > 3:
        durs = [visits[i + 1][1] - visits[i][1] for i in range(len(visits) - 1)]
        print("  visit durations, last 12:", durs[-12:])
        # growth ratio of durations over one full cycle (4 visits)
        if len(durs) > 8:
            print("  duration ratio per full cycle (last 4):", [round(durs[i] / durs[i - 4], 3) for i in range(len(durs) - 4, len(durs))])
    return cesaro, visits

def predicted_ratios(a, b, c, d):
    lp = lambda u: math.log1p(u); lm = lambda u: -math.log1p(-u)
    r1 = lm(a) * lm(c) / (lp(d) * lp(b))      # growth of L4 per cycle (a' = -log(1-a) is the shrink rate of x2 at e1)
    r2 = lm(b) * lm(d) / (lp(a) * lp(c))      # growth of L3 per cycle
    return r1, r2

if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 2_000_000
    cases = [
        (0.5, 0.5, 0.5, 0.5, [0.3, 0.2, 0.25, 0.25], "symmetric"),
        (0.5, 0.4, 0.5, 0.4, [0.3, 0.2, 0.25, 0.25], "ac>bd, both ratios>1"),
        (0.9, 0.1, 0.9, 0.1, [0.3, 0.2, 0.25, 0.25], "ac>bd, ratio2<1"),
        (0.9, 0.1, 0.9, 0.1, [0.01, 0.6, 0.01, 0.38], "ratio2<1, start near e2"),
    ]
    for a, b, c, d, x0, tag in cases:
        print("predicted per-cycle growth ratios (L4, L3):", [round(r, 3) for r in predicted_ratios(a, b, c, d)])
        run(a, b, c, d, x0, N, tag)
