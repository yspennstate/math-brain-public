"""E1 on random graphs on V vertices (seed given), every edge pair, via fastN. python e1_rand.py V seed count lo hi"""
import sys, random, itertools, time, fastN
from e1_check import e1_neg
V, seed, T, lo, hi = map(int, sys.argv[1:6]); rnd = random.Random(seed)
allE = list(itertools.combinations(range(V), 2)); cnt = bad = 0; t0 = time.time()
for t in range(T):
    E = sorted(rnd.sample(allE, rnd.randint(lo, hi)))
    for (e, f), N in fastN.all_N(V, E).items():
        if not N:
            continue
        cnt += 1
        b = e1_neg(N)
        if b:
            bad += 1
            if bad <= 5:
                print('FAIL', E, e, f, b[:3], flush=True)
print('%d random graphs on %d vertices (seed %d, %d..%d edges): pairs with N != 0: %d, E1 failures %d, %ds'
      % (T, V, seed, lo, hi, cnt, bad, time.time() - t0), flush=True)
