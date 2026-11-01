# Exhaustive search for the partition(s) of n with the maximal number of standard
# Young tableaux (= maximal-dimension irreducible representation of S_n).
# Numba loop over every partition of n with lambda_1 >= length(lambda) (the other
# half is the conjugate image, and dim is conjugation invariant); log-dimension by
# the hook-length formula; keeps the top K partitions by log-dimension.  Then an
# exact integer re-check in Python of the top candidates and of the gap.
import sys, time, json, math
import numpy as np
from numba import njit
from fractions import Fraction

@njit(cache=True)
def search(n, K):
    # ascending-composition partition generator (Kelleher), parts in a[0..k]
    logt = np.zeros(n + 2)
    for i in range(1, n + 2):
        logt[i] = math.log(i)
    a = np.zeros(n + 1, dtype=np.int64)
    lam = np.zeros(n + 1, dtype=np.int64)
    conj = np.zeros(n + 2, dtype=np.int64)
    bestv = np.full(K, -1e300)
    bestp = np.zeros((K, n + 1), dtype=np.int64)
    bestl = np.zeros(K, dtype=np.int64)
    count = 0
    k = 1
    a[0] = 0
    a[1] = n
    while k != 0:
        x = a[k - 1] + 1
        y = a[k] - 1
        k -= 1
        while x <= y:
            a[k] = x
            y -= x
            k += 1
        a[k] = x + y
        # partition = a[0..k] ascending; rows descending = reversed
        L = k + 1
        lam1 = a[k]
        if lam1 < L:
            continue  # its conjugate is enumerated instead
        count += 1
        for i in range(L):
            lam[i] = a[k - i]
        # conjugate
        for j in range(lam1 + 1):
            conj[j] = 0
        for i in range(L):
            for j in range(lam[i]):
                conj[j] += 1
        s = 0.0
        for i in range(L):
            li = lam[i]
            for j in range(li):
                s += logt[li - j + conj[j] - i - 1]
        v = -s  # log(dim) - log(n!)
        if v > bestv[K - 1]:
            pos = K - 1
            while pos > 0 and bestv[pos - 1] < v:
                bestv[pos] = bestv[pos - 1]
                bestl[pos] = bestl[pos - 1]
                for t in range(n + 1):
                    bestp[pos, t] = bestp[pos - 1, t]
                pos -= 1
            bestv[pos] = v
            bestl[pos] = L
            for t in range(n + 1):
                bestp[pos, t] = 0
            for t in range(L):
                bestp[pos, t] = lam[t]
    return bestv, bestp, bestl, count

def hooks_dim(lam):
    n = sum(lam)
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    p = 1
    for i, li in enumerate(lam):
        for j in range(li):
            p *= li - j + conj[j] - i - 1
    return math.factorial(n) // p, p

def conjugate(lam):
    return tuple(sum(1 for r in lam if r > j) for j in range(lam[0]))

if __name__ == "__main__":
    n0, n1 = int(sys.argv[1]), int(sys.argv[2])
    K = 6
    out = open("maxdim_results.jsonl", "a", encoding="utf-8")
    for n in range(n0, n1 + 1):
        t0 = time.time()
        bestv, bestp, bestl, count = search(n, K)
        cands = []
        for r in range(K):
            lam = tuple(int(x) for x in bestp[r, :bestl[r]])
            if sum(lam) != n: continue
            d, _ = hooks_dim(lam)
            cands.append((d, lam))
        cands.sort(reverse=True)
        dmax = cands[0][0]
        maxers = [lam for d, lam in cands if d == dmax]
        # distinct up to conjugation
        classes = []
        for lam in maxers:
            if lam not in classes and conjugate(lam) not in classes:
                classes.append(lam)
        second = [d for d, lam in cands if d < dmax]
        gap = math.log(dmax) - math.log(second[0]) if second else None
        # sanity: the top-K window must contain the max class and at least one strictly smaller value
        rec = dict(n=n, count=int(count), dmax=str(dmax), maximisers=maxers,
                   classes_up_to_conjugation=len(classes),
                   self_conjugate=(conjugate(maxers[0]) == maxers[0]),
                   log_gap_to_next=gap, second=(str(second[0]) if second else None),
                   second_shape=[lam for d, lam in cands if d < dmax][:1],
                   secs=round(time.time() - t0, 2))
        print(json.dumps(rec), flush=True)
        out.write(json.dumps(rec) + "\n"); out.flush()
