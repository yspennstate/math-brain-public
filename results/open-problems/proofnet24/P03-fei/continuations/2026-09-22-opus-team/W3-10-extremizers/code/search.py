"""Simulated annealing over truth tables (no structural assumption) for
   J = H/(I-1) over balanced functions (moves swap a true and a false point),
   ratio = H/I over all functions (single-point flips),
   rho0 = min_i Delta_i/Inf_i over all functions (single-point flips).
Incremental integer Walsh updates; phi via lookup tables on integer coefficients.
Usage: python search.py OBJ n restarts steps seed
"""
import sys, time, json
import numpy as np
import numba as nb
sys.path.insert(0, '.')
from core import polite, walsh_int, stats, is_prime, decompose, popc
from structure import max_coin_set

polite()


@nb.njit(cache=True)
def make_tab(N):
    # tab[w] = phi((w/N)^2) for integer w in [-2N, 2N] (index w + 2N)
    t = np.zeros(4 * N + 1)
    for w in range(-2 * N, 2 * N + 1):
        p = (w / N) ** 2
        if p > 0:
            t[w + 2 * N] = -p * np.log(p) / np.log(2.0)
    return t


@nb.njit(cache=True)
def objective(W, n, obj, tab, pc):
    N = W.shape[0]
    off = 2 * N
    H = 0.0
    I = 0.0
    for S in range(N):
        H += tab[W[S] + off]
        I += pc[S] * (W[S] / N) ** 2
    if obj == 0:  # J
        if W[0] != 0 or I <= 1.0 + 1e-9:
            return -1.0
        return H / (I - 1.0)
    if obj == 1:  # ratio
        if I <= 1e-12:
            return -1.0
        return H / I
    # rho0
    best = 1e300
    anyrel = False
    for i in range(n):
        bit = 1 << i
        Hp = 0.0
        Hm = 0.0
        inf = 0.0
        for T in range(N):
            if T & bit:
                continue
            u = W[T]
            v = W[T | bit]
            inf += (v / N) ** 2
            Hp += tab[u + v + off]
            Hm += tab[u - v + off]
        if inf > 1e-12:
            anyrel = True
            r = (H - 0.5 * (Hp + Hm)) / inf
            if r < best:
                best = r
    if not anyrel:
        return -1.0
    return best


@nb.njit(cache=True)
def flip(W, tt, x, chi_sign):
    # f(x) -> -f(x): W[S] -= 2 f(x) chi_S(x)
    N = W.shape[0]
    fx = tt[x]
    for S in range(N):
        if chi_sign[S, x]:
            W[S] += 2 * fx
        else:
            W[S] -= 2 * fx
    tt[x] = -fx


@nb.njit(cache=True)
def anneal(tt0, n, obj, steps, T0, T1, seed, chi_sign, tab, pc):
    np.random.seed(seed)
    N = 1 << n
    tt = tt0.copy()
    W = np.zeros(N, np.int64)
    for S in range(N):
        s = 0
        for x in range(N):
            if chi_sign[S, x]:
                s -= tt[x]
            else:
                s += tt[x]
        W[S] = s
    cur = objective(W, n, obj, tab, pc)
    best = cur
    btt = tt.copy()
    for it in range(steps):
        T = T0 * (T1 / T0) ** (it / steps)
        if obj == 0:
            # swap a true and a false point
            while True:
                x = np.random.randint(N)
                y = np.random.randint(N)
                if tt[x] != tt[y]:
                    break
            flip(W, tt, x, chi_sign)
            flip(W, tt, y, chi_sign)
            new = objective(W, n, obj, tab, pc)
            if new >= cur or np.random.random() < np.exp((new - cur) / T):
                cur = new
                if cur > best + 1e-12:
                    best = cur
                    btt[:] = tt
            else:
                flip(W, tt, x, chi_sign)
                flip(W, tt, y, chi_sign)
        else:
            x = np.random.randint(N)
            flip(W, tt, x, chi_sign)
            new = objective(W, n, obj, tab, pc)
            if new >= cur or np.random.random() < np.exp((new - cur) / T):
                cur = new
                if cur > best + 1e-12:
                    best = cur
                    btt[:] = tt
            else:
                flip(W, tt, x, chi_sign)
    return best, btt


def chi_matrix(n):
    N = 1 << n
    S = np.arange(N)[:, None]
    x = np.arange(N)[None, :]
    a = S & x
    par = np.zeros_like(a)
    for b in range(n):
        par ^= (a >> b) & 1
    return par.astype(np.bool_)  # True where chi_S(x) = -1


def run(obj, n, restarts, steps, seed, T0=0.3, T1=1e-4, log=None):
    N = 1 << n
    chi = chi_matrix(n)
    tab = make_tab(N)
    pc = np.array([bin(s).count('1') for s in range(N)], dtype=np.int64)
    rng = np.random.default_rng(seed)
    results = []
    for r in range(restarts):
        if obj == 0:
            t = np.array([1] * (N // 2) + [-1] * (N // 2), dtype=np.int64)
            rng.shuffle(t)
        else:
            t = np.where(rng.random(N) < rng.uniform(0.05, 0.5), -1, 1).astype(np.int64)
        b, bt = anneal(t, n, obj, steps, T0, T1, int(rng.integers(1 << 30)), chi, tab, pc)
        results.append((b, bt.astype(np.int8)))
    results.sort(key=lambda z: -z[0])
    return results


if __name__ == '__main__':
    objname = sys.argv[1]
    n = int(sys.argv[2])
    restarts = int(sys.argv[3])
    steps = int(sys.argv[4])
    seed = int(sys.argv[5])
    obj = {'J': 0, 'ratio': 1, 'rho0': 2}[objname]
    T0 = float(sys.argv[6]) if len(sys.argv) > 6 else 0.3
    t0 = time.time()
    res = run(obj, n, restarts, steps, seed, T0=T0)
    out = open('../logs/search_%s_n%d_s%d.log' % (objname, n, seed), 'w')
    seen = set()
    rows = []
    for b, t in res:
        key = t.tobytes()
        if key in seen:
            continue
        seen.add(key)
        s = stats(t)
        pr = is_prime(t)
        Y = max_coin_set(t)
        line = '%.9f nrel=%d prime=%s coins=%d H=%.6f I=%.6f mean=%.4f rho0=%.5f  %s' % (
            b, s['nrel'], pr, len(Y), s['H'], s['I'], s['mean'], s['rho0'], decompose(t))
        print(line)
        out.write(line + '\n')
        rows.append(dict(value=b, table=''.join('1' if v == -1 else '0' for v in t), prime=pr, coins=Y))
    json.dump(rows, open('../logs/search_%s_n%d_s%d.json' % (objname, n, seed), 'w'))
    print('time %.1fs' % (time.time() - t0))
    out.write('time %.1fs\n' % (time.time() - t0))
