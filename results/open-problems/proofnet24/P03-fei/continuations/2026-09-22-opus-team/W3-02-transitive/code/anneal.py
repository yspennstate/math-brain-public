"""Simulated annealing over G-invariant Boolean functions (numba inner loop).

Objectives:
  bal   : maximise H/(I-1) over exactly balanced functions (moves preserve balance exactly:
          swap two classes of opposite sign and equal size, or one class against two whose sizes add up)
  ratio : maximise H/I over all non-constant functions (single class flips)
  horb  : maximise H(orbit of S)/I
  elog  : maximise E log2|orbit of S| / I
Usage: python anneal.py GROUP OBJ STEPS RESTARTS SEED [T0]
"""
import sys, os, time, json
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import tlib, spaces
from numba import njit

tlib.setup_process()


@njit(cache=True)
def evaluate(c, osize, level, logo):
    H = 0.0; I = 0.0; Horb = 0.0; El = 0.0
    for o in range(c.shape[0]):
        p = c[o] * c[o]
        if p > 1e-300:
            H -= osize[o] * p * np.log2(p)
            w = osize[o] * p
            Horb -= w * np.log2(w)
            El += w * logo[o]
        I += osize[o] * level[o] * p
    return H, I, Horb, El


@njit(cache=True)
def objective(H, I, Horb, El, mean, obj):
    if obj == 0:  # bal
        if abs(mean) > 1e-9 or I <= 1.0 + 1e-12:
            return -1e9
        return H / (I - 1.0)
    if I < 1e-12:
        return -1e9
    if obj == 1:
        return H / I
    if obj == 2:
        return Horb / I
    return El / I


@njit(cache=True)
def anneal(F, K, osize, level, logo, steps, T0, T1, obj, seed, sizes_sorted_idx, bucket_start, bucket_size, bucket_of):
    np.random.seed(seed)
    k = F.shape[0]
    c = np.zeros(k)
    for a in range(k):
        if F[a] != 0:
            for o in range(k):
                c[o] += F[a] * K[a, o]
    H, I, Ho, El = evaluate(c, osize, level, logo)
    cur = objective(H, I, Ho, El, c[0], obj)
    best = cur
    bestF = F.copy()
    cn = np.zeros(k)
    nb = bucket_start.shape[0]
    for t in range(steps):
        T = T0 * (T1 / T0) ** (t / max(steps - 1, 1))
        # choose move
        a = np.random.randint(k)
        b = -1; d = -1
        if obj == 0:
            bk = bucket_of[a]
            st = bucket_start[bk]; sz = bucket_size[bk]
            if np.random.random() < 0.85 and sz > 1:
                # equal-size partner of opposite sign
                for tries in range(20):
                    cand = sizes_sorted_idx[st + np.random.randint(sz)]
                    if F[cand] == -F[a]:
                        b = cand
                        break
                if b < 0:
                    continue
            else:
                # two partners of opposite sign whose sizes add up to size(a)
                sa = osize[a]
                found = False
                for tries in range(40):
                    b1 = np.random.randint(k)
                    if F[b1] != -F[a] or osize[b1] >= sa:
                        continue
                    need = sa - osize[b1]
                    # find bucket with size need
                    lo = 0; hi = nb - 1; pos = -1
                    while lo <= hi:
                        mid = (lo + hi) // 2
                        s_mid = osize[sizes_sorted_idx[bucket_start[mid]]]
                        if s_mid == need:
                            pos = mid; break
                        elif s_mid < need:
                            lo = mid + 1
                        else:
                            hi = mid - 1
                    if pos < 0:
                        continue
                    st2 = bucket_start[pos]; sz2 = bucket_size[pos]
                    for tr2 in range(10):
                        d1 = sizes_sorted_idx[st2 + np.random.randint(sz2)]
                        if d1 != b1 and F[d1] == -F[a]:
                            b = b1; d = d1; found = True
                            break
                    if found:
                        break
                if not found:
                    continue
        for o in range(k):
            v = c[o] - 2.0 * F[a] * K[a, o]
            if b >= 0:
                v -= 2.0 * F[b] * K[b, o]
            if d >= 0:
                v -= 2.0 * F[d] * K[d, o]
            cn[o] = v
        H2, I2, Ho2, El2 = evaluate(cn, osize, level, logo)
        new = objective(H2, I2, Ho2, El2, cn[0], obj)
        if new >= cur or np.random.random() < np.exp((new - cur) / T):
            F[a] = -F[a]
            if b >= 0:
                F[b] = -F[b]
            if d >= 0:
                F[d] = -F[d]
            for o in range(k):
                c[o] = cn[o]
            cur = new
            if cur > best:
                best = cur
                bestF[:] = F[:]
    return best, bestF


def random_balanced(osize, rng):
    N = int(osize.sum())
    for attempt in range(1000):
        order = rng.permutation(len(osize))
        F = np.ones(len(osize), dtype=np.int64)
        tot = 0
        for a in order:
            if tot + osize[a] <= N // 2:
                F[a] = -1
                tot += osize[a]
            if tot == N // 2:
                break
        if tot == N // 2:
            return F
    raise RuntimeError("no balanced start")


def main():
    name, obj = sys.argv[1], sys.argv[2]
    steps, restarts, seed = int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
    T0 = float(sys.argv[6]) if len(sys.argv) > 6 else 0.05
    objcode = dict(bal=0, ratio=1, horb=2, elog=3)[obj]
    t0 = time.time()
    V = spaces.space(name)
    tb = time.time() - t0
    osize = V.osize.astype(np.float64)
    level = V.level.astype(np.float64)
    logo = np.log2(osize)
    order = np.argsort(V.osize, kind='stable')
    ss = V.osize[order]
    starts = [0]
    for i in range(1, len(ss)):
        if ss[i] != ss[i - 1]:
            starts.append(i)
    starts = np.array(starts, dtype=np.int64)
    sizes = np.diff(np.append(starts, len(ss))).astype(np.int64)
    bucket_of = np.zeros(V.k, dtype=np.int64)
    for bi, (st, sz) in enumerate(zip(starts, sizes)):
        bucket_of[order[st:st + sz]] = bi
    rng = np.random.default_rng(seed)
    results = []
    gbest = -1e9; gF = None
    for r in range(restarts):
        if objcode == 0:
            F = random_balanced(V.osize, rng)
        else:
            F = rng.choice([-1, 1], size=V.k).astype(np.int64)
        best, bestF = anneal(F.astype(np.float64), V.K, osize, level, logo, steps, T0, 1e-5, objcode,
                             int(seed * 1000 + r), order.astype(np.int64), starts, sizes, bucket_of)
        st = V.orbit_stats(bestF)
        results.append((best, st))
        if best > gbest:
            gbest = best; gF = bestF.copy()
        print("%s %s restart %d best %.9f  H=%.6f I=%.6f mean=%.2e Horb/I=%.3f Elog/I=%.3f" % (
            name, obj, r, best, st['H'], st['I'], st['mean'], st['Horb'] / max(st['I'], 1e-12), st['Elog'] / max(st['I'], 1e-12)), flush=True)
    out = dict(group=name, n=V.n, orbits=V.k, transitive=V.transitive, obj=obj, best=gbest,
               F=[int(v) for v in gF], stats=V.orbit_stats(gF), build_seconds=tb, seconds=time.time() - t0)
    fn = os.path.join(HERE, '..', 'logs', 'anneal_%s_%s_s%d.json' % (name, obj, seed))
    with open(fn, 'w') as fh:
        json.dump(out, fh)
    print("BEST", name, obj, gbest, "orbits", V.k, "n", V.n, "time %.1f" % (time.time() - t0))


if __name__ == '__main__':
    main()
