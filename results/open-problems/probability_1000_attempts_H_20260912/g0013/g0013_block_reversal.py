"""G0013: is every non-extremal permutation strictly improvable by a block reversal (reverse the values in
positions i..j, a 2-opt move) or by a transposition?  Also by a block reversal alone?"""
import itertools, sys, time
from g0013_exact_assignment import T_of

def main(n):
    t0 = time.time()
    perms = list(itertools.permutations(range(n)))
    T = {s: T_of(n, s) for s in perms}
    ident = tuple(range(n)); rev = tuple(range(n-1, -1, -1))
    okB = okBT = 0; badB = []; badBT = []
    for s in perms:
        if s in (ident, rev): continue
        v = T[s]; bestB = -1; bestT = -1
        for i in range(n):
            for j in range(i+1, n):
                t = list(s); t[i:j+1] = t[i:j+1][::-1]; bestB = max(bestB, T[tuple(t)])
                t = list(s); t[i], t[j] = t[j], t[i]; bestT = max(bestT, T[tuple(t)])
        if bestB > v: okB += 1
        else: badB.append((s, v, bestB))
        if max(bestB, bestT) > v: okBT += 1
        else: badBT.append((s, v))
    tot = len(perms) - 2
    print(f"n={n}: block reversal improves {okB}/{tot}; failures {badB[:6]}")
    print(f"      block reversal OR transposition improves {okBT}/{tot}; failures {badBT[:6]}  ({time.time()-t0:.0f}s)", flush=True)

if __name__ == "__main__":
    try:
        import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    except Exception: pass
    for n in [int(a) for a in sys.argv[1:]] or [5, 6, 7]:
        main(n)
