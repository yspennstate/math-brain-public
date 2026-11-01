import sys
from enum_maxdim import hooks_dim
from test_width_lemma import partitions
N = int(sys.argv[1])
def corners(lam):
    return [i for i in range(len(lam)) if i == len(lam) - 1 or lam[i] > lam[i + 1]]
def outer(lam):
    return [k for k in range(len(lam) + 1) if k == 0 or lam[k - 1] > (lam[k] if k < len(lam) else 0)]
f7 = []; f8 = []; f9 = []; tested = 0
for n in range(3, N + 1):
    for lam in partitions(n):
        l = len(lam)
        if lam[0] < l + 2: continue
        tested += 1
        d0, _ = hooks_dim(lam)
        r = sum(1 for x in lam if x == lam[0]) - 1   # index of top-right corner row
        # R7: some corner c -> new bottom row
        ok7 = False
        for i in corners(lam):
            mu = list(lam); mu[i] -= 1; mu.append(1); mu = tuple(x for x in mu if x > 0)
            if hooks_dim(mu)[0] > d0: ok7 = True; break
        # R8: top-right corner -> some outer corner
        ok8 = False; best8 = None
        for k in outer(lam):
            if k == r: continue
            mu = list(lam) + [0]; mu[r] -= 1; mu[k] += 1; mu = tuple(x for x in mu if x > 0)
            if list(mu) != sorted(mu, reverse=True): continue
            d1 = hooks_dim(mu)[0]
            if d1 > d0: ok8 = True; break
        # R9: bottom corner of the diagram (last row) -> ... no; instead: the LOWEST corner c=(l, lam_l) moved to (l+1,1)? that's a no-op shape change only if lam_l>1
        if not ok7: f7.append((n, lam))
        if not ok8: f8.append((n, lam))
print("tested", tested, "R7 fails", len(f7), "R8 fails", len(f8))
print(" R7 fail examples", f7[:8]); print(" R8 fail examples", f8[:8])
