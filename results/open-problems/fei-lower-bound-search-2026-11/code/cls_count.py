# class counts of candidate structures, two ways: the script's own orbit pass and Burnside over the closure of the
# generators (closure listed here, apart from the orbit code).  usage: python3 cls_count.py CODEDIR name ...
import sys
import time
sys.path.insert(0, sys.argv[1])
import sym_search as S


def cycles(p):
    seen = [False] * len(p); c = 0
    for i in range(len(p)):
        if not seen[i]:
            c += 1; j = i
            while not seen[j]:
                seen[j] = True; j = p[j]
    return c


for nm in sys.argv[2:]:
    t = time.time()
    try:
        m, gens, _ = S.struct(nm)
    except SystemExit as e:
        print(nm, "REFUSED", e, flush=True); continue
    gens = [tuple(g) for g in gens]
    idt = tuple(range(m)); seen = {idt}; stack = [idt]
    while stack and len(seen) < 200000:
        x = stack.pop()
        for g in gens:
            y = tuple(g[x[i]] for i in range(m))
            if y not in seen:
                seen.add(y); stack.append(y)
    burn = sum(1 << cycles(p) for p in seen)
    reps, cls, sizes = S.orbits(m, gens)
    K = len(reps)
    print("%s m %d order %d classes %d burnside %d exact %s sum %s two_mats_mb %d secs %.1f" % (
        nm, m, len(seen), K, burn // len(seen), burn % len(seen) == 0 and burn // len(seen) == K,
        int(sizes.sum()) == 1 << m, 2 * K * K * 8 // 1048576, time.time() - t), flush=True)
