# Brute force over ALL perfect matchings of the n-cycle (n even), n <= 14:
# which matching gives the fastest simple random walk on the resulting cubic graph?
# Criteria: SRW spectral gap 1 - lambda_2(A)/3 (lambda_2 = second largest adjacency eigenvalue),
# absolute spectral gap 1 - max(|lambda_2|,|lambda_n|)/3, and TV mixing time of the lazy walk.
import numpy as np, itertools, time, sys
def matchings(vs):
    if not vs: yield []; return
    a = vs[0]
    for i in range(1, len(vs)):
        b = vs[i]
        rest = vs[1:i] + vs[i+1:]
        for m in matchings(rest): yield [(a, b)] + m
def cycle_adj(n):
    A = np.zeros((n, n))
    for j in range(n): A[j, (j+1) % n] = A[(j+1) % n, j] = 1
    return A
def tmix_lazy(A, eps=0.25):
    n = len(A); P = A/3.0; Pl = 0.5*(np.eye(n) + P)
    dist = np.eye(n)[0]; t = 0
    while True:
        tv = 0.5*np.abs(dist - 1/n).sum()
        if tv <= eps: return t
        dist = dist @ Pl; t += 1
for n in [6, 8, 10, 12, 14]:
    A0 = cycle_adj(n); t0 = time.time()
    best = {}; cnt = 0; seen = set()
    stats = []
    for M in matchings(list(range(n))):
        if any(A0[a, b] for a, b in M): continue   # must add NEW edges (simple graph)
        A = A0.copy()
        for a, b in M: A[a, b] = A[b, a] = 1
        ev = np.sort(np.linalg.eigvalsh(A))[::-1]
        gap = 1 - ev[1]/3; agap = 1 - max(ev[1], -ev[-1])/3
        stats.append((gap, agap)); cnt += 1
        key = tuple(np.round(ev, 8))
        if key not in seen:
            seen.add(key); best[key] = (gap, agap, M, ev)
    stats = np.array(stats)
    print(f"n={n}: {cnt} matchings with no cycle edge, {len(seen)} distinct spectra, {time.time()-t0:.1f}s")
    print(f"   SRW gap: max {stats[:,0].max():.6f} mean {stats[:,0].mean():.6f} min {stats[:,0].min():.6f}; abs gap max {stats[:,1].max():.6f} mean {stats[:,1].mean():.6f}")
    top = sorted(best.values(), key=lambda r: -r[0])[:3]
    for gap, agap, M, ev in top:
        A = A0.copy()
        for a, b in M: A[a, b] = A[b, a] = 1
        print(f"   gap {gap:.6f} absgap {agap:.6f} lazy t_mix(1/4)={tmix_lazy(A)} matching {M} adjacency spectrum {np.round(ev,4)}")
    topa = sorted(best.values(), key=lambda r: -r[1])[:1]
    for gap, agap, M, ev in topa:
        print(f"   best ABS gap {agap:.6f} (gap {gap:.6f}) matching {M} spectrum {np.round(ev,4)}")
