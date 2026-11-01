# At every partition with lam_1 >= l+2 and n <= N where rule R7 fails, does SOME single-box
# move (remove any corner, add any outer corner) strictly increase the dimension?
import sys
from test_claim_c import partitions, hookprod
def single_moves(lam):
    lam = list(lam) + [0]
    for i in range(len(lam) - 1):
        if lam[i] > lam[i + 1]:
            for k in range(len(lam)):
                if k != i and (k == 0 or lam[k - 1] > lam[k]):
                    mu = lam[:]; mu[i] -= 1; mu[k] += 1
                    mu = tuple(x for x in mu if x > 0)
                    if list(mu) == sorted(mu, reverse=True): yield mu
N = int(sys.argv[1]); r7fail = 0; bfail = []
for n in range(3, N + 1):
    for lam in partitions(n):
        l = len(lam)
        if lam[0] < l + 2: continue
        P0 = hookprod(lam)
        ok7 = any(hookprod(tuple(list(lam[:i]) + [lam[i]-1] + list(lam[i+1:]) + [1])) < P0
                  for i in range(l) if (i == l-1 or lam[i] > lam[i+1]) and lam[i] > 1)
        if ok7: continue
        r7fail += 1
        if not any(hookprod(mu) < P0 for mu in single_moves(lam)):
            bfail.append((n, lam))
print("N", N, "R7 failures", r7fail, "of which NO single-box move helps:", len(bfail), bfail[:6])
