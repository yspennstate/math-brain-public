"""NPN classes of k-input Boolean functions.

D_G depends on the gate only through its spectrum, and the three NPN moves act on the data we feed it:
permuting inputs permutes the bias vector, negating input i maps p_i -> 1-p_i, negating the output maps
p_out -> 1-p_out.  Gamma, h(V) and V are symmetric about 1/2, so D_G is constant on an NPN class provided the
bias grid is itself symmetric under p -> 1-p and closed under permutation.  So one representative per class is
enough, and for k = 4 that is 222 gates instead of 65,536."""
import numpy as np, itertools, sys

def npn_classes(k):
    n = 1 << k
    FULL = (1 << n) - 1
    perms = list(itertools.permutations(range(k)))
    # precompute, for each (perm, input-negation mask), the permutation of the 2^n truth-table bit positions
    maps = []
    for pm in perms:
        for neg in range(1 << k):
            tgt = np.empty(n, dtype=np.int64)
            for x in range(n):
                y = 0
                for i in range(k):                      # input i of the transformed gate reads input pm[i]
                    b = (x >> i) & 1
                    if (neg >> i) & 1:
                        b ^= 1
                    y |= b << pm[i]
                tgt[x] = y
            maps.append(tgt)
    canon = {}
    reps = []
    seen = bytearray(1 << n)
    for tt in range(1 << n):
        if seen[tt]:
            continue
        orbit = set()
        bits = np.array([(tt >> x) & 1 for x in range(n)], dtype=np.int64)
        for tgt in maps:
            nb = np.zeros(n, dtype=np.int64)
            nb[tgt] = bits
            v = int((nb << np.arange(n)).sum())
            orbit.add(v); orbit.add((~v) & FULL)
        m = min(orbit)
        for v in orbit:
            seen[v] = 1
            canon[v] = m
        reps.append(m)
    reps = sorted(set(reps))
    return reps, canon

if __name__ == "__main__":
    k = int(sys.argv[1])
    reps, canon = npn_classes(k)
    print("arity %d: %d NPN classes of %d truth tables" % (k, len(reps), 1 << (1 << k)))
    np.save("npn_reps_k%d.npy" % k, np.array(reps, dtype=np.int64))
