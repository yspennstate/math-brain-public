# F0068 sanity check of the mechanism behind ABHK (EJP 2022) Theorem 1.1 -> width.
# A uniformly random plane tree with given degree statistics n = (n(c)) is sampled
# exactly by the cycle lemma: shuffle the multiset of child counts, take the unique
# cyclic rotation whose Lukasiewicz path stays >= 0, then rebuild heights.
# Prediction: wid(T) grows like sqrt(|n|_2^2) = sqrt(sum c^2 n(c)), i.e. wid/sqrt(N)
# grows like sqrt(|n|_2^2 / N) and is NOT bounded when |n|_2^2 / N -> infinity.
# Kept small on purpose (single process, seconds).
import numpy as np, time
rng = np.random.default_rng(20260909)

def sample_tree_widths(deg_multiset):
    d = np.array(deg_multiset, dtype=np.int64)
    N = len(d)
    assert d.sum() == N - 1
    p = rng.permutation(d)
    s = np.cumsum(p - 1)                 # Lukasiewicz path after each step
    # rotate so the path first hits its minimum at the end: start after argmin
    k = int(np.argmin(s))                # s[k] is the (first) minimum = -1
    q = np.concatenate([p[k+1:], p[:k+1]])
    # rebuild heights by depth-first order with an explicit stack of (remaining children, height)
    heights = np.empty(N, dtype=np.int64)
    stack_h = [0]; stack_c = [1]         # virtual parent of the root
    for i in range(N):
        while stack_c[-1] == 0:
            stack_c.pop(); stack_h.pop()
        h = stack_h[-1]; stack_c[-1] -= 1
        heights[i] = h
        if q[i] > 0:
            stack_h.append(h + 1); stack_c.append(int(q[i]))
    counts = np.bincount(heights)
    return counts.max(), heights.max()

def profile(N, a, frac):
    # frac*N children hang off vertices of outdegree a; the rest of the N-1 children
    # come from a subcritical-looking part (outdegree 0/1/2 mix); leaves fill the count.
    L = int(frac * N / a)
    big = [a] * L
    rest = N - 1 - a * L                 # children still to place
    # place them as outdegree-1 and -2 vertices, half and half by children
    n2 = rest // 4; n1 = rest - 2 * n2
    d = big + [2] * n2 + [1] * n1
    d += [0] * (N - len(d))
    assert len(d) == N and sum(d) == N - 1, (len(d), sum(d))
    return d

N = 40000
print("N =", N, " (frac of children under big vertices = 0.8, like 1-nu)")
print(" a   |n|_2^2/N   mean wid/sqrt(N)   mean ht/sqrt(N)   wid*ht/N   (5 samples each)")
t0 = time.time()
for a in [2, 8, 32, 128, 512]:
    d = profile(N, a, 0.8)
    n2 = sum(x * x for x in d) / N
    ws = []; hs = []
    for _ in range(5):
        w, h = sample_tree_widths(d); ws.append(w); hs.append(h)
    ws = np.array(ws); hs = np.array(hs)
    print(f"{a:4d}  {n2:9.1f}   {ws.mean()/N**0.5:14.2f}   {hs.mean()/N**0.5:14.2f}   {(ws*hs).mean()/N:8.2f}")
print("elapsed s:", round(time.time() - t0, 1))
