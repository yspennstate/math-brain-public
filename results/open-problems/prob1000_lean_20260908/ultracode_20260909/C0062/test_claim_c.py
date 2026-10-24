# Claim C / rule R7: for every partition lam with lam_1 >= l(lam) + 2 there is a corner c
# such that dim(lam - c + (l+1,1)) > dim(lam).  Exact integer check for all partitions of n <= N.
import sys, math
def partitions(n, maxpart=None):
    if maxpart is None: maxpart = n
    if n == 0: yield (); return
    for k in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - k, k): yield (k,) + rest
def hookprod(lam):
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    p = 1
    for i, li in enumerate(lam):
        for j in range(li): p *= li - j + conj[j] - i - 1
    return p
if __name__ == "__main__":
    N = int(sys.argv[1]); tested = 0; fails = []; ties = 0; witness_top = 0
    for n in range(3, N + 1):
        for lam in partitions(n):
            l = len(lam)
            if lam[0] < l + 2: continue
            tested += 1
            P0 = hookprod(lam)              # dim = n!/P, so larger dim <=> smaller hook product
            best = None
            for i in range(l):
                if i == l - 1 or lam[i] > lam[i + 1]:
                    if lam[i] == 1: continue   # c=(l,1) -> no-op
                    mu = list(lam); mu[i] -= 1; mu.append(1)
                    P1 = hookprod(tuple(mu))
                    if P1 < P0:
                        best = i; break
            if best is None: fails.append((n, lam))
            elif best == 0: witness_top += 1
    print("N", N, "tested", tested, "failures", len(fails), fails[:5], "witness is top-right corner in", witness_top)
